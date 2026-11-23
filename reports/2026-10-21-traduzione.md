# Traduzione inglese — 2026-10-21

Coda costruita da `content/posts/`: 3 articoli italiani senza gemello `.en.md`. Tutti e tre tradotti (limite di 6 per esecuzione non raggiunto). Nessun articolo saltato per `draft: true` o per meno di 200 parole.

## Articoli tradotti

| Titolo italiano | Titolo inglese | Percorso inglese |
|---|---|---|
| Venice sbarca a Zurigo, ma al token arriva un decimo dei ricavi | Venice Lands in Zurich, but the Token Gets a Tenth of the Revenue | `/en/2026/10/venice-lands-in-zurich-token-gets-a-tenth-of-revenue/` |
| Il catalogo di Hermes ha 644 plugin, non 700: la differenza conta | Hermes' Plugin Catalog Has 644 Entries, Not 700: the Difference Matters | `/en/2026/10/hermes-plugin-catalog-644-entries-not-700/` |
| Bitcoin, la domanda c'è ma passa da un solo sportello | Bitcoin: the Demand Is There, but It Comes Through a Single Door | `/en/2026/10/bitcoin-demand-through-a-single-door/` |

File creati: `content/posts/2026-10-21-venice-etp-burn.en.md` (650 parole), `content/posts/2026-10-21-hermes-catalogo-plugin.en.md` (594), `content/posts/2026-10-21-bitcoin-etf-finma-strive.en.md` (692). Frontmatter con stessa `date`, `draft: false`, titolo e summary in inglese, categorie inglesi (`Venice.ai`/`Crypto`, `Hermes`/`AI`, `Crypto`/`Blockchain`), tag tradotti con i nomi propri intatti (`francia` → `france`), `url` sotto `/en/`. Corpi senza nessun titolo `#`, solo `##`; riga finale fonti con etichetta `*Verified sources: ...*` e testate/date identiche all'italiano. Nessun fatto aggiunto.

## Link interni

`python3 scripts/lingua_link_inglesi.py --scrivi`: 83 coppie italiano → inglese con percorso dichiarato, 0 link interni riscritti (nessuna delle tre versioni inglesi punta a pagine italiane il cui gemello inglese esista). Nessun altro file toccato dallo script.

## Commit e deploy

- Commit `7bf4e7a` — `feat(i18n): versione inglese di 3 articoli (2026-10-21)`, 3 file, 121 inserimenti. Push su `main` riuscito (`4bc39b7..7bf4e7a`).
- Deploy: `gh run list -L 1 --workflow deploy.yml` → `status: completed`, `conclusion: success`, `headSha: 7bf4e7a` (il commit di questa traduzione). Nota: le prime due chiamate a `gh` sono andate in timeout su `api.github.com` (dial tcp i/o timeout); al terzo tentativo la risposta è arrivata regolare e il run era già verde.

## Verifica dal vivo (user-agent browser)

Versioni inglesi — tutte `200` e con il titolo inglese presente nella pagina:
- `/en/2026/10/venice-lands-in-zurich-token-gets-a-tenth-of-revenue/` → 200
- `/en/2026/10/hermes-plugin-catalog-644-entries-not-700/` → 200
- `/en/2026/10/bitcoin-demand-through-a-single-door/` → 200

Versioni italiane corrispondenti — tutte `200` e con il titolo italiano ancora presente:
- `/2026/10/venice-sbarca-a-zurigo-ma-al-token-arriva-un-decimo-dei-ricavi/` → 200
- `/2026/10/il-catalogo-di-hermes-ha-644-plugin-non-700-la-differenza-conta/` → 200
- `/2026/10/bitcoin-la-domanda-c%C3%A8-ma-passa-da-un-solo-sportello/` → 200

Abbinamento bilingue: ogni pagina inglese contiene tre riferimenti allo slug italiano (alternate `hreflang=it-it`, `hreflang=x-default` e link di cambio lingua), quindi il selettore di lingua è attivo su tutte e tre. Controllo di non-regressione: gli slug inglesi non creano pagine duplicate alla radice italiana (`/2026/10/bitcoin-demand-through-a-single-door/` e `/2026/10/hermes-plugin-catalog-644-entries-not-700/` → 404, corretto).

## Cose non andate lisce

- Due timeout consecutivi di `gh` verso `api.github.com` (rete, non credenziali): risolti al terzo tentativo, nessun impatto sul deploy.
- `https://raziel.news/` risponde `403` con un user-agent `Mozilla/5.0` secco (Bot Fight di Cloudflare) e `200` con la stringa browser completa: i controlli sono stati fatti con quest'ultima.
- Nessun problema riscontrato dentro i file di mia competenza. Fuori di essi restano file non tracciati preesistenti (`scripts/*.py` di altri job, `static/images/card-bg/`) che non ho toccato e che non sono nel commit.
