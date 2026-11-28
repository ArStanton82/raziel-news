import json
d = json.load(open('gh-com.json'))
for c in d:
    msg = c['commit']['message'].split('\n')[0]
    print(c['sha'][:40], c['commit']['committer']['date'], msg[:100])
