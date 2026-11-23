import json, statistics as st
from datetime import datetime, timedelta, timezone
from collections import defaultdict

CET = timezone(timedelta(hours=1))
rows = json.load(open('reports/x-2026-11-16/rows.json'))
for r in rows:
    r['dt'] = datetime.fromisoformat(r['dt'])
tw = json.load(open('reports/x-2026-11-16/tweets_full.json'))['data']
byid = {t['id']: t for t in tw}

ed = [r for r in rows if not r['reply'] and not (r['link_body'] and not r['media'])]
now = datetime(2026, 11, 16, 8, 0, tzinfo=timezone.utc)
w1 = [r for r in ed if now - timedelta(days=7) <= r['dt'] < now]          # 9->16 nov
w0 = [r for r in ed if now - timedelta(days=14) <= r['dt'] < now - timedelta(days=7)]  # 2->9 nov
print('settimana 9-16 nov: n=%d mediana=%s' % (len(w1), st.median([r['imp'] for r in w1])))
print('settimana 2-9 nov : n=%d mediana=%s (riletta oggi, eta 7-14 gg)' % (len(w0), st.median([r['imp'] for r in w0])))

def slot(r):
    h = r['dt'].astimezone(CET).hour
    return 'mattutino 08:15' if h < 11 else ('giornata 13:15' if h < 17 else 'serale 20:15')

for label, grp in (('9-16 nov', w1), ('2-9 nov', w0)):
    per = defaultdict(list)
    for r in grp:
        per[slot(r)].append(r['imp'])
    print(label, {k: (len(v), st.median(v), max(v)) for k, v in per.items()})

# eta' dei post di questa settimana non ancora a 7 giorni: segnala
print()
print('--- editoriali 9-16 nov, eta\' in giorni ---')
for r in sorted(w1, key=lambda x: x['dt']):
    age = (now - r['dt']).days
    print('%-17s eta=%2dg imp=%3d like=%d bm=%d rc=%d %-45s %s' % (
        r['dt'].astimezone(CET).strftime('%Y-%m-%d %H:%M'), age, r['imp'], r['like'], r['bm'], r['rc'],
        r['text'][:44], r['id']))

# click e bookmark di questa settimana (tutti i post creati)
wk = [r for r in rows if now - timedelta(days=7) <= r['dt'] < now]
print()
print('click profilo organic 7gg =', sum(r['org_prof'] or 0 for r in wk), ' link organic 7gg =', sum(r['org_link'] or 0 for r in wk))
print('promoted click profilo =', 0, 'promoted link =', 0)
print('bookmark 7gg =', sum(r['bm'] for r in wk), ' bookmark finestra intera =', sum(r['bm'] for r in rows))
print('like 7gg =', sum(r['like'] for r in wk))

# risposte umane: reply_count degli editoriali meno le nostre link-reply
edc = [r for r in ed]
print()
for label, grp in (('9-16 nov', w1), ('2-9 nov', w0)):
    mine = 0
    ids = {r['id'] for r in grp}
    for r in rows:
        if r['reply'] and r['fmt'] == 'prima_risposta_link':
            pass
    # conta nostre reply il cui conversation_id e' un editoriale del gruppo
    for t in tw:
        rt = t.get('referenced_tweets', [])
        if rt and rt[0]['type'] == 'replied_to' and rt[0]['id'] in ids:
            mine += 1
    rc = sum(r['rc'] for r in grp)
    print('%s: reply_count editoriali=%d, nostre prime risposte nel gruppo=%d -> umane~%d su %d post = %.2f' % (label, rc, mine, rc - mine, len(grp), (rc - mine) / len(grp)))

# menzioni ultimi 7 giorni
M = json.load(open('reports/x-2026-11-16/mentions.json'))
print('\nmenzioni 7gg:', M.get('meta', {}).get('result_count'))
for t in M.get('data', []):
    print(' ', t['created_at'][:16], t.get('conversation_id'), 'e\' nostro post:', t.get('conversation_id') in byid, '|', t['text'][:70])
