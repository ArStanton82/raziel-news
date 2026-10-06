#!/usr/bin/env python3
"""Illustrazioni per gli articoli che non ne hanno ancora una.

La pipeline pubblica tre articoli al giorno: se l'illustrazione la si genera
solo a mano, dopo tre giorni il sito e' di nuovo senza immagini. Questo script
e' il pezzo che tiene la coda in pari, e nasce per girare da solo (job cron
senza agente: nessun token di modello speso per avviarlo).

Cosa fa, per ogni articolo italiano senza illustrazione:

  1. sceglie il soggetto, in quest'ordine:
       a. il campo `illustrazione:` del frontmatter, se c'e' (e' la via per
          farlo decidere a chi scrive l'articolo);
       b. altrimenti lo chiede a un modello di testo di Venice, leggendo
          titolo e sommario (e' il caso normale: un oggetto per articolo);
       c. altrimenti ripiega sull'oggetto della categoria/del tag
          (arte_card.SOGGETTO_CATEGORIA / SOGGETTO_TAG);
  2. genera l'immagine con Venice riusando `scripts/arte_card.py` — stesso
     preset di stile ("Pop Art"), stesso indice, stessa cartella;
  3. scrive `data/card_immagini.json`, la fonte che leggono la pagina
     dell'articolo (partial illustrazione.html) e la card di condivisione
     (scripts/genera_og.py).

Il soggetto lo scrive **claude-opus-5-5**: misurato il 2026-10-06 sugli stessi
due articoli contro gemini-3-5-flash-lite, gpt-56-sol-pro e qwen-3-8-max, e' il
solo che prende i dettagli dell'articolo (i mixer, le regole ritirate) senza
inventare e senza riempire il prompt di roba. ~2.300 token e 5-6 s per articolo.

Uso:
  python3 scripts/arte_mancanti.py                 # prova a vuoto: chi manca
  python3 scripts/arte_mancanti.py --genera        # genera (non tocca git)
  python3 scripts/arte_mancanti.py --pubblica      # genera, commit e push
  python3 scripts/arte_mancanti.py --rigenera --pubblica   # rifa' tutte (cambia stile)
  python3 scripts/arte_mancanti.py --genera --limite 6
  python3 scripts/arte_mancanti.py --genera --solo-soggetti   # stampa e basta

Chiave: HERMES_CUSTOM_API_VENICE_AI_API_KEY (nel .env del profilo, come
arte_card.py). Modello di testo: --modello-testo o ARTE_MODELLO_TESTO
(predefinito claude-opus-5-5).

Non e' un job della catena editoriale e non blocca nulla: se la chiave manca,
se Venice non risponde o se un articolo non ha titolo, lo dice e prosegue con
gli altri. Esce 0 se non c'e' niente da fare o se ha fatto quello che poteva.
"""

from __future__ import annotations

import argparse
import json
import os
import pathlib
import re
import subprocess
import sys
import time
import urllib.error
import urllib.request

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import arte_card  # noqa: E402  (sta nella stessa cartella)

RADICE = arte_card.RADICE
ARTICOLI = arte_card.ARTICOLI
IMMAGINI = arte_card.IMMAGINI
INDICE = arte_card.INDICE
CHAT = "https://api.venice.ai/api/v1/chat/completions"
MODELLO_TESTO = os.environ.get("ARTE_MODELLO_TESTO", "claude-opus-5-5")

ISTRUZIONI = (
    "You are the art director of a pop art poster series for a technology news site. "
    "For the article below, choose ONE single emblematic object — the kind of thing that "
    "would fill a silkscreen poster. Answer with one sentence in English, at most 30 words: "
    "the object, its scale, its position in the frame. It must be concrete and tied to the "
    "SPECIFICS of this article (the actual machines, documents, places or numbers it talks "
    "about), not generic. Avoid clichés: no generic glowing bitcoin, no futuristic city, no "
    "rows of server racks. No people, no faces, no text, no letters, no logos. The object "
    "fills the frame; the bottom third stays simple. Reply with the sentence alone, nothing "
    "else, and do not think out loud."
)

