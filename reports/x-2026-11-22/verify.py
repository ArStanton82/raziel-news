import json, glob, os, re, sys

base = "/root/.hermes/profiles/raziel-news/workspace/raziel-news"
raw = os.path.join(base, "reports/x-2026-11-22")
rep = os.path.join(base, "reports/2026-11-22-report.md")

posts = {}
for f in glob.glob(os.path.join(raw, "*.json")):
    try:
        d = json.load(open(f))
    except Exception:
        continue
    users = {u["id"]: u["username"] for u in (d.get("includes") or {}).get("users", []) or []}
    for p in d.get("data") or []:
        posts.setdefault(p["id"], []).append((users.get(p.get("author_id"), "?"), f.split("/")[-1],
                                              p.get("created_at"), p.get("public_metrics", {})))

txt = open(rep).read()
blocks = re.split(r"\n### ", txt)
problems = []
web_links = []
for b in blocks[1:]:
    title = b.split("\n")[0][:80]
    linkline = [l for l in b.split("\n") if l.startswith("- **Link**")]
    if not linkline:
        problems.append("NO LINK LINE: " + title)
        continue
    urls = re.findall(r"https?://[^\s;,]+", linkline[0])
    for u in urls:
        m = re.match(r"https://x\.com/([A-Za-z0-9_]+)/status/(\d+)", u)
        if m:
            user, pid = m.group(1), m.group(2)
            if pid not in posts:
                problems.append("ID NOT IN RAW: %s (%s)" % (pid, title))
            else:
                okuser = [x for x in posts[pid] if x[0].lower() == user.lower()]
                if not okuser:
                    problems.append("USER MISMATCH %s -> %s (%s)" % (pid, [x[0] for x in posts[pid]], title))
        else:
            web_links.append((u, title))

print("items:", len(blocks) - 1)
print("x ids checked:", sum(1 for b in blocks[1:] for l in b.split("\n") if l.startswith("- **Link**") for u in re.findall(r"x\.com/[A-Za-z0-9_]+/status/\d+", l)))
print("problems:", problems if problems else "none")
print("--- web links to check:", len(web_links))
for u, t in web_links:
    print(u)
print("--- tail ---")
print("\n".join(txt.rstrip().split("\n")[-3:]))
