#!/usr/bin/env python3
"""Rimuove dal corpo degli articoli l'H1 che duplica il title del frontmatter.

Perche': il tema hello-4s3ti renderizza gia' il title del frontmatter come
<h1 class="post-title"> (themes/hello-4s3ti/layouts/posts/single.html).
Se il corpo markdown inizia con "# <stesso titolo>", il titolo appare due
volte nella pagina dell'articolo.

Uso:
    python3 scripts/strip_duplicate_h1.py [path ...]

Senza argomenti analizza content/posts/*.md. Con argomenti accetta file o
directory (es. `python3 scripts/strip_duplicate_h1.py content/posts drafts`).
Lo script e' idempotente: se non c'e' nulla da rimuovere non riscrive il file.
In CI gira prima di `hugo --minify`: e' una rete di sicurezza deterministica,
non sostituisce la regola editoriale (le bozze non devono contenere l'H1).
"""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def normalizza(testo: str) -> str:
    """Normalizza per confronto: via virgolette/backslash, apostrofi uniformi."""
    t = testo.strip().strip('"').strip("'")
    t = t.replace("\\", "")
    t = t.replace("\u2019", "'").replace("\u2018", "'")
    t = t.replace("\u201c", '"').replace("\u201d", '"')
    return " ".join(t.split()).casefold()


def split_frontmatter(testo: str) -> tuple[str, str]:
    """Restituisce (frontmatter, corpo). Se manca il frontmatter, corpo=testo."""
    righe = testo.splitlines(keepends=True)
    if not righe or righe[0].strip() != "---":
        return "", testo
    for i in range(1, len(righe)):
        if righe[i].strip() == "---":
            return "".join(righe[: i + 1]), "".join(righe[i + 1 :])
    return "", testo


def leggi_title(frontmatter: str) -> str:
    for riga in frontmatter.splitlines():
        if riga.startswith("title:"):
            return riga.split(":", 1)[1].strip()
    return ""


def processa(path: Path) -> str:
    originale = path.read_text(encoding="utf-8")
    frontmatter, corpo = split_frontmatter(originale)
    title = leggi_title(frontmatter)
    if not title:
        return f"SALTATO  {path} (nessun title nel frontmatter)"

    righe = corpo.splitlines(keepends=True)
    idx = None
    for i, riga in enumerate(righe):
        if not riga.strip():
            continue
        idx = i
        break
    if idx is None:
        return f"OK       {path} (corpo vuoto)"

    prima = righe[idx].rstrip("\n")
    if not prima.startswith("# ") or prima.startswith("## "):
        return f"OK       {path} (nessun H1 nel corpo)"

    if normalizza(prima[2:]) != normalizza(title):
        return f"ATTENZIONE {path}: H1 '{prima[2:].strip()}' != title '{title.strip()}' — non rimosso"

    del righe[idx]
    while righe and idx < len(righe) and not righe[idx].strip():
        del righe[idx]
    nuovo = frontmatter + "".join(righe)
    if nuovo == originale:
        return f"OK       {path}"
    path.write_text(nuovo, encoding="utf-8")
    return f"RIMOSSO  {path} (H1 duplicato del title)"


def raccogli(argomenti: list[str]) -> list[Path]:
    if not argomenti:
        argomenti = ["content/posts"]
    files: list[Path] = []
    for arg in argomenti:
        p = ROOT / arg if not Path(arg).is_absolute() else Path(arg)
        if p.is_dir():
            files.extend(sorted(f for f in p.glob("*.md") if f.is_file()))
        elif p.is_file():
            files.append(p)
    return files


def main() -> int:
    files = raccogli([a for a in sys.argv[1:] if not a.startswith("-")])
    if not files:
        print("Nessun file markdown trovato.")
        return 0
    for f in files:
        print(processa(f))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
