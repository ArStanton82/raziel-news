#!/usr/bin/env python3
"""Genera l'illustrazione di un articolo con Venice, in stile poster pop art.

Il lavoro grafico lo fa il **preset di stile nativo** di Venice ("Pop Art",
"Comic Book", "Graffiti", ... — l'elenco lo da' GET /api/v1/image/styles):
chiedere lo stile a parole dentro il prompt produceva un ibrido, non un poster
(misurato: saturazione 0,82 col preset contro 0,29 senza). Al prompt resta il
soggetto, e il soggetto e' **un oggetto solo, emblematico, che riempie il
riquadro** — non una scena con scrivania, oggetti e sfondo.

L'immagine va in `static/images/card-arte/<cartella>/<nome-base>.jpg` (la
cartella predefinita e' `v2`: Cloudflare serve gli asset statici per nome dalla
cache, quindi riscrivere un file gia' pubblicato non arriverebbe ai lettori) e
il riferimento va in `data/card_immagini.json`. Quell'indice lo leggono la
pagina dell'articolo (layouts/partials/illustrazione.html) e la card di
condivisione (scripts/genera_og.py): una sola fonte di verita'.

Perche' le immagini stanno nel repo e non si generano in CI: la card la
costruisce genera_og.py durante la build, e il CI non ha la chiave di Venice.

Etichetta: un'immagine generata con AI non e' una fotografia, e su un sito di
notizie va dichiarata. Il credito stampato sulla card e' "Immagine generata con
AI" (inglese: "AI-generated image").

Uso:
  python3 scripts/arte_card.py --articolo 2026-10-06-crypto-treasury-cftc-sec
  python3 scripts/arte_card.py --articolo <nome> --soggetto "un timbro gigante su un foglio"
  python3 scripts/arte_card.py --articolo <nome> --forza          # rigenera
  python3 scripts/arte_card.py --articolo <nome> --solo-prompt    # mostra il prompt
  python3 scripts/arte_card.py --articolo <nome> --preset "Comic Book" --modello nano-banana-pro
  python3 scripts/arte_card.py --articolo <nome> --cartella ""    # nella cartella di prima

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
IMMAGINI = RADICE / "static" / "images"
INDICE = RADICE / "data" / "card_immagini.json"
ENV = pathlib.Path(__file__).resolve().parent.parent.parent / ".env"

MODELLO = "venice-sd35"          # 0,01 DIEM per immagine
PRESET = "Pop Art"               # preset di stile nativo di Venice
CARTELLA = "v2"                  # sottocartella di static/images/card-arte/
LARGHEZZA, ALTEZZA = 1280, 720
STEPS = 30
QUALITA = 88
LARGHEZZA_FINALE = 1600

ETICHETTA = {"it": "Immagine generata con AI", "en": "AI-generated image"}

# Il preset fa lo stile: qui restano il taglio della scena e i divieti.
STILE = (
    "Silkscreen poster of a single emblematic object. One object only, large, filling the frame, "
    "centred, on a flat field of colour. Flat spot colours, heavy black outlines, no gradients, "
    "no shading, no photorealism, no 3D. No people, no faces, no text, no letters, no words, "
    "no numbers, no logos, no signature, no frame, no border. The bottom third stays simple and "
    "quiet, because the headline of the card is printed over it. Object: "
)

# Soggetto di ripiego per categoria e per tag: si usa solo se il soggetto non
# arriva dal frontmatter ne' dal modello di testo. E' un oggetto, non una scena.
SOGGETTO_CATEGORIA = {
    "AI": "a single dark server blade standing upright, one light on",
    "Crypto": "a single heavy coin standing on its edge",
    "Blockchain": "a single chain link, macro, filling the frame",
    "Hermes": "a single open plug, half inserted, macro",
    "Venice.ai": "a single graphics card standing on its edge, macro",
    "Filosofia dell'AI": "a single empty stone chair in a shaft of light",
}

SOGGETTO_TAG = {
    "bitcoin": "a single coin standing on its edge, macro",
    "stablecoin": "a single stack of coins beside a closed ledger",
    "etf": "a single ticker board, dark, one line still lit",
    "udienza": "a single microphone on an empty desk",
    "responsabilita": "a single gavel resting on a closed folder",
    "liability": "a single gavel resting on a closed folder",
    "regolamentazione": "a single official stamp coming down on a sheet",
    "papa": "a single stone column in cold morning light",
    "sicurezza": "a single padlocked server cabinet, closed",
    "gpu": "a single graphics card standing on its edge, macro",
    "nvidia": "a single graphics card standing on its edge, macro",
    "hermes": "a single open plug, half inserted, macro",
    "plugin": "a single cartridge slotting into a dark panel",
    "memoria": "a single hard drive, open, its platter visible",
    "openai": "a single dark server blade standing upright",
    "anthropic": "a single dark server blade standing upright",
    "agenti autonomi": "a single switch flipped on, macro",
    "intelligenza artificiale": "a single dark server blade standing upright",
}


def chiave() -> str:
    """La chiave di Venice: prima l'ambiente, poi il .env del profilo."""
    if os.environ.get("HERMES_CUSTOM_API_VENICE_AI_API_KEY"):
        return os.environ["HERMES_CUSTOM_API_VENICE_AI_API_KEY"]
    for percorso_env in (ENV, RADICE.parent.parent / ".env"):
        if percorso_env.exists():
            for riga in percorso_env.read_text().splitlines():
                m = re.match(r"^HERMES_CUSTOM_API_VENICE_AI_API_KEY\s*=\s*\"?([^\"\n]+)\"?", riga)
                if m:
                    return m.group(1).strip()
    return ""


