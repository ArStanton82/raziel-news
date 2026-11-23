# Traduzione inglese — 2026-10-28

Coda di partenza: 3 articoli senza gemello `.en.md` (tutti i `*.md` del 2026-10-28). Tradotti tutti e 3, sotto il tetto di 6. Nessun articolo saltato per `draft: true` o per lunghezza inferiore a 200 parole.

## Articoli tradotti

| Titolo italiano | Titolo inglese | Percorso inglese |
|---|---|---|
| La CFTC cita in giudizio lo Utah: chi decide se un prediction market è una scommessa | The CFTC Sues Utah: Who Decides Whether a Prediction Market Is Gambling | `/en/2026/10/the-cftc-sues-utah-who-decides-whether-a-prediction-market-is-gambling/` |
| Da credito a orologio: Hermes Agent riscrive i suoi abbonamenti | From Credit to Clock: Hermes Agent Rewrites Its Subscriptions | `/en/2026/10/from-credit-to-clock-hermes-agent-rewrites-its-subscriptions/` |
| Due badge, due promesse: Venice mette la privacy accanto al nome del modello | Two Badges, Two Promises: Venice Puts Privacy Next to the Model Name | `/en/2026/10/two-badges-two-promises-venice-puts-privacy-next-to-the-model-name/` |

File creati: `content/posts/2026-10-28-crypto-cftc-utah-prediction-market.en.md`, `content/posts/2026-10-28-hermes-abbonamenti-cloud.en.md`, `content/posts/2026-10-28-venice-badge-tee-e2ee.en.md`. Nessun altro file toccato.

## Script link interni

`python3 scripts/lingua_link_inglesi.py --scrivi`: 105 coppie italiano→inglese riconosciute, `_index.en.md` saltato (senza `url:`), **0 link riscritti in 0 articoli**. I tre articoli del giorno non contengono link interni nel corpo, quindi non c'era nulla da rimappare.

## Deploy

Commit `0cae707` — `feat(i18n): versione inglese di 3 articoli (2026-10-28)`, 3 file, 96 righe aggiunte. Push su `main` riuscito (`3c676c2..0cae707`).
GitHub Actions `deploy.yml`: atteso circa 5 minuti fra `in_progress` e la conclusione, esito **success** sullo SHA `0cae707e98b89113e60ef224dd9dd84af0d228b2`.

## Controlli dal vivo (user-agent browser)

Pagine inglesi — tutte `200`:
- `/en/2026/10/the-cftc-sues-utah-who-decides-whether-a-prediction-market-is-gambling/`
- `/en/2026/10/from-credit-to-clock-hermes-agent-rewrites-its-subscriptions/`
- `/en/2026/10/two-badges-two-promises-venice-puts-privacy-next-to-the-model-name/`

`<title>` corretto su tutte e tre. Conteggio parole dei file (frontmatter e riga fonti inclusi, quindi confronto omogeneo): CFTC 661 → 619, Hermes 591 → 594, Venice 600 → 580.

Pagine italiane corrispondenti — tutte `200` e con il titolo italiano intatto:
- `/2026/10/la-cftc-cita-in-giudizio-lo-utah-chi-decide-se-un-prediction-market-è-una-scommessa/` → «La CFTC cita in giudizio lo Utah: chi decide se un prediction market è una scommessa»
- `/2026/10/da-credito-a-orologio-hermes-agent-riscrive-i-suoi-abbonamenti/` → «Da credito a orologio: Hermes Agent riscrive i suoi abbonamenti»
- `/2026/10/due-badge-due-promesse-venice-mette-la-privacy-accanto-al-nome-del-modello/` → «Due badge, due promesse: Venice mette la privacy accanto al nome del modello»

Cambio lingua: sulle tre pagine inglesi il markup `hreflang`/`alternate` è identico a quello di una pagina inglese già in produzione (controllo comparativo su `/en/2026/10/one-dollar-a-million-.../`), con il collegamento all'URL italiano presente 3 volte. Il selettore lingua sta dentro il menù a tendina (non in `<head>` con `hreflang="it"` letterale), per questo il primo grep non lo trovava: non è un difetto, è la struttura del tema.

## Note

- Numeri, nomi, citazioni e riserve sono rimasti quelli dell'italiano, comprese le attribuzioni prudenti (la cifra di 60 milioni nello Utah, la discrepanza sul TVL Venice di 1,748 mld, l'omissione delle metriche social Hermes) e le note finali sulle fonti, con etichetta `*Verified sources: ...*`.
- Categorie: `Crypto`/`Blockchain`, `Hermes`/`AI`, `Venice.ai`/`AI`. Tag tradotti solo nei nomi comuni (`regolamentazione` → `regulation`, `usa` → `united-states`, `abbonamenti` → `subscriptions`), nomi propri e termini tecnici lasciati come sono (`kalshi`, `tee`, `e2ee`, `hermes-agent`).
- Nessun problema fuori dai file di mia competenza rilevato.
- Restano 0 articoli in coda: la prossima esecuzione non avrà nulla da tradurre salvo nuove pubblicazioni.
