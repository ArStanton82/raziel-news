# Traduzione inglese — 2026-10-19

Coda: 3 articoli italiani senza gemello `.en.md` (tutti del 2026-10-19). Tradotti tutti e 3, nessuno saltato (nessun `draft: true`, tutti sopra le 200 parole).

## Articoli tradotti

| Titolo italiano | Titolo inglese | Percorso inglese |
|---|---|---|
| La CFTC scrive il manuale: le cripto retail cercano regole federali | The CFTC writes the manual: retail crypto goes looking for federal rules | `/en/2026/10/the-cftc-writes-the-manual-retail-crypto-federal-rules/` |
| DeepSeek 1017 su Venice: lo stesso modello, un altro conto | DeepSeek 1017 on Venice: the same model, a different bill | `/en/2026/10/deepseek-1017-on-venice-the-same-model-a-different-bill/` |
| Hermes SEO: quarantacinque competenze in cerca di un catalogo | Hermes SEO: forty-five skills in search of a catalogue | `/en/2026/10/hermes-seo-forty-five-skills-in-search-of-a-catalogue/` |

File creati: `content/posts/2026-10-19-crypto-cftc-reg-ctx-cam.en.md`, `2026-10-19-venice-deepseek-1017-vvv.en.md`, `2026-10-19-hermes-seo-plugin.en.md`.

Note di traduzione: categorie rese con i nomi inglesi (`Crypto`, `Blockchain`, `Venice.ai`, `AI`, `Hermes`); tag tradotti nei nomi comuni (`regolamentazione` → `regulation`, `mercati` → `markets`, `modelli` → `models`) e lasciati intatti nei nomi propri (`cftc`, `bitcoin`, `deepseek`, `vvv`, `seo`, `mcp`). Le righe finali delle fonti riportano testate, link e date identici all'italiano, con l'etichetta `*Verified sources: ...*`. Le discrepanze segnalate negli articoli italiani (il «Reg CM» del post CoinDesk, il TVL di 1,68 mld del report di Echo, il «catalogo» del post su Hermes SEO) sono rimaste nel testo inglese con lo stesso tono prudente.

## Lingua dei link interni

`python3 scripts/lingua_link_inglesi.py --scrivi` eseguito prima del commit: 77 coppie it→en riconosciute, **0 link riscritti** in 0 articoli (nessuno dei tre articoli contiene link interni verso pagine italiane). Nessuna modifica da includere nel commit.

## Commit e deploy

- Commit `5998a95` — `feat(i18n): versione inglese di 3 articoli (2026-10-19)` (3 file, 88 inserimenti), push su `main` riuscito (`89730e6..5998a95`).
- Workflow `deploy.yml` (headSha `5998a95`): `completed` / **success**. I primi due controlli dopo i 90 secondi davano ancora `in_progress`; il run è arrivato a `success` dopo circa cinque minuti.

## Verifiche dal vivo

Cloudflare (Bot Fight Mode) respinge le richieste da datacenter con `403`: le prime curl con il solo `-A "Mozilla/5.0"` sono state bloccate tutte e tre. Ripetendo con uno user-agent Chrome completo più `Accept` e `Accept-Language` da browser le pagine arrivano con `200` e contenuto corretto. È il comportamento noto dell'infrastruttura, non un problema del sito.

Pagine inglesi — tutte `200`:

| Percorso | HTTP | Titolo servito |
|---|---|---|
| `/en/2026/10/the-cftc-writes-the-manual-retail-crypto-federal-rules/` | 200 | The CFTC writes the manual: retail crypto goes looking for federal rules |
| `/en/2026/10/deepseek-1017-on-venice-the-same-model-a-different-bill/` | 200 | DeepSeek 1017 on Venice: the same model, a different bill |
| `/en/2026/10/hermes-seo-forty-five-skills-in-search-of-a-catalogue/` | 200 | Hermes SEO: forty-five skills in search of a catalogue |

Pagine italiane corrispondenti — tutte `200` e con il titolo italiano intatto:

| Percorso | HTTP | Titolo servito |
|---|---|---|
| `/2026/10/la-cftc-scrive-il-manuale-le-cripto-retail-cercano-regole-federali/` | 200 | La CFTC scrive il manuale: le cripto retail cercano regole federali |
| `/2026/10/deepseek-1017-su-venice-lo-stesso-modello-un-altro-conto/` | 200 | DeepSeek 1017 su Venice: lo stesso modello, un altro conto |
| `/2026/10/hermes-seo-quarantacinque-competenze-in-cerca-di-un-catalogo/` | 200 | Hermes SEO: quarantacinque competenze in cerca di un catalogo |

Cambio lingua verificato in entrambe le direzioni: ogni pagina inglese dichiara `hreflang=it-it` verso l'italiano e `hreflang=en-us` verso sé stessa; ogni pagina italiana contiene il link `hreflang=en-us` al gemello. Struttura dei titoli corretta: un solo `<h1>` (stampato dal sito) e le sezioni `##` rese come `<h2>`, nessun `#` nel corpo.

## Altro

- I percorsi italiani derivano dal `title` e non dal nome del file (permalink `/:year/:month/:title/`), quindi sono stati letti direttamente dal tag `hreflang=it-it` della pagina inglese invece di essere indovinati.
- Nessun problema riscontrato fuori dai file di mia competenza; nessuna modifica fatta a script, layout, configurazione, immagini o file italiani.
