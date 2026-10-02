#!/usr/bin/env python3
"""source_radar.py — radar delle fonti gratuite per raziel.news.

Legge in ~30 secondi la rete di fonti PRIMARIE gratuite (RSS/API ufficiali) dei
tre pilastri, senza toccare l'API X (a pagamento). Serve a tre cose:

  1. NOTIZIE: cosa e' uscito nelle ultime N ore, raggruppato per STORIA (piu'
     testate sulla stessa storia = piu' rilevante), con fonte e link.
  2. RADAR FONTI: quante volte ciascuna fonte compare nella finestra => chi
     copre davvero il pilastro. Serve a scoprire fonti nuove e potare le morte.
  3. GAP: con --gap confronta i feed con l'ultimo report dello scout e segnala
     le storie che il report NON copre (misura il "ci stiamo perdendo le fonti
     migliori" invece di intuirlo).

Uso:
    python3 scripts/source_radar.py                      # 48h, stampa a video
    python3 scripts/source_radar.py --hours 24 -o out.md
    python3 scripts/source_radar.py --gap reports/2026-10-02-report.md

Solo libreria standard (urllib + xml.etree): nessuna dipendenza da installare.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys
import urllib.request
import xml.etree.ElementTree as ET
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timedelta, timezone
from email.utils import parsedate_to_datetime

UA = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120 Safari/537.36"
TIMEOUT = 25
GN_CAP = 25  # gli RSS di Google News restituiscono 100 item (mesi di archivio): ne teniamo 25

# ---------------------------------------------------------------- configurazione
# (nome, url, pilastro, tipo)  tipo: rss | atom | gnews | ghrel | ghcommit | ghrepos | hn | hf | llama | gecko | html
FEEDS: list[tuple[str, str, str, str]] = [
    # --- Hermes AI / agenti ---
    ("GitHub · hermes-agent commit",   "https://api.github.com/repos/NousResearch/hermes-agent/commits?per_page=15", "hermes", "ghcommit"),
    ("GitHub · hermes-agent releases", "https://api.github.com/repos/NousResearch/hermes-agent/releases?per_page=6", "hermes", "ghrel"),
    ("GitHub · org NousResearch (repo attivi)", "https://api.github.com/orgs/NousResearch/repos?sort=pushed&per_page=10", "hermes", "ghrepos"),
    ("Hacker News · \"hermes agent\"",  "https://hn.algolia.com/api/v1/search_by_date?query=%22hermes%20agent%22&tags=story&hitsPerPage=15", "hermes", "hn"),
    ("Reddit · r/LocalLLaMA",          "https://www.reddit.com/r/LocalLLaMA/.rss", "hermes", "rss"),
    ("HuggingFace · modelli trending", "https://huggingface.co/api/models?sort=trendingScore&limit=15", "hermes", "hf"),
    ("Google News · Nous/Hermes",      "https://news.google.com/rss/search?q=%22Nous%20Research%22%20OR%20%22Hermes%20Agent%22&hl=en-US&gl=US&ceid=US:en", "hermes", "gnews"),
    # --- Venice.ai / VVV / DIEM ---
    ("Venice · blog ufficiale",        "https://venice.ai/blog", "venice", "html"),
    ("Venice · pagina burn",           "https://venice.ai/token/burns", "venice", "html"),
    ("DefiLlama · protocollo Venice",  "https://api.llama.fi/protocol/venice", "venice", "llama"),
    ("CoinGecko · VVV",                "https://api.coingecko.com/api/v3/coins/venice-token?localization=false&tickers=false&community_data=false&developer_data=false", "venice", "gecko"),
    ("Google News · Venice/VVV/DIEM",  "https://news.google.com/rss/search?q=Venice.ai%20OR%20%22VVV%20token%22%20OR%20%22DIEM%20token%22&hl=en-US&gl=US&ceid=US:en", "venice", "gnews"),
    # --- Bitcoin / crypto / regole ---
    ("SEC · comunicati stampa",        "https://www.sec.gov/news/pressreleases.rss", "crypto", "rss"),
    ("CFTC · comunicati",              "https://www.cftc.gov/RSS/RSSGP/rssgp.xml", "crypto", "rss"),
    ("Federal Reserve · press",        "https://www.federalreserve.gov/feeds/press_all.xml", "crypto", "rss"),
    ("CoinDesk",                       "https://www.coindesk.com/arc/outboundfeeds/rss/?outputType=xml", "crypto", "rss"),
    ("Cointelegraph",                  "https://cointelegraph.com/rss", "crypto", "rss"),
    ("The Block",                      "https://www.theblock.co/rss.xml", "crypto", "rss"),
    ("Bitcoin Magazine",               "https://bitcoinmagazine.com/feed", "crypto", "rss"),
    ("Google News · ETF+stablecoin+regole", "https://news.google.com/rss/search?q=bitcoin%20ETF%20OR%20stablecoin%20regulation%20OR%20MiCA&hl=en-US&gl=US&ceid=US:en", "crypto", "gnews"),
]

PILLARS = {"hermes": "Hermes AI", "venice": "Venice.ai / VVV / DIEM", "crypto": "Bitcoin & Crypto"}

# fonti che sono DATI (non notizie): non entrano nel conteggio del gap
DATA_SOURCES = ("DefiLlama", "CoinGecko", "HuggingFace", "Venice · pagina burn")
# fonti di solo contesto tecnico: rumorose, escluse dal gap
CONTEXT_ONLY = ("GitHub · hermes-agent commit", "GitHub · org NousResearch (repo attivi)", "Hacker News")

STOP = {"the", "and", "for", "with", "from", "that", "this", "after", "over", "into", "amid", "its",
        "della", "delle", "degli", "essere", "sono", "come", "piu", "dopo", "alla", "nel", "nella",
        "bitcoin", "btc", "crypto", "cripto", "2026", "price", "says", "new", "just", "here", "what",
        # parole di titolo: troppo comuni nei lanci d'agenzia per provare una copertura
        "jobs", "data", "above", "hits", "hits", "near", "nears", "since", "highest", "weak", "weak",
        "rises", "rose", "surges", "jumps", "proposes", "proposed", "rules", "rule", "framework",
        "today", "amid", "top", "briefly", "trading", "market", "markets", "update", "news", "report",
        "million", "billion", "per", "more", "most", "than", "expected", "softer", "rate", "usd"}


# ------------------------------------------------------------------- fetch/rete
def fetch(url: str) -> str:
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "*/*"})
    with urllib.request.urlopen(req, timeout=TIMEOUT) as r:
        return r.read().decode("utf-8", "replace")


def _dt_iso(s):
    if not s:
        return None
    try:
        return datetime.fromisoformat(str(s).replace("Z", "+00:00")).astimezone(timezone.utc)
    except ValueError:
        return None


def _dt_rfc(s):
    if not s:
        return None
    try:
        d = parsedate_to_datetime(s)
        return d.astimezone(timezone.utc) if d.tzinfo else d.replace(tzinfo=timezone.utc)
    except (TypeError, ValueError):
        return None


# ------------------------------------------------------------------ parser per tipo
def parse_rss_like(body: str):
    """RSS 2.0 o Atom -> lista dict(title, link, dt, source)."""
    out = []
    try:
        root = ET.fromstring(body)
    except ET.ParseError:
        return out
    for it in root.iter():
        tag = it.tag.split("}")[-1]
        if tag not in ("item", "entry"):
            continue
        title = (it.findtext("title") or "").strip()
        if not title:
            continue
        link = (it.findtext("link") or "").strip()
        if not link:
            for l in it.findall("{http://www.w3.org/2005/Atom}link"):
                if l.get("rel") in (None, "alternate"):
                    link = l.get("href") or ""
                    break
        dt = (_dt_rfc(it.findtext("pubDate")) or _dt_iso(it.findtext("published"))
              or _dt_iso(it.findtext("updated")))
        src = it.find("source")
        out.append({"title": re.sub(r"\s+", " ", title), "link": link, "dt": dt,
                    "source": (src.text.strip() if src is not None and src.text else None)})
    return out


def parse_feed(name, url, kind):
    body = fetch(url)
    items = []
    if kind in ("rss", "atom", "gnews"):
        items = parse_rss_like(body)
        if kind == "gnews":
            items = items[:GN_CAP]
    elif kind == "ghrel":
        for r in json.loads(body):
            items.append({"title": f"{r['tag_name']} — {(r.get('name') or '').strip()}",
                          "link": r["html_url"], "dt": _dt_iso(r.get("published_at")), "source": None})
    elif kind == "ghcommit":
        for c in json.loads(body):
            msg = c["commit"]["message"].splitlines()[0][:110]
            items.append({"title": f"commit: {msg}", "link": c["html_url"],
                          "dt": _dt_iso(c["commit"]["author"]["date"]), "source": None})
    elif kind == "ghrepos":
        for r in json.loads(body):
            items.append({"title": f"repo {r['name']} (★{r['stargazers_count']}) push {r['pushed_at'][:16]}",
                          "link": r["html_url"], "dt": _dt_iso(r["pushed_at"]), "source": None})
    elif kind == "hn":
        for h in json.loads(body).get("hits", []):
            items.append({"title": (h.get("title") or "")[:120],
                          "link": h.get("url") or f"https://news.ycombinator.com/item?id={h['objectID']}",
                          "dt": _dt_iso(h.get("created_at")), "source": f"HN · {h.get('points') or 0} punti"})
    elif kind == "hf":
        for m in json.loads(body)[:5]:
            items.append({"title": f"HF trending: {m['modelId']} (↓{m.get('downloads', 0)} · ♥{m.get('likes', 0)})",
                          "link": f"https://huggingface.co/{m['modelId']}", "dt": _dt_iso(m.get("lastModified")),
                          "source": None})
    elif kind == "llama":
        d = json.loads(body)
        tvl = d.get("currentChainTvls") or {}
        vals = []
        if isinstance(tvl, dict):
            for v in tvl.values():
                if isinstance(v, (int, float)):
                    vals.append(v)
                elif isinstance(v, dict):
                    vals.extend(x for x in v.values() if isinstance(x, (int, float)))
        base = sum(vals) if vals else d.get("tvl")
        txt = f"DefiLlama Venice: TVL {float(base):,.0f} USD" if isinstance(base, (int, float)) else "DefiLlama Venice: TVL n/d"
        items.append({"title": txt, "link": "https://defillama.com/protocol/venice", "dt": None, "source": None})
    elif kind == "gecko":
        d = json.loads(body)["market_data"]
        items.append({"title": (f"VVV {d['current_price']['usd']}$ "
                                f"({d['price_change_percentage_24h']:+.1f}% 24h) · vol {d['total_volume']['usd']:,.0f}$ · "
                                f"mcap {d['market_cap']['usd']:,.0f}$"),
                      "link": "https://www.coingecko.com/en/coins/venice-token", "dt": None, "source": None})
    elif kind == "html":
        dates = re.findall(r"(20\d\d-\d\d-\d\d)", body)
        items.append({"title": f"pagina viva ({len(body)//1024} KB)"
                               + (f", ultima data rilevata {max(dates)}" if dates else ""),
                      "link": url, "dt": None, "source": None})
    return items


# ------------------------------------------------------------------ clustering storie
def toks(title: str) -> set[str]:
    return {w for w in re.findall(r"[a-zà-ù]{4,}", title.lower()) if w not in STOP}


def cluster(items):
    """Union-find su somiglianza dei titoli (Jaccard >= 0.34) => storie, non singoli pezzi."""
    parent = list(range(len(items)))

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(a, b):
        ra, rb = find(a), find(b)
        if ra != rb:
            parent[rb] = ra

    tk = [toks(i["title"]) for i in items]
    for i in range(len(items)):
        for j in range(i + 1, len(items)):
            if not tk[i] or not tk[j]:
                continue
            inter = len(tk[i] & tk[j])
            if inter and inter / len(tk[i] | tk[j]) >= 0.34:
                union(i, j)
    groups: dict[int, list[int]] = {}
    for i in range(len(items)):
        groups.setdefault(find(i), []).append(i)
    return sorted(groups.values(), key=lambda g: (-len(g), -(items[g[0]]["dt"].timestamp() if items[g[0]]["dt"] else 0)))


def covered_by_report(title: str, rtok: set[str]) -> bool:
    """True se il titolo condivide una parola distintiva o un numero col report.

    Il confronto su numeri e nomi propri (es. '29,000', '4.2', 'mica', 'utexo')
    e' piu' affidabile delle parole comuni di titolo.
    """
    if not rtok:
        return True
    t = toks(title)
    if t & rtok:
        return True
    nums = set(re.findall(r"\d[\d\.,]*", title.replace(",", "")))
    return bool(nums & rtok)


# ------------------------------------------------------- mining delle fonti citate
SKIP_HOSTS = (
    "twitter.com", "x.com", "facebook.com", "linkedin.com", "t.me", "telegram", "whatsapp",
    "google.com", "gstatic", "doubleclick", "cloudflare", "googletagmanager", "bit.ly", "t.co",
    "instagram", "youtube.com", "apple.com", "spotify", "amazon.", "paypal", "wikimedia",
    "creativecommons", "schema.org", "w3.org", "gravatar", "wordpress", "wp.com", "feedburner",
    "reddit.com", "discord", "cointelegraph", "coindesk", "theblock", "bitcoinmagazine",
    "yahoo", "msn.com", "bing.com", "apps.apple", "play.google", "purl.org", "wellformedweb",
    "sanity.io", "ctmedia.io", "tbstat.com", "s.w.org", "fontawesome", "growthbook", "mux.com",
    "phobos-api", "tickers-api", "pubsubhubbub", "ct-api.org",
)
URL_RE = re.compile(r'https?://[A-Za-z0-9\.\-]+(?:/[^\s"\'<>\)\\]*)?')
HANDLE_RE = re.compile(r'(?:x|twitter)\.com/([A-Za-z0-9_]{2,20})(?:/|\b)')
JUNK_HANDLES = {"widgets", "intent", "share", "i", "home", "hashtag", "platform", "search", "compose", "messages"}

MINED_FEEDS = {
    "Bitcoin Magazine": "https://bitcoinmagazine.com/feed",
    "CoinDesk": "https://www.coindesk.com/arc/outboundfeeds/rss/?outputType=xml",
    "Cointelegraph": "https://cointelegraph.com/rss",
    "The Block": "https://www.theblock.co/rss.xml",
    "Google News · cripto": "https://news.google.com/rss/search?q=bitcoin%20ETF%20OR%20stablecoin%20regulation%20OR%20MiCA&hl=en-US&gl=US&ceid=US:en",
    "Google News · Hermes": "https://news.google.com/rss/search?q=%22Nous%20Research%22%20OR%20%22Hermes%20Agent%22&hl=en-US&gl=US&ceid=US:en",
    "Google News · Venice": "https://news.google.com/rss/search?q=Venice.ai%20OR%20%22VVV%20token%22%20OR%20%22DIEM%20token%22&hl=en-US&gl=US&ceid=US:en",
}


def load_curated(path: str | None) -> set[str]:
    """Handle gia' in lista (per marcare i candidati NUOVI). Lista inline + file skill."""
    known = {"HermesWatcher", "NousResearch", "Teknium", "venicestats", "AskVenice", "JonShapeShift",
             "CoinDesk", "BitcoinMagazine", "VitalikButerin", "tether", "circle", "SECGov", "CFTC",
             "paoloardoino", "roasbeef", "perplexity_ai", "simonw", "ErikVoorhees", "Ar_Stanton"}
    if path and os.path.exists(path):
        known |= set(re.findall(r"`@([A-Za-z0-9_]+)`", open(path, encoding="utf-8").read()))
    return known


