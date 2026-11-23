# Traduzione — 2026-11-14

## Coda e articoli tradotti

Coda trovata: 3 articoli senza gemello inglese, tutti del 2026-11-14 (verificato su tutti i 319 `*.md` di `content/posts/`: nessun altro file senza `.en.md`, nessun residuo di giorni precedenti). Nessuno escluso: tutti `draft: false` e tutti ben oltre 200 parole. Tradotti tutti e 3, quindi la coda è esaurita.

| Titolo italiano | Titolo inglese | Percorso inglese |
|---|---|---|
| Bitcoin sotto i 70 mila: la leva paga il conto, la politica risponde | Bitcoin Below $70,000: Leverage Pays the Bill, Policy Answers | `/en/2026/11/bitcoin-below-70000-leverage-pays-the-bill-policy-answers/` |
| Hermes smette di essere un programma e diventa un catalogo | Hermes Stops Being a Program and Becomes a Catalog | `/en/2026/11/hermes-stops-being-a-program-and-becomes-a-catalog/` |
| Venice brucia 458 mila dollari di VVV mentre il token perde metà del massimo | Venice Burns $458,000 of VVV While the Token Sits at Half Its Peak | `/en/2026/11/venice-burns-458000-of-vvv-while-the-token-sits-at-half-its-peak/` |

File creati:

- `content/posts/2026-11-14-bitcoin-sotto-70mila-liquidazioni.en.md`
- `content/posts/2026-11-14-hermes-ecosistema-plugin.en.md`
- `content/posts/2026-11-14-venice-burn-record-prezzo.en.md`

Nessun articolo saltato. Nessun file italiano, di tema, di layout o di script toccato.

## Link interni

`python3 scripts/lingua_link_inglesi.py --scrivi` eseguito prima del commit: 160 coppie italiano→inglese con percorso dichiarato, `link interni riscritti: 0 in 0 articoli inglesi`. Nessuna modifica da includere nel commit, come previsto quando gli articoli di una giornata non si linkano tra loro.

## Commit e deploy

- Commit `59ba86a`, messaggio `feat(i18n): versione inglese di 3 articoli (2026-11-14)`, 3 file, 102 inserzioni.
- Push su `main`: `f7bb186..59ba86a`.
- GitHub Actions `deploy.yml`, run sul commit `59ba86a`: **conclusion = success**. (Rimasto `in_progress` per circa cinque minuti, poi passato a success; nessun rilancio.)

## Verifica dal vivo

Tutti i controlli con user-agent da browser (`Mozilla/5.0 ... Chrome/131`), dopo il deploy.

Pagine inglesi — tutte `200`:

- `/en/2026/11/bitcoin-below-70000-leverage-pays-the-bill-policy-answers/` → 200
- `/en/2026/11/hermes-stops-being-a-program-and-becomes-a-catalog/` → 200
- `/en/2026/11/venice-burns-458000-of-vvv-while-the-token-sits-at-half-its-peak/` → 200

Pagine italiane corrispondenti (URL presi dal sitemap `/it/sitemap.xml`) — tutte `200`, con il titolo italiano ancora in pagina:

- `/2026/11/bitcoin-sotto-i-70-mila-la-leva-paga-il-conto-la-politica-risponde/` → 200, `<title>Bitcoin sotto i 70 mila: la leva paga il conto, la politica risponde</title>`
- `/2026/11/hermes-smette-di-essere-un-programma-e-diventa-un-catalogo/` → 200, `<title>Hermes smette di essere un programma e diventa un catalogo</title>`
- `/2026/11/venice-brucia-458-mila-dollari-di-vvv-mentre-il-token-perde-met%C3%A0-del-massimo/` → 200, `<title>Venice brucia 458 mila dollari di VVV mentre il token perde metà del massimo</title>`

Titoli inglesi in pagina corretti su tutte e tre. Abbinamento bilingue verificato sugli `<link rel=alternate hreflang>`: su ogni pagina inglese `it-it` punta all'URL italiano e `en-us` all'URL `/en/`, quindi il cambio lingua funziona. Corpo inglese completo in pagina (sezioni `Leverage pays the bill`, `The problem that arrives with success`, `The product runs ahead of the token` tutte presenti) e riga finale `*Verified sources: ...*` presente.

## Altro

Nessun problema fuori dai miei file: niente da segnalare su layout, script, `hugo.yaml` o configurazione.
