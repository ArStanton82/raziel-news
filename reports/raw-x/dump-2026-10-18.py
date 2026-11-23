import json, glob, os

BASE = os.path.dirname(os.path.abspath(__file__))
DATE = "2026-10-18"
files = sorted(glob.glob(os.path.join(BASE, DATE + "-*.json")))
out = []
for f in files:
    tag = os.path.basename(f)[len(DATE) + 1:-5]
    try:
        raw = open(f, encoding="utf-8").read()
        d = json.loads(raw)
    except Exception as e:
        out.append("### %s : ERRORE parse %s" % (tag, e))
        continue
    posts = d.get("data") or []
    users = {}
    for u in (d.get("includes") or {}).get("users") or []:
        users[u["id"]] = u["username"]
    out.append("=== %s : %d post ===" % (tag, len(posts)))
    for p in posts:
        uid = p.get("author_id")
        un = users.get(uid, "?" + str(uid))
        m = p.get("public_metrics") or {}
        metrics = "likes=%s rt=%s replies=%s views=%s" % (
            m.get("like_count"), m.get("retweet_count"), m.get("reply_count"),
            m.get("impression_count"))
        txt = (p.get("text") or "").replace("\n", " ")
        out.append("[%s] %s | %s | https://x.com/%s/status/%s | %s" % (
            tag, un, p.get("created_at"), un, p.get("id"), metrics))
        out.append("    " + txt[:600])
    out.append("")
print("\n".join(out))
