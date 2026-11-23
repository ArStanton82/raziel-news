import json, glob, os
from datetime import datetime
files = sorted(glob.glob('/root/.hermes/profiles/raziel-news/x-queue/2026-1*.json'))
for f in files[-12:]:
    try:
        d = json.load(open(f))
    except Exception as e:
        print(f, 'ERR', e); continue
    posts = d if isinstance(d, list) else d.get('posts', d.get('drafts', []))
    print('==', os.path.basename(f), 'n=', len(posts) if isinstance(posts, list) else type(posts))
    if isinstance(posts, list):
        for p in posts:
            print('   slot=%-10s status=%-8s publ=%-24s appr=%s id=%s' % (
                p.get('slot'), p.get('status'), str(p.get('published_at'))[:19], p.get('approved'), p.get('published_tweet_id')))
