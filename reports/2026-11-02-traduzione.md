# Traduzione inglese — 2026-11-02

Coda iniziale: 3 articoli senza gemello `.en.md` (tutti del 2026-11-02). Tradotti tutti e 3, nessun residuo in coda.

## Articoli tradotti

1. **Il prezzo scende, gli staker comprano: la settimana di VVV senza il TVL inventato**
   → *The Price Falls, the Stakers Buy: VVV's Week Without the Invented TVL*
   file: `content/posts/2026-11-02-venice-settimana-staking.en.md`
   percorso inglese: `/en/2026/11/venice-settimana-staking/`

2. **Hermes vuole che il tuo setup non sappia su quante macchine vive**
   → *Hermes Wants Your Setup to Forget How Many Machines It Runs On*
   file: `content/posts/2026-11-02-hermes-gateway-multipli.en.md`
   percorso inglese: `/en/2026/11/hermes-gateway-multipli/`

3. **Il conto dell'hack arriva in tre posti: ETF, prelievi e un ponte che si ferma**
   → *The Hack's Bill Arrives in Three Places: ETFs, Withdrawals and a Bridge That Stops*
   file: `content/posts/2026-11-02-binance-hack-conto.en.md`
   percorso inglese: `/en/2026/11/binance-hack-conto/`

Nessun articolo saltato: tutti e tre hanno `draft: false` e oltre 600 parole. Nessuna versione inglese preesistente è stata sovrascritta.

## Commit e deploy

- `scripts/lingua_link_inglesi.py --scrivi`: 122 coppie IT→EN note, **0 link riscritti** (nessun articolo inglese puntava a pagine italiane con gemello appena creato).
- Commit `bab5c1c` — `feat(i18n): versione inglese di 3 articoli (2026-11-02)`, 3 file, 100 righe aggiunte. Push su `main` riuscito (`5e8d5ec..bab5c1c`).
- Deploy GitHub Actions (`deploy.yml`, run 41437457460, sha `bab5c1c`): **success** (concluso alle 11:35:45 UTC).

## Controlli dal vivo (curl con user-agent da browser)

| Pagina | HTTP |
|---|---|
| `/en/2026/11/venice-settimana-staking/` | 200 |
| `/en/2026/11/hermes-gateway-multipli/` | 200 |
| `/en/2026/11/binance-hack-conto/` | 200 |
| `/2026/11/il-prezzo-scende-gli-staker-comprano-la-settimana-di-vvv-senza-il-tvl-inventato/` | 200 |
| `/2026/11/hermes-vuole-che-il-tuo-setup-non-sappia-su-quante-macchine-vive/` | 200 |
| `/2026/11/il-conto-dellhack-arriva-in-tre-posti-etf-prelievi-e-un-ponte-che-si-ferma/` | 200 |

Le pagine italiane mostrano ancora i titoli italiani originali (`<title>` verificato). Tutti e tre gli articoli inglesi espongono `hreflang=it-it` / `hreflang=en-us` corretti e il cambio lingua compare anche sulle pagine italiane (`hreflang=en lang=en title=English`).

## Note

- Il percorso inglese usa lo slug del nome file (convenzione già in uso nel repo: gli altri `.en.md` mantengono lo slug italiano), mentre l'URL italiano resta derivato dal titolo (`/:year/:month/:title/`). Una prima verifica con lo slug del file sulle pagine italiane ha dato 404: era un errore di costruzione dell'URL nel controllo, non un problema del sito, e i percorsi corretti sono stati ricavati da `/it/sitemap.xml`.
- Nessun problema rilevato fuori dai file di traduzione; nessuna modifica a script, layout, tema o immagini.
