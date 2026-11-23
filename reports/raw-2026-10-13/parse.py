#!/usr/bin/env python3
import json, glob, os, datetime

BASE = os.path.dirname(os.path.abspath(__file__))

def load(path):
    try:
        with open(path) as f:
            return json.load(f)
    except Exception as e:
        return {"__error__": str(e)}

for path in sorted(glob.glob(os.path.join(BASE, "*.json"))):
    name = os.path.basename(path)
    d = load(path)
    if "__error__" in d:
        print(f"### {name}: ERRORE {d['__error__']}")
        continue
    users = {u["id"]: u["username"] for u in d.get("includes", {}).get("users", [])}
    data = d.get("data", [])
    print(f"### {name} — {len(data)} post")
    for p in data:
        uid = p.get("author_id")
        un = users.get(uid, "?")
        pm = p.get("public_metrics", {})
        txt = p.get("text", "").replace("\n", " ")
        print(f"  [{un}] {p.get('created_at','?')} id={p.get('id')}")
        print(f"     {txt[:400]}")
        print(f"     like={pm.get('like_count')} rt={pm.get('retweet_count')} imp={pm.get('impression_count')}")
    print()
