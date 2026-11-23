import json, statistics

d = json.load(open('reports/raw-x/2026-10-12-tweets.json'))
tw = d["data"]
print("meta:", d.get("meta"))
print("n tweets:", len(tw))
print("date range:", min(t["created_at"] for t in tw), "->", max(t["created_at"] for t in tw))

# profile
p = json.load(open('reports/raw-x/2026-10-12-profile.json'))
pm = p["data"]["public_metrics"]
followers = pm["followers_count"]
print("followers:", followers, "delta vs 416:", followers - 416)

def imp(t):
    o = t.get("organic_metrics") or {}
    pr = t.get("promoted_metrics") or {}
    np = t.get("non_public_metrics") or {}
    return (o.get("impression_count"), pr.get("impression_count"), np.get("impression_count"))

org_total = 0
promo_total = 0
org_imps = []
promo_posts = 0
for t in tw:
    o, pr, np = imp(t)
    o = o or 0
    pr = pr or 0
    org_total += o
    promo_total += pr
    org_imps.append(o)
    if pr > 0:
        promo_posts += 1

print("organic impressions total:", org_total)
print("promoted impressions total:", promo_total)
print("posts with promoted:", promo_posts)
print("median organic impressions:", statistics.median(org_imps))
print("mean organic impressions:", round(statistics.mean(org_imps), 2))

# composition: retweets (referenced_tweets type retweeted), replies (replied_to), originals
rt = 0
replies = 0
originals = 0
for t in tw:
    refs = t.get("referenced_tweets") or []
    types = [r["type"] for r in refs]
    if "retweeted" in types:
        rt += 1
    elif "replied_to" in types:
        replies += 1
    else:
        originals += 1
print("RT:", rt, "replies:", replies, "originals:", originals)

# clicks
prof_clicks = sum((t.get("organic_metrics") or {}).get("user_profile_clicks", 0) or 0 for t in tw)
link_clicks = sum((t.get("organic_metrics") or {}).get("url_link_clicks", 0) or 0 for t in tw)
print("profile clicks (organic):", prof_clicks)
print("link clicks (organic):", link_clicks)

# top 5 by organic impressions
tops = sorted(tw, key=lambda t: (t.get("organic_metrics") or {}).get("impression_count", 0) or 0, reverse=True)[:5]
print("\nTOP 5 by organic impressions:")
for t in tops:
    o = t.get("organic_metrics") or {}
    refs = t.get("referenced_tweets") or []
    kind = "orig" if not refs else ("rt" if any(r["type"]=="retweeted" for r in refs) else "reply")
    print(f"  {t['id']} imp={o.get('impression_count')} likes={o.get('like_count')} rt={o.get('retweet_count')} reply={o.get('reply_count')} prof={o.get('user_profile_clicks')} link={o.get('url_link_clicks')} kind={kind} lang={t.get('lang')} date={t['created_at'][:10]}")

# posts above 5x median
med = statistics.median(org_imps)
above = [t for t in tw if ((t.get("organic_metrics") or {}).get("impression_count",0) or 0) > 5*med]
print("\nposts > 5x median (%.1f): %d" % (med, len(above)))
for t in above:
    o=t.get("organic_metrics") or {}
    print("   ", t["id"], o.get("impression_count"), t["created_at"][:10])

# CTR organico
if org_total:
    print("\nCTR organico (link clicks / impressions): %.4f%%" % (100.0*link_clicks/org_total))
