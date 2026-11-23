import json, glob, re, sys

# snapshots: id -> list of (user, created, like, rt, views)
snap = {}
for path in glob.glob("reports/.raw/*.json"):
    try:
        d = json.load(open(path))
    except Exception:
        continue
    users = {u["id"]: u["username"] for u in (d.get("includes") or {}).get("users", [])}
    for p in d.get("data") or []:
        pm = p.get("public_metrics") or {}
        snap.setdefault(p["id"], []).append(
            (users.get(p.get("author_id"), "?"), p.get("created_at", "")[:10],
             pm.get("like_count"), pm.get("retweet_count"), pm.get("impression_count"))
        )

txt = open("reports/2026-10-20-report.md", encoding="utf-8").read()
blocks = re.split(r"\n### ", txt)[1:]
errors = []
checked = 0

def fmt(n):
    return f"{n:,}".replace(",", ".")

for b in blocks:
    title = b.splitlines()[0].strip()
    links = [l for l in b.splitlines() if l.strip().startswith("- **Link**:")]
    if not links:
        errors.append(f"[{title}] nessuna riga Link")
        continue
    linkline = links[0]
    xurls = re.findall(r"https?://x\.com/([A-Za-z0-9_]+)/status/(\d+)", linkline)
    dataline = [l for l in b.splitlines() if l.strip().startswith("- **Data**:")]
    date = dataline[0].split(":", 1)[1].strip() if dataline else ""
    mline = [l for l in b.splitlines() if l.strip().startswith("- **Metriche**:")]
    metrics = mline[0].split(":", 1)[1].strip() if mline else ""

    for user, pid in xurls:
        checked += 1
        if pid not in snap:
            errors.append(f"[{title}] id {pid} NON presente nei JSON")
            continue
        snaps = snap[pid]
        if user not in [s[0] for s in snaps]:
            errors.append(f"[{title}] username @{user} non corrisponde per id {pid} ({snaps})")
            continue
        if date and date not in [s[1] for s in snaps]:
            errors.append(f"[{title}] data {date} != {snaps[0][1]} per id {pid}")
        # metrics: find a snapshot whose rendered numbers all appear in the item metrics line
        norm = metrics.replace(".", "")
        found = False
        for s in snaps:
            nums = [n for n in s[2:] if n is not None]
            ok = all(str(n) in norm for n in nums) if nums else True
            if ok:
                found = True
                break
        if not found:
            errors.append(f"[{title}] metriche '{metrics}' non combaciano con nessuno snapshot di {pid}: {snaps}")

print("blocchi:", len(blocks), "link X verificati:", checked)
if errors:
    print("ERRORI:")
    for e in errors:
        print(" -", e)
else:
    print("OK: tutti i link X verificati")

last = [l for l in txt.strip().splitlines() if l.strip()][-3:]
print("ULTIME RIGHE:")
for l in last:
    print(l)
for sec in ["## Hermes AI", "## Venice.ai / VVV / DIEM", "## Bitcoin & Crypto"]:
    part = txt.split(sec)[1]
    nxt = [p for p in ["## Venice.ai", "## Bitcoin"] if p in part]
    n = len(re.findall(r"\n### \d+\.", part if not nxt else part.split(nxt[0])[0]))
    print(sec, "->", n)
