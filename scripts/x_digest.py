"""Legge un JSON di xurl (search o timeline) e stampa i post ordinati per like.

Uso: python3 scripts/x_digest.py FILE [--min-like N] [--top N]
Non fa chiamate di rete: lavora solo sul file gia' salvato.
"""
import json
import sys


def carica(path):
    with open(path, "r", encoding="utf-8") as fh:
        raw = fh.read()
    try:
        return json.loads(raw)
    except json.JSONDecodeError:
        return None


def main():
    args = sys.argv[1:]
    if not args:
        print("serve un file")
        return
    path = args[0]
    top = 20
    min_like = 0
    if "--top" in args:
        top = int(args[args.index("--top") + 1])
    if "--min-like" in args:
        min_like = int(args[args.index("--min-like") + 1])

    data = carica(path)
    if data is None:
        print(f"NON-JSON: {path} (errore o output non parsabile)")
        return
    if "errors" in data and "data" not in data:
        print("ERRORI API:")
        for err in data["errors"]:
            print(" -", err.get("title"), "/", err.get("detail"))
        return

    items = data.get("data") or []
    rows = []
    for it in items:
        m = it.get("public_metrics") or {}
        note = (it.get("note_tweet") or {}).get("text")
        text = note or it.get("text") or ""
        text = " ".join(text.split())
        rows.append(
            {
                "created": it.get("created_at", ""),
                "like": m.get("like_count", 0),
                "rt": m.get("retweet_count", 0),
                "rep": m.get("reply_count", 0),
                "qt": m.get("quote_count", 0),
                "views": m.get("impression_count", 0),
                "author": (it.get("author_id") or ""),
                "id": it.get("id", ""),
                "text": text,
            }
        )
    rows = [r for r in rows if r["like"] >= min_like]
    rows.sort(key=lambda r: (r["like"], r["views"]), reverse=True)
    meta = data.get("meta") or {}
    print(f"{path}: {len(items)} post (result_count={meta.get('result_count')})")
    for r in rows[:top]:
        print(
            f"[{r['created'][:16]}] like={r['like']} rt={r['rt']} rep={r['rep']} qt={r['qt']} views={r['views']} id={r['id']}"
        )
        print(f"   {r['text'][:900]}")
        print("")


if __name__ == "__main__":
    main()
