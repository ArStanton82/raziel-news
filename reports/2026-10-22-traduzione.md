# Traduzione inglese — 2026-10-22

Coda iniziale: 3 articoli senza gemello `.en.md`. Tradotti tutti e 3 (limite per esecuzione: 6). Nessun articolo saltato: tutti `draft: false` e sopra le 200 parole.

## Articoli tradotti

1. «VVV recupera il 21 per cento, ma il suo TVL non esiste» → «VVV Is Up 21 Percent, but Its TVL Doesn't Exist»
   - file: `content/posts/2026-10-22-venice-vvv-staking-lumara.en.md`
   - percorso inglese: https://raziel.news/en/2026/10/vvv-recovers-21-percent-but-its-tvl-does-not-exist/
2. «Hermes chiude il keynote di Nvidia, e il catalogo diventa il prodotto» → «Hermes Closes Out Nvidia's Keynote, and the Catalog Becomes the Product»
   - file: `content/posts/2026-10-22-hermes-gtc-catalogo-meshy.en.md`
   - percorso inglese: https://raziel.news/en/2026/10/hermes-closes-nvidias-keynote-and-the-catalog-becomes-the-product/
3. «Il perimetro si chiude, il prezzo non se ne accorge» → «The Perimeter Closes, the Price Doesn't Notice»
   - file: `content/posts/2026-10-22-crypto-occ-fca-perimetro.en.md`
   - percorso inglese: https://raziel.news/en/2026/10/the-perimeter-closes-the-price-does-not-notice/

## Pre-commit

`python3 scripts/lingua_link_inglesi.py --scrivi` eseguito: 86 coppie italiano→inglese riconosciute, 0 link interni riscritti in 0 articoli (nessun rimando incrociato da correggere in questa tornata). `_index.en.md` saltato per assenza di `url:`, come previsto dallo script.

Commit `72e22e1` — `feat(i18n): versione inglese di 3 articoli (2026-10-22)`, 3 file, 101 righe aggiunte, push su `main` riuscito (`0ab4445..72e22e1`). Nessun altro file del repository toccato: verificato con `git status content/posts` prima del commit, solo i tre `.en.md` nuovi.

## Deploy

`deploy.yml`, run creata alle 10:31:34Z: `status: completed`, `conclusion: success`.

## Controlli dal vivo (user-agent da browser)

Pagine inglesi, tutte `200`:

| URL | HTTP |
|---|---|
| /en/2026/10/vvv-recovers-21-percent-but-its-tvl-does-not-exist/ | 200 |
| /en/2026/10/hermes-closes-nvidias-keynote-and-the-catalog-becomes-the-product/ | 200 |
| /en/2026/10/the-perimeter-closes-the-price-does-not-notice/ | 200 |

Pagine italiane corrispondenti, tutte `200` e con il titolo italiano ancora presente nell'HTML:

| URL | HTTP | titolo |
|---|---|---|
| /2026/10/vvv-recupera-il-21-per-cento-ma-il-suo-tvl-non-esiste/ | 200 | presente |
| /2026/10/hermes-chiude-il-keynote-di-nvidia-e-il-catalogo-diventa-il-prodotto/ | 200 | presente |
| /2026/10/il-perimetro-si-chiude-il-prezzo-non-se-ne-accorge/ | 200 | presente |

Altri controlli sulle pagine inglesi: `<title>` corretto in tutte e tre, un solo `<h1>` (quello del template, nessun titolo duplicato nel corpo), `h2` di sezione 4 / 3 / 4 come negli originali, cambio lingua funzionante in entrambe le direzioni (il link "IT" su ogni pagina inglese punta all'URL italiano giusto).

## Note

- Nessun problema riscontrato fuori dai file di mia competenza. Nessuna correzione applicata a script, layout, configurazione o immagini.
- Coda residua dopo questa esecuzione: zero articoli italiani in attesa di traduzione.
