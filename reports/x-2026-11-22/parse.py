import json, glob, os, datetime

files = sorted(glob.glob(os.path.join(os.path.dirname(os.path.abspath(__file__)), "*.json")))
for f in files:
    try:
        d = json.load(open(f))
    except Exception as e:
        print("==", os.path.basename(f), "PARSE ERROR", e)
        continue
    data = d.get("data") or []
    users = {}
    for u in (d.get("includes") or {}).get("users", []) or []:
        users[u["id"]] = u["username"]
    print("==", os.path.basename(f), "count=", len(data), "meta=", d.get("meta"))
    for p in data:
        pm = p.get("public_metrics", {}) or {}
        txt = " ".join(p.get("text", "").split())
        print("--", p["id"], "@" + users.get(p.get("author_id"), "?"), p.get("created_at"),
              "L%s RT%s R%s Q%s" % (pm.get("like_count", "?"), pm.get("retweet_count", "?"),
                                    pm.get("reply_count", "?"), pm.get("quote_count", "?")),
              "views=%s" % pm.get("impression_count"))
        print("   ", txt[:600])
