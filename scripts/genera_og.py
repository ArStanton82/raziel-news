#!/usr/bin/env python3
"""Genera le immagini di condivisione (Open Graph) di raziel.news.

Produce, dentro static/images/:
  og/v2/default.png        1200x630  immagine di ripiego (home, pagine informative)
  og/v2/en/default.png     1200x630  la stessa, in inglese
  logo-512.png              512x512  logo del publisher per i dati strutturati
  og/v2/<basename>.png     1200x630  una per articolo italiano (--articoli)
  og/v2/en/<basename>.png  1200x630  una per articolo inglese (--articoli)

Perche' "v2": Cloudflare serve gli asset statici per nome dalla cache, quindi
riscrivere un file gia' pubblicato non arriverebbe ai lettori. Un percorso nuovo
(e' il caso di og/v2/) non ha cache da svecchiare; i file vecchi restano dove
sono e fanno da ripiego nel partial extra-head.html.

La lingua di un articolo la dice il nome del file: il gemello inglese e' il
file italiano piu' ".en.md" (2026-10-02-foo.md / 2026-10-02-foo.en.md), la
stessa chiave con cui il sito accoppia le due versioni (layouts/partials/
extra-head.html usa .File.ContentBaseName per l'italiana e og/v2/en/ per
l'inglese). Data e motto seguono la lingua; il titolo e l'etichetta del tema
vengono dal frontmatter di quel file, quindi sono gia' tradotti.

La fotografia di sfondo (variante A: foto a tutta pagina, velo scuro dal basso,
titolo in basso) viene da static/images/card-bg/<basename>.jpg: la sceglie e la
scarica scripts/foto_card.py da Wikimedia Commons con licenza libera verificata,
e il credito da stampare in piccolo in fondo alla card sta in
data/card_immagini.json. Se la foto non c'e', l'articolo usa la card scura di
prima: nessuna pagina resta senza immagine.

Perche' uno script: il PNG deve restare riproducibile. Si costruisce una pagina
HTML con le stesse tinte del sito e la si fotografa con Chrome headless alla
dimensione esatta. I caratteri (Atkinson Hyperlegible) sono incorporati in
base64, cosi' non serve un server.

La dimensione del titolo non e' scelta a occhio: il JS dentro la pagina prova
le misure dall'alto verso il basso e sceglie la piu' grande che sta nelle righe
e nell'altezza previste (3 righe/250px con la foto, 4 righe/340px senza); il
valore scelto viene letto dal dump del DOM (stesso passaggio della fotografia) e
stampato, cosi' resta verificabile.

Uso:  python3 scripts/genera_og.py                    (immagine di ripiego + logo)
      python3 scripts/genera_og.py --articoli         (una immagine per articolo)
      python3 scripts/genera_og.py --verifica         (quali articoli sono coperti)
      CHROME=/percorso/chrome python3 scripts/genera_og.py

Se Chrome non c'e', lo script lo dice e non fa nulla: il sito usa l'immagine di
ripiego e il build non si rompe (layouts/partials/extra-head.html controlla che
il file esista prima di citarlo).
"""

from __future__ import annotations

import argparse
import base64
import html
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

RADICE = Path(__file__).resolve().parent.parent
FONT = RADICE / "static" / "static" / "fonts"
USCITA = RADICE / "static" / "images"
USCITA_ARTICOLI = USCITA / "og" / "v2"
FOTO_SFONDO = USCITA / "card-bg"
INDICE_FOTO = RADICE / "data" / "card_immagini.json"
ARTICOLI = RADICE / "content" / "posts"

CANDIDATI_CHROME = [
    "google-chrome", "google-chrome-stable", "chromium", "chromium-browser",
    "/root/.cache/ms-playwright/chromium-1243/chrome-linux64/chrome",
]

ACCENTO = "#6d5ae6"
ACCENTO_FOTO = "#8d7cf0"
FONDO = "#1b1c1d"
TESTO = "#f2f2f2"
TENUE = "#a9a9b3"