def run_mining(curated_path: str | None = None) -> list[str]:
    """Cosa citano i feed: handle X incorporati (=chi fa notizia) e fonti esterne.

    Nota di metodo: le testate NON citano le fonti primarie in modo estraibile
    (verificato il 2026-10-02: 24 articoli letti, zero link utili); l'unico
    segnale affidabile sono i tweet incorporati nei feed, che compaiono nel
    corpo RSS di alcune testate (Bitcoin Magazine in primis).
    """
    from collections import Counter
    from urllib.parse import urlparse

    known = load_curated(curated_path)
    hands, hosts, where = Counter(), Counter(), {}
    ok = 0
    for name, url in MINED_FEEDS.items():
        try:
            body = fetch(url)
            ok += 1
        except Exception:
            continue
        for hx in HANDLE_RE.findall(body):
            if hx.lower() in JUNK_HANDLES or "widget" in hx.lower():
                continue
            # gli id di condivisione incorporati sono alfanumerici senza spazi: non sono handle
            if len(hx) >= 9 and re.search(r"[a-z]", hx) and re.search(r"[A-Z]", hx) and re.search(r"\d", hx):
                continue
            hands[hx] += 1
            where.setdefault(hx, name)
        for z in URL_RE.findall(body):
            host = urlparse(z).netloc.replace("www.", "").lower()
            if not host or any(s in host for s in SKIP_HOSTS):
                continue
            hosts[host] += 1
            where.setdefault(host, name)

    out = ["## Mining: chi fanno citare i feed (= candidati fonti)",
           f"Feed letti: {ok}/{len(MINED_FEEDS)}. Solo alcune testate incorporano i tweet negli RSS:",
           "gli handle qui sotto sono account che le testate di settore citano davvero.", ""]
    new_handles = [(h, n) for h, n in hands.most_common(40) if h not in known]
    out.append("### Handle X citati e NON in lista (candidati da verificare)")
    if new_handles:
        for h, n in new_handles[:20]:
            out.append(f"- {n}× @{h}  ← da {where.get(h, '?')}")
    else:
        out.append("- (nessuno nella finestra di questo feed)")
    out.append("")
    out.append("### Fonti esterne citate (domini non social)")
    for host, n in hosts.most_common(15):
        out.append(f"- {n}× {host}  ← da {where.get(host, '?')}")
    out.append("")
    out.append("### Handle X in lista, riconfermati dai feed")
    for h, n in hands.most_common(40):
        if h in known:
            out.append(f"- {n}× @{h}")
    out.append("")
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--hours", type=int, default=48)
    ap.add_argument("-o", "--out")
    ap.add_argument("--gap", help="report dello scout da confrontare (markdown)")
    ap.add_argument("--mining", action="store_true",
                    help="mina i link esterni e gli handle X citati dalle testate di settore")
    ap.add_argument("--curated", help="file con la lista fonti curate (per marcare i candidati nuovi)")
    args = ap.parse_args()

    now = datetime.now(timezone.utc)
    cutoff = now - timedelta(hours=args.hours)
    report_text = open(args.gap, encoding="utf-8").read() if args.gap else ""
    rtok = toks(report_text) if report_text else set()
    # i link del report contengono gli slug in inglese: aiutano il confronto
    # con i titoli delle testate (il report e' in italiano, le fonti in inglese)
    if report_text:
        for u in re.findall(r"https?://\S+", report_text):
            rtok |= toks(u.replace("-", " ").replace("/", " "))

    results, errors = {}, {}
    with ThreadPoolExecutor(max_workers=10) as ex:
        fut = {ex.submit(parse_feed, n, u, k): (n, p) for n, u, p, k in FEEDS}
        for f in fut:
            n, pillar = fut[f]
            try:
                results[n] = (pillar, f.result())
            except Exception as e:
                errors[n] = f"{type(e).__name__}: {e}"

    L: list[str] = []
    add = L.append
    add(f"# Radar fonti (gratuito) — {now:%Y-%m-%d %H:%M} UTC")
    add(f"Finestra: ultime {args.hours} ore · fonti lette: {len(results)}/{len(FEEDS)}"
        + (f" · non raggiungibili: {', '.join(errors)}" if errors else ""))
    add("")

    src_in_window: dict[str, int] = {}
    gaps: list[tuple[str, str, str]] = []   # (pilastro, titolo, fonte)

    for pillar, label in PILLARS.items():
        fresh = []
        for name, (p, items) in results.items():
            if p != pillar:
                continue
            for it in items:
                if it["dt"] and it["dt"] < cutoff:
                    continue
                fresh.append({"feed": name, **it})
        if not fresh:
            add(f"## {label}\n- (nessun item nella finestra)\n")
            continue
        # fonti nel conteggio solo per item di notizia dentro la finestra
        for it in fresh:
            src_in_window[it["feed"]] = src_in_window.get(it["feed"], 0) + 1

        news = [it for it in fresh if it["dt"]]           # item con data = notizia
        statics = [it for it in fresh if not it["dt"]]    # dati/probe
        add(f"## {label}")
        add(f"### Storie ({len(cluster(news))} cluster da {len(news)} item)")
        for g in cluster(news)[:8]:
            g = sorted(g, key=lambda i: (news[i]["dt"] or now), reverse=True)
            head = news[g[0]]
            outlets = sorted({(news[i]["source"] or news[i]["feed"]) for i in g})
            multi = f" · **{len(outlets)} testate**" if len(outlets) > 1 else ""
            notcov = ""
            if rtok and head["feed"] not in CONTEXT_ONLY and head["feed"] not in DATA_SOURCES:
                if not any(covered_by_report(news[i]["title"], rtok) for i in g):
                    notcov = "  ⚠ NON NEL REPORT DI OGGI"
                    gaps.append((label, head["title"], ", ".join(outlets[:3])))
            add(f"- `{head['dt']:%d/%m %H:%M}` **{head['title']}**{multi} — {', '.join(outlets[:3])}{notcov}")
            for i in g[1:4]:
                add(f"    - {news[i]['dt']:%d/%m %H:%M} · {news[i]['source'] or news[i]['feed']}: {news[i]['title'][:90]}")
        if statics:
            add("### Dati / fonti vive")
            for it in statics:
                add(f"- {it['title']} — {it['feed']}" + (f" · {it['link']}" if it["link"] else ""))
        add("")

    add("## Copertura per fonte nella finestra (chi copre davvero il pilastro)")
    for name, n in sorted(src_in_window.items(), key=lambda x: -x[1]):
        add(f"- {n:>3} item · {name}  ({PILLARS[results[name][0]]})")
    add("")

    if errors:
        add("## Fonti non raggiungibili in questa esecuzione")
        for n, e in errors.items():
            add(f"- {n}: {e}")
        add("")

    if args.mining:
        add("")
        L.extend(run_mining(args.curated))

    if report_text:
        add(f"## Gap rispetto a {args.gap}")
        add(f"Storie dei feed che il report non copre: **{len(gaps)}**")
        for label, t, src in gaps:
            add(f"- [{label}] {t} — {src}")

    out = "\n".join(L)
    if args.out:
        open(args.out, "w", encoding="utf-8").write(out + "\n")
        print(f"scritto {args.out} ({len(out)} byte)")
    else:
        print(out)
    return 0


if __name__ == "__main__":
    sys.exit(main())
