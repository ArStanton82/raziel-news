# Traduzione inglese — 2026-11-27

Coda: 3 articoli senza gemello `.en.md`, tutti del 2026-11-27. Nessuno con `draft: true`, nessuno sotto le 200 parole. Tradotti tutti e tre, nessuno saltato.

## Articoli tradotti

| Titolo italiano | Titolo inglese | Percorso inglese |
|---|---|---|
| La parola «privato» costa un chiarimento | The word 'private' costs a clarification | /en/2026/11/the-word-private-costs-a-clarification/ |
| Il vault resta tuo. Le note, forse no | The vault stays yours. The notes, maybe not | /en/2026/11/the-vault-stays-yours-the-notes-maybe-not/ |
| La regola corre più veloce del mercato | The rule runs faster than the market | /en/2026/11/the-rule-runs-faster-than-the-market/ |

Titoli, summary, categorie e tag in inglese; `url` sotto `/en/`; corpo senza `#`; fonte finale dopo `---` con etichetta `*Verified sources: ...*`, testate link e date identici all'italiano. La `date`, gli altri campi, i nomi propri nei tag (Hermes, Venice.ai, Bitcoin) sono rimasti quelli dell'italiano dove previsto.

## Link interni

`python3 scripts/lingua_link_inglesi.py --scrivi`: 202 coppie italiano→inglese con percorso dichiarato, 0 link interni riscritti (nessuno dei tre articoli ne conteneva).

## Commit e deploy

Commit `3f00208`, `feat(i18n): versione inglese di 3 articoli (2026-11-27)`, push su `main` riuscito. Run `deploy.yml` 45991119335 sullo SHA `3f00208`: conclusione `success`. Il run è stato in coda un paio di minuti più del solito prima di partire; nessun errore.

## Controlli dal vivo (UA browser)

Tutte le pagine inglesi rispondono `200`:
- /en/2026/11/the-word-private-costs-a-clarification/ → 200
- /en/2026/11/the-vault-stays-yours-the-notes-maybe-not/ → 200
- /en/2026/11/the-rule-runs-faster-than-the-market/ → 200

Pagine italiane corrispondenti: tutte `200` e con il titolo italiano ancora in pagina:
- /2026/11/la-parola-privato-costa-un-chiarimento/ → 200, titolo presente
- /2026/11/il-vault-resta-tuo.-le-note-forse-no/ → 200, titolo presente
- /2026/11/la-regola-corre-più-veloce-del-mercato/ → 200, titolo presente

Ogni pagina inglese rende correttamente il proprio titolo nell'`h1` e il cambio lingua verso l'italiano.

## Altro

Nessun problema riscontrato. Nulla da correggere fuori dai file `.en.md`.
