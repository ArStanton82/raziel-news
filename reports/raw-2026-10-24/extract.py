import json, glob, os, datetime

RAW = "reports/raw-2026-10-24"
posts = {}
for f in sorted(glob.glob(os.path.join(RAW, "*.json"))):
    tag = os.path.basename(f)[:-5]
    try:
        d = json.load(open(f))
    except Exception as e:
        print("PARSE FAIL", f, e)
        continue
    users = {}
    for u in (d.get("includes") or {}).get("users", []) or []:
        users[u["id"]] = u.get("username")
    for p in d.get("data", []) or []:
        pid = p["id"]
        rec = posts.setdefault(pid, {"id": pid, "tags": [], "text": p.get("text", ""),
                                     "created_at": p.get("created_at", ""),
                                     "author_id": p.get("author_id"),
                                     "metrics": p.get("public_metrics") or {}})
        rec["tags"].append(tag)
        if not rec.get("username"):
            rec["username"] = users.get(p.get("author_id"))
        if p.get("public_metrics"):
            rec["metrics"] = p["public_metrics"]

rows = []
for r in posts.values():
    rows.append(r)
rows.sort(key=lambda r: r["created_at"], reverse=True)

print("TOTALE POST UNICI:", len(rows))
for r in rows:
    m = r["metrics"]
    ts = r["created_at"][:16].replace("T", " ")
    print("=" * 100)
    print(f"id={r['id']} @{r.get('username')} {ts} tags={','.join(r['tags'])}")
    print(f"  like={m.get('like_count')} rt={m.get('retweet_count')} rep={m.get('reply_count')} views={m.get('impression_count')}")
    t = " ".join(r["text"].split())
    print("  TXT:", t[:700])
