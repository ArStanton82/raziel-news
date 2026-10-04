#!/usr/bin/env python3
"""Sceglie la fotografia di sfondo delle card di condivisione (Open Graph).

Per ogni articolo (la coppia italiano/inglese conta una volta sola, perche' le
due card condividono la foto) cerca su Wikimedia Commons un'immagine a licenza
libera pertinente al tema, la normalizza e la salva in
`static/images/card-bg/<nome-base>.jpg`, scrivendo credito e licenza in
`data/card_immagini.json`.

Perche' le foto stanno nel repo e non si scaricano in CI: la card la costruisce
`scripts/genera_og.py` durante la build, quindi il file deve esistere li'. La
scelta invece la fa questo script, una volta, e resta scritta nel JSON: cosi' il
PNG e' riproducibile e la foto non cambia a ogni deploy.

Regole sulle immagini (non negoziabili):
  - solo licenze libere: pubblico dominio, CC0, CC BY, CC BY-SA;
  - niente immagini con restrizioni dichiarate su Commons;
  - orizzontali, almeno 1600px di larghezza;
  - il credito (autore + licenza) finisce stampato in piccolo sulla card:
    obbligatorio per le CC BY, buona pratica per le altre.

Uso:
  python3 scripts/foto_card.py                 assegna una foto agli articoli che non ce l'hanno
  python3 scripts/foto_card.py --articolo NOME  solo quell'articolo (nome file senza .md)
  python3 scripts/foto_card.py --forza          risceglie anche se la foto c'e' gia'
  python3 scripts/foto_card.py --verifica       elenca chi manca, senza scaricare nulla
  python3 scripts/foto_card.py --query "..."    prova una ricerca e mostra i candidati
"""

from __future__ import annotations

import argparse
import html
import json
import re
import sys
import urllib.parse
import urllib.request
from pathlib import Path

RADICE = Path(__file__).resolve().parent.parent
ARTICOLI = RADICE / "content" / "posts"
FOTO = RADICE / "static" / "images" / "card-bg"
INDICE = RADICE / "data" / "card_immagini.json"
UA = "raziel-news-bot/1.0 (https://raziel.news; redazione@raziel.news)"

LARGHEZZA_MIN = 1600
LARGHEZZA_FINALE = 1600
QUALITA = 82

LICENZE_OK = ("cc0", "public domain", "pubblico dominio", "cc by", "cc by-sa", "pdm")
MIME_OK = ("image/jpeg", "image/png", "image/webp")

# Termini di ricerca per categoria: Commons non ha foto di "Hermes" o "VVV",
# quindi si cerca l'oggetto fisico che rappresenta il tema (sala macchine,
# data center, sala audizioni, sala contrattazioni).
QUERY_CATEGORIA = {
    "AI": "artificial intelligence computer",
    "Crypto": "bitcoin cryptocurrency",
    "Blockchain": "blockchain technology ledger",
    "Hermes": "data center server room",
    "Venice.ai": "graphics card GPU computing",
    "Filosofia dell'AI": "philosophy books library",
}

# Tag italiani (o ambigui) tradotti in termini utili a Commons.
TAG_QUERY = {
    "bitcoin": "bitcoin",
    "stablecoin": "bitcoin ATM",
    "etf": "stock exchange trading floor",
    "blockchain": "bitcoin mining facility",
    "tokenomics": "supercomputer",
    "vvv": "GPU graphics card",
    "diem": "GPU graphics card",
    "venice": "GPU graphics card",
    "venice.ai": "GPU graphics card",
    "agenti autonomi": "data center server room",
    "agenti": "data center server room",
    "hermes": "server rack",
    "hermes agent": "server rack",
    "openclaw": "server rack",
    "plugin": "source code screen",
    "open-source": "source code screen",
    "memoria": "server rack",
    "privacy": "cybersecurity",
    "intelligenza artificiale": "supercomputer",
    "openai": "supercomputer",
    "anthropic": "supercomputer",
    "regolamentazione": "parliament chamber",
    "sec": "stock exchange trading floor",
    "papa": "St Peter's Square Vatican",
    "udienza": "senate hearing room",
    "responsabilita": "courtroom",
    "liability": "courtroom",
    "sicurezza": "cybersecurity",
    "nvidia": "GPU graphics card",
    "gpu": "GPU graphics card",
    "ricerca web": "source code screen",
    "discord": "smartphone app screen",
    "app": "smartphone app screen",
}