# Il frontmatter e' YAML semplice: bastano titolo e sommario, letti a righe.
def frontmatter(nome: str) -> dict:
    p = ARTICOLI / f"{nome}.md"
    if not p.exists():
        return {}
    pezzi = p.read_text(encoding="utf-8").split("---", 2)
    if len(pezzi) < 3:
        return {}
    dati = {}
    for riga in pezzi[1].splitlines():
        m = re.match(r"^(title|summary|illustrazione):\s*(.*)$", riga)
        if m:
            dati[m.group(1)] = m.group(2).strip().strip('"\'')
    return dati


def articoli_italiani() -> list[str]:
    return sorted(
        p.name[:-3]
        for p in ARTICOLI.glob("*.md")
        if not p.name.endswith(".en.md") and not p.name.startswith("_")
    )


def senza_illustrazione(indice: dict) -> list[str]:
    """Articoli senza immagine: o il file indicato non c'e', o l'indice non li conosce."""
    fuori = []
    for nome in articoli_italiani():
        voce = indice.get(nome) or {}
        relativo = voce.get("file") or ""
        if not relativo or not (IMMAGINI / relativo).exists():
            fuori.append(nome)
    return fuori


def pulisci(testo: str) -> str:
    """Toglie numerazioni, virgolette e righe di ragionamento dal modello."""
    righe = [r.strip() for r in (testo or "").splitlines() if r.strip()]
    if not righe:
        return ""
    riga = righe[-1]
    riga = re.sub(r'^[\*\-\u2022\d\.\)\s"\']+', "", riga).strip().strip('"\'').strip()
    riga = re.sub(r"\s+", " ", riga)
    if len(riga) < 20 or len(riga) > 300 or riga.endswith((",", ")", "*", ":")):
        return ""
    return riga


def soggetto_da_testo(titolo: str, sommario: str, chiave: str, modello: str) -> str:
    corpo = {
        "model": modello,
        "messages": [
            {"role": "system", "content": ISTRUZIONI},
            {"role": "user", "content": f"Article title: {titolo}\nSummary: {sommario}"},
        ],
        "temperature": 0.6,
        "max_tokens": 1500,
    }
    req = urllib.request.Request(
        CHAT, data=json.dumps(corpo).encode(),
        headers={"Authorization": f"Bearer {chiave}", "Content-Type": "application/json"},
        method="POST")
    with urllib.request.urlopen(req, timeout=180) as f:
        risposta = json.load(f)
    return pulisci(risposta["choices"][0]["message"]["content"])


def soggetto(nome: str, chiave: str, modello: str) -> tuple[str, str]:
    """(soggetto, da dove viene)."""
    dati = frontmatter(nome)
    if dati.get("illustrazione"):
        return dati["illustrazione"], "frontmatter"
    titolo, sommario = dati.get("title", ""), dati.get("summary", "")
    if titolo and chiave:
        try:
            scelto = soggetto_da_testo(titolo, sommario, chiave, modello)
            if scelto:
                return scelto, f"testo:{modello}"
        except Exception as e:
            print(f"  ! {nome}: il modello di testo non ha risposto ({e})", flush=True)
    return arte_card.soggetto(nome), "categoria/tag"


def git(*comandi: str) -> tuple[int, str]:
    esito = subprocess.run(["git", *comandi], cwd=RADICE, capture_output=True, text=True)
    return esito.returncode, (esito.stdout + esito.stderr).strip()


