#!/usr/bin/env python3
"""Genera l'illustrazione di un post X con un modello immagine di Venice.ai.

Uso:
    python3 scripts/x_image.py --prompt "..." --out x-queue/images/2026-10-06-en-1.png
    python3 scripts/x_image.py --prompt-file /tmp/p.txt --out out.png --model z-image-turbo

Modello predefinito: venice-sd35 (0,01 USD per generazione, soggetto leggibile in miniatura).
Fallback automatico: z-image-turbo (stesso prezzo, piu' veloce) se il primo fallisce.
`hide_watermark` e' sempre True: senza, Venice stampa la firma "Venice" nell'angolo in basso a
sinistra e il post sembra contenuto di terzi.

Nessun segreto in questo file: la chiave si legge da VENICE_API_KEY nell'ambiente oppure dal .env
del profilo indicato da --env-file.
"""
from __future__ import annotations

import argparse
import base64
import json
import os
import re
import sys
import time
import urllib.request

API = "https://api.venice.ai/api/v1/image/generate"
DEFAULT_MODEL = "venice-sd35"
FALLBACK_MODEL = "z-image-turbo"
# Prezzi verificati il 5 ottobre 2026 via /api/v1/models?type=image: entrambi 0,01 USD.
# Alternativa allo stesso prezzo: chroma. Da evitare per un sito di notizie:
# lustify-* (contenuti adulti) e wai-Illustrious (anime).
KEY_RE = re.compile(r"^(?:VENICE_API_KEY|HERMES_CUSTOM_API_VENICE_AI_API_KEY)=(.*)$")


def read_key(env_file: str | None) -> str:
    key = os.environ.get("VENICE_API_KEY") or os.environ.get("HERMES_CUSTOM_API_VENICE_AI_API_KEY")
    if key:
        return key.strip().strip('"')
    candidates = [env_file] if env_file else []
    candidates += [
        "/root/.hermes/profiles/raziel-news/.env",
        os.path.expanduser("~/.hermes/.env"),
    ]
    for path in candidates:
        if not path or not os.path.exists(path):
            continue
        for line in open(path, encoding="utf-8", errors="ignore"):
            m = KEY_RE.match(line.strip())
            if m:
                return m.group(1).strip().strip('"')
    sys.exit("errore: nessuna chiave Venice trovata (VENICE_API_KEY o --env-file)")


def generate(key: str, model: str, prompt: str, width: int, height: int, steps: int, timeout: int) -> bytes:
    body = json.dumps({
        "model": model,
        "prompt": prompt,
        "width": width,
        "height": height,
        "steps": steps,
        "format": "png",
        "safe_mode": True,
        "hide_watermark": True,
    }).encode()
    req = urllib.request.Request(
        API, data=body,
        headers={"Authorization": f"Bearer {key}", "Content-Type": "application/json"},
    )
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        data = json.load(resp)
    images = data.get("images") or []
    if not images:
        raise RuntimeError(f"{model}: risposta senza immagini")
    return base64.b64decode(images[0])


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--prompt")
    ap.add_argument("--prompt-file")
    ap.add_argument("--out", required=True)
    ap.add_argument("--model", default=DEFAULT_MODEL)
    ap.add_argument("--width", type=int, default=1024)
    ap.add_argument("--height", type=int, default=576)
    ap.add_argument("--steps", type=int, default=25)
    ap.add_argument("--timeout", type=int, default=180)
    ap.add_argument("--env-file")
    args = ap.parse_args()

    prompt = args.prompt
    if args.prompt_file:
        prompt = open(args.prompt_file, encoding="utf-8").read().strip()
    if not prompt:
        sys.exit("errore: serve --prompt o --prompt-file")

    # I divisori dei modelli sono 8 o 16: arrotondo per non far rifiutare la richiesta.
    args.width -= args.width % 16
    args.height -= args.height % 16

    key = read_key(args.env_file)
    os.makedirs(os.path.dirname(os.path.abspath(args.out)), exist_ok=True)

    chain = [args.model]
    if args.model == DEFAULT_MODEL:
        chain.append(FALLBACK_MODEL)

    last_err: Exception | None = None
    for model in chain:
        steps = 8 if model == FALLBACK_MODEL else args.steps
        t0 = time.time()
        try:
            blob = generate(key, model, prompt, args.width, args.height, steps, args.timeout)
            with open(args.out, "wb") as fh:
                fh.write(blob)
            print(json.dumps({
                "status": "ok",
                "model": model,
                "path": os.path.abspath(args.out),
                "bytes": len(blob),
                "seconds": round(time.time() - t0, 1),
                "cost_usd": 0.01,
                "width": args.width,
                "height": args.height,
            }, ensure_ascii=False))
            return 0
        except Exception as exc:  # noqa: BLE001 - si prova il fallback, poi si riporta
            detail = exc.read().decode()[:300] if hasattr(exc, "read") else str(exc)
            last_err = RuntimeError(f"{model}: {detail}")
            print(f"attenzione: {model} ha fallito ({detail})", file=sys.stderr)

    sys.exit(f"errore: nessun modello ha prodotto l'immagine — {last_err}")


if __name__ == "__main__":
    raise SystemExit(main())
