# STADIO 3 — PUBBLICAZIONE — 2026-10-08

Esito: completato

## Articoli pubblicati (3)
1. content/posts/2026-10-08-crypto-hormuz-btc.md
   slug: bitcoin-sotto-83.000-dollari-hormuz-il-petrolio-e-il-ritorno-della-paura
   URL: https://raziel.news/2026/10/bitcoin-sotto-83.000-dollari-hormuz-il-petrolio-e-il-ritorno-della-paura/
2. content/posts/2026-10-08-hermes-series-b-business.md
   slug: nous-research-vale-15-miliardi-hermes-esce-dalla-nicchia-e-bussa-alle-imprese
   URL: https://raziel.news/2026/10/nous-research-vale-15-miliardi-hermes-esce-dalla-nicchia-e-bussa-alle-imprese/
3. content/posts/2026-10-08-venice-burn-record-haiku55.md
   slug: venice-brucia-il-record-di-vvv-e-apre-le-porte-a-claude-haiku-5.5
   URL: https://raziel.news/2026/10/venice-brucia-il-record-di-vvv-e-apre-le-porte-a-claude-haiku-5.5/

## Git
commit: c07338155fef39b55783a430797dc45000f5a6e3
messaggio: feat(posts): articoli del 2026-10-08
push: d8dea70..c073381 main -> main (origin)

## Deploy
workflow: Deploy to GitHub Pages
run: https://github.com/ArStanton82/raziel-news/actions/runs/37757645375
headSha: c07338155fef39b55783a430797dc45000f5a6e3
conclusion: success

## Verifica online
- raziel.news: 200 su tutti e 3 gli URL (curl con User-Agent browser + Accept-Encoding: identity)
- arstanton82.github.io/raziel-news (origine Pages): 301 -> raziel.news, finale 200 su tutti e 3 con User-Agent browser

## Note
- Nessun H1 duplicato nel corpo (scripts/strip_duplicate_h1.py: OK su tutti e 3).
- Nessuna bozza saltata per idempotenza (nessun file 2026-10-08 preesistente in content/posts/).
- Nessuna bozza .workspace-copy.md tra quelle di oggi.
- Slug ricavati dal build Hugo locale (hugo --destination <scratch>): confermati il punto (83.000, 5.5) e gli accenti mantenuti.
- Nessun errore. Annotazioni del run solo informative (deprecazione Node.js 20 negli action).
