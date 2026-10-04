#!/usr/bin/env python3
"""Genera l'immagine di sfondo della card di un articolo con Venice (SD35).

Su richiesta, un articolo alla volta: non c'e' nessuna generazione di massa.
L'immagine viene salvata in `static/images/card-arte/<nome-base>.jpg` e il suo
riferimento in `data/card_immagini.json` con `"fonte": "ai"`.

Perche' le immagini stanno nel repo e non si generano in CI: la card la
costruisce `scripts/genera_og.py` durante la build, e il CI non ha la chiave di
Venice. Si genera qui, una volta, e la si committa.

Etichetta: un'immagine generata con AI non e' una fotografia, e su un sito di
notizie va dichiarata. Il credito stampato sulla card e' "Immagine generata con
AI" (inglese: "AI-generated image").

Stile di casa: fondo carbone scuro, accento violetto (#6d5ae6), luce
cinematografica, minimale, niente testo ne' loghi, soggetto nei due terzi alti e
terzo inferiore scuro e calmo, perche' il titolo ci va sopra.

Uso:
  python3 scripts/arte_card.py --articolo 2026-10-04-chi-risponde-quando-l-agente-sbaglia
  python3 scripts/arte_card.py --articolo <nome> --soggetto "una sala server vuota al buio"
  python3 scripts/arte_card.py --articolo <nome> --forza          # rigenera
  python3 scripts/arte_card.py --articolo <nome> --solo-prompt    # mostra il prompt, non genera

Chiave: la variabile HERMES_CUSTOM_API_VENICE_AI_API_KEY (nel .env del profilo).
"""

from __future__ import annotations

import argparse
import base64
import json
import os
import pathlib
import re
import sys
import time
import urllib.error
import urllib.request

RADICE = pathlib.Path(__file__).resolve().parent.parent
ARTICOLI = RADICE / "content" / "posts"
ARTE = RADICE / "static" / "images" / "card-arte"
INDICE = RADICE / "data" / "card_immagini.json"
ENV = pathlib.Path(__file__).resolve().parent.parent.parent / ".env"

MODELLO = "venice-sd35"          # 0,01 DIEM per immagine, 16:9 nativo
LARGHEZZA, ALTEZZA = 1280, 720
STEPS = 30
QUALITA = 88
LARGHEZZA_FINALE = 1600

ETICHETTA = {"it": "Immagine generata con AI", "en": "AI-generated image"}

STILE = (
    "Editorial illustration for a technology news site. Dark charcoal background, "
    "deep violet accent light, cinematic, moody, minimal, high detail. "
    "No text, no letters, no words, no numbers, no logos, no watermark, no signature. "
    "The subject sits in the upper two thirds; the bottom third stays dark and quiet "
    "so a headline can be placed over it. Subject: "
)

# Soggetto visivo per categoria: si parte da qui e si puo' sempre correggere con
# --soggetto. Non e' una descrizione dell'articolo, e' una scena.
SOGGETTO_CATEGORIA = {
    "AI": "a vast dark hall of humming computer racks seen from a low angle",
    "Crypto": "an empty trading floor at night with dim screens on the desks",
    "Blockchain": "a chain of glowing ledger blocks receding into darkness",
    "Hermes": "an empty server room aisle at night, cold light and cables",
    "Venice.ai": "an open graphics card on a dark workbench, macro detail, violet backlight",
    "Filosofia dell'AI": "an empty courtroom with tall windows and hard light",
}

SOGGETTO_TAG = {
    "bitcoin": "a single coin resting on a dark ledger book, macro",
    "stablecoin": "a stack of coins beside a bank ledger, cold light",
    "etf": "an empty stock exchange hall with quotation screens",
    "udienza": "a nearly empty senate hearing room, rows of desks and microphones",
    "responsabilita": "an empty courtroom, a judge's bench in half light",
    "liability": "an empty courtroom, a judge's bench in half light",
    "regolamentazione": "an empty parliamentary chamber seen from the benches",
    "papa": "a colonnade in shadow, long perspective, cold morning light",
    "sicurezza": "a dark room with a single padlocked server cabinet",
    "gpu": "an open graphics card on a dark workbench, macro detail",
    "nvidia": "an open graphics card on a dark workbench, macro detail",
    "hermes": "an empty server room aisle at night, cold light and cables",
    "plugin": "a dark desk with a keyboard lit by screen glow",
    "memoria": "rows of hard drives in a dark rack, macro detail",
    "openai": "a vast dark hall of humming computer racks",
    "anthropic": "a vast dark hall of humming computer racks",
    "agenti autonomi": "an empty control room with many dark monitors",
    "intelligenza artificiale": "a vast dark hall of humming computer racks",
}


def chiave() -> str:
    """La chiave di Venice: prima l'ambiente, poi il .env del profilo."""
    if os.environ.get("HERMES_CUSTOM_API_VENICE_AI_API_KEY"):
        return os.environ["HERMES_CUSTOM_API_VENICE_AI_API_KEY"]
    for percorso in (ENV, RADICE.parent.parent / ".env"):
        if percorso.exists():
            for riga in percorso.read_text().splitlines():
                m = re.match(r"^HERMES_CUSTOM_API_VENICE_AI_API_KEY\s*=\s*\"?([^\"\n]+)\"?", riga)
                if m:
                    return m.group(1).strip()
    return ""


