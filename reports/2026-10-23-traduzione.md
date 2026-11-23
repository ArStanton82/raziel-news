# Traduzione — 2026-10-23

Coda iniziale: 3 articoli (tutti del 2026-10-23, nessuno escluso). Tradotti: 3. Coda residua: 0.

## Articoli tradotti

1. **Hermes 0.22.5: il computer che si condivide** → **Hermes 0.22.5: the computer you share**
   - file: `content/posts/2026-10-23-hermes-v0225-ecosistema.en.md`
   - percorso inglese: `/en/2026/10/hermes-0-22-5-the-computer-you-share/`
   - italiano: `/2026/10/hermes-0.22.5-il-computer-che-si-condivide/`

2. **DIEM, un dollaro di calcolo al giorno** → **DIEM: a dollar of compute a day**
   - file: `content/posts/2026-10-23-diem-un-dollaro-al-giorno.en.md`
   - percorso inglese: `/en/2026/10/diem-a-dollar-of-compute-a-day/`
   - italiano: `/2026/10/diem-un-dollaro-di-calcolo-al-giorno/`

3. **Bitcoin al 60%, e il crypto che smette di chiamarsi così** → **Bitcoin at 60%, and crypto dropping the name**
   - file: `content/posts/2026-10-23-bitcoin-dominanza-a16z-frontier.en.md`
   - percorso inglese: `/en/2026/10/bitcoin-at-60-and-crypto-dropping-the-name/`
   - italiano: `/2026/10/bitcoin-al-60-e-il-crypto-che-smette-di-chiamarsi-cosi/`

## Commit e deploy

- `scripts/lingua_link_inglesi.py --scrivi`: eseguito prima del commit, 89 coppie it→en riconosciute, **0 link riscritti** (anche `_index.en.md` saltato perché senza `url:`).
- Commit `86f15d3` — `feat(i18n): versione inglese di 3 articoli (2026-10-23)`, 3 file aggiunti, 98 righe inserite. Push su `main` riuscito (`d8eb025..86f15d3`).
- Deploy `deploy.yml` sul commit `86f15d3`: **success** (dopo circa 4 minuti; due controlli intermedi lo davano ancora `in_progress`).

## Controlli dal vivo (user-agent browser)

| URL | esito |
|---|---|
| `/en/2026/10/hermes-0-22-5-the-computer-you-share/` | 200 |
| `/en/2026/10/diem-a-dollar-of-compute-a-day/` | 200 |
| `/en/2026/10/bitcoin-at-60-and-crypto-dropping-the-name/` | 200 |
| `/2026/10/hermes-0.22.5-il-computer-che-si-condivide/` | 200, titolo italiano presente |
| `/2026/10/diem-un-dollaro-di-calcolo-al-giorno/` | 200, titolo italiano presente |
| `/2026/10/bitcoin-al-60-e-il-crypto-che-smette-di-chiamarsi-cosi/` | 200, titolo italiano presente |

Controllo di contenuto sul primo file inglese: titolo inglese, corpo e cifre (`888.49 million`) renderizzati, `hreflang` presente.

## Note

- Nessun articolo saltato per `draft: true` o per lunghezza sotto le 200 parole.
- Nessuna modifica fuori da `content/posts/*.en.md` e da questo report. Il repository ha molte directory non tracciate (`reports/raw-*`, `reports/.raw/`, `scripts/*.py` di altri job, `static/images/card-bg/`): non sono state toccate e restano fuori dal commit.
- Percorsi italiani ricavati da `https://raziel.news/it/sitemap.xml` (lo slug dipende dal titolo, non dal nome file). Nota per il futuro: l'articolo Hermes ha un punto nel percorso italiano (`hermes-0.22.5-...`), mentre lo slug inglese è stato scritto in ASCII senza punto.
- Coda di traduzione vuota: al prossimo giro di contenuti nuovi riparte da zero.
