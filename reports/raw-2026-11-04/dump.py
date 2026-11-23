import json, glob, os
base = os.path.dirname(os.path.abspath(__file__))
want = {
 '2117696344756252822','2117859453496389694','2117807901112926465','2117740189577785598',
 '2117596013204811950','2117596079449612605','2117596045614178336','2117344256558027225',
 '2117653739171409954','2117637883523960881','2117272224814219720','2117744680079372429',
 '2117728088809488686','2117832738543997116','2117861618373865794','2117768445123088463',
}
found = {}
for f in glob.glob(os.path.join(base,'*.json')):
    try:
        d = json.load(open(f))
    except Exception:
        continue
    users = {u['id']: u['username'] for u in d.get('includes',{}).get('users',[])}
    for t in d.get('data',[]):
        if t['id'] in want and t['id'] not in found:
            m = t.get('public_metrics',{})
            found[t['id']] = (users.get(t.get('author_id'),'?'), t.get('created_at'), m, t.get('text',''))
for i in sorted(want):
    if i in found:
        u, ca, m, tx = found[i]
        print('### %s @%s %s L=%s RT=%s V=%s' % (i, u, ca, m.get('like_count'), m.get('retweet_count'), m.get('impression_count')))
        print(tx)
        print()
    else:
        print('### MISSING', i)
