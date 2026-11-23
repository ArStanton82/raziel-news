import json, glob, os, re

RAW = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(RAW, "..", ".."))
TODAY = "2026-10-10"
report = open(os.path.join(REPO, "reports", "%s-report.md" % TODAY), encoding="utf-8").read()

# index all posts: id -> username, and metrics/created
idx = {}
for path in glob.glob(os.path.join(RAW, "*.json")):
    d = json.load(open(path, encoding="utf-8"))
    users = {u["id"]: u.get("username") for u in d.get("includes", {}).get("users", [])}
    for p in d.get("data", []):
        idx[p.get("id")] = {
            "user": users.get(p.get("author_id")),
            "metrics": p.get("public_metrics", {}),
            "created": p.get("created_at", "")[:10],
        }

errors = []
xlinks = re.findall(r"https://x\.com/([A-Za-z0-9_]+)/status/(\d+)", report)
print("X links found in report:", len(xlinks))
for user, pid in xlinks:
    if pid not in idx:
        errors.append("id %s NOT in raw JSON" % pid)
        continue
    if idx[pid]["user"] != user:
        errors.append("id %s username mismatch: report=%s json=%s" % (pid, user, idx[pid]["user"]))

# check metrics lines vs json
for m in re.finditer(r"https://x\.com/([A-Za-z0-9_]+)/status/(\d+)\n- \*\*Metriche\*\*: ([^\n]+)", report):
    user, pid, met = m.group(1), m.group(2), m.group(3)
    if pid not in idx:
        continue
    pm = idx[pid]["metrics"]
    exp = "like=%s, repost=%s" % (pm.get("like_count", 0), pm.get("retweet_count", 0))
    imp = pm.get("impression_count", 0)
    if imp:
        exp += ", views=%s" % imp
    if met.strip() != exp:
        errors.append("metrics mismatch id %s: report='%s' expected='%s'" % (pid, met.strip(), exp))

# check dates
for m in re.finditer(r"### \d+\. [^\n]+\n- \*\*Account\*\*: @([A-Za-z0-9_]+)\n- \*\*Data\*\*: (\d{4}-\d{2}-\d{2})\n[^\n]*\n- \*\*Link\*\*: https://x\.com/[A-Za-z0-9_]+/status/(\d+)", report):
    user, date, pid = m.group(1), m.group(2), m.group(3)
    if pid in idx and idx[pid]["created"] != date:
        errors.append("date mismatch id %s: report=%s json=%s" % (pid, date, idx[pid]["created"]))

# footer check
last = [l for l in report.strip().splitlines() if l.strip()][-1]
exp_last = "<!-- report-status: %s complete hermes=7 venice=7 crypto=8 -->" % TODAY
if last != exp_last:
    errors.append("last line mismatch: '%s'" % last)

# header check
if not report.startswith("# Report — %s\nData: %s" % (TODAY, TODAY)):
    errors.append("header mismatch")

print("errors:", len(errors))
for e in errors:
    print("  -", e)
