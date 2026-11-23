import json, re

BASE = '/root/.hermes/profiles/raziel-news/workspace/raziel-news'
items = json.load(open(f'{BASE}/reports/raw-2026-11-15/all.json'))
idx = {}
for it in items:
    idx[it['id']] = it

def fmt(n):
    return f"{n:,}".replace(",", ".")

def expected_metrics(it):
    m = it.get('metrics') or {}
    parts = []
    if m.get('like_count') is not None:
        parts.append(f"{fmt(m['like_count'])} like")
    if m.get('retweet_count') is not None:
        parts.append(f"{fmt(m['retweet_count'])} repost")
    v = m.get('impression_count') or 0
    if v:
        parts.append(f"{fmt(v)} visualizzazioni")
    return " · ".join(parts)

txt = open(f'{BASE}/reports/2026-11-15-report.md').read()
blocks = re.split(r'\n### ', txt)
errors = []
checked = 0
web_entries = 0
for b in blocks[1:]:
    title = b.split('\n', 1)[0]
    if '**Account**:' in b:
        acc = re.search(r'- \*\*Account\*\*: @([A-Za-z0-9_]+)', b).group(1)
        linkline = [l for l in b.split('\n') if l.startswith('- **Link**')][0]
        m = re.search(r'https://x\.com/([A-Za-z0-9_]+)/status/(\d+)', linkline)
        if not m:
            errors.append(f"{title}: nessun link X trovato")
            continue
        user, pid = m.group(1), m.group(2)
        it = idx.get(pid)
        if not it:
            errors.append(f"{title}: id {pid} assente nei JSON grezzi")
            continue
        if it['user'] != user or acc != user:
            errors.append(f"{title}: username mismatch acc={acc} link={user} json={it['user']}")
        dateline = re.search(r'- \*\*Data\*\*: (\d{4}-\d{2}-\d{2})', b).group(1)
        jsondate = (it['created_at'] or '')[:10]
        if dateline != jsondate:
            errors.append(f"{title}: data {dateline} != json {jsondate}")
        metline = re.search(r'- \*\*Metriche\*\*: (.*)', b).group(1).strip()
        exp = expected_metrics(it)
        if metline != exp:
            errors.append(f"{title}: metriche '{metline}' != attese '{exp}'")
        checked += 1
    elif '**Fonte**:' in b:
        web_entries += 1
        linkline = [l for l in b.split('\n') if l.startswith('- **Link**')][0]
        urls = re.findall(r'https?://[^\s;]+', linkline)
        if len(urls) < 2:
            errors.append(f"{title}: voci web con meno di 2 link ({len(urls)})")
        if not re.search(r'- \*\*Data\*\*: \d{4}-\d{2}-\d{2}', b):
            errors.append(f"{title}: data mancante o malformata")
        if '- **Metriche**: non disponibili' not in b:
            errors.append(f"{title}: metriche web non 'non disponibili'")

print("blocchi X verificati:", checked, "| voci web:", web_entries)
print("ERRORI:", len(errors))
for e in errors:
    print(" -", e)

last = [l for l in txt.strip().split('\n') if l.strip()][-1]
print("ULTIMA RIGA:", last)
print("ok-status:", bool(re.search(r'<!-- report-status: 2026-11-15 complete hermes=5 venice=7 crypto=7 -->', last)))
