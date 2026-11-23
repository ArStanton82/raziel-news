import json, glob, os, re

T = "2026-10-24"
RAW = "reports/raw-2026-10-24"

posts = {}
users = {}
for f in glob.glob(os.path.join(RAW, "*.json")):
    d = json.load(open(f))
    for u in (d.get("includes") or {}).get("users", []) or []:
        users[u["id"]] = u.get("username")
    for p in d.get("data", []) or []:
        posts.setdefault(p["id"], p)


def fmt(n):
    if n is None:
        return "n/d"
    return f"{n:,}".replace(",", ".")


text = open("reports/%s-report.md" % T, encoding="utf-8").read()
blocks = text.split("\n### ")[1:]
errors = []
xcount = 0
webcount = 0

for b in blocks:
    title = b.split("\n")[0].strip()
    # anchor on the Link line only (per pitfall note)
    mlink = re.search(r"^- \*\*Link\*\*: (.+)$", b, re.M)
    if not mlink:
        errors.append("blocco senza Link: " + title)
        continue
    links = [u.strip() for u in mlink.group(1).split("\u00b7")]
    md = re.search(r"^- \*\*Data\*\*: (\d{4}-\d{2}-\d{2})$", b, re.M)
    mm = re.search(r"^- \*\*Metriche\*\*: (.+)$", b, re.M)
    is_web = re.search(r"^- \*\*Fonte\*\*:", b, re.M) is not None
    if is_web:
        webcount += 1
        if len(links) < 2:
            errors.append("voce web con meno di 2 link: " + title)
        if not md:
            errors.append("voce web senza data: " + title)
        if not mm or mm.group(1).strip() != "non disponibili":
            errors.append("voce web con metriche diverse da 'non disponibili': " + title)
    else:
        xcount += 1
    for L in links:
        mm2 = re.match(r"https://x\.com/([A-Za-z0-9_]+)/status/(\d+)$", L)
        if not mm2:
            continue
        uname, pid = mm2.group(1), mm2.group(2)
        if pid not in posts:
            errors.append("id assente dai JSON: %s (%s)" % (pid, title))
            continue
        p = posts[pid]
        if users.get(p["author_id"]) != uname:
            errors.append("username non coerente per %s: file=%s json=%s" % (pid, uname, users.get(p["author_id"])))
        if not is_web and md and md.group(1) != p["created_at"][:10]:
            errors.append("data non coerente per %s: file=%s json=%s" % (pid, md.group(1), p["created_at"][:10]))
        if not is_web and mm and L == links[0]:
            pm = p.get("public_metrics") or {}
            exp = [f"like={fmt(pm.get('like_count'))}", f"repost={fmt(pm.get('retweet_count'))}",
                   f"risposte={fmt(pm.get('reply_count'))}"]
            if pm.get("impression_count"):
                exp.append(f"view={fmt(pm.get('impression_count'))}")
            if mm.group(1).strip() != " \u00b7 ".join(exp):
                errors.append("metriche non coerenti per %s:\n  file=%s\n  json=%s" % (pid, mm.group(1).strip(), " \u00b7 ".join(exp)))

last = text.rstrip().split("\n")[-1]
if not re.fullmatch(r"<!-- report-status: %s complete hermes=\d+ venice=\d+ crypto=\d+ -->" % T, last):
    errors.append("ultima riga non conforme al contratto: " + last)

itemline = [l for l in text.split("\n") if l.startswith("Item: ")][0]
print("BLOCCHI: %d (X: %d, web: %d)" % (len(blocks), xcount, webcount))
print(itemline)
print("ULTIMA RIGA:", last)
print("ERRORI:", len(errors))
for e in errors:
    print(" -", e)