MESI = {
    "it": ["gennaio", "febbraio", "marzo", "aprile", "maggio", "giugno", "luglio",
           "agosto", "settembre", "ottobre", "novembre", "dicembre"],
    "en": ["January", "February", "March", "April", "May", "June", "July",
           "August", "September", "October", "November", "December"],
}

# Le due lingue del sito. La cartella delle card inglesi e' separata
# ("og/v2/en/") per non sovrascrivere un file gia' in cache su Cloudflare: un
# asset statico servito con lo stesso nome resta quello vecchio.
LINGUA_BASE = "it"
LINGUE = ("it", "en")

# Motto del sito in fondo alla card. Fonte: hugo.yaml ->
# languages.<lingua>.params.footer.bottomText[0]. Se cambia li', va cambiato qui.
MOTTO = {
    "it": "Il peso delle scelte non svanisce.",
    "en": "The weight of choices does not fade.",
}

# Testo della card di ripiego (home e pagine informative), per lingua.
CARD_RIPIEGO = {
    "it": "Cronache e riflessioni su <em>intelligenza artificiale</em>, agenti autonomi e Venice.ai",
    "en": "Notes and reflections on <em>artificial intelligence</em>, autonomous agents and Venice.ai",
}


def trova_chrome() -> str | None:
    if os.environ.get("CHROME"):
        return os.environ["CHROME"]
    for candidato in CANDIDATI_CHROME:
        trovato = shutil.which(candidato) or (candidato if candidato.startswith("/") and Path(candidato).exists() else None)
        if trovato:
            return trovato
    return None


def font_base64(nome: str) -> str:
    dati = (FONT / nome).read_bytes()
    return base64.b64encode(dati).decode("ascii")


def stile() -> str:
    normale = font_base64("AtkinsonHyperlegible-400-latin.woff2")
    grassetto = font_base64("AtkinsonHyperlegible-700-latin.woff2")
    return f"""
    @font-face {{ font-family:'Atkinson Hyperlegible'; font-weight:400;
      src:url(data:font/woff2;base64,{normale}) format('woff2'); }}
    @font-face {{ font-family:'Atkinson Hyperlegible'; font-weight:700;
      src:url(data:font/woff2;base64,{grassetto}) format('woff2'); }}
    *{{margin:0;padding:0;box-sizing:border-box}}
    body{{background:{FONDO};color:{TESTO};
      font-family:'Atkinson Hyperlegible',DejaVu Sans,sans-serif;
      -webkit-font-smoothing:antialiased}}
    """


def html_card(lingua: str = LINGUA_BASE) -> str:
    return f"""<!doctype html><html lang="{lingua}"><head><meta charset="utf-8"><style>{stile()}
      body{{width:1200px;height:630px;padding:64px 72px;display:flex;flex-direction:column;justify-content:space-between}}
      .marca{{display:flex;align-items:baseline;gap:10px;font-size:38px;font-weight:700;letter-spacing:0}}
      .marca .segno{{color:{ACCENTO}}}
      h1{{font-size:74px;line-height:1.08;font-weight:700;letter-spacing:-0.01em;max-width:1000px}}
      h1 em{{font-style:normal;color:{ACCENTO}}}
      .piede{{display:flex;align-items:baseline;justify-content:space-between;font-size:26px;color:{TENUE}}}
      .piede .motto{{font-style:italic}}
    </style></head><body>
      <div class="marca"><span class="segno">&gt;</span><span>Raziel.news</span></div>
      <h1>{CARD_RIPIEGO[lingua]}</h1>
      <div class="piede"><span>raziel.news</span><span class="motto">{MOTTO[lingua]}</span></div>
    </body></html>"""


def html_logo() -> str:
    return f"""<!doctype html><html lang="it"><head><meta charset="utf-8"><style>{stile()}
      body{{width:512px;height:512px;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:6px}}
      .segno{{color:{ACCENTO};font-size:150px;font-weight:700;line-height:1}}
      .nome{{font-size:64px;font-weight:700;letter-spacing:0}}
    </style></head><body>
      <div class="segno">&gt;</div><div class="nome">Raziel.news</div>
    </body></html>"""


