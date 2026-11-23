import json, glob, os, re

BASE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(BASE))
TODAY = "2026-10-09"
dest = os.path.join(REPO, "reports", f"{TODAY}-report.md")

X = {}
for path in glob.glob(os.path.join(BASE, "*.json")):
    try:
        d = json.load(open(path, encoding="utf-8"))
    except Exception:
        continue
    users = {u["id"]: u.get("username") for u in d.get("includes", {}).get("users", [])}
    for p in d.get("data", []):
        X[p["id"]] = (users.get(p.get("author_id"), "?"), p.get("public_metrics", {}), (p.get("created_at") or "")[:10])

text = open(dest, encoding="utf-8").read()
links = re.findall(r"https://x\.com/([A-Za-z0-9_]+)/status/(\d+)", text)
print(f"link X trovati: {len(links)}")
bad = 0
for user, tid in links:
    if tid not in X:
        print(f"  ERRORE: id {tid} non presente nei JSON"); bad += 1; continue
    juser, m, d = X[tid]
    if juser != user:
        print(f"  ERRORE: username {user} != {juser} per id {tid}"); bad += 1
    else:
        print(f"  OK {tid} @{user} {d} like={m.get('like_count')} rt={m.get('retweet_count')} imp={m.get('impression_count')}")

# check metrics strings present in file match
for tid, (user, m, d) in X.items():
    if tid in text:
        exp = f"like {m.get('like_count')} \u00b7 repost {m.get('retweet_count')}"
        if exp not in text:
            print(f"  CHECK metriche: '{exp}' non trovato nel file (id {tid})")

print("\nultime 3 righe:")
for line in text.rstrip().splitlines()[-3:]:
    print("  " + line)
print("\nbad:", bad)
print("conteggio voci: hermes=%d venice=%d crypto=%d" % (
    text.count("### ") - text.count("### "), 0, 0))
import collections
secs = re.findall(r"^## (.+)$", text, re.M)
print("sezioni:", secs)
h = len(re.findall(r"^### \d+\.", text, re.M))
print("voci totali (### N.):", h)
