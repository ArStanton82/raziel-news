import json, glob, re, os

REP = '/root/.hermes/profiles/raziel-news/workspace/raziel-news/reports/2026-11-20-report.md'
text = open(REP).read()
# collect id -> metrics from all raw json
idmap = {}
for f in glob.glob('/root/.hermes/profiles/raziel-news/workspace/raziel-news/reports/x-2026-11-20/*.json'):
    try:
        d = json.load(open(f))
    except Exception:
        continue
    users = {u['id']: u.get('username') for u in (d.get('includes') or {}).get('users') or []}
    for p in d.get('data') or []:
        m = p.get('public_metrics') or {}
        idmap.setdefault(p['id'], []).append((users.get(p.get('author_id')), m, os.path.basename(f)))

print('post x totali nei JSON:', len(idmap))
# find x links in report
links = set(re.findall(r'https://x\.com/([A-Za-z0-9_]+)/status/(\d+)', text))
bad = []
for user, pid in sorted(links):
    if pid not in idmap:
        bad.append((user, pid, 'ID NON NEI JSON'))
        continue
    names = {n for n, _, _ in idmap[pid]}
    if user not in names:
        bad.append((user, pid, 'username mismatch %s' % names))
print('link X usati nel report:', len(links))
print('problemi link:', bad if bad else 'nessuno')

# check declared metrics lines against json for each "### " block
print('--- blocchi con link X e riga Metriche ---')
for blk in text.split('\n### ')[1:]:
    title = blk.split('\n')[0][:60]
    mx = re.findall(r'https://x\.com/([A-Za-z0-9_]+)/status/(\d+)', blk)
    if not mx:
        continue
    for user, pid in mx:
        cand = idmap.get(pid)
        if not cand:
            print('  [X]', title, pid, 'assente')
            continue
        metrics = [m for _, m, _ in cand]
        print('  ok', user, pid, [(m.get('like_count'), m.get('retweet_count'), m.get('reply_count'), m.get('impression_count')) for m in metrics])

# contract tail
lines = [l for l in text.strip().split('\n') if l.strip()]
print('--- ultime 3 righe ---')
for l in lines[-3:]:
    print(repr(l[:160]))
print('bytes', len(text))
