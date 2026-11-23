# Traduzione inglese — 2026-11-17

Coda: 3 articoli senza gemello `.en.md` (tutti i file del 17 novembre). Nessun articolo saltato: nessuno era `draft: true`, nessuno sotto le 200 parole.

## Articoli tradotti

1. «Non hanno bucato Trezor né la BBC: hanno bucato i loro fornitori» → «Nobody Breached Trezor or the BBC: Their Suppliers Got Breached»
   - IT: `/2026/11/non-hanno-bucato-trezor-n%C3%A9-la-bbc-hanno-bucato-i-loro-fornitori/`
   - EN: `/en/2026/11/nobody-breached-trezor-or-the-bbc-their-suppliers-got-breached/`
2. «Hermes 0.23.2: una patch con dentro quasi duemila pull request» → «Hermes 0.23.2: A Patch Carrying Almost Two Thousand Pull Requests»
   - IT: `/2026/11/hermes-0.23.2-una-patch-con-dentro-quasi-duemila-pull-request/`
   - EN: `/en/2026/11/hermes-0-23-2-a-patch-carrying-almost-two-thousand-pull-requests/`
3. «Venice taglia il prezzo il giorno dopo il lancio: la corsa al ribasso dell'intelligenza» → «Venice Cuts the Price a Day After Launch: The Downward Race of Intelligence»
   - IT: `/2026/11/venice-taglia-il-prezzo-il-giorno-dopo-il-lancio-la-corsa-al-ribasso-dellintelligenza/`
   - EN: `/en/2026/11/venice-cuts-the-price-a-day-after-launch-the-downward-race-of-intelligence/`

Frontmatter allineato all'italiano (stessa `date`, `draft: false`, categorie inglesi, tag tradotti con i nomi propri intatti), `url:` sotto `/en/`, corpo senza H1, riga finale `*Verified sources: ...*` con testate, link e date identici.

## Link interni

`python3 scripts/lingua_link_inglesi.py --scrivi`: 170 coppie IT→EN riconosciute, **0 link riscritti** (i tre articoli non hanno link interni verso pagine italiane da rimappare). Nessuna modifica extra da includere nel commit.

## Commit e deploy

- Commit `d6be88f` — `feat(i18n): versione inglese di 3 articoli (2026-11-17)` — 3 file, 96 righe aggiunte. Push su `main` riuscito (`3cd1c25..d6be88f`).
- GitHub Actions `deploy.yml`: **success** (run sul commit `d6be88f`), verificato con `gh run list -L 1`.

## Controlli dal vivo (user-agent browser)

| Pagina | Codice |
|---|---|
| EN Trezor/BBC | 200 |
| EN Hermes 0.23.2 | 200 |
| EN Venice Qwen | 200 |
| IT Trezor/BBC | 200 |
| IT Hermes 0.23.2 | 200 |
| IT Venice Qwen | 200 |

- Titoli italiani ancora presenti sulle pagine italiane, invariati: «Non hanno bucato Trezor né la BBC: hanno bucato i loro fornitori», «Hermes 0.23.2: una patch con dentro quasi duemila pull request», «Venice taglia il prezzo il giorno dopo il lancio: la corsa al ribasso dell'intelligenza».
- Ogni pagina inglese stampa il titolo inglese, le sezioni `##` attese e gli `hreflang` corretti (`it-it` → pagina italiana, `en-us` → sé stessa), con il link di cambio lingua «IT» funzionante.
- Tutte e tre le URL inglesi compaiono in `/en/sitemap.xml`.

## Note

- Nessun problema riscontrato fuori dai file tradotti; niente da segnalare a monte.
- Lo slug italiano usa il carattere accentato codificato (`n%C3%A9`): è la regola del tema, non un errore, e non l'ho toccato.