def frontmatter(nome: str) -> dict:
    """Campi del frontmatter che servono (title, categories, tags)."""
    for suffisso in (".md", ".en.md"):
        p = ARTICOLI / f"{nome}{suffisso}"
        if p.exists() and not nome.endswith(".en"):
            break
    else:
        p = ARTICOLI / f"{nome}.md"
    if not p.exists():
        return {}
    pezzi = p.read_text(encoding="utf-8").split("---", 2)
    if len(pezzi) < 3:
        return {}
    dati: dict[str, list[str] | str] = {}
    corrente = None
    for riga in pezzi[1].splitlines():
        m = re.match(r"^\s*-\s+(.*)$", riga)
        if m and corrente:
            attuale = dati.get(corrente)
            if isinstance(attuale, list):
                attuale.append(m.group(1).strip().strip("\"'"))
            continue
        m = re.match(r"^([A-Za-z_]+):\s*(.*)$", riga)
        if not m:
            continue
        campo, valore = m.group(1), m.group(2).strip()
        corrente = None
        if campo not in ("title", "categories", "tags", "summary"):
            continue
        if valore.startswith("[") and valore.endswith("]"):
            dati[campo] = [v.strip().strip("\"'") for v in valore[1:-1].split(",") if v.strip()]
        elif valore == "":
            dati[campo] = []
            corrente = campo
        else:
            dati[campo] = valore.strip("\"'")
    return dati


def soggetto(nome: str, esplicito: str = "") -> str:
    if esplicito:
        return esplicito
    dati = frontmatter(nome)
    tag = dati.get("tags") or []
    if isinstance(tag, str):
        tag = [tag]
    for t in tag:
        chiave_tag = str(t).strip().lower()
        if chiave_tag in SOGGETTO_TAG:
            return SOGGETTO_TAG[chiave_tag]
    categorie = dati.get("categories") or []
    if isinstance(categorie, str):
        categorie = [categorie]
    for c in categorie:
        if str(c).strip() in SOGGETTO_CATEGORIA:
            return SOGGETTO_CATEGORIA[str(c).strip()]
    return "an abstract dark architectural space with violet light"


def genera(prompt: str, k: str, destinazione: pathlib.Path) -> str:
    """Chiama Venice e scrive il JPEG. Restituisce una riga di esito."""
    corpo = {"model": MODELLO, "prompt": prompt, "width": LARGHEZZA, "height": ALTEZZA,
             "steps": STEPS, "format": "webp", "safe_mode": False, "hide_watermark": True}
    req = urllib.request.Request(
        "https://api.venice.ai/api/v1/image/generate",
        data=json.dumps(corpo).encode(),
        headers={"Authorization": f"Bearer {k}", "Content-Type": "application/json"},
        method="POST")
    inizio = time.time()
    try:
        with urllib.request.urlopen(req, timeout=300) as f:
            risposta = json.load(f)
    except urllib.error.HTTPError as e:
        return f"errore HTTP {e.code}: {e.read().decode()[:200]}"
    except Exception as e:
        return f"errore: {e}"
    immagini = risposta.get("images") or []
    if not immagini:
        return f"nessuna immagine nella risposta ({list(risposta)[:5]})"
    grezzo = base64.b64decode(immagini[0])
    destinazione.parent.mkdir(parents=True, exist_ok=True)
    try:
        from PIL import Image
        import io
        immagine = Image.open(io.BytesIO(grezzo)).convert("RGB")
        ricampionamento = getattr(Image, "Resampling", Image).LANCZOS
        if immagine.width > LARGHEZZA_FINALE:
            immagine = immagine.resize((LARGHEZZA_FINALE, round(immagine.height * LARGHEZZA_FINALE / immagine.width)), ricampionamento)
        immagine.save(destinazione, "JPEG", quality=QUALITA, optimize=True, progressive=True)
    except ImportError:
        destinazione.write_bytes(grezzo)
    return f"ok in {time.time() - inizio:.0f}s — {destinazione.stat().st_size} byte"


def main() -> int:
    ap = argparse.ArgumentParser(description="Immagine di card generata con Venice")
    ap.add_argument("--articolo", required=True, help="nome file senza .md")
    ap.add_argument("--soggetto", default="", help="scena da illustrare (sostituisce quella dedotta)")
    ap.add_argument("--forza", action="store_true", help="rigenera anche se l'immagine esiste")
    ap.add_argument("--solo-prompt", action="store_true", help="mostra il prompt e non genera")
    argomenti = ap.parse_args()

    nome = argomenti.articolo
    if not (ARTICOLI / f"{nome}.md").exists() and not (ARTICOLI / f"{nome}.en.md").exists():
        print(f"articolo non trovato: {nome}")
        return 1
    prompt = STILE + soggetto(nome, argomenti.soggetto)
    if argomenti.solo_prompt:
        print(prompt)
        return 0

    destinazione = ARTE / f"{nome}.jpg"
    if destinazione.exists() and not argomenti.forza:
        print(f"esiste già: {destinazione.relative_to(RADICE)} (usa --forza per rigenerarla)")
        return 0

    k = chiave()
    if not k:
        print("chiave Venice non trovata (HERMES_CUSTOM_API_VENICE_AI_API_KEY)")
        return 1
    esito = genera(prompt, k, destinazione)
    print(f"{nome}: {esito}")
    if not esito.startswith("ok"):
        return 1

    indice = json.loads(INDICE.read_text(encoding="utf-8")) if INDICE.exists() else {"versione": 1, "foto": {}}
    indice.setdefault("foto", {})[nome] = {
        "file": f"card-arte/{destinazione.name}",
        "fonte": "ai",
        "modello": MODELLO,
        "soggetto": soggetto(nome, argomenti.soggetto),
        "licenza": "immagine generata con AI",
        "credito": dict(ETICHETTA),
        "pagina": "",
    }
    INDICE.write_text(json.dumps(indice, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"indice aggiornato: {INDICE.relative_to(RADICE)}")
    print(f"ora: python3 scripts/genera_og.py --articolo {nome}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