def frontmatter(nome: str) -> dict:
    """Campi del frontmatter che servono (title, categories, tags, illustrazione)."""
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
        if campo not in ("title", "categories", "tags", "summary", "illustrazione"):
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
    if dati.get("illustrazione"):
        return str(dati["illustrazione"])
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
    return "a single abstract geometric object standing alone on a flat field"


def percorso(nome: str, cartella: str = CARTELLA) -> pathlib.Path:
    """Dove va l'immagine (e cosa finisce in `file` nell'indice)."""
    if cartella:
        return ARTE / cartella / f"{nome}.jpg"
    return ARTE / f"{nome}.jpg"


def genera(prompt: str, k: str, destinazione: pathlib.Path,
           modello: str = MODELLO, preset: str = PRESET) -> str:
    """Chiama Venice e scrive il JPEG. Restituisce una riga di esito."""
    corpo = {"model": modello, "prompt": prompt, "format": "webp",
             "safe_mode": False, "hide_watermark": True}
    if preset:
        corpo["style_preset"] = preset
    if modello.startswith("venice-sd35"):
        # i modelli a pixel vogliono width/height, quelli ad aspect_ratio no
        corpo.update({"width": LARGHEZZA, "height": ALTEZZA, "steps": STEPS})
    else:
        corpo.update({"aspect_ratio": "16:9", "resolution": "1K"})
    req = urllib.request.Request(
        "https://api.venice.ai/api/v1/image/generate",
        data=json.dumps(corpo).encode(),
        headers={"Authorization": f"Bearer {k}", "Content-Type": "application/json"},
        method="POST")
    inizio = time.time()
    try:
        with urllib.request.urlopen(req, timeout=400) as f:
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
            immagine = immagine.resize(
                (LARGHEZZA_FINALE, round(immagine.height * LARGHEZZA_FINALE / immagine.width)),
                ricampionamento)
        immagine.save(destinazione, "JPEG", quality=QUALITA, optimize=True, progressive=True)
    except ImportError:
        destinazione.write_bytes(grezzo)
    return f"ok in {time.time() - inizio:.0f}s — {destinazione.stat().st_size} byte"


def scrivi_indice(nome: str, scena: str, destinazione: pathlib.Path,
                  modello: str = MODELLO, preset: str = PRESET, origine: str = "") -> None:
    """Registra l'immagine nell'indice, con il percorso relativo a static/images/."""
    indice = json.loads(INDICE.read_text(encoding="utf-8")) if INDICE.exists() else {"versione": 1, "foto": {}}
    indice.setdefault("foto", {})
    voce = {
        "file": str(destinazione.relative_to(IMMAGINI)),
        "fonte": "ai",
        "modello": modello,
        "preset": preset,
        "soggetto": scena,
        "licenza": "immagine generata con AI",
        "credito": dict(ETICHETTA),
        "pagina": "",
    }
    if origine:
        voce["soggetto_scelto_da"] = origine
    indice["foto"][nome] = voce
    INDICE.write_text(json.dumps(indice, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def main() -> int:
    ap = argparse.ArgumentParser(description="Illustrazione pop art di un articolo (Venice)")
    ap.add_argument("--articolo", required=True, help="nome file senza .md")
    ap.add_argument("--soggetto", default="", help="oggetto da illustrare (sostituisce quello dedotto)")
    ap.add_argument("--forza", action="store_true", help="rigenera anche se l'immagine esiste")
    ap.add_argument("--solo-prompt", action="store_true", help="mostra il prompt e non genera")
    ap.add_argument("--modello", default=MODELLO, help="modello immagine di Venice")
    ap.add_argument("--preset", default=PRESET, help="preset di stile (stringa vuota per nessuno)")
    ap.add_argument("--cartella", default=CARTELLA, help="sottocartella di card-arte/ (vuota = card-arte/)")
    argomenti = ap.parse_args()

    nome = argomenti.articolo
    if not (ARTICOLI / f"{nome}.md").exists() and not (ARTICOLI / f"{nome}.en.md").exists():
        print(f"articolo non trovato: {nome}")
        return 1
    scena = soggetto(nome, argomenti.soggetto)
    prompt = STILE + scena
    if argomenti.solo_prompt:
        print(prompt)
        return 0

    destinazione = percorso(nome, argomenti.cartella)
    if destinazione.exists() and not argomenti.forza:
        print(f"esiste già: {destinazione.relative_to(RADICE)} (usa --forza per rigenerarla)")
        return 0

    k = chiave()
    if not k:
        print("chiave Venice non trovata (HERMES_CUSTOM_API_VENICE_AI_API_KEY)")
        return 1
    esito = genera(prompt, k, destinazione, argomenti.modello, argomenti.preset)
    print(f"{nome}: {esito}")
    if not esito.startswith("ok"):
        return 1

    scrivi_indice(nome, scena, destinazione, argomenti.modello, argomenti.preset)
    print(f"indice aggiornato: {INDICE.relative_to(RADICE)}")
    print(f"ora: python3 scripts/genera_og.py --articolo {nome}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