def html_articolo(titolo: str, etichetta: str, data: str,
                  lingua: str = LINGUA_BASE, foto: Path | None = None,
                  credito: str = "") -> str:
    """Card di un articolo: etichetta del tema, titolo, data, credito e motto.

    Con `foto` si usa la variante A (fotografia a tutta pagina, velo scuro dal
    basso, testo in basso); senza, la card scura di sempre. In entrambi i casi
    la dimensione del titolo la sceglie il JS in base allo spazio disponibile.
    """
    if foto:
        misure = [64, 58, 52, 46, 40, 36, 32, 28]
        base64_foto = base64.b64encode(foto.read_bytes()).decode("ascii")
        sfondo = (f'\n      <div class="foto"></div><div class="velo"></div>')
        stile_foto = f"""
      .foto{{position:absolute;inset:0;background:#0d0d10 url(data:image/jpeg;base64,{base64_foto}) center 30%/cover no-repeat}}
      .velo{{position:absolute;inset:0;background:linear-gradient(to top,rgba(12,12,14,.94) 0%,rgba(12,12,14,.86) 38%,rgba(12,12,14,.35) 68%,rgba(12,12,14,.55) 100%)}}"""
        corpo = "width:1200px;height:630px;position:relative;overflow:hidden"
        marca_pos = "position:absolute;top:52px;left:64px;font-size:34px;text-shadow:0 1px 12px rgba(0,0,0,.55)"
        testo_pos = "position:absolute;left:64px;right:64px;bottom:52px;text-shadow:0 1px 12px rgba(0,0,0,.55)"
        colore_etichetta = ACCENTO_FOTO
        altezza_max, righe_max = 250, 3
        piede_colore, piede_misura, piede_margine = "#d7d7de", 22, 18
    else:
        misure = [76, 70, 64, 58, 52, 46, 40, 34, 30]
        base64_foto = ""
        sfondo = ""
        stile_foto = ""
        corpo = "width:1200px;height:630px;padding:60px 72px;display:flex;flex-direction:column;justify-content:space-between"
        marca_pos = "font-size:36px"
        testo_pos = "max-width:1056px"
        colore_etichetta = ACCENTO
        altezza_max, righe_max = 340, 4
        piede_colore, piede_misura, piede_margine = TENUE, 25, 0
    blocco_credito = (f'<span class="credito">{html.escape(credito)}</span>' if credito else "")
    return f"""<!doctype html><html lang="{lingua}"><head><meta charset="utf-8"><style>{stile()}
      body{{{corpo}}}{stile_foto}
      .marca{{display:flex;align-items:baseline;gap:10px;font-weight:700;z-index:2;{marca_pos}}}
      .marca .segno{{color:{ACCENTO_FOTO if foto else ACCENTO}}}
      .testo{{z-index:2;{testo_pos}}}
      .etichetta{{color:{colore_etichetta};font-size:{'24' if foto else '27'}px;font-weight:700;letter-spacing:0.12em;text-transform:uppercase;margin-bottom:{'14' if foto else '22'}px}}
      h1{{font-weight:700;line-height:1.1;letter-spacing:-0.01em;max-height:{altezza_max}px;overflow:hidden;max-width:1056px}}
      .piede{{display:flex;align-items:baseline;gap:18px;font-size:{piede_misura}px;color:{piede_colore};margin-top:{piede_margine}px}}
      .piede .motto{{font-style:italic;margin-left:auto;text-align:right}}
      .credito{{font-size:16px;color:{'#b9b9c4' if foto else '#9a9aa6'}}}
    </style></head><body>{sfondo}
      <div class="marca"><span class="segno">&gt;</span><span>Raziel.news</span></div>
      <div class="testo">
        <div class="etichetta">{html.escape(etichetta)}</div>
        <h1 id="titolo">{html.escape(titolo)}</h1>
        <div class="piede">
          <span>{html.escape(data)} &middot; raziel.news</span>
          {blocco_credito}
          <span class="motto">{MOTTO[lingua]}</span>
        </div>
      </div>
      <div id="misura" hidden></div>
      <script>
        const t = document.getElementById('titolo');
        const passi = {json.dumps(misure)};
        const ALTEZZA_MAX = {altezza_max}, RIGHE_MAX = {righe_max};
        let scelta = passi[passi.length - 1], righe = 0, altezza = 0;
        for (const s of passi) {{
          t.style.fontSize = s + 'px';
          const h = Math.round(t.getBoundingClientRect().height);
          const n = Math.round(h / (s * 1.1));
          if (h <= ALTEZZA_MAX && n <= RIGHE_MAX) {{ scelta = s; righe = n; altezza = h; break; }}
          scelta = s; righe = n; altezza = h;
        }}
        t.style.fontSize = scelta + 'px';
        document.getElementById('misura').textContent = JSON.stringify(
          {{ dimensione: scelta, righe: righe, altezza: altezza, caratteri: t.textContent.length }});
      </script>
    </body></html>"""


