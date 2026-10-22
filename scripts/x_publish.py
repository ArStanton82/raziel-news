#!/usr/bin/env python3
"""Helper di pubblicazione X per raziel.news — costruisce i payload senza quoting di shell.

Uso:
  x_publish.py upload <draft_id> <image_path> [--media-type image/jpeg]
  x_publish.py post   <draft_id> <media_id>
  x_publish.py reply  <draft_id> <tweet_id>
  x_publish.py check  <draft_id> <tweet_id>   # rilegge, confronta con la coda (note_tweet.text), verifica lang+media
  x_publish.py setmedia <draft_id> <media_id>
  x_publish.py verify <tweet_id>
  x_publish.py save   <draft_id> <tweet_id> <reply_id> <media_id>
"""
import json
import subprocess
import sys
from pathlib import Path

QUEUE_DIR = Path("/root/.hermes/profiles/raziel-news/x-queue")


def queue_file_for(draft_id):
    date = draft_id[:10]
    return QUEUE_DIR / f"{date}.json"


def load(draft_id):
    p = queue_file_for(draft_id)
    return p, json.loads(p.read_text(encoding="utf-8"))


def find(data, draft_id):
    for d in data["drafts"]:
        if d["id"] == draft_id:
            return d
    raise SystemExit(f"draft {draft_id} non trovato")


def xurl(args, timeout=120):
    r = subprocess.run(["xurl"] + args, capture_output=True, text=True, timeout=timeout)
    return r.returncode, r.stdout, r.stderr


def _parse_json(out):
    """Estrae il primo oggetto JSON dall'output di xurl (che aggiunge righe di log)."""
    dec = json.JSONDecoder()
    for i, ch in enumerate(out):
        if ch == "{":
            try:
                obj, _ = dec.raw_decode(out[i:])
                return obj
            except Exception:
                continue
    raise ValueError("nessun JSON nell'output")


def cmd_upload(draft_id, image_path, media_type=None):
    p, data = load(draft_id)
    d = find(data, draft_id)
    if not Path(image_path).exists():
        raise SystemExit(f"IMMAGINE MANCANTE: {image_path}")
    args = ["media", "upload", image_path]
    if media_type:
        args += ["--media-type", media_type]
    rc, out, err = xurl(args)
    if rc != 0:
        raise SystemExit(f"upload fallito rc={rc}\n{out}\n{err}")
    try:
        mid = _parse_json(out)["data"]["id"]
    except Exception:
        raise SystemExit(f"upload: risposta non parsabile\n{out}\n{err}")
    d["media_id"] = mid
    p.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"media_id={mid}")


def cmd_post(draft_id, media_id):
    p, data = load(draft_id)
    d = find(data, draft_id)
    payload = {"text": d["text"], "media": {"media_ids": [media_id]}}
    body = json.dumps(payload, ensure_ascii=False)
    rc, out, err = xurl(["-X", "POST", "/2/tweets", "-d", body])
    if rc != 0:
        raise SystemExit(f"post fallito rc={rc}\n{out}\n{err}")
    try:
        tid = _parse_json(out)["data"]["id"]
    except Exception:
        raise SystemExit(f"post: risposta non parsabile\n{out}\n{err}")
    d["published_tweet_id"] = tid
    p.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"tweet_id={tid}")


def cmd_reply(draft_id, tweet_id):
    p, data = load(draft_id)
    d = find(data, draft_id)
    payload = {"text": d["reply_link"], "reply": {"in_reply_to_tweet_id": tweet_id}}
    body = json.dumps(payload, ensure_ascii=False)
    rc, out, err = xurl(["-X", "POST", "/2/tweets", "-d", body])
    if rc != 0:
        raise SystemExit(f"reply fallita rc={rc}\n{out}\n{err}")
    try:
        rid = _parse_json(out)["data"]["id"]
    except Exception:
        raise SystemExit(f"reply: risposta non parsabile\n{out}\n{err}")
    d["reply_tweet_id"] = rid
    p.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"reply_id={rid}")


def cmd_verify(tweet_id):
    rc, out, err = xurl([f"/2/tweets/{tweet_id}?tweet.fields=created_at,lang,entities,attachments,note_tweet,text"])
    if rc != 0:
        raise SystemExit(f"verify fallito rc={rc}\n{out}\n{err}")
    print(out)


def cmd_save(draft_id, tweet_id, reply_id, media_id):
    p, data = load(draft_id)
    d = find(data, draft_id)
    d["published_tweet_id"] = tweet_id
    d["reply_tweet_id"] = reply_id
    d["media_id"] = media_id
    d["status"] = "published"
    p.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"salvato {draft_id}: {tweet_id} / reply {reply_id} / media {media_id}")


def cmd_setmedia(draft_id, media_id):
    p, data = load(draft_id)
    d = find(data, draft_id)
    d["media_id"] = media_id
    p.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"media_id={media_id} salvato su {draft_id}")


def cmd_check(draft_id, tweet_id):
    p, data = load(draft_id)
    d = find(data, draft_id)
    rc, out, err = xurl([f"/2/tweets/{tweet_id}?tweet.fields=created_at,lang,entities,attachments,note_tweet,text"])
    if rc != 0:
        raise SystemExit(f"verify fallito rc={rc}\n{out}\n{err}")
    obj = _parse_json(out)["data"]
    full = (obj.get("note_tweet") or {}).get("text") or obj.get("text") or ""
    media_keys = (obj.get("attachments") or {}).get("media_keys") or []
    print(f"id: {obj.get('id')}")
    print(f"created_at: {obj.get('created_at')}")
    print(f"lang: {obj.get('lang')} (attesa: {d.get('lang')})")
    print(f"media_keys: {media_keys}")
    print(f"lunghezza pubblicata: {len(full)} / coda: {len(d['text'])}")
    print(f"testo identico: {full.strip() == d['text'].strip()}")
    if full.strip() != d["text"].strip():
        print("--- PUBBLICATO ---")
        print(full)
        print("--- CODA ---")
        print(d["text"])
    print(f"url: https://x.com/Ar_Stanton/status/{obj.get('id')}")


if __name__ == "__main__":
    cmd = sys.argv[1]
    if cmd == "upload":
        mt = None
        if "--media-type" in sys.argv:
            mt = sys.argv[sys.argv.index("--media-type") + 1]
        cmd_upload(sys.argv[2], sys.argv[3], mt)
    elif cmd == "post":
        cmd_post(sys.argv[2], sys.argv[3])
    elif cmd == "reply":
        cmd_reply(sys.argv[2], sys.argv[3])
    elif cmd == "verify":
        cmd_verify(sys.argv[2])
    elif cmd == "check":
        cmd_check(sys.argv[2], sys.argv[3])
    elif cmd == "setmedia":
        cmd_setmedia(sys.argv[2], sys.argv[3])
    elif cmd == "save":
        cmd_save(sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5])
    else:
        raise SystemExit(__doc__)
