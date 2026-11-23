import json, glob, os, re

base = "/root/.hermes/profiles/raziel-news/workspace/raziel-news/reports/.raw/2026-10-28"
report = "/root/.hermes/profiles/raziel-news/workspace/raziel-news/reports/2026-10-28-report.md"

index = {}
for f in glob.glob(os.path.join(base, "*.json")):
    d = json.load(open(f))
    users = {u["id"]: u["username"] for u in (d.get("includes", {}).get("users") or [])}
    for p in (d.get("data") or []):
        uname = users.get(p.get("author_id"))
        pm = p.get("public_metrics") or {}
        index.setdefault(p["id"], {"unames": set(), "snaps": []})
        index[p["id"]]["unames"].add(uname)
        index[p["id"]]["snaps"].append(pm)

text = open(report, encoding="utf-8").read()
blocks = re.split(r"\n### ", text)
errors, checked = [], 0

def num(s):
    return int(s.replace(".", "").replace("\u00a0", ""))

for b in blocks[1:]:
    title = b.split("\n")[0]
    m_acct = re.search(r"^- \*\*Account\*\*: @(\S+)", b, re.M)
    if not m_acct:
        continue
    handle = m_acct.group(1)
    m_link = re.search(r"^- \*\*Link\*\*: (.+)$", b, re.M)
    if not m_link:
        errors.append(f"{title}: riga Link mancante")
        continue
    m_url = re.search(r"https://x\.com/([^/]+)/status/(\d+)", m_link.group(1))
    if not m_url:
        errors.append(f"{title}: nessun URL x.com/status nella riga Link")
        continue
    user, pid = m_url.group(1), m_url.group(2)
    if pid not in index:
        errors.append(f"{title}: id {pid} non presente nei JSON grezzi")
        continue
    ent = index[pid]
    if user != handle:
        errors.append(f"{title}: username link ({user}) != Account ({handle})")
    if handle not in ent["unames"]:
        errors.append(f"{title}: id {pid} appartiene a {sorted(ent['unames'])}, non a {handle}")

    # data
    m_date = re.search(r"^- \*\*Data\*\*: (\d{4}-\d{2}-\d{2})", b, re.M)
    if m_date:
        dates = set()
        for f in glob.glob(os.path.join(base, "*.json")):
            d = json.load(open(f))
            for p in (d.get("data") or []):
                if p["id"] == pid:
                    dates.add(p["created_at"][:10])
        if m_date.group(1) not in dates:
            errors.append(f"{title}: Data {m_date.group(1)} != created_at {sorted(dates)}")

    # metriche
    m_met = re.search(r"^- \*\*Metriche\*\*: (.+)$", b, re.M)
    if m_met and "non disponibili" not in m_met.group(1):
        mnums = re.findall(r"([\d.]+) (like|repost|risposte|views)", m_met.group(1))
        if mnums:
            ok = False
            for snap in ent["snaps"]:
                want = {"like": snap.get("like_count", 0), "repost": snap.get("retweet_count", 0),
                        "risposte": snap.get("reply_count", 0), "views": snap.get("impression_count", 0)}
                if all(num(v) == want[k] for v, k in mnums):
                    ok = True
                    break
            if not ok:
                errors.append(f"{title}: Metriche {m_met.group(1)!r} non combaciano con alcuno snapshot {ent['snaps']}")
    checked += 1

# conteggi sezioni
def count(sec):
    m = re.search(r"## " + sec + r"\n(.*?)(?=\n## |\nItem:)", text, re.S)
    return len(re.findall(r"\n### ", m.group(1))) if m else -1

h, v, c = count("Hermes AI"), count("Venice.ai / VVV / DIEM"), count("Bitcoin & Crypto")
last = [l for l in text.strip().split("\n") if l.strip()][-1]
m_item = re.search(r"^Item: hermes=(\d+) venice=(\d+) crypto=(\d+)$", text, re.M)
m_stat = re.search(r"^<!-- report-status: (\d{4}-\d{2}-\d{2}) complete hermes=(\d+) venice=(\d+) crypto=(\d+) -->$", text, re.M)

print(f"blocchi X verificati: {checked}")
print(f"conteggi sezione: hermes={h} venice={v} crypto={c}")
print(f"riga Item: {m_item.groups() if m_item else 'MANCANTE'}")
print(f"riga status: {m_stat.groups() if m_stat else 'MANCANTE'}")
print(f"ultima riga: {last[:90]}")
if m_item and (int(m_item.group(1)), int(m_item.group(2)), int(m_item.group(3))) != (h, v, c):
    errors.append("conteggi Item != voci nelle sezioni")
if m_stat and (int(m_stat.group(2)), int(m_stat.group(3)), int(m_stat.group(4))) != (h, v, c):
    errors.append("conteggi report-status != voci nelle sezioni")
if not last.startswith("<!-- report-status"):
    errors.append("ultima riga non e' la riga report-status")
print("\nERRORI:", len(errors))
for e in errors:
    print(" -", e)
