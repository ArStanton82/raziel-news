#!/usr/bin/env python3
"""Guardia meccanica per i post di raziel.news su X.

Uso:
    python3 scripts/x_post_guard.py <file-di-coda.json> [--json] [--quiet]

Esce con 0 se tutte le bozze pronte passano, 1 se almeno una va bloccata.
La guardia NON pubblica e NON modifica niente: legge la coda e dice cosa non puo' uscire.

Perche' esiste: dal 2026-10-07 i post escono **senza approvazione umana** (decisione di Kain,
l'approvazione manuale faceva perdere la finestra buona). Il testo lo scrive un modello, quindi i
controlli che prima faceva Kain li fanno test meccanici, deterministici e verificabili. La guardia
gira due volte: alla creazione della bozza e come ultimo cancello prima della pubblicazione.

Non fa chiamate di rete: e' deterministica e non puo' bloccare un job per un timeout.
"""
from __future__ import annotations

import argparse
import json
import os
import pathlib
import re
import sys
import unicodedata

RADICE = pathlib.Path(__file__).resolve().parent.parent
CODA = pathlib.Path("/root/.hermes/profiles/raziel-news/x-queue")

MIN_CARATTERI = 80          # sotto questa soglia non e' un post, e' un segnaposto
MAX_CARATTERI = 2000        # blocco: oltre, il post non e' piu' leggibile
CARATTERI_CONSIGLIATI = 1500   # avviso, non blocco (sezione 5 della strategia)
MIN_LATO = 900              # lato minimo dell'immagine
RAPPORTO_MIN, RAPPORTO_MAX = 1.60, 1.86   # 16:9 = 1,78

LINK = re.compile(r"https?://|www\.|t\.co/", re.I)
MENTION = re.compile(r"(?<![\w@])@[A-Za-z0-9_]{2,}")
HASHTAG = re.compile(r"(?<!\w)#\w+")
EMOJI = re.compile(
    "[\U0001F000-\U0001FAFF\u2600-\u27BF\u2190-\u21FF\u2B00-\u2BFF\uFE0F\u200D]"
)
SEGNAPOSTO = re.compile(r"\{\{|\}\}|<[a-z][a-z0-9-]*>|TODO|XXX|\[\[|Lorem ipsum")

# Marcatori di lingua: si blocca solo quando la lingua sbagliata domina quella giusta.
IT = re.compile(r"\b(il|lo|la|gli|le|che|non|per|con|una|sono|come|più|perché|anche|questo|"
                r"questa|dopo|prima|senza|tra|fra|molto|essere|avere|quando|dove|suo|sua|loro)\b", re.I)
EN = re.compile(r"\b(the|and|that|with|for|this|are|not|from|which|its|has|have|was|were|"
                r"but|they|their|into|than|when|where|about|after|before|without)\b", re.I)

MESI_IT = ("gennaio", "febbraio", "marzo", "aprile", "maggio", "giugno", "luglio", "agosto",
           "settembre", "ottobre", "novembre", "dicembre")


def normalizza(testo: str) -> str:
    testo = unicodedata.normalize("NFKD", testo.lower())
    return re.sub(r"[^a-z0-9]+", " ", testo).strip()


def parole(testo: str) -> set[str]:
    return {p for p in normalizza(testo).split() if len(p) > 3}


def formato_immagine(blob: bytes) -> str:
    if blob[:8] == b"\x89PNG\r\n\x1a\n":
        return "png"
    if blob[:2] == b"\xff\xd8":
        return "jpeg"
    if blob[:4] == b"RIFF" and blob[8:12] == b"WEBP":
        return "webp"
    return "sconosciuto"


