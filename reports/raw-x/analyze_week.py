import json, statistics, datetime

d = json.load(open('reports/raw-x/2026-10-12-tweets.json'))
tw = d["data"]

def org(t): return t.get("organic_metrics") or {}
def pro(t): return t.get("promoted_metrics") or {}

# weekly window: last 7 days = 2026-10-05 .. 2026-10-11
cut = "2026-10-05"
week = [t for t in tw if t["created_at"][:10] >= cut]
print("WEEK 2026-10-05..2026-10-11 : n =", len(week))
oi = [ (org(t).get("impression_count") or 0) for t in week ]
print("  organic imps total:", sum(oi), " median:", statistics.median(oi) if oi else 0)
rt=rp=ori=0
for t in week:
    refs=[r["type"] for r in (t.get("referenced_tweets") or [])]
    if "retweeted" in refs: rt+=1
    elif "replied_to" in refs: rp+=1
    else: ori+=1
print("  RT:",rt,"replies:",rp,"originals:",ori)
print("  profile clicks:", sum((org(t).get("user_profile_clicks") or 0) for t in week))
print("  link clicks:", sum((org(t).get("url_link_clicks") or 0) for t in week))
print("  promoted imps:", sum((pro(t).get("impression_count") or 0) for t in week))

print("\nORIGINALS in week (pipeline posts):")
for t in sorted(week,key=lambda x:x["created_at"]):
    refs=[r["type"] for r in (t.get("referenced_tweets") or [])]
    if not refs:
        o=org(t)
        print(f"  {t['id']} {t['created_at'][:16]} imp={o.get('impression_count')} likes={o.get('like_count')} rt={o.get('retweet_count')} rep={o.get('reply_count')} prof={o.get('user_profile_clicks')} link={o.get('url_link_clicks')} lang={t.get('lang')}")

# breakdown all-time window lang
from collections import Counter
print("\nlang counts (100):", Counter(t.get("lang") for t in tw))
