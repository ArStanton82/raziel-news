import json, glob, os

for path in sorted(glob.glob('*.json')):
    try:
        d = json.load(open(path))
    except Exception as e:
        print(f"== {path}: ERRORE {e}")
        continue
    data = d.get('data') or []
    users = {u['id']: u['username'] for u in (d.get('includes') or {}).get('users', [])}
    print(f"== {path} ({len(data)})")
    for p in data:
        u = users.get(p.get('author_id'), '?')
        m = p.get('public_metrics') or {}
        txt = ' '.join(p.get('text', '').split())
        print(f"- @{u} {p.get('created_at')} id={p.get('id')} lk={m.get('like_count')} rt={m.get('retweet_count')} vw={m.get('impression_count')}")
        print(f"  {txt[:400]}")
    print()
