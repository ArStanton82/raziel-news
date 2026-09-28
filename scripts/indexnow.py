#!/usr/bin/env python3
"""Segnala a IndexNow gli URL di raziel.news.

IndexNow e' il protocollo condiviso da Bing, Yandex, Seznam e Naver: si invia
l'elenco degli URL nuovi e loro li ricontrollano subito, senza aspettare che
passino a raccogliere la sitemap. Google non partecipa: per Google serve
Search Console.

Come funziona: la chiave deve essere leggibile dal sito all'indirizzo
https://raziel.news/<chiave>.txt e il suo contenuto deve essere la chiave
stessa. Il file e' static/<chiave>.txt nel repo; la chiave e' anche in
scripts/indexnow_key.txt per poterla leggere dagli script e dal workflow.

Uso:
    python3 scripts/indexnow.py                  # legge la sitemap dal sito live
    python3 scripts/indexnow.py --da-public      # legge public/sitemap.xml appena costruita
    python3 scripts/indexnow.py URL [URL ...]    # segnala URL specifici

Esce con 0 se il servizio accetta (200 o 202), 2 altrimenti: il workflow lo
chiama con continue-on-error perche' un intoppo di rete non deve bloccare il
deploy.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
import urllib.error
import urllib.request
from pathlib import Path

RADICE = Path(__file__).resolve().parent.parent
SITO = "raziel.news"
ENDPOINT = "https://api.indexnow.org/indexnow"


def chiave() -> str:
    """Trova la chiave: variabile INDEXNOW_KEY, oppure il file già presente in
    static/ (il cui nome è la chiave e il cui contenuto deve essere identico)."""
    if os.environ.get("INDEXNOW_KEY"):
        return os.environ["INDEXNOW_KEY"].strip()
    for file_pubblico in sorted((RADICE / "static").glob("*.txt")):
        nome = file_pubblico.stem
        if not re.fullmatch(r"[0-9a-f]{8,128}", nome):
            continue
        if file_pubblico.read_text(encoding="utf-8").strip() == nome:
            return nome
    raise SystemExit(
        "chiave IndexNow non trovata: serve static/<chiave>.txt il cui contenuto "
        "sia la chiave stessa (oppure la variabile INDEXNOW_KEY)"
    )


def url_da_sitemap(testo: str) -> list[str]:
    return re.findall(r"<loc>\s*([^<\s]+)\s*</loc>", testo)


def scarica_sitemap() -> list[str]:
    url = f"https://{SITO}/sitemap.xml"
    richiesta = urllib.request.Request(url, headers={"User-Agent": "raziel-news-indexnow/1.0"})
    with urllib.request.urlopen(richiesta, timeout=30) as risposta:
        return url_da_sitemap(risposta.read().decode("utf-8"))


def main() -> int:
    ap = argparse.ArgumentParser(description="Segnala URL a IndexNow")
    ap.add_argument("url", nargs="*", help="URL da segnalare (se omesso, usa la sitemap)")
    ap.add_argument("--da-public", action="store_true", help="usa public/sitemap.xml invece del sito live")
    ap.add_argument("--solo-elenco", metavar="FILE",
                    help="scrive l'elenco degli URL in FILE ed esce, senza inviare nulla")
    ap.add_argument("--elenco", metavar="FILE",
                    help="legge gli URL da FILE (uno per riga), invece che dalla sitemap")
    ap.add_argument("--prova", action="store_true", help="mostra il carico utile senza inviarlo")
    argomenti = ap.parse_args()

    if argomenti.url:
        urls = argomenti.url
    elif argomenti.elenco:
        urls = [u.strip() for u in Path(argomenti.elenco).read_text(encoding="utf-8").splitlines() if u.strip()]
    elif argomenti.da_public:
        sitemap = RADICE / "public" / "sitemap.xml"
        if not sitemap.exists():
            raise SystemExit(f"{sitemap} non esiste: costruisci prima il sito")
        urls = url_da_sitemap(sitemap.read_text(encoding="utf-8"))
    else:
        urls = scarica_sitemap()

    urls = [u for u in dict.fromkeys(urls) if u.startswith(f"https://{SITO}/")]
    if not urls:
        print("nessun URL da segnalare")
        return 0

    carico = {
        "host": SITO,
        "key": chiave(),
        "keyLocation": f"https://{SITO}/{chiave()}.txt",
        "urlList": urls,
    }
    print(f"URL da segnalare: {len(urls)}")
    for u in urls:
        print("  ", u)
    if argomenti.solo_elenco:
        Path(argomenti.solo_elenco).write_text("\n".join(urls) + "\n", encoding="utf-8")
        print(f"elenco scritto in {argomenti.solo_elenco}: {len(urls)} URL")
        return 0
    if argomenti.prova:
        print(json.dumps(carico, ensure_ascii=False, indent=2)[:400])
        return 0

    richiesta = urllib.request.Request(
        ENDPOINT,
        data=json.dumps(carico).encode("utf-8"),
        headers={"Content-Type": "application/json; charset=utf-8",
                 "User-Agent": "raziel-news-indexnow/1.0"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(richiesta, timeout=30) as risposta:
            codice = risposta.status
            corpo = risposta.read().decode("utf-8", errors="replace")[:300]
    except urllib.error.HTTPError as e:
        codice = e.code
        corpo = e.read().decode("utf-8", errors="replace")[:300]
    print(f"risposta IndexNow: HTTP {codice} {corpo}")
    if codice in (200, 202):
        print("accettato: i motori ricontrolleranno gli URL segnalati")
        return 0
    print("NON accettato: controlla chiave, file pubblico e formato degli URL")
    return 2


if __name__ == "__main__":
    sys.exit(main())
