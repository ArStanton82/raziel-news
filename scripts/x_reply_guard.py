#!/usr/bin/env python3
"""Guardia per le bozze di risposta X di raziel.news.

Verifica in modo meccanico che una bozza di risposta rispetti le regole della
strategia (reports/x-strategy.md, sezione 6) prima che possa essere pubblicata.
Serve a distinguere le risposte "di sostanza" dall'engagement fabbricato: solo
le bozze che passano tutti i controlli sono candidate alla pubblicazione.

Uso:
    python3 scripts/x_reply_guard.py <file-replies.json> [--json]

Esce con 0 se tutte le bozze passano, 1 se almeno una fallisce.
Non pubblica nulla: legge, valuta, stampa.
"""

from __future__ import annotations

import argparse
import difflib
import glob
import json
import os
import re
import sys
import unicodedata

QUEUE_DIR = "/root/.hermes/profiles/raziel-news/x-queue"

MAX_LEN = 220            # limite della strategia per le risposte
MIN_LEN = 110            # sotto questa soglia non c'e' spazio per un dato
MAX_PER_ACCOUNT_DAY = 1  # mai due risposte allo stesso account nello stesso giorno
MAX_PER_DAY = 6          # tetto giornaliero complessivo
SIMILARITY_MAX = 0.75    # somiglianza massima con una risposta gia' pubblicata

# Frasi di riempimento: se compaiono, la bozza non e' una risposta di sostanza.
BLOCKLIST = [
    "ottimo post", "gran post", "bel post", "complimenti", "bravo", "brava",
    "sono d'accordo", "totalmente d'accordo", "esatto", "quoto",
    "great post", "nice post", "well said", "love this", "so true",
    "couldn't agree more", "thanks for sharing", "this!", "spot on",
    "amazing", "awesome", "fantastic", "interesting take", "good point",
]

# Marcatori di sostanza: contrasto, causa, condizione, quantita'.
MARKERS = [
    " ma ", " pero'", " però", " invece", " tranne", " solo se", " finche",
    " finché", " perche", " perché", " significa", " vuol dire", " costa",
    " dipende", " il punto", " il numero", " resta", " manca", " non basta",
    " but ", " however", " unless", " only if", " the point", " the number",
    " which means", " depends", " costs", " instead", " while ", " that's why",
    "the hard part", " earns its", ", not ", " is not ", " isn't ", " aren't ",
    " rather than", " instead of", " non e'", " non è ", " ma non ",
]

LINK_RE = re.compile(r"(https?://|www\.|raziel\.news|t\.me/|\.com/|\.news/)", re.I)
MENTION_RE = re.compile(r"@[A-Za-z0-9_]+")
HASHTAG_RE = re.compile(r"#\w+")
WORD_RE = re.compile(r"[A-Za-zÀ-ÿ']{5,}")
EMOJI_RE = re.compile(
    "[\U0001F000-\U0001FAFF\U00002600-\U000027BF\U0001F1E6-\U0001F1FF\u2190-\u21FF\u2B00-\u2BFF]"
)


def normalize(text: str) -> str:
    t = unicodedata.normalize("NFC", text)
    return re.sub(r"\s+", " ", t).strip()


def keywords(text: str) -> set[str]:
    return {w.lower() for w in WORD_RE.findall(text)}


def shares_topic(draft_text: str, target_text: str) -> list[str]:
    """Parole condivise fra bozza e post di riferimento, con confronto per prefisso.

    Serve a verificare che la risposta parli davvero del post a cui risponde.
    Il confronto per prefisso (5 caratteri) assorbe le flessioni: 'francese'
    aggancia 'Francia', 'relentless' aggancia 'relentlessly'.
    """
    d = keywords(draft_text)
    t = keywords(target_text)
    hits = set()
    for a in d:
        for b in t:
            if a == b or a.startswith(b[:5]) or b.startswith(a[:5]):
                hits.add(b)
    return sorted(hits)


