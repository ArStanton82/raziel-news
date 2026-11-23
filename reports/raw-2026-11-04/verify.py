import json, glob, os, re

base = '/root/.hermes/profiles/raziel-news/workspace/raziel-news/reports/raw-2026-11-04'
rep = '/root/.hermes/profiles/raziel-news/workspace/raziel-news/reports/2026-11-04-report.md'

# build id -> list of snapshots (username, created_at, metrics)
snap = {}
for f in glob.glob(os.path.join(base, '*.json')):
    try:
        d = json.load(open(f))
    except Exception:
        continue
    users = {u['id']: u['username'] for u in d.get('includes', {}).get('users', [])}
    for t in d.get('data', []):
        snap.setdefault(t['id'], []).append((
            users.get(t.get('author_id'), '?'),
            t.get('created_at', ''),
            t.get('public_metrics', {}),
        ))

txt = open(rep, encoding='utf-8').read()
blocks = [b for b in txt.split('### ') if b.strip()]
errors = []
items = 0
for b in blocks[1:]:
    items += 1
    lines = b.splitlines()
    title = lines[0].strip()
    acct = re.search(r'\*\*Account\*\*: @(\w+)', b)
    fonte = re.search(r'\*\*Fonte\*\*: ([^\n]+)', b)
    linkline = re.search(r'- \*\*Link\*\*: ([^\n]+)', b)
    dateline = re.search(r'\*\*Data\*\*: (\d{4}-\d{2}-\d{2})', b)
    metline = re.search(r'\*\*Metriche\*\*: ([^\n]+)', b)
    if not linkline:
        errors.append('NO LINK: ' + title); continue
    links = linkline.group(1)
    if acct:
        handle = acct.group(1)
        m = re.search(r'https://x\.com/(\w+)/status/(\d+)', links)
        if not m:
            errors.append('NO X URL in Link for X item: ' + title); continue
        un, tid = m.group(1), m.group(2)
        if un.lower() != handle.lower():
            errors.append('USERNAME MISMATCH %s vs @%s : %s' % (un, handle, title))
        if tid not in snap:
            errors.append('ID NOT IN JSON: %s : %s' % (tid, title)); continue
        cands = snap[tid]
        # metrics check: accept any real snapshot
        mm = metline.group(1) if metline else ''
        nums = re.findall(r'([\d.]+)', mm.replace('.', ''))
        vals = set()
        for _, _, p in cands:
            for k in ('like_count', 'retweet_count', 'impression_count'):
                if p.get(k) is not None:
                    vals.add(str(int(p[k])))
        claimed = re.findall(r'(\d+(?:\.\d{3})*)\s*(?:like|retweet|views)', mm)
        claimed_nums = [c.replace('.', '') for c in claimed]
        for c in claimed_nums:
            if c not in {str(int(v)) for v in vals}:
                errors.append('METRIC %s not in %s : %s' % (c, sorted(vals), title))
        ca = cands[0][1][:10]
        if dateline and dateline.group(1) != ca:
            errors.append('DATE %s vs %s : %s' % (dateline.group(1), ca, title))
    else:
        # web item: need >=2 links
        urls = re.findall(r'https?://[^\s;]+', links)
        if len(urls) < 2:
            errors.append('WEB ITEM WITH <2 LINKS: ' + title)

print('items:', items)
last = [l for l in txt.strip().splitlines() if l.strip()][-2:]
print('LAST2:', last)
print('ERRORS:', len(errors))
for e in errors:
    print(' -', e)
