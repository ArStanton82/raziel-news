import json, glob, os, sys

d = "/root/.hermes/profiles/raziel-news/workspace/raziel-news/reports/raw-2026-10-26"
files = sorted(glob.glob(os.path.join(d, "*.json")))
for f in files:
    name = os.path.basename(f)
    try:
        j = json.load(open(f))
    except Exception as e:
        print("FILE", name, "PARSE_ERROR", e)
        continue
    data = j.get("data") or []
    users = {}
    for u in (j.get("includes") or {}).get("users") or []:
        users[u["id"]] = u["username"]
    print("=" * 70)
    print("FILE", name, "count", len(data))
    for p in data:
        un = users.get(p.get("author_id"), "?")
        pm = p.get("public_metrics") or {}
        txt = " ".join(p.get("text", "").split())
        print("-" * 60)
        print("id:", p.get("id"), "| user:", un, "| created:", p.get("created_at"))
        print("metrics: like=%s rt=%s reply=%s quote=%s imp=%s" % (pm.get("like_count"), pm.get("retweet_count"), pm.get("reply_count"), pm.get("quote_count"), pm.get("impression_count")))
        print("text:", txt[:700])
