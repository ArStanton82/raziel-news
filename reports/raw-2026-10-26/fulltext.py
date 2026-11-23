import json, glob, os

d = "/root/.hermes/profiles/raziel-news/workspace/raziel-news/reports/raw-2026-10-26"
want = ["2114582798866726989", "2114595512137752671", "2114530795868373035", "2114529595617931403",
        "2114365481801130315", "2114409306162376923", "2114608206483779620", "2114534202788225513",
        "2114349790792417617", "2114205312727302338", "2114613208590016742", "2114457575408259084",
        "2114358677490512296", "2114367268369117525", "2114607210877821024"]
found = {}
for f in glob.glob(os.path.join(d, "*.json")):
    try:
        j = json.load(open(f))
    except Exception:
        continue
    for p in j.get("data") or []:
        if p.get("id") in want:
            found.setdefault(p["id"], p)
for i in want:
    p = found.get(i)
    if not p:
        print("MISSING", i)
        continue
    print("=" * 60)
    print("id", i, p.get("created_at"))
    print(p.get("text"))
    print("metrics", p.get("public_metrics"))
