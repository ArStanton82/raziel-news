# Traduzione — 2026-11-13

## Coda e articoli tradotti

Coda trovata: 3 articoli senza gemello inglese, tutti del 2026-11-13. Nessuno escluso (tutti `draft: false`, tutti ben oltre 200 parole). Tradotti tutti e 3, quindi la coda è esaurita: nessun residuo da smaltire nei prossimi giri.

| Titolo italiano | Titolo inglese | Percorso inglese |
|---|---|---|
| Venice, i conti di KR1 e quelli che il sito non conferma | Venice, KR1's Numbers and the Ones the Site Won't Confirm | `/en/2026/11/venice-kr1-numbers-and-the-ones-the-site-wont-confirm/` |
| Otto messaggi e poi un file: la notte in cui Hermes ha smesso di troncare le risposte | Eight Messages and Then a File: the Night Hermes Stopped Cutting Replies Short | `/en/2026/11/eight-messages-and-then-a-file-the-night-hermes-stopped-cutting-replies-short/` |
| Bitcoin sotto i 69.000 dollari: a cedere per primo è stato il margine | Bitcoin Below $69,000: the Margin Gave Way First | `/en/2026/11/bitcoin-below-69000-the-margin-gave-way-first/` |

File creati:

- `content/posts/2026-11-13-venice-kr1-numeri.en.md`
- `content/posts/2026-11-13-hermes-otto-messaggi-file.en.md`
- `content/posts/2026-11-13-bitcoin-leva-liquidazioni.en.md`

## Link interni

`python3 scripts/lingua_link_inglesi.py --scrivi` eseguito prima del commit: 157 coppie italiano→inglese con percorso dichiarato, `link interni riscritti: 0 in 0 articoli inglesi`. Nessuna modifica da includere nel commit, come previsto quando gli articoli di una giornata non si linkano tra loro.

## Commit e deploy

- Commit `be58f02`, messaggio `feat(i18n): versione inglese di 3 articoli (2026-11-13)`, 3 file, 98 inserzioni.
- Push su `main`: `c11e11d..be58f02`.
- GitHub Actions `deploy.yml`, run sul commit `be58f02`: **conclusion = success**. (Il run è rimasto `in_progress` per circa sei minuti, poi è passato a success; nessun rilancio.)

## Verifica dal vivo

Tutti i controlli con user-agent da browser (`Mozilla/5.0 ... Chrome/131`).

Pagine inglesi — tutte `200`:

- `/en/2026/11/venice-kr1-numbers-and-the-ones-the-site-wont-confirm/` → 200
- `/en/2026/11/eight-messages-and-then-a-file-the-night-hermes-stopped-cutting-replies-short/` → 200
- `/en/2026/11/bitcoin-below-69000-the-margin-gave-way-first/` → 200

Pagine italiane corrispondenti — tutte `200`, con il titolo italiano ancora in pagina:

- `/2026/11/venice-i-conti-di-kr1-e-quelli-che-il-sito-non-conferma/` → 200, `<title>Venice, i conti di KR1 e quelli che il sito non conferma</title>`
- `/2026/11/otto-messaggi-e-poi-un-file-la-notte-in-cui-hermes-ha-smesso-di-troncare-le-risposte/` → 200, titolo italiano presente
- `/2026/11/bitcoin-sotto-i-69.000-dollari-a-cedere-per-primo-%C3%A8-stato-il-margine/` → 200, titolo italiano presente

Abbinamento bilingue verificato sugli `<link rel=alternate hreflang>` della pagina inglese del pezzo Bitcoin: `it-it` punta all'URL italiano, `en-us` all'URL `/en/`, quindi il cambio lingua funziona. I titoli inglesi in pagina sono corretti su tutte e tre.

## Altro

Nessun problema fuori dai miei file: niente da segnalare su layout, script o configurazione. Nessun articolo saltato. Nessun file italiano, di tema o di script toccato.