def fotografa(html_pagina: str, larghezza: int, altezza: int, destinazione: Path,
              chrome: str) -> dict:
    """Fotografa la pagina e restituisce la misura scritta dal JS."""
    with tempfile.TemporaryDirectory() as tmp:
        pagina = Path(tmp) / "card.html"
        pagina.write_text(html_pagina, encoding="utf-8")
        esito = subprocess.run(
            [
                chrome, "--headless=new", "--no-sandbox", "--disable-gpu",
                "--hide-scrollbars", "--force-device-scale-factor=1",
                "--virtual-time-budget=1500",
                f"--window-size={larghezza},{altezza}",
                f"--screenshot={destinazione}",
                "--dump-dom",
                pagina.as_uri(),
            ],
            check=True, capture_output=True, text=True, timeout=180,
        )
        trovata = re.search(r'<div id="misura"[^>]*>(.*?)</div>', esito.stdout, re.S)
        if not trovata:
            return {}
        try:
            return json.loads(trovata.group(1))
        except json.JSONDecodeError:
            return {}


# ---------------------------------------------------------------- articoli

def leggi_frontmatter(percorso: Path) -> dict[str, str]:
    """Estrae solo i campi che servono alla card, senza dipendere da PyYAML."""
    testo = percorso.read_text(encoding="utf-8")
    pezzi = testo.split("---")
    if len(pezzi) < 3:
        return {}
    blocco = pezzi[1]
    dati: dict[str, str] = {}
    lista: str | None = None
    for riga in blocco.splitlines():
        riga_pulita = riga.strip()
        if riga_pulita.startswith("- ") and lista:
            dati.setdefault(lista, "")
            dati[lista] = (dati[lista] + ", " + riga_pulita[2:].strip()).strip(", ")
            continue
        if not riga_pulita or ":" not in riga_pulita:
            continue
        chiave, _, valore = riga_pulita.partition(":")
        chiave, valore = chiave.strip(), valore.strip().strip('"\'')
        lista = None
        if chiave in ("title", "date", "summary", "categories"):
            if valore.startswith("[") and valore.endswith("]"):
                valore = ", ".join(v.strip().strip('"\'') for v in valore[1:-1].split(",") if v.strip())
            elif valore == "":
                lista = chiave
                valore = ""
            dati[chiave] = valore
    return dati


def data_lingua(iso: str, lingua: str = LINGUA_BASE) -> str:
    """2 ottobre 2026 / October 2, 2026."""
    m = re.match(r"(\d{4})-(\d{2})-(\d{2})", iso or "")
    if not m:
        return ""
    anno, mese, giorno = int(m.group(1)), int(m.group(2)), int(m.group(3))
    if not 1 <= mese <= 12:
        return ""
    mesi = MESI[lingua]
    if lingua == "en":
        return f"{mesi[mese - 1]} {giorno}, {anno}"
    return f"{giorno} {mesi[mese - 1]} {anno}"


