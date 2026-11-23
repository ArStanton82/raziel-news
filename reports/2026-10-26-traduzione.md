# Traduzione inglese — 2026-10-26

Coda di partenza: 3 articoli senza gemello `.en.md`. Tradotti tutti e 3 (limite di 6 per esecuzione non raggiunto).

## Articoli tradotti

1. «Venice vince al cinema, mentre il mercato le conta zero dollari di TVL» → «Venice Wins at the Movies While the Market Counts Zero Dollars of TVL»
   - file: `content/posts/2026-10-26-venice-lumara-tvl-zero.en.md`
   - percorso inglese: `/en/2026/10/venice-wins-at-the-movies-while-the-market-counts-zero-dollars-of-tvl/`
2. «Hermes esce dal terminale: il Desktop nel browser e la skill che cancella i data broker» → «Hermes Leaves the Terminal: the Desktop in the Browser and the Skill That Erases the Data Brokers»
   - file: `content/posts/2026-10-26-hermes-desktop-web-unbroker.en.md`
   - percorso inglese: `/en/2026/10/hermes-leaves-the-terminal-the-desktop-in-the-browser-and-the-skill-that-erases-the-data-brokers/`
3. «Il wallet più sicuro è quello di chi non conosce il tuo indirizzo di casa» → «The Safest Wallet Belongs to Whoever Never Told You Where They Live»
   - file: `content/posts/2026-10-26-crypto-keystone-indirizzi.en.md`
   - percorso inglese: `/en/2026/10/the-safest-wallet-belongs-to-whoever-never-told-you-where-they-live/`

Nessun articolo saltato: tutti e tre hanno `draft: false` e superano le 200 parole.

## Link interni

`python3 scripts/lingua_link_inglesi.py --scrivi` eseguito prima del commit: 99 coppie italiano→inglese riconosciute, 0 link interni riscritti (i tre articoli non contengono link interni verso altri pezzi). Nessun file toccato dallo script.

## Commit e deploy

- commit `4cacdd5` — `feat(i18n): versione inglese di 3 articoli (2026-10-26)`, 3 file, 92 righe aggiunte, solo i tre `.en.md`.
- push su `main`: `33966d2..4cacdd5`, riuscito.
- deploy GitHub Actions (`deploy.yml`, run su `4cacdd5`): **success** (verificato dopo attesa; il primo controllo dava ancora `in_progress`, il run è stato seguito fino alla conclusione).

## Controlli dal vivo (user-agent browser, `Mozilla/5.0 ... Chrome/131`)

| URL | HTTP |
|---|---|
| `/en/2026/10/venice-wins-at-the-movies-while-the-market-counts-zero-dollars-of-tvl/` | 200 |
| `/en/2026/10/hermes-leaves-the-terminal-the-desktop-in-the-browser-and-the-skill-that-erases-the-data-brokers/` | 200 |
| `/en/2026/10/the-safest-wallet-belongs-to-whoever-never-told-you-where-they-live/` | 200 |
| `/2026/10/venice-vince-al-cinema-mentre-il-mercato-le-conta-zero-dollari-di-tvl/` | 200 |
| `/2026/10/hermes-esce-dal-terminale-il-desktop-nel-browser-e-la-skill-che-cancella-i-data-broker/` | 200 |
| `/2026/10/il-wallet-più-sicuro-è-quello-di-chi-non-conosce-il-tuo-indirizzo-di-casa/` | 200 |

- Le pagine italiane contengono ancora il titolo italiano (verificato nel sorgente HTML).
- Le pagine inglesi mostrano il titolo inglese nel `<title>`.
- Cambio lingua bidirezionale attivo su tutte e tre le coppie: dalla pagina italiana il link `hreflang=en` punta al nuovo indirizzo `/en/...`, dalla pagina inglese il link `hreflang=it` punta all'italiano.

## Note

- Nessun problema riscontrato fuori dai file di mia competenza.
- Nessuna anomalia sul deploy, nessun intervento manuale necessario.
