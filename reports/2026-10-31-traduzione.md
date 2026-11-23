# Traduzione inglese — 2026-10-31

Coda: 3 articoli senza gemello `.en.md` (massimo 6 per esecuzione, nessuno rimandato).
Commit: `b5b445e` — "feat(i18n): versione inglese di 3 articoli (2026-10-31)", 3 file, tutti e soli i nuovi `.en.md` in `content/posts/`.

## Articoli tradotti

1. «Sei miliardi propri, due che mancano» → **"Six Billion of Its Own, Two That Are Still Missing"**
   percorso inglese: `/en/2026/10/six-billion-of-its-own-two-that-are-still-missing/`
   file: `content/posts/2026-10-31-binance-copertura-buco.en.md`
2. «Il segreto stava nella cartella sbagliata» → **"The Secret Was in the Wrong Folder"**
   percorso inglese: `/en/2026/10/the-secret-was-in-the-wrong-folder/`
   file: `content/posts/2026-10-31-hermes-segreti-percorso.en.md`
3. «Trentasei per cento sotto il massimo, e una sala piena a New York» → **"Thirty-Six Percent Below the Peak, and a Full House in New York"**
   percorso inglese: `/en/2026/10/thirty-six-percent-below-the-peak-and-a-full-house-in-new-york/`
   file: `content/posts/2026-10-31-venice-prezzo-lumara.en.md`

## Script link interni

`python3 scripts/lingua_link_inglesi.py --scrivi`: 115 coppie italiano → inglese riconosciute, **0 link riscritti** (nessun link interno da correggere in questo giro). Incluso nel commit insieme ai tre file; nessuna modifica dello script oltre ai tre `.en.md`.

## Deploy

`gh run list -L 1 --workflow deploy.yml`: run su `b5b445e` → `status: completed`, `conclusion: success` (dopo circa 5 minuti di attesa; le prime due verifiche a 90" e 210" erano ancora `in_progress`).

## Controlli dal vivo (user-agent browser)

Pagine inglesi — tutte `200`:
- `/en/2026/10/six-billion-of-its-own-two-that-are-still-missing/` → 200
- `/en/2026/10/the-secret-was-in-the-wrong-folder/` → 200
- `/en/2026/10/thirty-six-percent-below-the-peak-and-a-full-house-in-new-york/` → 200

Pagine italiane corrispondenti — tutte `200`, titolo italiano intatto nell'`<h1>`:
- `/2026/10/sei-miliardi-propri-due-che-mancano/` → 200, h1 «Sei miliardi propri, due che mancano»
- `/2026/10/il-segreto-stava-nella-cartella-sbagliata/` → 200, h1 «Il segreto stava nella cartella sbagliata»
- `/2026/10/trentasei-per-cento-sotto-il-massimo-e-una-sala-piena-a-new-york/` → 200, h1 «Trentasei per cento sotto il massimo, e una sala piena a New York»

Home `https://raziel.news/` → 200.

Commuta lingua verificato nei due sensi sulla pagina Hermes: l'italiana espone `class=lingua` con link a `/en/2026/10/the-secret-was-in-the-wrong-folder/`, l'inglese espone il link di ritorno a `/2026/10/il-segreto-stava-nella-cartella-sbagliata/`; gli `<link rel=alternate hreflang>` it-it / en-us / x-default sono presenti e corretti.

## Note

- Nessun articolo saltato: tutti e tre `draft: false` e ben oltre le 200 parole.
- Nessun problema riscontrato fuori dai file di mia competenza.
- La coda per i prossimi giri è vuota: in `content/posts/` non restano `.md` senza gemello `.en.md`.
