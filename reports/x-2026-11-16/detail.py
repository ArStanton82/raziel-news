import json, statistics as st
from datetime import datetime, timedelta, timezone
from collections import Counter, defaultdict

D = json.load(open('reports/x-2026-11-16/tweets_full.json'))
tw = D['data']
print('bookmark_count presente in', sum(1 for t in tw if 'bookmark_count' in t.get('public_metrics', {})), '/', len(tw))
sample = tw[0]
print('public_metrics keys:', sorted(sample.get('public_metrics', {}).keys()))
print('non_public_metrics keys:', sorted((sample.get('non_public_metrics') or {}).keys()))
print('organic keys:', sorted((sample.get('organic_metrics') or {}).keys()))
print('promoted keys:', sorted((sample.get('promoted_metrics') or {}).keys()))

tot_imp = sum(t['public_metrics'].get('impression_count', 0) for t in tw)
org_imp = sum((t.get('organic_metrics') or {}).get('impression_count', 0) for t in tw)
prm_imp = sum((t.get('promoted_metrics') or {}).get('impression_count', 0) for t in tw)
print('imp totali', tot_imp, 'organic', org_imp, 'promoted', prm_imp)
print('bm tot', sum(t['public_metrics'].get('bookmark_count', 0) for t in tw))

M = json.load(open('reports/x-2026-11-16/mentions.json'))
print('\n--- mentions ---')
print('meta', M.get('meta'))
print('errors', M.get('errors'))
users = {u['id']: u for u in M.get('includes', {}).get('users', [])}
for t in M.get('data', []):
    a = users.get(t['author_id'], {})
    print(t['created_at'], '@' + a.get('username', '?'), 'fol=' + str(a.get('public_metrics', {}).get('followers_count')), 'conv=' + t.get('conversation_id', ''), '|', t['text'][:100].replace('\n', ' '))
