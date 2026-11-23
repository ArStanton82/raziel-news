import json, glob, os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

out = []
for path in sorted(glob.glob("*.json")):
    try:
        d = json.load(open(path, encoding="utf-8"))
    except Exception as e:
        out.append(f"### {path}: PARSE ERROR {e}")
        continue
    data = d.get("data", [])
    users = {u["id"]: u.get("username") for u in d.get("includes", {}).get("users", [])}
    out.append(f"\n===== {path} ({len(data)} post) =====")
    for p in data:
        u = users.get(p.get("author_id"), "?")
        m = p.get("public_metrics", {})
        txt = p.get("text", "").replace("\n", " ")
        out.append(f"[{p.get('created_at','?')}] @{u} id={p.get('id')} like={m.get('like_count')} rt={m.get('retweet_count')} imp={m.get('impression_count')}")
        out.append(f"   {txt[:500]}")

open("digest.txt", "w", encoding="utf-8").write("\n".join(out))
print("wrote digest.txt", len("\n".join(out)), "bytes")