# Immagini che non sono fotografie (diagrammi, mappe, icone): la card vuole una
# scena, non un grafico. Si penalizzano, non si escludono: meglio una mappa che
# nessuna immagine.
PAROLE_NON_FOTO = ("diagram", "chart", "graph", "map of", "map ", "logo", "icon",
                   "screenshot", "plot", "infographic", "scale.png", "distribution")

ETICHETTE_LICENZA = {
    "public domain": {"it": "pubblico dominio", "en": "public domain"},
    "cc0": {"it": "CC0", "en": "CC0"},
}


# ------------------------------------------------------------------ frontmatter

def frontmatter(percorso: Path) -> dict[str, list[str] | str]:
    """Legge i campi del frontmatter che servono (senza dipendere da PyYAML)."""
    testo = percorso.read_text(encoding="utf-8")
    pezzi = testo.split("---", 2)
    if len(pezzi) < 3:
        return {}
    dati: dict[str, list[str] | str] = {}
    chiave_corrente: str | None = None
    for riga in pezzi[1].splitlines():
        if re.match(r"^\s*-\s", riga) and chiave_corrente:
            valore = riga.strip()[2:].strip().strip("\"'")
            attuale = dati.get(chiave_corrente)
            if isinstance(attuale, list):
                attuale.append(valore)
            continue
        m = re.match(r"^([A-Za-z_]+):\s*(.*)$", riga)
        if not m:
            continue
        chiave, valore = m.group(1), m.group(2).strip()
        chiave_corrente = None
        if chiave not in ("title", "date", "categories", "tags", "summary"):
            continue
        if valore.startswith("[") and valore.endswith("]"):
            dati[chiave] = [v.strip().strip("\"'") for v in valore[1:-1].split(",") if v.strip()]
        elif valore == "":
            dati[chiave] = []
            chiave_corrente = chiave
        else:
            dati[chiave] = valore.strip("\"'")
    return dati


def coppie_articoli() -> list[str]:
    """Nomi base degli articoli: i .en.md contano una volta sola, col gemello."""
    nomi = set()
    for p in sorted(ARTICOLI.glob("*.md")):
        if p.stem.startswith("_"):
            continue
        nomi.add(re.sub(r"\.en$", "", p.stem))
    return sorted(nomi)


def file_italiano(nome: str) -> Path | None:
    for suffisso in (".md", ".en.md"):
        p = ARTICOLI / f"{nome}{suffisso}"
        if p.exists() and not nome.endswith(".en"):
            return p
    p = ARTICOLI / f"{nome}.md"
    return p if p.exists() else None


def query_per(nome: str) -> list[str]:
    """Cascata di ricerche: i tag (tradotti), poi la categoria, poi un tema generico.

    Commons tratta la query come una AND di tutte le parole, quindi una ricerca
    lunga non trova nulla: si prova dal più specifico al più generico e si usa
    la prima che restituisce candidati.
    """
    p = file_italiano(nome)
    if not p:
        return ["data center server room"]
    dati = frontmatter(p)
    tag = dati.get("tags") or []
    if isinstance(tag, str):
        tag = [tag]
    termini: list[str] = []
    for t in tag:
        chiave = str(t).strip().lower()
        if chiave in TAG_QUERY and TAG_QUERY[chiave] not in termini:
            termini.append(TAG_QUERY[chiave])
    categorie = dati.get("categories") or []
    if isinstance(categorie, str):
        categorie = [categorie]
    per_categoria = ""
    for c in categorie:
        if str(c).strip() in QUERY_CATEGORIA:
            per_categoria = QUERY_CATEGORIA[str(c).strip()]
            break

    cascata: list[str] = []
    if len(termini) >= 2:
        cascata.append(f"{termini[0]} {termini[1]}")
    cascata.extend(termini[:2])
    if per_categoria:
        cascata.append(per_categoria)
    cascata.append("data center server room")
    viste, fuori = set(), []
    for q in cascata:
        if q and q not in viste:
            viste.add(q)
            fuori.append(q)
    return fuori


# ---------------------------------------------------------------------- commons

