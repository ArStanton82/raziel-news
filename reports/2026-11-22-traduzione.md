# Traduzione inglese — 2026-11-22

## Coda

4 articoli in coda (tutti i file `content/posts/2026-11-22-*.md` senza gemello `.en.md`). Nessun altro articolo non tradotto nel repository: tutta la produzione dal 2026-05-30 al 2026-11-21 ha già il suo `.en.md`. Nessun articolo saltato per `draft: true` o per lunghezza sotto le 200 parole.

## Articoli tradotti (4)

1. «Chi dice no al posto nostro» → «Who says no on our behalf»
   percorso inglese: `/en/2026/11/who-says-no-on-our-behalf/`
   italiano: `/2026/11/chi-dice-no-al-posto-nostro/`
2. «Sotto i 60.000 dollari, mentre i bridge continuano a sanguinare» → «Below 60,000 dollars, while the bridges keep bleeding»
   percorso inglese: `/en/2026/11/below-60000-dollars-while-the-bridges-keep-bleeding/`
   italiano: `/2026/11/sotto-i-60.000-dollari-mentre-i-bridge-continuano-a-sanguinare/`
3. «VVV nuota controcorrente mentre il mercato ha paura» → «VVV swims against the current while the market is afraid»
   percorso inglese: `/en/2026/11/vvv-swims-against-the-current-while-the-market-is-afraid/`
   italiano: `/2026/11/vvv-nuota-controcorrente-mentre-il-mercato-ha-paura/`
4. «Hermes esce dalla chat: il browser diventa una finestra sull'agente» → «Hermes steps out of the chat: the browser becomes a window on the agent»
   percorso inglese: `/en/2026/11/hermes-steps-out-of-the-chat-the-browser-becomes-a-window-on-the-agent/`
   italiano: `/2026/11/hermes-esce-dalla-chat-il-browser-diventa-una-finestra-sullagente/`

Categorie usate: `Philosophy of AI` + `AI`, `Crypto` + `Blockchain`, `Venice.ai` + `Crypto`, `AI` + `Hermes`. Tag tradotti lasciando i nomi propri (Bitcoin, Chainflip, Cyber, Kalshi, VVV, Venice.ai, DefiLlama, hermes) e traducendo i nomi comuni («paura e avidità» → «fear and greed», «armi autonome» → «autonomous weapons», «proattività» → «proactivity»). Righe delle fonti in fondo con l'etichetta `*Verified sources: ...*`, testate, link e date identici all'italiano.

## Script link interni

`python3 scripts/lingua_link_inglesi.py --scrivi` eseguito prima del commit: 186 coppie italiano → inglese con percorso dichiarato, **0 link interni riscritti** in 0 articoli. Nessuna modifica da includere nel commit da parte dello script.

## Commit e deploy

- Commit: `b2cf90b` — `feat(i18n): versione inglese di 4 articoli (2026-11-22)`, 4 file, 154 righe aggiunte, push su `main` riuscito.
- GitHub Actions `deploy.yml` (run 45017903719): conclusione **success**.

## Controlli dal vivo (user-agent da browser, dopo il deploy)

Pagine inglesi, tutte `200` e con il titolo inglese in pagina:

| URL inglese | HTTP |
|---|---|
| `/en/2026/11/who-says-no-on-our-behalf/` | 200 |
| `/en/2026/11/below-60000-dollars-while-the-bridges-keep-bleeding/` | 200 |
| `/en/2026/11/vvv-swims-against-the-current-while-the-market-is-afraid/` | 200 |
| `/en/2026/11/hermes-steps-out-of-the-chat-the-browser-becomes-a-window-on-the-agent/` | 200 |

Pagine italiane corrispondenti, tutte `200` e con il titolo italiano ancora presente:

| URL italiano | HTTP | titolo italiano |
|---|---|---|
| `/2026/11/chi-dice-no-al-posto-nostro/` | 200 | sì |
| `/2026/11/sotto-i-60.000-dollari-mentre-i-bridge-continuano-a-sanguinare/` | 200 | sì |
| `/2026/11/vvv-nuota-controcorrente-mentre-il-mercato-ha-paura/` | 200 | sì |
| `/2026/11/hermes-esce-dalla-chat-il-browser-diventa-una-finestra-sullagente/` | 200 | sì |

## Note e cose fuori dai miei file

- L'URL italiano del secondo articolo conserva il punto nella parte numerica: `/2026/11/sotto-i-60.000-dollari-.../`. È il permalink che Hugo genera dal titolo italiano; non ho toccato nulla e il controllo dal vivo dà `200`.
- Tre dei quattro articoli italiani non hanno il campo `url:` nel frontmatter; per le versioni inglesi l'ho comunque dichiarato, con slug inglese sotto `/en/2026/11/`, come per le altre coppie del sito. Gli indirizzi italiani restano invariati.
- Nel repository ci sono molte directory e file non tracciati (`reports/` storici, vari `scripts/*.py` di singole esecuzioni, `cache/`, `static/images/card-bg/`): non li ho toccati né aggiunti al commit. Il commit contiene solo i 4 file `content/posts/*.en.md`.
- Nessun problema di template o configurazione da segnalare per la correzione: le pagine si generano e si servono correttamente.
