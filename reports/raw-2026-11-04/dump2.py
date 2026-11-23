import json, glob, os
base = os.path.dirname(os.path.abspath(__file__))
want = {'2117859876861051116','2117865948090609878'}
for f in glob.glob(os.path.join(base,'*.json')):
    try:
        d = json.load(open(f))
    except Exception:
        continue
    users = {u['id']: u['username'] for u in d.get('includes',{}).get('users',[])}
    for t in d.get('data',[]):
        if t['id'] in want:
            m = t.get('public_metrics',{})
            print('###', t['id'], '@'+users.get(t.get('author_id'),'?'), t.get('created_at'), 'L=%s RT=%s V=%s' % (m.get('like_count'), m.get('retweet_count'), m.get('impression_count')))
            print(t.get('text',''))
            print()