def dimensioni(percorso: pathlib.Path) -> tuple[str, int, int]:
    """Formato e dimensioni reali leggendo l'header: nessuna dipendenza da Pillow."""
    try:
        with open(percorso, "rb") as fh:
            testa = fh.read(4096)
    except OSError:
        return "illeggibile", 0, 0
    formato = formato_immagine(testa)
    if formato == "png" and len(testa) >= 24:
        return formato, int.from_bytes(testa[16:20], "big"), int.from_bytes(testa[20:24], "big")
    if formato == "jpeg":
        i = 2
        while i + 9 < len(testa):
            if testa[i] != 0xFF:
                i += 1
                continue
            marcatore = testa[i + 1]
            if marcatore in (0xD8, 0x01) or 0xD0 <= marcatore <= 0xD7:
                i += 2
                continue
            lunghezza = int.from_bytes(testa[i + 2:i + 4], "big")
            if marcatore in (0xC0, 0xC1, 0xC2, 0xC3, 0xC5, 0xC6, 0xC7, 0xC9, 0xCA, 0xCB,
                             0xCD, 0xCE, 0xCF):
                return formato, int.from_bytes(testa[i + 7:i + 9], "big"), int.from_bytes(testa[i + 5:i + 7], "big")
            i += 2 + lunghezza
    return formato, 0, 0


def testo_pubblicato(draft: dict) -> str:
    return draft.get("text") or draft.get("note_tweet", {}).get("text") or ""


def controlla(draft: dict, pubblicati: list[str]) -> tuple[list[str], list[str]]:
    """Ritorna (motivi di blocco, avvisi). Blocchi vuoti = la bozza puo' uscire."""
    problemi: list[str] = []
    avvisi: list[str] = []
    testo = draft.get("text") or ""

    if not testo.strip():
        problemi.append("testo vuoto")
    else:
        if len(testo) < MIN_CARATTERI:
            problemi.append(f"testo troppo corto ({len(testo)} caratteri, minimo {MIN_CARATTERI})")
        if len(testo) > MAX_CARATTERI:
            problemi.append(f"testo troppo lungo ({len(testo)} caratteri, massimo {MAX_CARATTERI})")
        elif len(testo) > CARATTERI_CONSIGLIATI:
            avvisi.append(f"testo lungo {len(testo)} caratteri (oltre i {CARATTERI_CONSIGLIATI} consigliati)")
        if LINK.search(testo):
            problemi.append("link nel corpo del post (il link va nella prima risposta)")
        if MENTION.search(testo):
            problemi.append("menzione nel corpo del post")
        if HASHTAG.search(testo):
            problemi.append("hashtag")
        if EMOJI.search(testo):
            problemi.append("emoji")
        if SEGNAPOSTO.search(testo):
            problemi.append("segnaposto non risolto nel testo")

        n_it = len(IT.findall(testo))
        n_en = len(EN.findall(testo))
        lingua = (draft.get("lang") or "").lower()
        if lingua == "en" and n_it > n_en:
            problemi.append(f"slot 'en' ma il testo sembra italiano (marcatori it={n_it}, en={n_en})")
        if lingua == "it" and n_en > n_it:
            problemi.append(f"slot 'it' ma il testo sembra inglese (marcatori it={n_it}, en={n_en})")
        if lingua not in ("it", "en"):
            problemi.append(f"lingua non riconosciuta: {lingua!r}")

    link = draft.get("reply_link") or ""
    if not link.startswith("https://raziel.news/"):
        problemi.append(f"reply_link non valido: {link!r}")
    else:
        e_inglese = "/en/" in link
        if draft.get("lang") == "en" and not e_inglese:
            problemi.append("slot 'en' ma il reply_link non punta alla versione /en/")
        if draft.get("lang") == "it" and e_inglese:
            problemi.append("slot 'it' ma il reply_link punta alla versione /en/")

    if draft.get("slot") not in ("reach", "depth"):
        problemi.append(f"slot mancante o non riconosciuto: {draft.get('slot')!r}")
    if not (draft.get("article") or "").strip():
        problemi.append("titolo dell'articolo mancante")

    percorso = pathlib.Path(draft.get("image_path") or "")
    if not draft.get("image_path"):
        problemi.append("image_path mancante: senza card la bozza non esce")
    elif not percorso.exists():
        problemi.append(f"immagine assente su disco: {percorso}")
    else:
        formato, larghezza, altezza = dimensioni(percorso)
        if formato == "sconosciuto" or not larghezza:
            problemi.append(f"immagine illeggibile o formato non riconosciuto: {percorso.name}")
        else:
            if formato not in ("png", "jpeg"):
                problemi.append(f"formato immagine non supportato da X: {formato}")
            if larghezza < MIN_LATO:
                problemi.append(f"immagine troppo piccola: {larghezza}x{altezza}")
            rapporto = larghezza / altezza if altezza else 0
            if not RAPPORTO_MIN <= rapporto <= RAPPORTO_MAX:
                problemi.append(
                    f"immagine non 16:9: {larghezza}x{altezza} (rapporto {rapporto:.2f})"
                )
            if percorso.suffix.lower() == ".png" and formato == "jpeg":
                avvisi.append(f"file .png ma i byte sono JPEG ({percorso.name}): l'upload dichiarerebbe il tipo sbagliato")

    normalizzato = normalizza(testo)
    for precedente in pubblicati:
        if not precedente:
            continue
        if normalizzato and normalizzato in normalizza(precedente):
            problemi.append("testo gia' pubblicato (identico)")
            break
        a, b = parole(testo), parole(precedente)
        if a and b:
            jaccard = len(a & b) / len(a | b)
            if jaccard >= 0.85:
                problemi.append(f"testo quasi identico a un post gia' pubblicato (somiglianza {jaccard:.2f})")
                break

    return problemi, avvisi


