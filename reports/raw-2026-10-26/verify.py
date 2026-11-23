import json, glob, os, re

RAW = "/root/.hermes/profiles/raziel-news/workspace/raziel-news/reports/raw-2026-10-26"
F = "/root/.hermes/profiles/raziel-news/workspace/raziel-news/reports/2026-10-26-report.md"
TODAY = "2026-10-26"

# ogni id -> lista di snapshot (public_metrics, created_at, username)
snaps = {}
users = {}
for f in glob.glob(os.path.join(RAW, "*.json")):
    try:
        j = json.load(open(f))
    except Exception:
        continue
    for u in (j.get("includes") or {}).get("users") or []:
        users[u["id"]] = u["username"]
    for p in j.get("data") or []:
        snaps.setdefault(p["id"], []).append(p)

text = open(F).read()
blocks = text.split("\n### ")[1:]
errs = []
ok = 0
for b in blocks:
    head = b.split("\n")[0]
    is_web = "- **Fonte**:" in b
    link_line = [l for l in b.split("\n") if l.startswith("- **Link**:")]
    met_line = [l for l in b.split("\n") if l.startswith("- **Metriche**:")]
    date_line = [l for l in b.split("\n") if l.startswith("- **Data**:")]
    if not link_line:
        errs.append("BLOCK senza Link: " + head)
        continue
    links = [x.strip() for x in link_line[0].replace("- **Link**:", "").split(";")]
    if is_web:
        if len(links) < 2:
            errs.append("WEB con meno di 2 link: " + head)
        for l in links:
            if "x.com/" in l:
                errs.append("WEB con link x.com: " + head)
        if met_line and met_line[0].strip() != "- **Metriche**: non disponibili":
            errs.append("WEB con metriche non 'non disponibili': " + head)
        ok += 1
        continue
    acc = re.search(r"- \*\*Account\*\*: @(\S+)", b)
    if not acc:
        errs.append("X senza account: " + head)
        continue
    acc = acc.group(1)
    date_rep = date_line[0].replace("- **Data**:", "").strip() if date_line else ""
    met_rep = met_line[0].replace("- **Metriche**:", "").strip() if met_line else ""
    for l in links:
        m = re.search(r"https://x\.com/([^/]+)/status/(\d+)", l)
        if not m:
            errs.append("link X malformato: %s (%s)" % (l, head))
            continue
        un_doc, pid = m.group(1), m.group(2)
        if pid not in snaps:
            errs.append("id assente dai JSON: %s (%s)" % (pid, head))
            continue
        if un_doc != users.get(snaps[pid][0].get("author_id"), "?"):
            errs.append("username non coincidente per %s: %s vs %s" % (pid, un_doc, users.get(snaps[pid][0].get("author_id"))))
        if un_doc != acc and l.strip() == links[0].strip():
            errs.append("account della voce != autore del primo link: %s vs %s (%s)" % (acc, un_doc, head))
    # metriche vs almeno uno snapshot del primo id
    pid0 = re.search(r"/status/(\d+)", links[0]).group(1)
    found_met = False
    for p in snaps.get(pid0, []):
        pm = p.get("public_metrics") or {}
        cand = []
        if pm.get("like_count") is not None:
            cand.append("like %s" % pm["like_count"])
        if pm.get("retweet_count") is not None:
            cand.append("repost %s" % pm["retweet_count"])
        if pm.get("reply_count") is not None:
            cand.append("risposte %s" % pm["reply_count"])
        if pm.get("bookmark_count"):
            cand.append("bookmark %s" % pm["bookmark_count"])
        if pm.get("impression_count"):
            cand.append("views %s" % pm["impression_count"])
        if " · ".join(cand) == met_rep:
            found_met = True
    if not found_met:
        errs.append("metriche non combaciano con alcuno snapshot: %s -> '%s'" % (pid0, met_rep))
    # data vs created_at del primo id
    d0 = snaps.get(pid0, [{}])[0].get("created_at", "")[:10]
    if d0 != date_rep:
        errs.append("data non coincidente: report %s vs json %s (%s)" % (date_rep, d0, pid0))
    ok += 1

# controlli di coda
tail = [l for l in text.rstrip().split("\n") if l.strip()]
if not re.match(r"^<!-- report-status: %s complete hermes=\d+ venice=\d+ crypto=\d+ -->$" % TODAY, tail[-1]):
    errs.append("ultima riga non conforme: " + tail[-1])
if not re.match(r"^Item: hermes=\d+ venice=\d+ crypto=\d+$", tail[-3]):
    errs.append("riga Item non conforme: " + tail[-3])
if not text.startswith("# Report — %s\nData: %s\n" % (TODAY, TODAY)):
    errs.append("intestazione non conforme")
# conteggi coerenti
cnt = {"hermes": 0, "venice": 0, "crypto": 0}
for sec, key in [("## Hermes AI", "hermes"), ("## Venice.ai / VVV / DIEM", "venice"), ("## Bitcoin & Crypto", "crypto")]:
    part = text.split(sec)[1].split("\n## ")[0]
    cnt[key] = len(re.findall(r"\n### \d+\. ", part))
declared = re.search(r"Item: hermes=(\d+) venice=(\d+) crypto=(\d+)", text)
for k, i in [("hermes", 1), ("venice", 2), ("crypto", 3)]:
    if int(declared.group(i)) != cnt[k]:
        errs.append("conteggio %s dichiarato %s vs reale %s" % (k, declared.group(i), cnt[k]))

print("blocchi verificati:", ok, "| conteggi:", cnt)
print("errori:", len(errs))
for e in errs:
    print(" -", e)
