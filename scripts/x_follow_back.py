#!/usr/bin/env python3
"""Ricambio dei follow su X: segue chi ci ha menzionato o chi ci segue da poco.

Uso:
    python3 scripts/x_follow_back.py [--dry] [--max 12]

Perche' esiste: il codice di ranking pubblicato da X (home-mixer/params/param.rs) assegna
BidirectionalFollowReplyWeightBoost = 15.0 alla probabilita' di reply fra account che si
seguono a vicenda, contro un ReplyWeight di base di 5.0. Al 25 novembre 2026 solo il 10% dei
nostri follower e' un follow bidirezionale (20 su un campione di 200): il premio piu' alto del
sistema resta spento. Questo script riporta il rapporto verso destinatari plausibili e NIENTE
altro: nessun unfollow, nessun follow a caso.

Fonti, in ordine di priorita':
  1. autori delle menzioni degli ultimi 7 giorni (conversazione reale);
  2. follower recenti con almeno 100 follower propri (account non vuoti).
Si salta chi seguiamo gia'. Limite giornaliero 12, conteggiato su un log per data.

Esce 0 sempre (un follow non riuscito non deve far fallire il job), stampa un riepilogo breve.
"""
from __future__ import annotations

import argparse
import json
import pathlib
import subprocess
import sys
import time

PROFILO = "/root/.hermes/profiles/raziel-news"
LOG = pathlib.Path(PROFILO) / "x-queue" / "follow-back-log.json"
ME = "1397653619172954118"
MAX_DEFAULT = 12
MIN_FOLLOWER_AUTORE = 100
PAUSA = pathlib.Path(PROFILO) / "x-queue" / "PAUSA"


def xurl(percorso: str) -> dict:
    """Chiama xurl e torna il JSON; su errore torna {} (lo script non deve morire)."""
    try:
        esito = subprocess.run(["xurl", percorso], capture_output=True, text=True, timeout=90)
        return json.loads(esito.stdout, strict=False) if esito.stdout.strip() else {}
    except (subprocess.TimeoutExpired, ValueError):
        return {}


def seguiti_oggi() -> list[str]:
    try:
        dati = json.loads(LOG.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        dati = {}
    return dati.get(timeout_key(), [])


def timeout_key() -> str:
    return time.strftime("%Y-%m-%d")


def registra(ids: list[str]) -> None:
    try:
        dati = json.loads(LOG.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        dati = {}
    oggi = timeout_key()
    dati[oggi] = sorted(set(dati.get(oggi, [])) | set(ids))
    # tiene solo gli ultimi 60 giorni di log
    for chiave in sorted(dati)[:-60]:
        dati.pop(chiave, None)
    LOG.parent.mkdir(parents=True, exist_ok=True)
    LOG.write_text(json.dumps(dati, ensure_ascii=False, indent=2), encoding="utf-8")


def candidati() -> list[dict]:
    """Ritorna [{'id','username','motivo'}] in ordine di priorita'."""
    fuori: list[dict] = []
    visti: set[str] = set()

    menzioni = xurl(f"/2/users/{ME}/mentions?max_results=100&tweet.fields=author_id,created_at")
    for tweet in menzioni.get("data", []) or []:
        autore = str(tweet.get("author_id") or "")
        if autore and autore != ME and autore not in visti:
            visti.add(autore)
            fuori.append({"id": autore, "motivo": "menzione"})

    if len(fuori) < 40:  # solo se le menzioni non bastano
        follower = xurl(
            f"/2/users/{ME}/followers?max_results=100&user.fields=public_metrics"
        )
        for utente in follower.get("data", []) or []:
            uid = str(utente.get("id") or "")
            if not uid or uid in visti:
                continue
            if (utente.get("public_metrics") or {}).get("followers_count", 0) < MIN_FOLLOWER_AUTORE:
                continue
            visti.add(uid)
            fuori.append({"id": uid, "motivo": "follower"})

    return fuori


def stato_relazione(ids: list[str]) -> dict[str, list[str]]:
    """connection_status per id: dice chi seguiamo gia' (utile per saltarlo)."""
    fuori: dict[str, list[str]] = {}
    for avvio in range(0, len(ids), 100):
        blocco = ids[avvio:avvio + 100]
        dati = xurl(f"/2/users?ids={','.join(blocco)}&user.fields=connection_status")
        for utente in dati.get("data", []) or []:
            fuori[str(utente["id"])] = utente.get("connection_status") or []
    return fuori


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry", action="store_true", help="mostra chi seguirebbe senza seguire")
    ap.add_argument("--max", type=int, default=MAX_DEFAULT)
    arg = ap.parse_args()

    if PAUSA.exists() and not arg.dry:
        print("pausa attiva (file x-queue/PAUSA): nessun follow")
        return 0

    gia = seguiti_oggi()
    restano = max(0, arg.max - len(gia))
    if restano <= 0:
        print(f"limite giornaliero raggiunto ({len(gia)}/{arg.max}): niente da fare")
        return 0

    elenco = candidati()
    if not elenco:
        print("nessun candidato (menzioni e follower recenti gia' a posto)")
        return 0

    stato = stato_relazione([c["id"] for c in elenco[:150]])
    da_seguire = [
        c for c in elenco
        if "following" not in stato.get(c["id"], [])
    ][:restano]

    if not da_seguire:
        print("tutti i candidati sono gia' seguiti: niente da fare")
        return 0

    fatti: list[str] = []
    for cand in da_seguire:
        if arg.dry:
            fatti.append(cand["id"])
            print(f"  (dry) {cand['id']} — {cand['motivo']}")
            continue
        esito = subprocess.run(["xurl", "follow", cand["id"]], capture_output=True, text=True, timeout=90)
        if esito.returncode == 0 and '"errors"' not in (esito.stdout or ""):
            fatti.append(cand["id"])
            print(f"  seguito {cand['id']} ({cand['motivo']})")
        else:
            print(f"  non riuscito {cand['id']}: {(esito.stdout or esito.stderr).strip()[:120]}")
        time.sleep(2)

    if not arg.dry and fatti:
        registra(fatti)

    reciproci = sum(1 for c in elenco[:150] if "followed_by" in stato.get(c["id"], []))
    print(
        f"follow nuovi: {len(fatti)} | totale di oggi: {len(gia) + len(fatti)}/{arg.max} | "
        f"candidati visti: {len(elenco)} | bidirezionali fra i candidati: {reciproci}"
    )
    if arg.dry:
        print("(prova a vuoto: niente e' stato scritto)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
