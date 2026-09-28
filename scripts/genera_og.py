#!/usr/bin/env python3
"""Genera le immagini di condivisione (Open Graph) di raziel.news.

Produce, dentro static/images/:
  og-default.png   1200x630  immagine usata da og:image e twitter:image
  logo-512.png      512x512  logo del publisher per i dati strutturati

Perche' uno script: il PNG deve restare riproducibile. Si costruisce una
pagina HTML con le stesse tinte del sito e la si fotografa con Chrome
headless alla dimensione esatta. I caratteri (Atkinson Hyperlegible) sono
incorporati in base64, cosi' non serve un server.

Uso:  python3 scripts/genera_og.py            (dalla radice del repo)
      CHROME=/percorso/chrome python3 scripts/genera_og.py
"""

from __future__ import annotations

import base64
import os
import subprocess
import tempfile
from pathlib import Path

RADICE = Path(__file__).resolve().parent.parent
FONT = RADICE / "static" / "static" / "fonts"
USCITA = RADICE / "static" / "images"
CHROME = os.environ.get(
    "CHROME", "/root/.cache/ms-playwright/chromium-1243/chrome-linux64/chrome"
)

ACCENTO = "#6d5ae6"
FONDO = "#1b1c1d"
TESTO = "#f2f2f2"
TENUE = "#a9a9b3"


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


def html_card() -> str:
    return f"""<!doctype html><html lang="it"><head><meta charset="utf-8"><style>{stile()}
      body{{width:1200px;height:630px;padding:64px 72px;display:flex;flex-direction:column;justify-content:space-between}}
      .marca{{display:flex;align-items:baseline;gap:10px;font-size:38px;font-weight:700;letter-spacing:0}}
      .marca .segno{{color:{ACCENTO}}}
      h1{{font-size:74px;line-height:1.08;font-weight:700;letter-spacing:-0.01em;max-width:1000px}}
      h1 em{{font-style:normal;color:{ACCENTO}}}
      .piede{{display:flex;align-items:baseline;justify-content:space-between;font-size:26px;color:{TENUE}}}
      .piede .motto{{font-style:italic}}
    </style></head><body>
      <div class="marca"><span class="segno">&gt;</span><span>Raziel.news</span></div>
      <h1>Cronache e riflessioni su <em>intelligenza artificiale</em>, agenti autonomi e Venice.ai</h1>
      <div class="piede"><span>raziel.news</span><span class="motto">Il peso delle scelte non svanisce.</span></div>
    </body></html>"""


def html_logo() -> str:
    return f"""<!doctype html><html lang="it"><head><meta charset="utf-8"><style>{stile()}
      body{{width:512px;height:512px;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:6px}}
      .segno{{color:{ACCENTO};font-size:150px;font-weight:700;line-height:1}}
      .nome{{font-size:64px;font-weight:700;letter-spacing:0}}
    </style></head><body>
      <div class="segno">&gt;</div><div class="nome">Raziel.news</div>
    </body></html>"""


def fotografa(html: str, larghezza: int, altezza: int, destinazione: Path) -> None:
    with tempfile.TemporaryDirectory() as tmp:
        pagina = Path(tmp) / "card.html"
        pagina.write_text(html, encoding="utf-8")
        subprocess.run(
            [
                CHROME, "--headless=new", "--no-sandbox", "--disable-gpu",
                "--hide-scrollbars", "--force-device-scale-factor=1",
                f"--window-size={larghezza},{altezza}",
                f"--screenshot={destinazione}",
                pagina.as_uri(),
            ],
            check=True, capture_output=True, timeout=120,
        )


def main() -> int:
    USCITA.mkdir(parents=True, exist_ok=True)
    fotografa(html_card(), 1200, 630, USCITA / "og-default.png")
    fotografa(html_logo(), 512, 512, USCITA / "logo-512.png")
    for nome in ("og-default.png", "logo-512.png"):
        f = USCITA / nome
        print(f"{f.relative_to(RADICE)}  {f.stat().st_size} byte")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
