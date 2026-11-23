# STADIO 3 — PUBBLICAZIONE — 2026-10-28

Esito: completato

## Articoli pubblicati (3)
1. content/posts/2026-10-28-crypto-cftc-utah-prediction-market.md
   slug: la-cftc-cita-in-giudizio-lo-utah-chi-decide-se-un-prediction-market-è-una-scommessa
   URL: https://raziel.news/2026/10/la-cftc-cita-in-giudizio-lo-utah-chi-decide-se-un-prediction-market-%C3%A8-una-scommessa/
2. content/posts/2026-10-28-hermes-abbonamenti-cloud.md
   slug: da-credito-a-orologio-hermes-agent-riscrive-i-suoi-abbonamenti
   URL: https://raziel.news/2026/10/da-credito-a-orologio-hermes-agent-riscrive-i-suoi-abbonamenti/
3. content/posts/2026-10-28-venice-badge-tee-e2ee.md
   slug: due-badge-due-promesse-venice-mette-la-privacy-accanto-al-nome-del-modello
   URL: https://raziel.news/2026/10/due-badge-due-promesse-venice-mette-la-privacy-accanto-al-nome-del-modello/

## Git
commit: 3c676c26b40ce565160b370bdfb3dcdc332820d8
messaggio: feat(posts): articoli del 2026-10-28
push: b4859ab..3c676c2 main -> main (origin)
file nel commit: 3 (solo content/posts/)

## Deploy
workflow: Deploy to GitHub Pages
run: https://github.com/ArStanton82/raziel-news/actions/runs/40672809950
headSha: 3c676c26b40ce565160b370bdfb3dcdc332820d8
conclusion: success

## Verifica online
- raziel.news: 200 su tutti e 3 gli URL (curl con User-Agent browser + Accept-Encoding: identity)
- titoli serviti corretti su tutti e 3 (verifica del tag <title>)
- arstanton82.github.io/raziel-news (origine Pages): 301 -> raziel.news, finale 200

## Note
- Nessun H1 duplicato nel corpo (scripts/strip_duplicate_h1.py: OK su tutti e 3).
- Nessuna bozza saltata per idempotenza (nessun file 2026-10-28 preesistente in content/posts/).
- Nessuna bozza .workspace-copy.md tra quelle di oggi.
- Diff bozza -> post: solo draft: true -> false su tutti e 3 i file.
- Slug ricavati dal build Hugo locale (hugo --destination <scratch>): confermati l'accento mantenuto (è) e il resto slugificato.
- Nessun errore. Nessun force push.
