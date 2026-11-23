# Traduzione — 2026-11-03

Coda iniziale: 3 articoli italiani senza gemello inglese, tutti del 2026-11-03. Tradotti tutti e 3 (nessun articolo saltato: nessun `draft: true`, nessuno sotto le 200 parole).

## Articoli tradotti

| Titolo italiano | Titolo inglese | Percorso inglese |
|---|---|---|
| Ottobre, il mese in cui i burn di Venice hanno superato il milione | October: The Month Venice's Burns Crossed One Million | /en/2026/11/venice-burns-cross-one-million/ |
| Hermes 0.22.6 e il trasloco degli altri: la migrazione come funzione | Hermes 0.22.6 and the Move From Other Agents: Migration as a Feature | /en/2026/11/hermes-0226-migration-as-a-feature/ |
| Binance riapre a pezzi, Pyongyang nega: la coda del furto da 6,3 miliardi | Binance Reopens in Pieces, Pyongyang Denies: The Aftermath of the $6.3 Billion Theft | /en/2026/11/binance-reopens-in-pieces-pyongyang-denies/ |

Commit: `6a4521e` — "feat(i18n): versione inglese di 3 articoli (2026-11-03)", 3 file aggiunti, `git push` su `main` riuscito.

## Link interni

`python3 scripts/lingua_link_inglesi.py --scrivi` eseguito prima del commit: 125 coppie italiano → inglese note, **0 link riscritti** (i tre articoli non contengono rimandi interni ad altri pezzi). Nessun file toccato dallo script oltre a quelli creati.

## Deploy

`deploy.yml` per lo SHA `6a4521e` (run 41628240706): **success** (tre controlli a 90 s, 190 s e 310 s; concluso al terzo).

## Verifica dal vivo (user-agent Chrome, dopo il deploy)

Tutte le pagine rispondono **200** e i titoli sono quelli attesi.

| URL | HTTP | `<title>` |
|---|---|---|
| /en/2026/11/venice-burns-cross-one-million/ | 200 | October: The Month Venice's Burns Crossed One Million |
| /2026/11/ottobre-il-mese-in-cui-i-burn-di-venice-hanno-superato-il-milione/ | 200 | Ottobre, il mese in cui i burn di Venice hanno superato il milione |
| /en/2026/11/hermes-0226-migration-as-a-feature/ | 200 | Hermes 0.22.6 and the Move From Other Agents: Migration as a Feature |
| /2026/11/hermes-0.22.6-e-il-trasloco-degli-altri-la-migrazione-come-funzione/ | 200 | Hermes 0.22.6 e il trasloco degli altri: la migrazione come funzione |
| /en/2026/11/binance-reopens-in-pieces-pyongyang-denies/ | 200 | Binance Reopens in Pieces, Pyongyang Denies: The Aftermath of the $6.3 Billion Theft |
| /2026/11/binance-riapre-a-pezzi-pyongyang-nega-la-coda-del-furto-da-63-miliardi/ | 200 | Binance riapre a pezzi, Pyongyang nega: la coda del furto da 6,3 miliardi |

Accoppiamento bilingue verificato: su tutte e tre le pagine inglesi il selettore lingua (`.lingua`) e il `rel=alternate hreflang=it-it` puntano alla pagina italiana corrispondente, e `og:locale:alternate` riporta `it_IT`. L'`<h1>` inglese è stampato dal sito dal frontmatter, il corpo non contiene titoli `#`. I tre URL inglesi compaiono in `https://raziel.news/en/sitemap.xml` sotto 2026/11.

## Note

- Coda residua: **vuota**. Con questo giro tutti gli articoli pubblicati hanno il gemello inglese.
- Nessun problema riscontrato fuori dai file di mia competenza; nessuna modifica a script, layout, static, hugo.yaml, i18n o file italiani.
- Slug inglesi scelti tradotti (non il nome file italiano), come da esempio nelle istruzioni; le immagini OG restano agganciate al basename del file, quindi non serve rigenerare nulla.
