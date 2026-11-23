import json, statistics as st
from datetime import datetime, timedelta, timezone

D = json.load(open('reports/x-2026-11-16/tweets_full.json'))
tweets = D['data']
media = {m['media_key']: m.get('type') for m in D.get('includes', {}).get('media', [])}

ME = '1397653619172954118'

def parse(dt):
    return datetime.fromisoformat(dt.replace('Z', '+00:00'))

def is_reply(t):
    return any(r['type'] == 'replied_to' for r in t.get('referenced_tweets', []))

def has_link_body(t):
    ents = t.get('entities', {})
    return bool(ents.get('urls'))

def has_media(t):
    keys = t.get('attachments', {}).get('media_keys', [])
    return any(media.get(k) == 'photo' for k in keys)

rows = []
for t in tweets:
    t['_dt'] = parse(t['created_at'])
    pm = t.get('public_metrics', {})
    npm = t.get('non_public_metrics', {}) or {}
    org = t.get('organic_metrics', {}) or {}
    prm = t.get('promoted_metrics', {}) or {}
    rows.append({
        'id': t['id'],
        'dt': t['_dt'],
        'reply': is_reply(t),
        'link_body': has_link_body(t),
        'media': has_media(t),
        'text': (t.get('note_tweet', {}).get('text') or t['text'])[:120].replace('\n', ' '),
        'imp': pm.get('impression_count', 0),
        'like': pm.get('like_count', 0),
        'bm': pm.get('bookmark_count', 0),
        'rt': pm.get('retweet_count', 0),
        'rc': pm.get('reply_count', 0),
        'qc': pm.get('quote_count', 0),
        'org_imp': org.get('impression_count'),
        'prm_imp': prm.get('impression_count'),
        'org_prof': org.get('user_profile_clicks'),
        'org_link': org.get('url_link_clicks'),
        'npm_prof': npm.get('user_profile_clicks'),
        'npm_link': npm.get('url_link_clicks'),
        'lang': t.get('lang'),
    })

rows.sort(key=lambda r: r['dt'], reverse=True)
oldest, newest = rows[-1]['dt'], rows[0]['dt']
print('finestra:', oldest.isoformat(), '->', newest.isoformat(), 'n=', len(rows))

# classification
def fmt(r):
    if r['reply']:
        # our first reply carrying the link vs other replies
        if r['link_body'] and not has_media_row(r):
            return 'prima_risposta_link'
        return 'risposta'
    if r['link_body'] and not has_media_row(r):
        return 'post_con_solo_link'
    if has_media_row(r):
        return 'post_con_immagine'
    return 'altro'

def has_media_row(r):
    return r['media']

for r in rows:
    r['fmt'] = fmt(r)

# editorial = not reply, not link-only body
ed = [r for r in rows if not r['reply'] and not (r['link_body'] and not r['media'])]
print('editoriali n=', len(ed))
imps = [r['imp'] for r in ed]
print('mediana impressioni editoriali=', st.median(imps), 'media=', round(st.mean(imps), 1), 'min=', min(imps), 'max=', max(imps))

# per format
from collections import defaultdict
by = defaultdict(list)
for r in rows:
    by[r['fmt']].append(r['imp'])
for k, v in sorted(by.items(), key=lambda kv: -st.median(kv[1])):
    print(f'{k:24s} n={len(v):3d} mediana={st.median(v):7.1f} max={max(v)}')

# mediana per formato editoriale: immagine / prima risposta link / menzione / altro
print()
print('--- dettaglio editoriali per tipo ---')
ed_img = [r for r in ed if r['media']]
ed_txt = [r for r in ed if not r['media']]
print('con immagine  n=%d mediana=%s' % (len(ed_img), st.median([r['imp'] for r in ed_img]) if ed_img else None))
print('senza immagine n=%d mediana=%s' % (len(ed_txt), st.median([r['imp'] for r in ed_txt]) if ed_txt else None))

# clicks
def agg(field):
    vals = [r[field] for r in rows if r[field] is not None]
    return sum(vals), len(vals)

for f in ['org_prof', 'org_link', 'npm_prof', 'npm_link']:
    print(f, agg(f))

print('bookmark totali=', sum(r['bm'] for r in rows), 'like=', sum(r['like'] for r in rows), 'risposte(count)=', sum(r['rc'] for r in rows))
print('impressioni totali=', sum(r['imp'] for r in rows))
print('promoted impressions somma=', sum(r['prm_imp'] or 0 for r in rows))

# post per giorno
from collections import Counter
days = Counter(r['dt'].astimezone(timezone(timedelta(hours=1))).date().isoformat() for r in ed)
print()
print('--- editoriali per giorno ---')
for d in sorted(days, reverse=True):
    print(d, days[d])

# ultimi 7 giorni
cut = datetime.now(timezone.utc) - timedelta(days=7)
ed7 = [r for r in ed if r['dt'] >= cut]
print()
print('ultimi 7 gg: editoriali n=', len(ed7), 'mediana imp=', st.median([r['imp'] for r in ed7]) if ed7 else None)
print('risposte totali (nostre) n=', len([r for r in rows if r['reply'] and r['dt'] >= cut]))
print('link clicks org ultimi 7gg=', sum(r['org_link'] or 0 for r in rows if r['dt'] >= cut))
print('profile clicks org ultimi 7gg=', sum(r['org_prof'] or 0 for r in rows if r['dt'] >= cut))
print('bookmark ultimi 7gg=', sum(r['bm'] for r in rows if r['dt'] >= cut))

print()
print('--- top 5 e bottom 5 editoriali ---')
for r in sorted(ed, key=lambda x: -x['imp'])[:6]:
    print(r['imp'], r['dt'].isoformat(), r['fmt'], r['dm'] if 'dm' in r else '', r['text'][:80])
print('...')
for r in sorted(ed, key=lambda x: x['imp'])[:6]:
    print(r['imp'], r['dt'].isoformat(), r['fmt'], r['text'][:80])

json.dump([{k: (v.isoformat() if k == 'dt' else v) for k, v in r.items()} for r in rows],
          open('reports/x-2026-11-16/rows.json', 'w'), ensure_ascii=False, indent=1)
