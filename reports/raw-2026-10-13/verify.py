#!/usr/bin/env python3
import json, glob, os, re

REPO = "/root/.hermes/profiles/raziel-news/workspace/raziel-news"
RAW = os.path.join(REPO, "reports/raw-2026-10-13")
REPORT = os.path.join(REPO, "reports/2026-10-13-report.md")

# build id -> (username, created_at, metrics)
index = {}
for path in glob.glob(os.path.join(RAW, "*.json")):
    try:
        d = json.load(open(path))
    except Exception:
        continue
    users = {u["id"]: u["username"] for u in d.get("includes", {}).get("users", [])}
    for p in d.get("data", []):
        index[p["id"]] = {
            "user": users.get(p.get("author_id"), "?"),
            "created": p.get("created_at", ""),
            "metrics": p.get("public_metrics", {}),
            "file": os.path.basename(path),
        }

text = open(REPORT).read()
links = re.findall(r"https://x\.com/([A-Za-z0-9_]+)/status/(\d+)", text)
print(f"link X trovati nel report: {len(links)}")
bad = 0
for un, sid in links:
    e = index.get(sid)
    if not e:
        print(f"  MANCANTE nei JSON: {un}/{sid}")
        bad += 1
        continue
    ok = "OK" if e["user"].lower() == un.lower() else "USERNAME-DIVERSO"
    if ok != "OK":
        bad += 1
    print(f"  {ok}: {un}/{sid} | json_user={e['user']} | {e['created']} | {e['file']}")

print()
print("--- controllo date/metriche delle voci X ---")
# spot-check specific claims
checks = [
    ("2109881066119151722", "2026-10-13", {"like": 52, "rt": 2, "imp": 3176}),
    ("2109826462178234558", "2026-10-13", {"like": 53, "rt": 1, "imp": 3197}),
    ("2109735914994020672", "2026-10-12", {"like": 51, "rt": 2, "imp": 3509}),
    ("2109781162680087015", "2026-10-12", {"like": 104, "rt": 4, "imp": 4411}),
    ("2109871756077129976", "2026-10-13", {"like": 24, "rt": 4, "imp": 1027}),
    ("2109449248156577953", "2026-10-12", {"like": 48, "rt": 6, "imp": 836}),
    ("2109731628746715496", "2026-10-12", {"like": 35, "rt": 2, "imp": 890}),
    ("2109626773826674987", "2026-10-12", {"like": 31, "rt": 2, "imp": 687}),
    ("2109864226538107058", "2026-10-13", {"like": 4, "rt": 0, "imp": 390}),
    ("2109601020011798932", "2026-10-12", {"like": 209, "rt": 29, "imp": 13175}),
    ("2107886262237761740", "2026-10-07", {"like": 103, "rt": 9, "imp": 1783}),
    ("2109648410475192486", "2026-10-12", {"like": 93, "rt": 10, "imp": 36177}),
    ("2109751997268176955", "2026-10-12", {"like": 747, "rt": 81, "imp": 54874}),
    ("2109727532845076573", "2026-10-12", {"like": 1726, "rt": 234, "imp": 78488}),
    ("2109584821043482720", "2026-10-12", {"like": 401, "rt": 55, "imp": 61447}),
    ("2109662163170124208", "2026-10-12", {"like": 734, "rt": 88, "imp": 76554}),
    ("2109886798898098551", "2026-10-13", {"like": 11, "rt": 0, "imp": 4620}),
]
for sid, want_date, want_m in checks:
    e = index.get(sid)
    if not e:
        print(f"  MANCANTE {sid}")
        bad += 1
        continue
    pm = e["metrics"]
    got_date = e["created"][:10]
    got_m = {"like": pm.get("like_count"), "rt": pm.get("retweet_count"), "imp": pm.get("impression_count")}
    status = "OK" if (got_date == want_date and got_m == want_m) else "DIVERSO"
    if status != "OK":
        bad += 1
    print(f"  {status} {sid} data={got_date}(attesa {want_date}) metriche={got_m}(attese {want_m})")

print()
print("--- contratto finale ---")
last = [l for l in text.strip().splitlines() if l.strip()][-1]
print("ultima riga:", last)
print("match:", bool(re.fullmatch(r"<!-- report-status: 2026-10-13 complete hermes=8 venice=8 crypto=8 -->", last)))
print("Item line ok:", "Item: hermes=8 venice=8 crypto=8" in text)
print()
print(f"TOTALE PROBLEMI: {bad}")