def testi_gia_pubblicati(percorsi: list[pathlib.Path], escluso: pathlib.Path) -> list[str]:
    fuori: list[str] = []
    for percorso in percorsi:
        if percorso.resolve() == escluso.resolve():
            continue
        try:
            dati = json.loads(percorso.read_text(encoding="utf-8"))
        except (OSError, ValueError):
            continue
        for draft in dati.get("drafts", []) or []:
            if draft.get("published_tweet_id"):
                fuori.append(testo_pubblicato(draft))
    return fuori


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("path", help="file di coda <YYYY-MM-DD>.json da validare")
    ap.add_argument("--json", action="store_true", help="output JSON")
    ap.add_argument("--quiet", action="store_true", help="stampa solo i blocchi")
    argomenti = ap.parse_args()

    percorso = pathlib.Path(argomenti.path)
    if not percorso.exists():
        sys.exit(f"errore: coda non trovata: {percorso}")
    try:
        dati = json.loads(percorso.read_text(encoding="utf-8"))
    except ValueError as exc:
        sys.exit(f"errore: JSON non valido in {percorso}: {exc}")

    vicini = sorted(p for p in percorso.parent.glob("*.json")
                    if re.fullmatch(r"\d{4}-\d{2}-\d{2}", p.stem))
    pubblicati = testi_gia_pubblicati(vicini, percorso)

    esiti = []
    for draft in dati.get("drafts", []) or []:
        if draft.get("published_tweet_id"):
            continue
        problemi, avvisi = controlla(draft, pubblicati)
        esiti.append({
            "id": draft.get("id"),
            "approved": bool(draft.get("approved")),
            "problemi": problemi,
            "avvisi": avvisi,
            "ok": not problemi,
        })

    pronti = [e for e in esiti if e["approved"]]
    bloccati = [e for e in pronti if not e["ok"]]

    if argomenti.json:
        print(json.dumps({
            "coda": str(percorso),
            "esiti": esiti,
            "pronti": len(pronti),
            "bloccati": len(bloccati),
        }, ensure_ascii=False, indent=2))
        return 1 if bloccati else 0

    if not argomenti.quiet:
        print(f"GUARDIA POST — {percorso.name} (testi pubblicati confrontati: {len(pubblicati)})")
    for esito in esiti:
        if esito["ok"] and argomenti.quiet:
            continue
        stato = "OK" if esito["ok"] else "BLOCCATO"
        attesa = "" if esito["approved"] else "  [in attesa, non uscira']"
        print(f"  {esito['id']}: {stato}{attesa}")
        for problema in esito["problemi"]:
            print(f"      - {problema}")
        for avviso in esito["avvisi"]:
            print(f"      ~ {avviso}")
    if not argomenti.quiet:
        print(f"ESITO: {len(pronti) - len(bloccati)} pronte da pubblicare, {len(bloccati)} bloccate, "
              f"{len(esiti) - len(pronti)} in attesa")

    return 1 if bloccati else 0


if __name__ == "__main__":
    raise SystemExit(main())
