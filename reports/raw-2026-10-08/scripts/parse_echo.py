import json, os, glob

RAW = "reports/raw-2026-10-08"
files = sorted(glob.glob(os.path.join(RAW, "*.json")))
for f in files:
    try:
        d = json.load(open(f, encoding="utf-8"))
    except Exception as e:
        print("=== %s PARSE ERROR %s" % (f, e)); continue
    data = d.get("data") or []
    users = {}
    for u in (d.get("includes", {}) or {}).get("users", []) or []:
        users[u["id"]] = u.get("username")
    print("=== %s  posts=%d" % (os.path.basename(f), len(data)))
    for p in data:
        uid = p.get("author_id")
        un = users.get(uid, "?")
        pm = p.get("public_metrics", {}) or {}
        txt = (p.get("text") or "").replace("\n", " ")
        print("  @%s | %s | id=%s | like=%s rt=%s imp=%s" % (
            un, p.get("created_at"), p.get("id"),
            pm.get("like_count"), pm.get("retweet_count"), pm.get("impression_count")))
        print("     %s" % txt[:400])
