# Traduzione inglese — 2026-11-20

Coda iniziale: 6 articoli (era esattamente il massimo per esecuzione). Coda residua a fine giro: **0** — tutte le versioni italiane in `content/posts/` hanno ora il gemello `.en.md`.

## Articoli tradotti (6)

| Titolo italiano | Titolo inglese | Percorso inglese |
|---|---|---|
| Il credito che scade a mezzanotte: KR1 vende l'inferenza di Venice come una rendita | The credit that expires at midnight: KR1 sells Venice inference as an annuity | /en/2026/11/the-credit-that-expires-at-midnight-kr1-sells-venice-inference-as-an-annuity/ |
| Hermes 0.23.3: la patch che non vuole raccontarsi | Hermes 0.23.3: the patch that refuses to explain itself | /en/2026/11/hermes-0-23-3-the-patch-that-refuses-to-explain-itself/ |
| Il record degli ETF è vero, ma porta la data del 30 settembre | The ETF record is real, but it carries a 30 September date | /en/2026/11/the-etf-record-is-real-but-it-carries-a-30-september-date/ |
| Venice: i crediti galoppano, gli abbonati si sono fermati | Venice: credits gallop, subscribers have stalled | /en/2026/11/venice-credits-gallop-subscribers-have-stalled/ |
| Hermes entra in Teams, e porta in ufficio le abitudini dei colleghi | Hermes walks into Teams, and brings its colleagues' habits to the office | /en/2026/11/hermes-walks-into-teams-and-brings-its-colleagues-habits-to-the-office/ |
| Un'ingiunzione da 6,5 miliardi non è denaro recuperato | A $6.5 billion injunction is not money recovered | /en/2026/11/a-6-5-billion-injunction-is-not-money-recovered/ |

Nessun articolo saltato: nessuno era `draft: true`, tutti sopra le 200 parole (564–659 parole nella versione inglese).

## Commit e deploy

- Commit `b55b1a4` — `feat(i18n): versione inglese di 6 articoli (2026-11-20)`, 6 file, 196 righe aggiunte, push su `main` riuscito.
- `scripts/lingua_link_inglesi.py --scrivi`: 0 link interni riscritti (179 coppie it→en note, nessuna da correggere in questo giro). Nessuna modifica da includere oltre ai sei file nuovi.
- Deploy GitHub Actions (`deploy.yml`, run 44728339381): **success** (build, guardia anti-titolo duplicato, immagini di condivisione, verifica meta, deploy su Pages e IndexNow tutti verdi).

## Controlli dal vivo (user-agent browser)

Tutte le sei pagine inglesi rispondono **200**; tutte le sei pagine italiane corrispondenti rispondono **200** e contengono ancora il titolo italiano in pagina. I titoli inglesi compaiono regolarmente nelle pagine `/en/`.

| Pagina | HTTP | Titolo in pagina |
|---|---|---|
| /en/…the-credit-that-expires-at-midnight…/ | 200 | sì |
| /en/…hermes-0-23-3-the-patch-that-refuses…/ | 200 | sì |
| /en/…the-etf-record-is-real…/ | 200 | sì |
| /en/…venice-credits-gallop…/ | 200 | sì |
| /en/…hermes-walks-into-teams…/ | 200 | sì |
| /en/…a-6-5-billion-injunction…/ | 200 | sì |
| (le 6 controparti italiane) | 200 | sì, titolo italiano invariato |

Le sei coordinate `/en/` compaiono anche in `https://raziel.news/en/sitemap.xml`.

## Note

- Come da memoria di profilo, il markup delle pagine articolo non emette `hreflang` né un link diretto fra gemello italiano e inglese: problema noto e fuori dal perimetro di questo job (template), non toccato.
- Nessun file fuori da `content/posts/*.en.md` e da questo report è stato creato o modificato.