def commons(query: str, limite: int = 12) -> list[dict]:
    parametri = urllib.parse.urlencode({
        "action": "query",
        "generator": "search",
        "gsrsearch": f"filetype:bitmap {query}",
        "gsrnamespace": "6",
        "gsrlimit": str(limite),
        "prop": "imageinfo",
        "iiprop": "url|size|mime|extmetadata",
        "iiurlwidth": str(LARGHEZZA_FINALE),
        "format": "json",
    })
    req = urllib.request.Request(f"https://commons.wikimedia.org/w/api.php?{parametri}",
                                headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=45) as f:
        dati = json.load(f)
    fuori = []
    for pagina in (dati.get("query") or {}).get("pages", {}).values():
        info = (pagina.get("imageinfo") or [{}])[0]
        em = info.get("extmetadata", {})
        licenza = ((em.get("LicenseShortName") or {}).get("value") or "").strip()
        restrizioni = ((em.get("Restrictions") or {}).get("value") or "").strip()
        larghezza, altezza = info.get("width", 0), info.get("height", 0)
        if info.get("mime") not in MIME_OK:
            continue
        if not any(l in licenza.lower() for l in LICENZE_OK):
            continue
        if restrizioni:
            continue
        if larghezza < LARGHEZZA_MIN or larghezza <= altezza:
            continue
        fuori.append({
            "titolo": pagina.get("title", ""),
            "licenza": licenza,
            "autore": re.sub(r"<[^>]+>", "", (em.get("Artist") or {}).get("value") or "").strip()[:90],
            "descrizione": re.sub(r"<[^>]+>", "", (em.get("ImageDescription") or {}).get("value") or "").strip(),
            "url": info.get("thumburl") or info.get("url"),
            "pagina": "https://commons.wikimedia.org/wiki/" + urllib.parse.quote(pagina.get("title", "").replace(" ", "_")),
            "w": larghezza,
            "h": altezza,
        })
    return fuori


def punteggio(candidato: dict, query: str, usati: set[str]) -> tuple:
    """Ordina i candidati: pertinenza, poi varietà, poi qualità dell'immagine.

    L'ordine dei criteri conta: prima che la foto c'entri col tema, poi che non
    sia già usata da un altro articolo (una griglia di card tutte uguali è
    peggio di una foto meno precisa), poi che sia una fotografia e non un
    diagramma, e infine la forma (più vicina a 16:9) e la risoluzione.
    """
    testo = (candidato["titolo"] + " " + candidato["descrizione"]).lower()
    parole = [p for p in re.split(r"\W+", query.lower()) if len(p) > 3]
    centri = sum(1 for p in parole if p in testo)
    ripetuta = 1 if candidato["titolo"] in usati else 0
    e_foto = 0 if any(p in testo for p in PAROLE_NON_FOTO) else 1
    proporzione = candidato["w"] / max(candidato["h"], 1)
    forma = -abs(proporzione - 16 / 9)
    return (-ripetuta, centri, e_foto, round(forma, 3), candidato["w"])


def scarica(url: str, destinazione: Path) -> int:
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=90) as f:
        dati = f.read()
    try:
        from PIL import Image
        import io
        immagine = Image.open(io.BytesIO(dati)).convert("RGB")
        ricampionamento = getattr(Image, "Resampling", Image).LANCZOS
        if immagine.width > LARGHEZZA_FINALE:
            altezza = round(immagine.height * LARGHEZZA_FINALE / immagine.width)
            immagine = immagine.resize((LARGHEZZA_FINALE, altezza), ricampionamento)
        destinazione.parent.mkdir(parents=True, exist_ok=True)
        immagine.save(destinazione, "JPEG", quality=QUALITA, optimize=True, progressive=True)
    except ImportError:
        destinazione.parent.mkdir(parents=True, exist_ok=True)
        destinazione.write_bytes(dati)
    return destinazione.stat().st_size


# ---------------------------------------------------------------------- indice

def leggi_indice() -> dict:
    if INDICE.exists():
        return json.loads(INDICE.read_text(encoding="utf-8"))
    return {"versione": 1, "nota": "Foto di sfondo delle card di condivisione. "
            "Scelte da scripts/foto_card.py su Wikimedia Commons (licenze libere). "
            "Modifica a mano 'file' e 'query' per correggere una scelta, poi rilancia "
            "lo script con --forza.", "foto": {}}


