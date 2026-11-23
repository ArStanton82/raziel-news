# Traduzione inglese — 2026-11-09

Coda iniziale: 4 articoli italiani senza gemello `.en.md`, tutti datati 2026-11-09. Tradotti tutti e 4 (sotto il tetto di 6 per esecuzione). Nessun articolo saltato: nessuno era `draft: true` e tutti superavano le 200 parole.

## Articoli tradotti

1. "La legge scade il 3 gennaio, il regolamento entra il 18" → "The Statute Dies on January 3. The Rulebook Starts on the 18th"
   `/en/2026/11/statute-dies-january-3-rulebook-starts-january-18/`
2. "Hermes impara a farsi l'audit (e a controllare chi approva)" → "Hermes Learns to Audit Itself, and to Check Who Signs Off"
   `/en/2026/11/hermes-audits-itself-and-checks-who-approves/`
3. "Il ponte riapre a metà, e Zcash vuole correre di nuovo" → "The Bridge Reopens Halfway, and Zcash Wants to Run Again"
   `/en/2026/11/tbtc-bridge-reopens-halfway-zcash-block-time/`
4. "Il ducato scende, la cassaforte si riempie" → "The Ducat Falls, the Vault Fills Up"
   `/en/2026/11/the-ducat-falls-the-vault-fills-up/`

Frontmatter: stesse `date`, `draft: false`, categorie in inglese (Crypto / AI+Hermes / Blockchain+Crypto / Venice.ai+Crypto), tag tradotti con i nomi propri invariati (CLARITY Act, GENIUS Act, tBTC, Threshold, Zcash, Aave, VVV, DIEM, Krea 3), `url` sotto `/en/2026/11/`. Corpi senza H1, solo `##` (tre sezioni per articolo, come l'italiano). Riga finale `*Verified sources: ...*` con testate, link e date identici all'italiano.

## Link interni

`python3 scripts/lingua_link_inglesi.py --scrivi`: 145 coppie italiano→inglese con percorso dichiarato, **0 link interni riscritti** in 0 articoli (nessuno dei 4 testi rimanda a un'altra pagina del sito). Nessuna modifica extra da includere nel commit.

## Commit e deploy

- Commit `8b0a5ce` — `feat(i18n): versione inglese di 4 articoli (2026-11-09)`, 4 file, 130 inserimenti.
- Push su `main` riuscito (`fb5b4f6..8b0a5ce`).
- Deploy GitHub Actions `deploy.yml` run `42609752719`: build `success`, deploy `success` (Pages + IndexNow). Il run è rimasto in coda qualche minuto prima di partire, poi è andato a termine senza errori.

## Verifica dal vivo (user-agent browser)

Versioni inglesi — tutte `200`:
- `/en/2026/11/statute-dies-january-3-rulebook-starts-january-18/` → 200
- `/en/2026/11/hermes-audits-itself-and-checks-who-approves/` → 200
- `/en/2026/11/tbtc-bridge-reopens-halfway-zcash-block-time/` → 200
- `/en/2026/11/the-ducat-falls-the-vault-fills-up/` → 200

Versioni italiane corrispondenti — tutte `200` e con il titolo italiano presente in pagina:
- `/2026/11/la-legge-scade-il-3-gennaio-il-regolamento-entra-il-18/` → 200, titolo "La legge scade" trovato
- `/2026/11/hermes-impara-a-farsi-laudit-e-a-controllare-chi-approva/` → 200, titolo "Hermes impara" trovato
- `/2026/11/il-ponte-riapre-a-met%C3%A0-e-zcash-vuole-correre-di-nuovo/` → 200, titolo "Il ponte riapre" trovato
- `/2026/11/il-ducato-scende-la-cassaforte-si-riempie/` → 200, titolo "Il ducato scende" trovato

Ogni pagina inglese dichiara `hreflang=it-it` verso l'italiano e `hreflang=en-us` verso sé stessa: il collegamento bilingue funziona, il cambio lingua compare.

## Note

Nessun problema riscontrato fuori dai file di competenza. Nessun file del repository modificato oltre ai 4 `content/posts/*.en.md` e a questo report.