def lingua_di(percorso: Path) -> str:
    return "en" if percorso.stem.endswith(".en") else LINGUA_BASE


def nome_base(percorso: Path) -> str:
    """Nome del file senza estensione e senza suffisso di lingua: e' la chiave
    con cui il sito accoppia le due versioni (.File.ContentBaseName)."""
    return re.sub(r"\.en$", "", percorso.stem)


def percorso_card(percorso: Path) -> Path:
    """Dove va l'immagine di un articolo.

    L'italiana in og/v2/<nome>.png, l'inglese in og/v2/en/<nome>.png: cartella
    nuova, quindi nessuna cache di Cloudflare da svecchiare e nessun rischio di
    sovrascrivere l'italiana con l'inglese.
    """
    lingua = lingua_di(percorso)
    if lingua == LINGUA_BASE:
        return USCITA_ARTICOLI / f"{percorso.stem}.png"
    return USCITA_ARTICOLI / lingua / f"{nome_base(percorso)}.png"


def leggi_foto() -> dict[str, dict]:
    """L'indice delle fotografie di sfondo (data/card_immagini.json)."""
    if not INDICE_FOTO.exists():
        return {}
    try:
        return json.loads(INDICE_FOTO.read_text(encoding="utf-8")).get("foto", {})
    except json.JSONDecodeError:
        print(f"ATTENZIONE: {INDICE_FOTO.relative_to(RADICE)} non è JSON valido: "
              "le card useranno lo sfondo scuro")
        return {}


def foto_di(nome: str, indice: dict[str, dict], lingua: str = LINGUA_BASE) -> tuple[Path | None, str]:
    """(file dello sfondo, credito) per un articolo; (None, "") se non c'è.

    Il percorso nell'indice è relativo a `static/images/` (es. "card-arte/foo.jpg"
    oppure "card-bg/foo.jpg"): va risolto da lì, non dentro una cartella fissa,
    altrimenti un'immagine generata finisce per essere cercata tra le fotografie.
    """
    voce = indice.get(nome)
    if not voce:
        return None, ""
    relativo = Path(voce.get("file", ""))
    percorso = (USCITA / relativo).resolve() if relativo.parts else None
    if not percorso or not percorso.exists() or not percorso.is_file():
        return None, ""
    return percorso, voce.get("credito", {}).get(lingua, "")


def genera_articoli(chrome: str, solo: str = "") -> int:
    USCITA_ARTICOLI.mkdir(parents=True, exist_ok=True)
    indice = leggi_foto()
    articoli = sorted(p for p in ARTICOLI.glob("*.md") if not p.stem.startswith("_"))
    if solo:
        articoli = [p for p in articoli if nome_base(p) == solo]
        if not articoli:
            print(f"nessun articolo per «{solo}»")
            return 1
    print(f"articoli trovati: {len(articoli)} | fotografie: {len(indice)}")
    falliti = []
    senza_foto = 0
    for articolo in articoli:
        dati = leggi_frontmatter(articolo)
        titolo = dati.get("title", "").strip()
        if not titolo:
            print(f"  SALTATO {articolo.name}: senza titolo nel frontmatter")
            falliti.append(articolo.name)
            continue
        lingua = lingua_di(articolo)
        categorie = [c for c in dati.get("categories", "").split(",") if c.strip()]
        etichetta = categorie[0].strip() if categorie else "Raziel.news"
        data = data_lingua(dati.get("date", ""), lingua)
        foto, credito = foto_di(nome_base(articolo), indice, lingua)
        if not foto:
            senza_foto += 1
            credito = ""
        destinazione = percorso_card(articolo)
        destinazione.parent.mkdir(parents=True, exist_ok=True)
        misura = fotografa(html_articolo(titolo, etichetta, data, lingua, foto, credito),
                           1200, 630, destinazione, chrome)
        righe = misura.get("righe", "?")
        dimensione = misura.get("dimensione", "?")
        stato = "ok" if misura and misura.get("altezza", 1e9) <= 345 and misura.get("righe", 99) <= 4 else "ATTENZIONE"
        print(f"  {str(destinazione.relative_to(USCITA)):56s} {righe} righe a {dimensione}px  "
              f"{destinazione.stat().st_size} byte  {'foto' if foto else 'scura':6s} {stato}")
        if not misura:
            falliti.append(articolo.name)
    if senza_foto:
        print(f"nota: {senza_foto} card senza fotografia (sfondo scuro): "
              "python3 scripts/foto_card.py per assegnarne una")
    if falliti:
        print(f"ATTENZIONE: immagini non generate o non misurate per {len(falliti)} articoli: {falliti}")
        return 1
    return 0


