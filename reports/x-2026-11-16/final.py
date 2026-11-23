import json, statistics as st
from datetime import datetime, timedelta, timezone
from collections import defaultdict

CET = timezone(timedelta(hours=1))
tw = json.load(open('reports/x-2026-11-16/tweets_full.json'))['data']
byid = {t['id']: t for t in tw}
rows = json.load(open('reports/x-2026-11-16/rows.json'))
for r in rows:
    r['dt'] = datetime.fromisoformat(r['dt'])
now = datetime(2026, 11, 16, 8, 0, tzinfo=timezone.utc)

for i in ['2119859510823043477', '2120494066840297491', '2120606255081496959']:
    t = byid[i]
    print('==', i, t['created_at'], 'ref=', t.get('referenced_tweets'), 'media=', t.get('attachments'), 'lang=', t.get('lang'))
    print('   ', (t.get('note_tweet', {}).get('text') or t['text'])[:300].replace('\n', ' '))
    print('   pm=', t['public_metrics'])

w1 = [r for r in rows if now - timedelta(days=7) <= r['dt'] < now and not r['reply'] and not (r['link_body'] and not r['media'])]
w0 = [r for r in rows if now - timedelta(days=14) <= r['dt'] < now - timedelta(days=7) and not r['reply'] and not (r['link_body'] and not r['media'])]
print()
print('imp tot settimana 9-16 =', sum(r['imp'] for r in w1), 'n=', len(w1))
print('imp tot settimana 2-9  =', sum(r['imp'] for r in w0), 'n=', len(w0))
print('like 9-16 =', sum(r['like'] for r in w1), ' like 2-9 =', sum(r['like'] for r in w0))
print('risposte ricevute (rc) 9-16 =', sum(r['rc'] for r in w1))
print()
print('--- TUTTI i post editoriali della finestra 100, per data ---')
for r in sorted(rows, key=lambda x: x['dt']):
    if r['reply'] or (r['link_body'] and not r['media']):
        continue
    t = byid[r['id']]
    print('%-16s %-5s %3d imp %d like %d bm %d rc %s' % (r['dt'].astimezone(CET).strftime('%d/%m %H:%M'), t.get('lang'), r['imp'], r['like'], r['bm'], r['rc'], r['text'][:90]))
