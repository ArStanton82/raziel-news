#!/usr/bin/env python3
"""Controlla i meta di condivisione nell'HTML costruito (public/).

Serve a non scoprire un errore di templating dal grafico di un link condiviso.
Per ogni articolo verifica che:
  - og:image e twitter:image siano presenti una volta sola e puntino a un file
    che esiste dentro public/ (non a un percorso immaginario);
  - il card di Twitter sia large_image;
  - i blocchi JSON-LD siano JSON valido e contengano un NewsArticle;
  - og:title ci sia e non sia vuoto.

Uso: python3 scripts/verifica_meta.py [--solo-articoli] [--tacere-ok]
Esce con 1 se trova un problema (nel workflow gira con continue-on-error).
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

RADICE = Path(__file__).resolve().parent.parent
PUBBLICO = RADICE / "public"


def valore_meta(html: str, chiave: str) -> list[str]:
    """Valori di un meta, con o senza virgolette (hugo --minify le toglie)."""
    schema = (r'<meta[^>]*\s(?:property|name)=["\']?' + re.escape(chiave) +
              r'["\']?\s[^>]*content=(["\'])(.*?)\1')
    return [m.group(2) for m in re.finditer(schema, html, re.S)]


def articoli_costruiti() -> list[Path]:
    return sorted(p for p in (PUBBLICO / "2026").rglob("index.html"))


def controlla(pagina: Path) -> list[str]:
    problemi: list[str] = []
    html = pagina.read_text(encoding="utf-8")
    rel = pagina.parent.relative_to(PUBBLICO)
    tipo_og = valore_meta(html, "og:type")

    for chiave in ("og:image", "twitter:image", "og:title", "twitter:card"):
        valori = valore_meta(html, chiave)
        if len(valori) != 1:
            problemi.append(f"{chiave}: {len(valori)} occorrenze (ne serve 1)")
        elif not valori[0].strip():
            problemi.append(f"{chiave}: vuoto")

    for chiave in ("og:image", "twitter:image"):
        valori = valore_meta(html, chiave)
        if len(valori) == 1:
            percorso = valori[0].replace("https://raziel.news/", "").lstrip("/")
            file_locale = PUBBLICO / percorso
            if not valori[0].startswith("https://raziel.news/"):
                problemi.append(f"{chiave}: non assoluto ({valori[0]})")
            elif not file_locale.exists():
                problemi.append(f"{chiave}: file mancante in public/ ({percorso})")

    # Ogni articolo deve avere la SUA immagine: se ripiega su quella di base,
    # vuol dire che la generazione non è arrivata nel build (file del cascade
    # rimasti, immagini non generate, oppure un file non committato).
    if tipo_og and tipo_og[0] == "article":
        immagini = valore_meta(html, "og:image")
        if len(immagini) == 1 and immagini[0].endswith("/og-default.png"):
            problemi.append("articolo con l'immagine di ripiego invece di quella generata")

    card = valore_meta(html, "twitter:card")
    if card and card[0] != "summary_large_image":
        problemi.append(f"twitter:card: {card[0]} invece di summary_large_image")

    blocchi = re.findall(r'<script type=["\']?application/ld\+json["\']?>(.*?)</script>', html, re.S)
    if not blocchi:
        problemi.append("JSON-LD assente")
    attesi = {"NewsArticle"} if (tipo_og and tipo_og[0] == "article") else {"WebSite", "WebPage", "CollectionPage"}
    for blocco in blocchi:
        try:
            dati = json.loads(blocco)
        except json.JSONDecodeError as e:
            problemi.append(f"JSON-LD non valido: {e}")
            continue
        grafo = dati.get("@graph", [dati]) if isinstance(dati, dict) else dati
        tipi = {n.get("@type") for n in grafo if isinstance(n, dict)}
        if not tipi & attesi:
            problemi.append(f"JSON-LD senza {'/'.join(sorted(attesi))} (tipi: {sorted(tipi)})")

    if problemi:
        print(f"  {rel}")
        for p in problemi:
            print(f"     - {p}")
    return problemi


def main() -> int:
    ap = argparse.ArgumentParser(description="Verifica dei meta di condivisione")
    ap.add_argument("--solo-articoli", action="store_true", help="controlla solo gli articoli")
    ap.add_argument("--tacere-ok", action="store_true", help="stampa solo i problemi")
    argomenti = ap.parse_args()

    if not PUBBLICO.exists():
        print(f"{PUBBLICO} non esiste: costruisci prima il sito")
        return 1

    pagine = articoli_costruiti()
    if not argomenti.solo_articoli:
        pagine += [PUBBLICO / "index.html"] + [
            p for p in PUBBLICO.glob("*/index.html")
            if p.parent.name not in {"2026"}
        ]

    print(f"pagine controllate: {len(pagine)}")
    totale = 0
    for pagina in pagine:
        if pagina.exists():
            totale += len(controlla(pagina))
    if totale:
        print(f"PROBLEMI: {totale}")
        return 1
    if not argomenti.tacere_ok:
        print("nessun problema: immagini, card e dati strutturati sono coerenti")
    return 0


if __name__ == "__main__":
    sys.exit(main())