def verifica() -> int:
    articoli = sorted(p for p in ARTICOLI.glob("*.md") if not p.stem.startswith("_"))
    indice = leggi_foto()
    for lingua in LINGUE:
        suoi = [p for p in articoli if lingua_di(p) == lingua]
        mancanti = [p.stem for p in suoi if not percorso_card(p).exists()]
        print(f"[{lingua}] articoli: {len(suoi)} | immagini: {len(suoi) - len(mancanti)}")
        if mancanti:
            print(f"[{lingua}] senza immagine ({len(mancanti)}): {mancanti}")
            print("nel sito userebbero og-default.png (il modello controlla che il file esista)")
        else:
            print(f"[{lingua}] tutti gli articoli hanno la loro immagine di condivisione")
    tutti = {nome_base(p) for p in articoli}
    senza_foto = sorted(n for n in tutti if not foto_di(n, indice)[0])
    print(f"[foto] articoli con fotografia di sfondo: {len(tutti) - len(senza_foto)} | senza: {len(senza_foto)}")
    if senza_foto:
        print(f"[foto] useranno la card scura: {senza_foto}")
    # Le card di ripiego: home, elenco articoli e pagine informative le citano,
    # quindi devono esistere davvero (una per lingua).
    for f in (USCITA / "og-default.png", USCITA_ARTICOLI / "default.png", USCITA_ARTICOLI / "en" / "default.png"):
        stato = "esiste" if f.exists() else "MANCA"
        print(f"[ripiego] {f.relative_to(RADICE)}: {stato}")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description="Immagini di condivisione di raziel.news")
    ap.add_argument("--articoli", action="store_true", help="una immagine per articolo")
    ap.add_argument("--articolo", default="", help="solo questo articolo (nome file senza .md)")
    ap.add_argument("--verifica", action="store_true", help="quali articoli hanno l'immagine")
    argomenti = ap.parse_args()

    if argomenti.verifica:
        return verifica()

    chrome = trova_chrome()
    if not chrome:
        print("ATTENZIONE: nessun Chrome trovato (usa CHROME=/percorso/chrome): "
              "immagini non generate, il sito userà quelle di ripiego")
        return 0
    print(f"chrome: {chrome}")

    USCITA.mkdir(parents=True, exist_ok=True)
    if argomenti.articoli or argomenti.articolo:
        return genera_articoli(chrome, argomenti.articolo)

    generate = []
    for lingua in LINGUE:
        if lingua == LINGUA_BASE:
            destinazioni = [USCITA / "og-default.png", USCITA_ARTICOLI / "default.png"]
        else:
            destinazioni = [USCITA_ARTICOLI / lingua / "default.png"]
        for destinazione in destinazioni:
            destinazione.parent.mkdir(parents=True, exist_ok=True)
            fotografa(html_card(lingua), 1200, 630, destinazione, chrome)
            generate.append(destinazione)
    logo = USCITA / "logo-512.png"
    fotografa(html_logo(), 512, 512, logo, chrome)
    for f in generate + [logo]:
        print(f"{f.relative_to(RADICE)}  {f.stat().st_size} byte")
    return 0


if __name__ == "__main__":
    sys.exit(main())
