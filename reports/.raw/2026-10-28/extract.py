import json, glob, os, sys

base = "/root/.hermes/profiles/raziel-news/workspace/raziel-news/reports/.raw/2026-10-28"
rows = []
for f in sorted(glob.glob(os.path.join(base, "*.json"))):
    tag = os.path.basename(f)[:-5]
    try:
        d = json.load(open(f))
    except Exception as e:
        print("PARSE FAIL", tag, e)
        continue
    posts = d.get("data") or []
    users = {u["id"]: u["username"] for u in (d.get("includes", {}).get("users") or [])}
    print("=== %s : %d posts" % (tag, len(posts)))
    for p in posts:
        uname = users.get(p.get("author_id"), "?")
        pm = p.get("public_metrics") or {}
        txt = " ".join(p.get("text", "").split())
        print("  [%s] @%s %s | id=%s | L%s RT%s R%s V%s" % (
            p.get("created_at"), uname, txt[:220], p["id"],
            pm.get("like_count"), pm.get("retweet_count"),
            pm.get("reply_count"), pm.get("impression_count")))
    print()
