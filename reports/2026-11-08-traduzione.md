# Traduzione — 2026-11-08

Coda: 4 articoli italiani senza gemello inglese, tutti nella stessa data. Tradotti tutti e quattro (sotto il limite di 6).

## Articoli tradotti

| Titolo italiano | Titolo inglese | Percorso inglese |
|---|---|---|
| Bitcoin sotto i 76 mila: gli ETF restituiscono il 2026 | Bitcoin Below 76K: the ETFs Hand 2026 Back | `/en/2026/11/bitcoin-below-76k-etfs-hand-back-2026/` |
| Un database, una coda e una riga UNVERIFIED: Hermes dà uno stato agli agenti | One Database, One Queue, One UNVERIFIED Line: Hermes Gives Agents a State | `/en/2026/11/one-database-one-queue-one-unverified-line/` |
| Il dovere di sapere e il diritto di guardare | The Duty to Know and the Right to Watch | `/en/2026/11/the-duty-to-know-and-the-right-to-watch/` |
| VVV diventa un prodotto quotato: cosa compra chi lo compra | VVV Becomes a Listed Product: What Its Buyers Are Actually Buying | `/en/2026/11/vvv-becomes-a-listed-product/` |

Commit: `caa164d` — `feat(i18n): versione inglese di 4 articoli (2026-11-08)` (4 file, 147 inserzioni).

## Controlli preliminari

- `python3 scripts/lingua_link_inglesi.py --scrivì`: 141 coppie it→en con percorso dichiarato, 0 link interni riscritti, 0 articoli toccati (i quattro articoli del giorno non contengono link interni ad altre pagine del sito).
- Nessun corpo inglese inizia con `# `: solo `##`.
- Build locale di controllo con Hugo v0.154.5+extended: exit 0, le quattro pagine compilano e finiscono sotto `/en/2026/11/`.
- Frontmatter: stessi campi e stessa `date` dell'italiano, `draft: false`, categorie con i nomi inglesi (la categoria "Filosofia dell'AI" diventa `Philosophy of AI`), tag tradotti con i nomi propri lasciati intatti.

## Deploy

`gh run list -L 1 --workflow deploy.yml` sul commit `caa164d`: **success** (il primo controllo a 90 s era ancora `in_progress`, completato dopo circa 4 minuti).

## Verifica dal vivo (user-agent browser completo)

Con `-A "Mozilla/5.0"` secco Cloudflare risponde 403 su tutto, come da comportamento noto; con lo user-agent Chrome completo del browser interno risposte corrette.

Pagine inglesi:
- `/en/2026/11/bitcoin-below-76k-etfs-hand-back-2026/` → **200**, `<title>Bitcoin Below 76K: the ETFs Hand 2026 Back`
- `/en/2026/11/one-database-one-queue-one-unverified-line/` → **200**, `<title>One Database, One Queue, One UNVERIFIED Line: Hermes Gives Agents a State`
- `/en/2026/11/the-duty-to-know-and-the-right-to-watch/` → **200**, `<title>The Duty to Know and the Right to Watch`
- `/en/2026/11/vvv-becomes-a-listed-product/` → **200**, `<title>VVV Becomes a Listed Product: What Its Buyers Are Actually Buying`

Pagine italiane corrispondenti: tutte **200** e con il titolo italiano ancora in pagina:
- `/2026/11/bitcoin-sotto-i-76-mila-gli-etf-restituiscono-il-2026/` → 200, «Bitcoin sotto i 76 mila: gli ETF restituiscono il 2026»
- `/2026/11/un-database-una-coda-e-una-riga-unverified-hermes-d%C3%A0-uno-stato-agli-agenti/` → 200, «Un database, una coda e una riga UNVERIFIED: Hermes dà uno stato agli agenti»
- `/2026/11/il-dovere-di-sapere-e-il-diritto-di-guardare/` → 200, «Il dovere di sapere e il diritto di guardare»
- `/2026/11/vvv-diventa-un-prodotto-quotato-cosa-compra-chi-lo-compra/` → 200, «VVV diventa un prodotto quotato: cosa compra chi lo compra»

Accoppiamento bilingue attivo: le pagine italiane espongono gli `hreflang` (it-it, en-us, x-default) e il link di cambio lingua verso il percorso `/en/`, e le pagine inglesi dichiarano il proprio `hreflang="en-us"`. La riga `*Verified sources:*` è presente in fondo a tutte e quattro le versioni inglesi.

## Note

- Il primo tentativo di verifica dell'articolo su Hermes Kanban ha dato 404 solo perché avevo indovinato il percorso italiano senza l'accento: lo slug reale è `.../unverified-hermes-d%C3%A0-uno-stato-agli-agenti/` (Hugo conserva la `à` percent-encoded). Con il percorso corretto la pagina risponde 200. Nessun problema di sito.
- Nessun articolo saltato: nessun `draft: true`, nessun file sotto le 200 parole.
- Nessun file toccato fuori da `content/posts/*.en.md` e da questo report.
