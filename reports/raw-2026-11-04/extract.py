import json, glob, os, datetime

base = os.path.dirname(os.path.abspath(__file__))
files = sorted(glob.glob(os.path.join(base, '*.json')))
cutoff = datetime.datetime(2026, 11, 2, 0, 0, 0)

for f in files:
    try:
        d = json.load(open(f))
    except Exception as e:
        print('ERR', os.path.basename(f), e)
        continue
    users = {}
    for u in d.get('includes', {}).get('users', []):
        users[u['id']] = u['username']
    rows = []
    for t in d.get('data', []):
        ca = t.get('created_at', '')
        try:
            dt = datetime.datetime.strptime(ca, '%Y-%m-%dT%H:%M:%S.%fZ')
        except Exception:
            dt = cutoff
        if dt < cutoff:
            continue
        m = t.get('public_metrics', {})
        rows.append((dt, t['id'], users.get(t.get('author_id'), '?'),
                     m.get('like_count'), m.get('retweet_count'), m.get('impression_count'),
                     t.get('text', '').replace('\n', ' ')))
    rows.sort(reverse=True)
    print('=====', os.path.basename(f), 'n=', len(rows), 'total_raw=', len(d.get('data', [])))
    for dt, tid, un, lk, rt, im, tx in rows:
        print('  [%s] @%s id=%s L=%s RT=%s V=%s' % (dt.strftime('%m-%d %H:%M'), un, tid, lk, rt, im))
        print('     ', tx[:300])
