# Traduzione inglese — 2026-11-04

**Articoli tradotti: 3** (coda esaurita, nessun arretrato)

| Titolo italiano | Titolo inglese | Percorso inglese |
|---|---|---|
| Venice, il burn come specchio: il 42% della supply è bruciato e il milione al mese non è fatturato | Venice and the Burn as a Mirror: 42% of Supply Is Gone, and That Million a Month Isn't Revenue | https://raziel.news/en/2026/11/venice-burn-as-a-mirror-42-percent-of-supply/ |
| Il giorno dopo: i Democratici prendono il Senato, la CFTC apre i perpetual sulle azioni | The Day After: Democrats Take the Senate, and the CFTC Opens Perpetuals on Single Stocks | https://raziel.news/en/2026/11/the-day-after-democrats-take-the-senate-cftc-perps-on-stocks/ |
| Hermes cresce di notte: la 0.22.7, una beta mobile già piena e i plugin che arrivano da fuori | Hermes Grows at Night: 0.22.7, a Mobile Beta Already Full, and Plugins Arriving From Outside | https://raziel.news/en/2026/11/hermes-grows-at-night-0227-mobile-beta-and-plugins/ |

## Deploy

Commit `3bc1490` — `feat(i18n): versione inglese di 3 articoli (2026-11-04)`, 3 file, +96 righe, push su `main`.
GitHub Actions `deploy.yml` su `3bc1490`: **success**.

## Controlli dal vivo (user-agent browser)

Tutti i codici HTTP verificati dopo il deploy:

- `/en/2026/11/venice-burn-as-a-mirror-42-percent-of-supply/` → **200**
- `/en/2026/11/the-day-after-democrats-take-the-senate-cftc-perps-on-stocks/` → **200**
- `/en/2026/11/hermes-grows-at-night-0227-mobile-beta-and-plugins/` → **200**
- pagina italiana corrispondente dell'articolo Venice → **200**, `<title>` italiano intatto
- pagina italiana corrispondente dell'articolo midterm/CFTC → **200**, `<title>` italiano intatto
- pagina italiana corrispondente dell'articolo Hermes 0.22.7 → **200**, `<title>` italiano intatto

Abbinamento bilingue: la pagina inglese dichiara `hreflang=it-it` verso l'URL italiano corretto, quindi il cambio lingua è attivo sulle sei pagine.

`scripts/lingua_link_inglesi.py --scrivi`: 128 coppie it→en riconosciute, **0 link riscritti** in questo giro (nessun articolo inglese puntava a una pagina italiana con gemello appena creato).

## Note

- Coda costruita su `content/posts/*.md` senza gemello `.en.md`: 3 file, tutti con `draft: false` e oltre 200 parole. Nessun articolo saltato.
- Nessuna anomalia fuori dai file di competenza. Nessuna modifica a script, layout, configurazione o immagini.
- Sitemap Cloudflare: `https://raziel.news/sitemap.xml` risponde 403 con lo user-agent corto `Mozilla/5.0` (challenge gestita) e 200 con lo user-agent completo `Mozilla/5.0 (Macintosh…) Chrome/131`. Non è un problema del sito, ma conviene usare l'UA completo nei controlli automatici.
