import json, glob, os, re

files = sorted(glob.glob('/root/.hermes/profiles/raziel-news/workspace/raziel-news/reports/raw-2026-11-15/*.json'))
items = []
for f in files:
    if f.endswith('extract.py') or f.endswith('all.json'):
        continue
    name = os.path.basename(f)[:-5]
    raw = open(f).read().strip()
    if not raw:
        print(f"== {name}: EMPTY FILE")
        continue
    try:
        d = json.loads(raw)
    except Exception as e:
        print(f"== {name}: PARSE ERROR {e} head={raw[:120]}")
        continue
    users = {}
    for u in (d.get('includes') or {}).get('users', []) or []:
        users[u['id']] = u['username']
    data = d.get('data') or []
    print(f"== {name}: {len(data)} posts")
    for t in data:
        m = t.get('public_metrics') or {}
        un = users.get(t.get('author_id'), '?' + str(t.get('author_id'))[:6])
        txt = re.sub(r'\s+', ' ', t.get('text', ''))
        print(f"- @{un} | {t.get('created_at','')} | id={t['id']} | L{m.get('like_count',0)} RT{m.get('retweet_count',0)} V{m.get('impression_count',0)}")
        print(f"  {txt[:600]}")
        items.append({'src': name, 'user': un, 'id': t['id'], 'created_at': t.get('created_at'), 'text': txt, 'metrics': m})

json.dump(items, open('/root/.hermes/profiles/raziel-news/workspace/raziel-news/reports/raw-2026-11-15/all.json', 'w'))
print("TOTAL", len(items))
