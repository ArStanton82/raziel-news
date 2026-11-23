import json, glob, os, datetime

CUT = datetime.datetime(2026, 11, 18, 7, 0, tzinfo=datetime.timezone.utc)
files = sorted(glob.glob('/root/.hermes/profiles/raziel-news/workspace/raziel-news/reports/x-2026-11-20/*.json'))
out = []
for f in files:
    name = os.path.basename(f)
    try:
        d = json.load(open(f))
    except Exception as e:
        out.append('### %s -- PARSE ERROR %s' % (name, e))
        continue
    data = d.get('data') or []
    users = {}
    for u in (d.get('includes') or {}).get('users') or []:
        users[u['id']] = u.get('username')
    out.append('### %s  (n=%d, meta=%s)' % (name, len(data), json.dumps(d.get('meta'))))
    rows = []
    for p in data:
        ca = p.get('created_at', '')
        try:
            dt = datetime.datetime.strptime(ca, '%Y-%m-%dT%H:%M:%S.000Z').replace(tzinfo=datetime.timezone.utc)
        except Exception:
            dt = None
        if dt and dt < CUT:
            continue
        m = p.get('public_metrics') or {}
        ui = users.get(p.get('author_id'), '?')
        txt = ' '.join((p.get('text') or '').split())
        rows.append('- %s | @%s | id=%s | like=%s rt=%s reply=%s views=%s\n  %s' % (
            ca, ui, p.get('id'), m.get('like_count'), m.get('retweet_count'),
            m.get('reply_count'), m.get('impression_count'), txt[:700]))
    if not rows:
        out.append('  (nessun post nelle ultime 48h su %d totali)' % len(data))
    out.extend(rows)

open('/root/.hermes/profiles/raziel-news/workspace/raziel-news/reports/x-2026-11-20/extract.txt', 'w').write('\n'.join(out))
print('\n'.join(out))
