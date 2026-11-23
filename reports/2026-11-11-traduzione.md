# Traduzione — 2026-11-11

Coda: 3 articoli senza gemello inglese (erano i tre pezzi del 2026-11-11). Tradotti tutti e tre in questa esecuzione, coda esaurita.

## Articoli tradotti

1. «Il denaro torna a costare: il CPI, la frase di Waller e il bitcoin a 73mila» → «Money Costs Something Again: the CPI, Waller's Sentence and Bitcoin at 73K»
   `/en/2026/11/money-costs-something-again-the-cpi-wallers-sentence-and-bitcoin-at-73k/`
2. «Il plugin è diventato il prodotto: l'hackathon di Hermes chiude stasera» → «The Plugin Became the Product: Hermes' Hackathon Closes Tonight»
   `/en/2026/11/the-plugin-became-the-product-hermes-hackathon-closes-tonight/`
3. «Venice brucia il suo record e il TVL resta zero: il conto che i titoli non fanno» → «Venice Burns Its Record and TVL Stays Zero: the Sum the Headlines Don't Do»
   `/en/2026/11/venice-burns-its-record-and-tvl-stays-zero-the-sum-the-headlines-dont-do/`

Nessun articolo saltato: tutti e tre `draft: false` e sopra le 200 parole.

## Pre-commit

- `python3 scripts/lingua_link_inglesi.py --scrivi`: 151 coppie italiano→inglese riconosciute, 0 link interni riscritti (i tre articoli non contengono link interni verso pagine italiane). Nessuna modifica da includere.
- Build locale di controllo (`hugo -d` in cache dir fuori dal repo): exit 0, le tre pagine inglesi generate esattamente nei percorsi dichiarati in `url:`.

## Commit e deploy

- Commit `9dee14f` — `feat(i18n): versione inglese di 3 articoli (2026-11-11)`, push su `main` eseguito.
- GitHub Actions `deploy.yml` sul commit `9dee14f`: **success** (avviato 11:31:45Z, concluso 11:37:07Z). Circa 6 minuti di build; nessun rilancio necessario.

## Controlli dal vivo (user-agent browser)

Tutti `200`:

- `/en/2026/11/money-costs-something-again-the-cpi-wallers-sentence-and-bitcoin-at-73k/`
- `/en/2026/11/the-plugin-became-the-product-hermes-hackathon-closes-tonight/`
- `/en/2026/11/venice-burns-its-record-and-tvl-stays-zero-the-sum-the-headlines-dont-do/`
- `/2026/11/il-denaro-torna-a-costare-il-cpi-la-frase-di-waller-e-il-bitcoin-a-73mila/`
- `/2026/11/il-plugin-è-diventato-il-prodotto-lhackathon-di-hermes-chiude-stasera/` (percent-encoded: `%C3%A8`)
- `/2026/11/venice-brucia-il-suo-record-e-il-tvl-resta-zero-il-conto-che-i-titoli-non-fanno/`

Verifiche aggiuntive:

- Le tre pagine italiane mostrano ancora il titolo italiano corretto nel `<title>`.
- Le tre pagine inglesi mostrano il titolo inglese nel `<title>`.
- Coppia bilingue corretta: su ogni pagina inglese `hreflang=it-it` punta alla pagina italiana esatta, e su ogni pagina italiana `hreflang=en-us` punta al nuovo indirizzo `/en/`.

## Note

- Il percorso italiano dell'articolo 3 non è derivabile dal titolo a occhio (slug `venice-brucia-il-suo-record-e-il-tvl-resta-zero-il-conto-che-i-titoli-non-fanno`): verificato sulla build, non corretto a mano — i file italiani non si toccano.
- Nessun problema rilevato fuori dai file di mia competenza. Nessun file del repo toccato oltre ai tre `*.en.md`.
