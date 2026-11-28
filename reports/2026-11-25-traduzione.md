# Traduzione — 2026-11-25

Coda: 3 articoli senza gemello inglese, tutti del 2026-11-25. Nessun file in coda oltre i 3, nessun `draft: true`, nessun articolo sotto le 200 parole.

## Articoli tradotti

1. «Bitcoin sotto 59mila: quasi cinque miliardi fuori dagli ETF e una fiducia da ricostruire» → «Bitcoin below $59,000: almost five billion out of the ETFs and a trust to rebuild» — `/en/2026/11/bitcoin-below-59-000-almost-five-billion-out-of-the-etfs-and-a-trust-to-rebuild/`
2. «Hermes 0.23.4: la patch più silenziosa è quella con più lavoro dentro» → «Hermes 0.23.4: the quietest patch is the one with the most work inside» — `/en/2026/11/hermes-0-23-4-the-quietest-patch-is-the-one-with-the-most-work-inside/`
3. «Venice dichiara 200 milioni annualizzati. Sulla catena se ne contano cinque» → «Venice claims $200 million annualised. On-chain there are five» — `/en/2026/11/venice-claims-200-million-annualised-on-chain-there-are-five/`

Commit: `6ae5ecd` — `feat(i18n): versione inglese di 3 articoli (2026-11-25)`, push su `main` eseguito.

`scripts/lingua_link_inglesi.py --scrivi`: 0 link interni riscritti, nessuna modifica da includere.

## Deploy

`gh run list -L 1 --workflow deploy.yml` → `conclusion: success`. Prima lettura in_progress, quindi attesa e rilettura: il workflow è arrivato a success.

## Controlli dal vivo (UA browser)

| URL | Esito |
|---|---|
| `/en/2026/11/bitcoin-below-59-000-.../` | 200 |
| `/en/2026/11/hermes-0-23-4-.../` | 200 |
| `/en/2026/11/venice-claims-200-million-annualised-.../` | 200 |
| `/2026/11/bitcoin-sotto-59mila-.../` | 200 |
| `/2026/11/hermes-0.23.4-.../` | 200 |
| `/2026/11/venice-dichiara-200-milioni-.../` | 200 |

Titoli verificati uno per uno: le tre pagine italiane portano ancora il titolo italiano, le tre inglesi il titolo inglese. Le pagine italiane emettono il `link rel=alternate hreflang=en-us` e il selettore di lingua verso il gemello corretto.

Nota fuori competenza (non corretta): nessun problema riscontrato. Il `sitemap.xml` di radice è un indice che punta a `/it/sitemap.xml` e `/en/sitemap.xml`, dove le pagine italiane compaiono senza prefisso di lingua: configurazione preesistente, non toccata.
