# STADIO 3 — PUBBLICAZIONE — 2026-10-06

Esito: completato

## Articoli pubblicati (3)
1. content/posts/2026-10-06-crypto-treasury-cftc-sec.md
   slug: washington-cambia-marcia-il-tesoro-ritira-due-regole-cftc-e-sec-scrivono-il-manuale-crypto
   URL: https://raziel.news/2026/10/washington-cambia-marcia-il-tesoro-ritira-due-regole-cftc-e-sec-scrivono-il-manuale-crypto/
2. content/posts/2026-10-06-hermes-plugin-catalog-hardware.md
   slug: hermes-e-il-catalogo-dei-plugin-la-fiducia-si-costruisce-con-un-commit-pinnato
   URL: https://raziel.news/2026/10/hermes-e-il-catalogo-dei-plugin-la-fiducia-si-costruisce-con-un-commit-pinnato/
3. content/posts/2026-10-06-venice-flux3-tokenomics.md
   slug: flux-3-arriva-su-venice-e-vvv-stringe-la-cinghia-meno-emissioni-più-burn
   URL: https://raziel.news/2026/10/flux-3-arriva-su-venice-e-vvv-stringe-la-cinghia-meno-emissioni-più-burn/

## Git
commit: d8ee1f92110a08c5794c5753184feaa3b6469c14
messaggio: feat(posts): articoli del 2026-10-06
push: 2ee3db7..d8ee1f9 main -> main (origin)

## Deploy
workflow: Deploy to GitHub Pages
run: https://github.com/ArStanton82/raziel-news/actions/runs/37443503569
headSha: d8ee1f92110a08c5794c5753184feaa3b6469c14
conclusion: success

## Verifica online
- raziel.news: 200 su tutti e 3 gli URL
- arstanton82.github.io/raziel-news (origine Pages): 301 -> raziel.news, finale 200 sui 2 URL ASCII-safe

## Note
- Nessun H1 duplicato nel corpo (scripts/strip_duplicate_h1.py: OK su tutti e 3).
- Nessuna bozza saltata per idempotenza (nessun file 2026-10-06 preesistente in content/posts/).
- Slug ricavati dal build Hugo locale (hugo --destination <scratch>): confermati i nomi con accento "più" e il punto non presente.
- URL accentato verificato via curl (200) costruendo il carattere UTF-8 con escape ANSI-C, perché la forma letterale veniva bloccata dallo scanner di sicurezza.
- Nessun errore. Annotazioni del run solo informative (deprecazione Node.js 20 negli action).
