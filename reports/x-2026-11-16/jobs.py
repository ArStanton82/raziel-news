import json, re
J = json.load(open('/root/.hermes/profiles/raziel-news/cron/jobs.json'))
jobs = J if isinstance(J, list) else J.get('jobs', J)
if isinstance(jobs, dict):
    jobs = list(jobs.values())
for j in jobs:
    name = j.get('name') or j.get('id')
    if 'x-' in str(name) or 'x' == str(j.get('id'))[:1]:
        pass
    print('---', name, '|', j.get('schedule'), '| enabled=', j.get('enabled'))
    p = str(j.get('prompt', ''))
    for line in p.split('\n'):
        if re.search(r'\d{1,2}[:.]\d{2}|mattutino|serale|20:15|08:15|tetto', line):
            print('   ', line.strip()[:220])