def check(draft: dict, published: list[dict], day_counts: dict) -> list[str]:
    """Restituisce la lista dei problemi. Lista vuota = bozza pubblicabile."""
    problems: list[str] = []
    text = normalize(draft.get("text", ""))
    target = normalize(draft.get("tweet_text", ""))
    account = (draft.get("account") or "").lstrip("@")

    if not text:
        return ["testo vuoto"]
    if len(text) > MAX_LEN:
        problems.append(f"troppo lunga: {len(text)} caratteri (max {MAX_LEN})")
    if len(text) < MIN_LEN:
        problems.append(f"troppo corta per un dato: {len(text)} caratteri (min {MIN_LEN})")

    if LINK_RE.search(text):
        problems.append("contiene un link")
    if MENTION_RE.search(text):
        problems.append("contiene una menzione @")
    if HASHTAG_RE.search(text):
        problems.append("contiene un hashtag")
    if EMOJI_RE.search(text):
        problems.append("contiene emoji")

    low = f" {text.lower()} "
    for bad in BLOCKLIST:
        if bad in low:
            problems.append(f"frase di riempimento: '{bad}'")

    if not re.search(r"\d", text) and not any(m in low for m in MARKERS):
        problems.append("nessun dato e nessun marcatore di sostanza (contrasto, causa, condizione)")

    # deve parlare del post a cui risponde
    if target:
        shared = shares_topic(text, target)
        if not shared:
            problems.append("nessun aggancio lessicale al post di riferimento")
        else:
            draft["_shared"] = sorted(shared)

    # non ripetere risposte gia' pubblicate
    for prev in published:
        ratio = difflib.SequenceMatcher(None, text.lower(), normalize(prev.get("text", "")).lower()).ratio()
        if ratio >= SIMILARITY_MAX:
            problems.append(f"troppo simile a una risposta gia' pubblicata ({prev.get('id')}, {ratio:.2f})")

    if account and day_counts.get(account, 0) >= MAX_PER_ACCOUNT_DAY:
        problems.append(f"limite giornaliero per @{account} gia' raggiunto")

    return problems


def load_published(queue_dir: str, exclude: str) -> list[dict]:
    out = []
    for path in sorted(glob.glob(os.path.join(queue_dir, "replies-*.json"))):
        if os.path.abspath(path) == os.path.abspath(exclude):
            continue
        try:
            data = json.load(open(path, encoding="utf-8"))
        except Exception:
            continue
        for r in data.get("replies", []):
            if r.get("status") == "published":
                out.append(r)
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("path", help="file replies-*.json da validare")
    ap.add_argument("--json", action="store_true", help="output JSON")
    args = ap.parse_args()

    data = json.load(open(args.path, encoding="utf-8"))
    replies = data.get("replies", [])
    published = load_published(os.path.dirname(os.path.abspath(args.path)) or QUEUE_DIR, args.path)

    day_counts: dict[str, int] = {}
    for r in published:
        acc = (r.get("account") or "").lstrip("@")
        day_counts[acc] = day_counts.get(acc, 0) + 1

    results = []
    failed = 0
    for r in replies:
        problems = check(r, published, day_counts)
        verdict = "PASS" if not problems else "FAIL"
        if problems:
            failed += 1
        results.append({
            "id": r.get("id"),
            "account": r.get("account"),
            "verdict": verdict,
            "problems": problems,
            "chars": len(normalize(r.get("text", ""))),
        })

    if args.json:
        print(json.dumps({"results": results, "failed": failed}, ensure_ascii=False, indent=2))
    else:
        print(f"Guardia risposte X — {len(replies)} bozze, {failed} bocciate")
        for res in results:
            print(f"\n[{res['verdict']}] {res['id']} @{res['account']} ({res['chars']} caratteri)")
            for p in res["problems"]:
                print(f"    - {p}")
        if failed:
            print("\nLe bozze bocciate non vanno pubblicate: correggile o scartale.")

    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
