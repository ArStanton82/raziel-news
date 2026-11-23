# Traduzione inglese — 2026-11-10

Coda iniziale: 3 articoli senza gemello `.en.md`, tutti pubblicati il 2026-11-10. Tradotti tutti e 3 (sotto il tetto di 6).

## Articoli tradotti

1. "Venezia brucia 458 mila dollari: il burn più grande vale lo 0,04% della supply"
   → "Venice Burns $458,000: Its Biggest Burn Is 0.04% of Supply"
   → `/en/2026/11/venice-burns-458000-its-biggest-burn-is-0-04-of-supply/`
   File: `content/posts/2026-11-10-venice-burn-record.en.md`

2. "Il plugin che non c'era: Hermes 0.23.1 e il tetto di due megabyte"
   → "The Plugin That Wasn't There: Hermes 0.23.1 and the Two-Megabyte Ceiling"
   → `/en/2026/11/the-plugin-that-wasnt-there-hermes-0-23-1-and-the-two-megabyte-ceiling/`
   File: `content/posts/2026-11-10-hermes-catalogo-16mib.en.md`

3. "Bitcoin sotto i 75 mila: il prezzo si ferma, i binari no"
   → "Bitcoin Below $75,000: The Price Stalls, the Rails Don't"
   → `/en/2026/11/bitcoin-below-75000-the-price-stalls-the-rails-dont/`
   File: `content/posts/2026-11-10-bitcoin-prezzo-binari.en.md`

Nessun articolo saltato: tutti e tre hanno `draft: false` e oltre 200 parole (593, 550, 619).

## Link interni

`python3 scripts/lingua_link_inglesi.py --scrivi`: 148 coppie italiano→inglese riconosciute, **0 link riscritti**. Corretto: i tre articoli non contengono link a pagine interne italiane, quindi non c'era nulla da spostare. Nessuna modifica al di fuori dei tre file creati.

## Commit e deploy

- Commit `98e6c10` — `feat(i18n): versione inglese di 3 articoli (2026-11-10)`, pushato su `main` (`96fb9a4..98e6c10`). Solo i 3 file `.en.md`, nessun altro file del repo.
- GitHub Actions `deploy.yml` sul commit `98e6c10`: **success** (build completata dopo circa 4 minuti).

## Verifica dal vivo (user-agent browser, Chrome/131)

Pagine inglesi — tutte `200`:
- `/en/2026/11/venice-burns-458000-its-biggest-burn-is-0-04-of-supply/` → 200
- `/en/2026/11/the-plugin-that-wasnt-there-hermes-0-23-1-and-the-two-megabyte-ceiling/` → 200
- `/en/2026/11/bitcoin-below-75000-the-price-stalls-the-rails-dont/` → 200

Pagine italiane corrispondenti — tutte `200`, con il titolo italiano intatto:
- `/2026/11/venezia-brucia-458-mila-dollari-il-burn-più-grande-vale-lo-004-della-supply/` → 200, titolo "Venezia brucia 458 mila dollari: il burn più grande vale lo 0,04% della supply"
- `/2026/11/il-plugin-che-non-cera-hermes-0.23.1-e-il-tetto-di-due-megabyte/` → 200, titolo "Il plugin che non c'era: Hermes 0.23.1 e il tetto di due megabyte"
- `/2026/11/bitcoin-sotto-i-75-mila-il-prezzo-si-ferma-i-binari-no/` → 200, titolo "Bitcoin sotto i 75 mila: il prezzo si ferma, i binari no"

Abbinamento delle lingue attivo: sulla pagina inglese di Bitcoin compaiono `hreflang=it-it`, `hreflang=en-us`, `hreflang=x-default` e il link di switch verso la pagina italiana.

## Note

- Primo tentativo di verifica con `-A "Mozilla/5.0"` secco: `403` su tutte le URL, compresa la home. È il Bot Fight di Cloudflare, non un problema del sito: con uno user-agent Chrome completo tutte le pagine rispondono `200`. Va usato lo user-agent completo nei controlli.
- Nessun problema riscontrato fuori dai file di mia competenza. Coda residua a zero: tutti gli articoli pubblicati hanno il gemello inglese.
