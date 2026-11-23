# Pubblicazione — 2026-09-30 (stadio 3 di 4)

Data: 2026-09-30
Esecuzione: cron, profilo kairo (Publishing Manager) — stadio 3 (PUBBLICAZIONE) della pipeline editoriale.
Repo: /root/.hermes/profiles/raziel-news/workspace/raziel-news (origin: ArStanton82/raziel-news, branch main).
Autorizzazione: esecuzione pianificata pre-autorizzata da Kain; commit e push eseguiti senza conferma interattiva.

## Input

Tre bozze di oggi in `drafts/` (nessuna `.workspace-copy.md` esclusa perché non presente per la data odierna):

- `drafts/2026-09-30-hermes-openclaw-agenti-enterprise.md`
- `drafts/2026-09-30-netherlands-tassa-bitcoin-non-realizzati.md`
- `drafts/2026-09-30-venice-vvv-tokenomics-diem.md`

## Esito

Tutti e tre gli articoli pubblicati, deployati e verificati online (HTTP 200 su entrambe le origini).

### 1. OpenClaw Enterprise e la fiducia che gli agenti devono ancora guadagnarsi
- File: `content/posts/2026-09-30-hermes-openclaw-agenti-enterprise.md` (`draft: false`)
- URL raziel.news: https://raziel.news/2026/09/openclaw-enterprise-e-la-fiducia-che-gli-agenti-devono-ancora-guadagnarsi/ — **200**
- URL origine GitHub Pages: https://arstanton82.github.io/raziel-news/2026/09/openclaw-enterprise-e-la-fiducia-che-gli-agenti-devono-ancora-guadagnarsi/ — **200**

### 2. Paesi Bassi, la tassa sui guadagni Bitcoin non realizzati che il governo sta gia' ridimensionando
- File: `content/posts/2026-09-30-netherlands-tassa-bitcoin-non-realizzati.md` (`draft: false`)
- URL raziel.news: https://raziel.news/2026/09/paesi-bassi-la-tassa-sui-guadagni-bitcoin-non-realizzati-che-il-governo-sta-gia-ridimensionando/ — **200**
- URL origine GitHub Pages: https://arstanton82.github.io/raziel-news/2026/09/paesi-bassi-la-tassa-sui-guadagni-bitcoin-non-realizzati-che-il-governo-sta-gia-ridimensionando/ — **200**

### 3. VVV tra buyback e DIEM: dove finisce davvero il valore
- File: `content/posts/2026-09-30-venice-vvv-tokenomics-diem.md` (`draft: false`)
- URL raziel.news: https://raziel.news/2026/09/vvv-tra-buyback-e-diem-dove-finisce-davvero-il-valore/ — **200**
- URL origine GitHub Pages: https://arstanton82.github.io/raziel-news/2026/09/vvv-tra-buyback-e-diem-dove-finisce-davvero-il-valore/ — **200**

Gli slug sono stati letti dal build locale (`hugo --destination <scratch>/hugo-out-20260930`), non dedotti a mano. Nessuno dei tre titoli produce permalink accentati: il problema "permalink con accento non servito" segnalato il 2026-09-30 per l'articolo ChatGPT/Hermes non si ripresenta in questa run.

Il corpo delle tre bozze non iniziava con un H1 e non conteneva H1: `python3 scripts/strip_duplicate_h1.py content/posts` ha restituito `OK ... (nessun H1 nel corpo)` sui tre file, quindi nessuna modifica al corpo. Frontmatter, categorie, tag, summary e riga finale `*Fonti verificate: ...*` copiati dalle bozze; unica modifica: `draft: true` → `draft: false`.

## Idempotenza

`content/posts/` non conteneva alcun file `2026-09-30-*` prima di questa run: pubblicati tutti e tre, nessuno saltato.

## Deploy (GitHub Actions "Deploy to GitHub Pages")

- Commit di pubblicazione: `0472010` — `feat(posts): articoli del 2026-09-30` (3 file, 90 inserimenti)
- Push: `4b12b74..0472010  main -> main`
- Run corrispondente a HEAD: https://github.com/ArStanton82/raziel-news/actions/runs/36709072457
- Esito: `status=completed`, `conclusion=success` (quattro poll a 20 s, allineato su `headSha == 0472010d1b1e889aee5ae54e57007a516f73aba5`)

## Errori

Nessun errore. Committato solo `content/posts/`; `reports/` e `drafts/` non sono stati toccati né committati.

<!-- pipeline-status: 2026-09-30 stage-3 complete -->
