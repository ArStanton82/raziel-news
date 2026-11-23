import json, glob, os, sys

rows = []
for path in sorted(glob.glob("reports/.raw/*.json")):
    try:
        d = json.load(open(path))
    except Exception as e:
        print("SKIP", path, e)
        continue
    data = d.get("data") or []
    users = {u["id"]: u["username"] for u in (d.get("includes") or {}).get("users", [])}
    for p in data:
        rows.append({
            "file": os.path.basename(path),
            "id": p.get("id"),
            "user": users.get(p.get("author_id"), "?"),
            "created": p.get("created_at", ""),
            "text": (p.get("text") or "").replace("\n", " "),
            "pm": p.get("public_metrics") or {},
        })

rows.sort(key=lambda r: r["created"], reverse=True)
for r in rows:
    pm = r["pm"]
    print("|".join([
        r["file"], r["id"], r["user"], r["created"],
        str(pm.get("like_count")), str(pm.get("retweet_count")), str(pm.get("impression_count")),
        r["text"][:400],
    ]))
print("TOTAL", len(rows))
