#!/usr/bin/env python3
"""Illustrazione in stile pop art a fumetto per gli articoli di raziel.news.

Serve a produrre le immagini degli articoli (e delle card) nel registro chiesto da Kain:
manifesto pop art / serigrafia anni Sessanta, tinte piatte, mezzitoni, contorni neri spessi.
Il soggetto resta concreto e unico; il testo dentro l'immagine NON e' mai generato dal
modello (inventa parole e numeri): se serve testo, si compone con il codice.

Uso:
    python3 scripts/arte_popart.py --subject "..." --out prova.jpg
    python3 scripts/arte_popart.py --subject "..." --out prova.jpg --model nano-banana-pro --preset "Pop Art"
    python3 scripts/arte_popart.py --prova --out-dir /tmp/prove    # giro di confronto su 4 modelli

La chiave si legge da VENICE_API_KEY, da HERMES_CUSTOM_API_VENICE_AI_API_KEY o dal .env del profilo.
"""
from __future__ import annotations

import argparse
import base64
import io
import json
import os
import pathlib
import re
import sys
import time
import urllib.error
import urllib.request

API = "https://api.venice.ai/api/v1/image/generate"
KEY_RE = re.compile(r"^(?:VENICE_API_KEY|HERMES_CUSTOM_API_VENICE_AI_API_KEY)=(.*)$")

STILE = (
    "Pop art comic poster, 1960s silkscreen printing. Flat spot colours only, four or five of them "
    "(magenta, cyan, yellow, black, one amber accent), coarse halftone dot pattern, heavy black ink "
    "outlines, no gradients, no soft shading, no photorealism, bold graphic shapes, high contrast, "
    "one clear focal subject readable at thumbnail size, wide 16:9 composition. "
    "No text, no words, no letters, no numbers, no logos, no signature, no frame, no border."
)

# Giro di confronto: modello + preset di stile di Venice.
PROVE = [
    ("venice-sd35", "Pop Art"),
    ("venice-sd35", "Comic Book"),
    ("nano-banana-pro", "Pop Art"),
    ("flux-2-pro", "Pop Art"),
]


def read_key(env_file: str | None = None) -> str:
    key = os.environ.get("VENICE_API_KEY") or os.environ.get("HERMES_CUSTOM_API_VENICE_AI_API_KEY")
    if key:
        return key.strip().strip('"')
    for path in [env_file, "/root/.hermes/profiles/raziel-news/.env", os.path.expanduser("~/.hermes/.env")]:
        if not path or not os.path.exists(path):
            continue
        for line in open(path, encoding="utf-8", errors="ignore"):
            m = KEY_RE.match(line.strip())
            if m:
                return m.group(1).strip().strip('"')
    sys.exit("errore: nessuna chiave Venice trovata")


def genera(key: str, model: str, preset: str | None, prompt: str, width: int, height: int,
           steps: int, timeout: int) -> tuple[bytes, float]:
    corpo: dict = {"model": model, "prompt": prompt, "format": "jpeg", "safe_mode": True,
                   "hide_watermark": True}
    if preset:
        corpo["style_preset"] = preset
    if model.startswith("venice-sd35"):
        corpo.update({"width": width - width % 16, "height": height - height % 16, "steps": steps})
    else:
        corpo.update({"aspect_ratio": "16:9", "resolution": "1K"})
    req = urllib.request.Request(
        API, data=json.dumps(corpo).encode(),
        headers={"Authorization": f"Bearer {key}", "Content-Type": "application/json"},
        method="POST")
    t0 = time.time()
    with urllib.request.urlopen(req, timeout=timeout) as f:
        data = json.load(f)
    immagini = data.get("images") or []
    if not immagini:
        raise RuntimeError(f"{model}: risposta senza immagini ({list(data)[:4]})")
    return base64.b64decode(immagini[0]), time.time() - t0


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--subject", help="soggetto concreto della scena, in inglese")
    ap.add_argument("--subject-file")
    ap.add_argument("--out")
    ap.add_argument("--out-dir", default="/root/.hermes/profiles/raziel-news/cache/scratch/prove-popart")
    ap.add_argument("--model", default="venice-sd35")
    ap.add_argument("--preset", default="Pop Art")
    ap.add_argument("--width", type=int, default=1280)
    ap.add_argument("--height", type=int, default=720)
    ap.add_argument("--steps", type=int, default=30)
    ap.add_argument("--timeout", type=int, default=300)
    ap.add_argument("--prova", action="store_true", help="giro di confronto su quattro modelli")
    args = ap.parse_args()

    subject = args.subject
    if args.subject_file:
        subject = pathlib.Path(args.subject_file).read_text(encoding="utf-8").strip()
    if not subject:
        sys.exit("errore: serve --subject o --subject-file")
    prompt = f"{subject}. {STILE}"

    key = read_key()
    esiti = []
    if args.prova:
        out_dir = pathlib.Path(args.out_dir)
        out_dir.mkdir(parents=True, exist_ok=True)
        for i, (model, preset) in enumerate(PROVE):
            etichetta = f"{i:02d}-{model}-{preset.replace(' ', '')}.jpg"
            percorso = out_dir / etichetta
            try:
                blob, durata = genera(key, model, preset, prompt, args.width, args.height, args.steps, args.timeout)
                percorso.write_bytes(blob)
                esiti.append({"file": str(percorso), "model": model, "preset": preset,
                              "seconds": round(durata, 1), "status": "ok"})
                print(f"ok   {etichetta}  {round(durata,1)}s", flush=True)
            except urllib.error.HTTPError as e:
                esiti.append({"file": None, "model": model, "preset": preset, "status": f"HTTP {e.code}: {e.read().decode()[:150]}"})
                print(f"errore {etichetta}: HTTP {e.code}", flush=True)
            except Exception as e:  # noqa: BLE001
                esiti.append({"file": None, "model": model, "preset": preset, "status": f"{type(e).__name__}: {e}"})
                print(f"errore {etichetta}: {e}", flush=True)
        (out_dir / "esiti.json").write_text(json.dumps(esiti, ensure_ascii=False, indent=2))
        print(json.dumps({"status": "done", "esiti": esiti}, ensure_ascii=False))
        return 0

    if not args.out:
        sys.exit("errore: serve --out")
    blob, durata = genera(key, args.model, args.preset, prompt, args.width, args.height, args.steps, args.timeout)
    pathlib.Path(args.out).parent.mkdir(parents=True, exist_ok=True)
    pathlib.Path(args.out).write_bytes(blob)
    print(json.dumps({"status": "ok", "model": args.model, "preset": args.preset,
                      "path": os.path.abspath(args.out), "bytes": len(blob),
                      "seconds": round(durata, 1)}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
