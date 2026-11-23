import json, statistics as st
from datetime import datetime, timedelta, timezone

CET = timezone(timedelta(hours=1))
rows = json.load(open('reports/x-2026-11-16/rows.json'))
for r in rows:
    r['dt'] = datetime.fromisoformat(r['dt'])
now = datetime(2026, 11, 16, 8, 0, tzinfo=timezone.utc)
FOLL = 408
ed = [r for r in rows if not r['reply'] and not (r['link_body'] and not r['media'])]
w1 = [r for r in ed if now - timedelta(days=7) <= r['dt'] < now]
w0 = [r for r in ed if now - timedelta(days=14) <= r['dt'] < now - timedelta(days=7)]

m_all = st.median([r['imp'] for r in ed])
m1 = st.median([r['imp'] for r in w1])
m0 = st.median([r['imp'] for r in w0])
print('mediane editoriale: finestra %.1f | settimana %.1f | settimana prima %.1f' % (m_all, m1, m0))
print('reach: finestra %.2f%% | settimana %.2f%% | prima %.2f%%' % (100 * m_all / FOLL, 100 * m1 / FOLL, 100 * m0 / FOLL))
print('risposte umane/post settimana: %.2f' % (2 / 17))
print('post/giorno: automatici 14/7=%.2f | tutti 17/7=%.2f' % (14 / 7, 17 / 7))
print('delta settimana prima->questa: %.1f%%' % (100 * (m1 - m0) / m0))
print('bookmark mese: 0 su %d post (finestra 19 giorni)' % len(rows))
print('click profilo 7gg 4 -> soglia 40 = %.1f%% ; link 2 -> 15 = %.1f%%' % (100 * 4 / 40, 100 * 2 / 15))
print('slot settimana: mattutino 7 post mediana %s ; giornata 8 post mediana %s' % (
    st.median([r['imp'] for r in w1 if r['dt'].astimezone(CET).hour < 11]),
    st.median([r['imp'] for r in w1 if 11 <= r['dt'].astimezone(CET).hour < 17])))
