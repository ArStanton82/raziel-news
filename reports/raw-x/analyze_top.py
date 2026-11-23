import json
from collections import Counter

d = json.load(open('reports/raw-x/2026-10-12-tweets.json'))
tw = d["data"]

def org(t): return t.get("organic_metrics") or {}
def txt(t):
    nt = t.get("note_tweet") or {}
    return (nt.get("text") or t.get("text") or "").replace("\n"," ")[:160]

# replies per day in week
week = [t for t in tw if t["created_at"][:10] >= "2026-10-05"]
c = Counter()
for t in week:
    refs=[r["type"] for r in (t.get("referenced_tweets") or [])]
    if "replied_to" in refs:
        c[t["created_at"][:10]] += 1
print("replies per day (week):", dict(sorted(c.items())))

print("\nTOP 5 text:")
for t in sorted(tw, key=lambda x:(org(x).get("impression_count") or 0), reverse=True)[:5]:
    print(f"  imp={org(t).get('impression_count')} {t['created_at'][:10]} :: {txt(t)}")

print("\nBest ORIGINAL pipeline posts:")
for t in sorted([t for t in tw if not (t.get('referenced_tweets'))], key=lambda x:(org(x).get("impression_count") or 0), reverse=True)[:5]:
    print(f"  imp={org(t).get('impression_count')} {t['created_at'][:10]} lang={t.get('lang')} :: {txt(t)}")
