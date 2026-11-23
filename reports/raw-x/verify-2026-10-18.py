import json, glob, os, re, sys

BASE = "/root/.hermes/profiles/raziel-news/workspace/raziel-news/reports/raw-x"
REPORT = "/root/.hermes/profiles/raziel-news/workspace/raziel-news/reports/2026-10-18-report.md"
DATE = "2026-10-18"

# 1) indice di tutti i post reali dai JSON grezzi (snapshot multipli ammessi)
snapshots = {}
for f in glob.glob(os.path.join(BASE, DATE + "-*.json")):
    try:
        d = json.load(open(f, encoding="utf-8"))
    except Exception as e:
        print("PARSE FAIL", f, e)
        continue
    users = {}
    for u in (d.get("includes") or {}).get("users") or []:
        users[u["id"]] = u["username"]
    for p in d.get("data") or []:
        pid = p.get("id")
        un = users.get(p.get("author_id"))
        m = p.get("public_metrics") or {}
        snapshots.setdefault(pid, []).append({
            "user": un, "created_at": p.get("created_at"), "text": p.get("text"),
            "likes": m.get("like_count"), "rt": m.get("retweet_count"),
            "replies": m.get("reply_count"), "views": m.get("impression_count"),
            "file": os.path.basename(f)})

# 2) blocchi del report
text = open(REPORT, encoding="utf-8").read()
lines = text.split("\n")
blocks, cur, section = [], None, None
for ln in lines:
    if ln.startswith("## "):
        section = ln[3:].strip()
    if ln.startswith("### "):
        if cur:
            blocks.append(cur)
        cur = {"title": ln[4:].strip(), "section": section, "lines": []}
    if cur is not None:
        cur["lines"].append(ln)
if cur:
    blocks.append(cur)

problems = []
x_urls_total = 0
for b in blocks:
    body = "\n".join(b["lines"])
    ids = re.findall(r"x\.com/([A-Za-z0-9_]+)/status/(\d+)", body)
    x_urls_total += len(ids)
    kind = "X" if re.search(r"- \*\*Account\*\*:", body) else "WEB"
    linkline = [l for l in b["lines"] if l.startswith("- **Link**:")]
    if not linkline:
        problems.append("%s [%s] manca la riga Link" % (b["title"], kind))
        continue
    linkids = re.findall(r"x\.com/([A-Za-z0-9_]+)/status/(\d+)", linkline[0])
    web_links = re.findall(r"https?://[^\s;]+", linkline[0])
    if kind == "X" and not linkids:
        problems.append("%s [X] la riga Link non contiene un post X" % b["title"])
    if kind == "WEB" and len([u for u in web_links if "x.com" not in u]) < 2:
        problems.append("%s [WEB] meno di 2 link web indipendenti" % b["title"])
    # ogni id citato nel blocco deve esistere con lo username giusto
    for un, pid in ids:
        if pid not in snapshots:
            problems.append("%s: id %s NON presente nei JSON grezzi" % (b["title"], pid))
            continue
        users = set(s["user"] for s in snapshots[pid])
        if un not in users:
            problems.append("%s: username %s != %s nei JSON" % (b["title"], un, users))
    # data
    dl = [l for l in b["lines"] if l.startswith("- **Data**:")]
    if dl:
        claimed = dl[0].split(":", 1)[1].strip()
        ok = False
        for un, pid in ids:
            for s in snapshots.get(pid, []):
                if s["created_at"] and s["created_at"][:10] == claimed:
                    ok = True
        if ids and not ok:
            problems.append("%s: Data %s non combacia con created_at" % (b["title"], claimed))
    # metriche
    ml = [l for l in b["lines"] if l.startswith("- **Metriche**:")]
    if ml and ids:
        nums = re.findall(r"(likes|repost|risposte|views)=(\d+)", ml[0])
        if nums:
            cand = None
            for un, pid in ids:
                for s in snapshots.get(pid, []):
                    if (s["likes"], s["rt"], s["replies"], s["views"]) == tuple(
                            int(v) for _, v in nums[:4]):
                        cand = (pid, s["file"])
            if not cand:
                problems.append("%s: metriche %s non trovate in alcuno snapshot" % (b["title"], nums))

print("blocchi:", len(blocks), "| link X totali nel report:", x_urls_total)
print("post unici indicizzati:", len(snapshots))
sec = {}
for b in blocks:
    sec[b["section"]] = sec.get(b["section"], 0) + 1
print("conteggio per sezione:", sec)
last = [l for l in lines if l.strip()][-1]
print("ultima riga:", last)
print("--- PROBLEMI ---")
print("\n".join(problems) if problems else "nessuno")
