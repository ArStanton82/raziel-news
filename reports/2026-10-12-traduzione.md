# Traduzione — 2026-10-12

## Coda

Articoli in `content/posts/` senza gemello `.en.md` all'inizio dell'esecuzione: **3**.

Tutti e tre idonei (`draft: false`, ben oltre 200 parole). Nessun articolo saltato.

## Articoli tradotti (3)

| Titolo italiano | Titolo inglese | Percorso inglese |
|---|---|---|
| VVV perde il 17% in una settimana ma i burn toccano il record: la doppia faccia di Venice | VVV drops 17% in a week but burns hit a record: the two faces of Venice | `/en/2026/10/vvv-drops-17-in-a-week-burns-hit-a-record-two-faces-of-venice/` |
| Hermes Agent v0.21.7 e la scelta delle release stabili: il progetto entra nella fase adulta | Hermes Agent v0.21.7 and the switch to tagged releases: the project grows up | `/en/2026/10/hermes-agent-v0217-tagged-releases-the-project-grows-up/` |
| Bitcoin regge sopra gli 84.000 dollari mentre l'Europa stringe i cordoni | Bitcoin holds above 84,000 dollars as Europe tightens the screws | `/en/2026/10/bitcoin-holds-above-84000-dollars-as-europe-tightens-the-screws/` |

File creati (soli file toccati): `content/posts/2026-10-12-venice-burn-record-prezzo.en.md`, `content/posts/2026-10-12-hermes-release-stabili-business.en.md`, `content/posts/2026-10-12-crypto-btc-84k-regole-europa.en.md`.

Frontmatter: stessa `date` (2026-10-12), `draft: false`, titolo/summary in inglese, categorie con i nomi inglesi (`Venice.ai`+`Crypto`, `Hermes`+`AI`, `Crypto`+`Blockchain`), tag tradotti (unico nome comune cambiato: `francia` → `france`). Corpo senza titolo `#`, solo `##`. Riga finale fonti dopo `---`, etichetta `*Verified sources: ...*`, testate/link/date identici all'italiano (incluse le note di discrepanza).

## Script link interni

`python3 scripts/lingua_link_inglesi.py --scrivi` → 55 coppie italiano→inglese note, **0 link interni riscritti** in 0 articoli (nessuno dei tre nuovi file contiene link interni a pagine italiane). Nessuna modifica da includere.

## Commit e deploy

- Commit `4c763b3` — `feat(i18n): versione inglese di 3 articoli (2026-10-12)`, 3 file, 98 inserimenti.
- Push su `main` riuscito (`cedcab2..4c763b3`).
- Workflow `deploy.yml` per `4c763b3`: **conclusion = success**.

## Verifiche dal vivo

- `curl -A "Mozilla/5.0"` diretto su raziel.news: **403 su tutte le URL**, incluse le pagine italiane preesistenti. Causa accertata leggendo le intestazioni: `cf-mitigated: challenge`, cioè la sfida gestita di Cloudflare contro il traffico da datacenter (comportamento noto di questa zona). **Non è un problema del deploy né delle pagine.**
- Verifica ripetuta con lo strumento di estrazione web (fetch da IP diverso, non sfidato):
  - 3 pagine inglesi: **200**, titolo inglese corretto, summary e tutte le sezioni presenti.
  - 3 pagine italiane corrispondenti: **200**, titolo italiano intatto (nessuna sovrascrittura).
- `hreflang` verificato su una build Hugo locale (output in scratch, fuori dal repo): su ogni coppia sono presenti `it-it` → pagina italiana, `en-us` → pagina inglese, `x-default` → pagina italiana, in entrambe le direzioni. Il gemello `.en.md` è quindi agganciato correttamente e il cambio lingua funziona.

## Note / problemi riscontrati (non corretti, fuori dai miei file)

1. Gli URL italiani non derivano dal nome del file ma dal titolo: `hugo.yaml` ha `permalinks: posts: "/:year/:month/:title/"`. Per questo l'italiano di oggi sta su `/2026/10/bitcoin-regge-sopra-gli-84.000-dollari-mentre-leuropa-stringe-i-cordoni/` e non su `/2026/10/crypto-btc-84k-regole-europa/`. Nessuna azione presa: i file inglesi hanno `url:` esplicito sotto `/en/`, quindi non sono interessati. Segnalo solo perché un controllo basato sul nome file italiano darebbe falsi 404.
2. La verifica via `curl` prevista dal job resta impraticabile da questo IP finché Cloudflare tiene attiva la Modalità Bot Fight: serve una fetch da IP non-datacenter (come fatto qui) oppure una regola di bypass.
