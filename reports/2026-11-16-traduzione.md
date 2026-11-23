# Traduzione inglese — 2026-11-16

Coda: 3 articoli non tradotti (tutti i `*.md` del 2026-11-16). Nessun articolo scartato: nessuno con `draft: true`, nessuno sotto le 200 parole. Nessun arretrato: tutti i file precedenti hanno già il gemello `.en.md`.

## Articoli tradotti (3)

1. «Bitcoin a 62 mila dollari: la settimana in cui ha ceduto la media a 200 giorni» → "Bitcoin at $62,000: the Week It Lost the 200-Day Average"
   - file: `content/posts/2026-11-16-bitcoin-minimo-quattro-mesi-62mila.en.md`
   - percorso inglese: `/en/2026/11/bitcoin-at-62000-the-week-it-lost-the-200-day-average/`
2. «Cento fix in un fine settimana: la sicurezza di Hermes si fa manutenzione» → "A Hundred Fixes in One Weekend: Hermes Makes Security a Maintenance Job"
   - file: `content/posts/2026-11-16-hermes-sicurezza-canary.en.md`
   - percorso inglese: `/en/2026/11/a-hundred-fixes-in-one-weekend-hermes-makes-security-a-maintenance-job/`
3. «Venice: 458 mila dollari bruciati e un Qwen da un milione di token» → "Venice Burns $458,000 and Ships a Million-Token Qwen"
   - file: `content/posts/2026-11-16-venice-burn-458mila-qwen.en.md`
   - percorso inglese: `/en/2026/11/venice-burns-458000-and-ships-a-million-token-qwen/`

Regole rispettate: stessa `date` (2026-11-16), `draft: false`, titoli e summary riscritti in inglese, `categories` in inglese (Crypto, Blockchain, Hermes, AI, Venice.ai), `tags` tradotti con i nomi propri intatti (`Qwen 4 Max`, `VVV`), `url` esplicito sotto `/en/`, corpo senza titolo `#`, fonti in fondo con etichetta `*Verified sources: ...*` e testate/date invariate. Nessun fatto, numero o giudizio aggiunto.

## Link interni

`python3 scripts/lingua_link_inglesi.py --scrivi` eseguito prima del commit: 167 coppie italiano→inglese con percorso dichiarato, 0 link interni riscritti (i tre articoli nuovi non contengono link interni ad altri articoli).

## Commit e deploy

- commit `2ed7439` — `feat(i18n): versione inglese di 3 articoli (2026-11-16)` (3 file, 98 righe aggiunte), push su `main` riuscito.
- GitHub Actions `deploy.yml`, run 43858493186: `success` (job `build` e `deploy` entrambi completati).

## Controlli dal vivo (user-agent da browser)

| URL | HTTP |
|---|---|
| /en/2026/11/bitcoin-at-62000-the-week-it-lost-the-200-day-average/ | 200 |
| /en/2026/11/a-hundred-fixes-in-one-weekend-hermes-makes-security-a-maintenance-job/ | 200 |
| /en/2026/11/venice-burns-458000-and-ships-a-million-token-qwen/ | 200 |
| /2026/11/bitcoin-a-62-mila-dollari-la-settimana-in-cui-ha-ceduto-la-media-a-200-giorni/ | 200 |
| /2026/11/cento-fix-in-un-fine-settimana-la-sicurezza-di-hermes-si-fa-manutenzione/ | 200 |
| /2026/11/venice-458-mila-dollari-bruciati-e-un-qwen-da-un-milione-di-token/ | 200 |

- Le tre pagine italiane mostrano ancora il titolo italiano corretto (`<title>` verificato).
- Il cambio lingua funziona in entrambe le direzioni: dalla pagina inglese il link `hreflang=it` punta all'URL italiano, dalla pagina italiana il link `hreflang=en` punta all'URL inglese.
- I tre nuovi URL risultano già nella sitemap inglese (`/en/sitemap.xml`).

## Note

- Nessun problema riscontrato fuori dai file `.en.md`.
- Nessuna correzione fuori perimetro effettuata; nessun file del repository toccato oltre ai tre `.en.md` e a questo report.