def pubblica(messaggio: str) -> int:
    for comando in (("add", "static/images/card-arte", "data/card_immagini.json"),
                    ("commit", "-m", messaggio),
                    ("pull", "--rebase", "--autostash", "origin", "main"),
                    ("push", "origin", "main")):
        codice, uscita = git(*comando)
        print(f"git {' '.join(comando[:2])}: {uscita.splitlines()[0] if uscita else 'ok'}", flush=True)
        if codice != 0 and comando[0] != "commit":
            return 1
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description="Illustrazioni per gli articoli che non ne hanno")
    ap.add_argument("--genera", action="store_true", help="genera le immagini mancanti")
    ap.add_argument("--pubblica", action="store_true", help="genera, poi commit e push")
    ap.add_argument("--rigenera", action="store_true",
                    help="rifa' l'illustrazione di TUTTI gli articoli (dopo un cambio di stile)")
    ap.add_argument("--limite", type=int, default=0, help="massimo di immagini per esecuzione")
    ap.add_argument("--solo-soggetti", action="store_true", help="stampa i soggetti senza generare")
    ap.add_argument("--silenzioso", action="store_true",
                    help="non stampa nulla se non c'e' niente da fare (per il job cron)")
    ap.add_argument("--modello-testo", default=MODELLO_TESTO, help="modello di testo di Venice")
    ap.add_argument("--modello", default=arte_card.MODELLO, help="modello immagine di Venice")
    ap.add_argument("--preset", default=arte_card.PRESET, help="preset di stile (vuoto = nessuno)")
    ap.add_argument("--cartella", default=arte_card.CARTELLA, help="sottocartella di card-arte/")
    argomenti = ap.parse_args()

    def di(msg: str = "") -> None:
        """Stampa, ma in modalita' silenziosa solo quando serve."""
        if not argomenti.silenzioso:
            print(msg, flush=True)

    indice = json.loads(INDICE.read_text(encoding="utf-8")) if INDICE.exists() else {"versione": 1, "foto": {}}
    indice.setdefault("foto", {})
    totale = articoli_italiani()
    coda = totale if argomenti.rigenera else senza_illustrazione(indice["foto"])
    if argomenti.silenzioso:
        if not coda:
            return 0
        print(f"articoli senza illustrazione: {len(coda)}")
    else:
        print(f"articoli: {len(totale)} | con illustrazione: {len(totale) - len(senza_illustrazione(indice['foto']))} | da fare: {len(coda)}"
              + ("  (rigenerazione completa)" if argomenti.rigenera else ""))
        if not coda:
            print("niente da fare: tutti gli articoli hanno un'illustrazione")
            return 0
        for nome in coda:
            print(f"  - {nome}")

    if not (argomenti.genera or argomenti.pubblica or argomenti.solo_soggetti):
        print("\n(prova a vuoto: usa --genera per generare, --pubblica per pubblicare)")
        return 0

    chiave = arte_card.chiave()
    if not chiave:
        print("chiave Venice non trovata (HERMES_CUSTOM_API_VENICE_AI_API_KEY)")
        return 1
    if argomenti.limite:
        coda = coda[: argomenti.limite]

    generate, errori = 0, 0
    for i, nome in enumerate(coda, 1):
        scena, origine = soggetto(nome, chiave, argomenti.modello_testo)
        di(f"\n[{i}/{len(coda)}] {nome}  (soggetto: {origine})\n    {scena}")
        if argomenti.solo_soggetti:
            continue
        destinazione = arte_card.percorso(nome, argomenti.cartella)
        esito = arte_card.genera(arte_card.STILE + scena, chiave, destinazione,
                                 argomenti.modello, argomenti.preset)
        di(f"    {esito}")
        if not esito.startswith("ok"):
            errori += 1
            continue
        arte_card.scrivi_indice(nome, scena, destinazione, argomenti.modello,
                                argomenti.preset, origine)
        generate += 1
        time.sleep(1)

    print(f"\ngenerate: {generate} | errori: {errori}")
    if generate and argomenti.pubblica:
        return pubblica(f"feat(arte): illustrazioni per {generate} articoli")
    return 0


if __name__ == "__main__":
    sys.exit(main())
