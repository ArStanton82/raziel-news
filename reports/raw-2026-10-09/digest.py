import json, glob, os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

for path in sorted(glob.glob("*.json")):
    try:
        d = json.load(open(path, encoding="utf-8"))
    except Exception as e:
        print(f"### {path}: PARSE ERROR {e}")
        continue
    data = d.get("data", [])
    users = {u["id"]: u.get("username") for u in d.get("includes", {}).get("users", [])}
    print(f"\n===== {path} ({len(data)} post) =====")
    for p in data:
        u = users.get(p.get("author_id"), "?")
        m = p.get("public_metrics", {})
        txt = p.get("text", "").replace("\n", " ")
        print(f"[{p.get('created_at','?')}] @{u} id={p.get('id')} like={m.get('like_count')} rt={m.get('retweet_count')} imp={m.get('impression_count')}")
        print(f"   {txt[:400]}")