def scrivi_indice(indice: dict) -> None:
    INDICE.parent.mkdir(parents=True, exist_ok=True)
    INDICE.write_text(json.dumps(indice, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def etichetta_licenza(licenza: str, lingua: str) -> str:
    chiave = licenza.strip().lower()
    for k, v in ETICHETTE_LICENZA.items():
        if k in chiave:
            return v.get(lingua, licenza)
    return licenza


# ------------------------------------------------------------------------ azioni

def assegna(nomi: list[str], forza: bool) -> int:
    indice = leggi_indice()
    foto = indice.setdefault("foto", {})
    esiti = {"nuove": 0, "saltate": 0, "fallite": 0}
    usati = {v.get("titolo", "") for v in foto.values() if v.get("scelta") == "manuale"}
    for nome in nomi:
        voce = foto.get(nome)
        if voce and voce.get("scelta") == "manuale":
            esiti["saltate"] += 1
            continue
        if voce and (FOTO / Path(voce["file"]).name).exists() and not forza:
            esiti["saltate"] += 1
            continue
        # Tutte le ricerche della cascata concorrono alla stessa rosa di
        # candidati: una query generica può pescare una foto migliore di quella
        # specifica che non trova nulla.
        candidati: dict[str, dict] = {}
        for tentativo in query_per(nome):
            try:
                trovati = commons(tentativo)
            except Exception as e:  # rete, timeout, API giu': si prova il tentativo successivo
                print(f"  ! {nome}: ricerca «{tentativo}» fallita ({e})")
                continue
            for c in trovati:
                c.setdefault("query", tentativo)
                candidati.setdefault(c["titolo"], c)
        if not candidati:
            print(f"  ! {nome}: nessun candidato da nessuna ricerca")
            esiti["fallite"] += 1
            continue
        ordinati = sorted(candidati.values(),
                          key=lambda c: (punteggio(c, c["query"], usati), c["titolo"]),
                          reverse=True)
        scelto = ordinati[0]
        query_scelta = scelto["query"]
        usati.add(scelto["titolo"])
        destinazione = FOTO / f"{nome}.jpg"
        try:
            byte = scarica(scelto["url"], destinazione)
        except Exception as e:
            print(f"  ! {nome}: scarico fallito ({e})")
            esiti["fallite"] += 1
            continue
        foto[nome] = {
            "file": f"card-bg/{destinazione.name}",
            "titolo": scelto["titolo"],
            "autore": scelto["autore"],
            "licenza": scelto["licenza"],
            "pagina": scelto["pagina"],
            "query": query_scelta,
            # Il credito è già composto per lingua: la card italiana scrive
            # "Foto:", quella inglese "Photo:", e la licenza è tradotta dove ha
            # senso ("pubblico dominio" / "public domain").
            "credito": {
                lingua: f"{'Foto' if lingua == 'it' else 'Photo'}: {scelto['autore']} / {etichetta_licenza(scelto['licenza'], lingua)}"
                for lingua in ("it", "en")
            },
        }
        print(f"  + {nome}: {scelto['titolo']} [{scelto['licenza']}] {byte} byte")
        esiti["nuove"] += 1
    scrivi_indice(indice)
    print(f"nuove: {esiti['nuove']} | gia' assegnate: {esiti['saltate']} | fallite: {esiti['fallite']}")
    return 0 if esiti["fallite"] == 0 else 1


def verifica() -> int:
    indice = leggi_indice()
    foto = indice.get("foto", {})
    nomi = coppie_articoli()
    mancanti = []
    for nome in nomi:
        voce = foto.get(nome)
        if not voce or not (FOTO / Path(voce["file"]).name).exists():
            mancanti.append(nome)
    print(f"articoli: {len(nomi)} | con foto: {len(nomi) - len(mancanti)}")
    if mancanti:
        print(f"senza foto ({len(mancanti)}) — useranno la card scura:")
        for n in mancanti:
            print("  -", n)
    licenze = {}
    for voce in foto.values():
        licenze[voce.get("licenza", "?")] = licenze.get(voce.get("licenza", "?"), 0) + 1
    print("licenze:", licenze)
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description="Foto di sfondo per le card di condivisione")
    ap.add_argument("--articolo", help="nome file senza .md (es. 2026-10-04-chi-risponde-...)")
    ap.add_argument("--forza", action="store_true", help="risceglie anche se la foto esiste")
    ap.add_argument("--verifica", action="store_true", help="elenca chi manca, non scarica")
    ap.add_argument("--query", help="prova una ricerca su Commons e mostra i candidati")
    argomenti = ap.parse_args()

    if argomenti.query:
        candidati = commons(argomenti.query)
        candidati.sort(key=lambda c: punteggio(c, argomenti.query, set()), reverse=True)
        print(f"query: {argomenti.query} -> {len(candidati)} candidati")
        for c in candidati[:10]:
            print(f"  {c['w']}x{c['h']}  {c['licenza']:22s} {c['autore'][:28]:28s} {c['titolo']}")
        return 0

    if argomenti.verifica:
        return verifica()

    nomi = [argomenti.articolo] if argomenti.articolo else coppie_articoli()
    return assegna(nomi, argomenti.forza)


if __name__ == "__main__":
    sys.exit(main())
