# Traduzione inglese — 2026-11-05

Coda: 3 articoli (tutti i `content/posts/*.md` senza gemello `.en.md`). Tradotti tutti e 3, sotto il tetto di 6.

## Articoli tradotti

| Titolo italiano | Titolo inglese | Percorso inglese |
|---|---|---|
| Kimi K3.1 Pro è «privato» su Venice: una promessa contrattuale, non una prova crittografica | Kimi K3.1 Pro Is 'Private' on Venice: a Contractual Promise, Not a Cryptographic Proof | `/en/2026/11/kimi-k3-1-pro-private-contract-not-cryptography/` |
| Polygon riscrive un saldo: il fork da 6,8 milioni e la costituzione delle eccezioni | Polygon Rewrites a Balance: the $6.8 Million Fork and the Constitution of Exceptions | `/en/2026/11/polygon-rewrites-a-balance-6-8-million-fork/` |
| Ventimila dollari e una riga nel catalogo: il premio vero dell'hackathon di Hermes | Twenty Thousand Dollars and One Line in the Catalogue: the Real Prize of the Hermes Hackathon | `/en/2026/11/twenty-thousand-dollars-and-one-catalogue-line/` |

## Link interni

`python3 scripts/lingua_link_inglesi.py --scrivi`: 131 coppie italiano → inglese con percorso dichiarato, **0 link interni riscritti** (i tre articoli non contengono link a pagine italiane). Nessuna modifica da includere oltre ai tre file nuovi.

## Commit e deploy

- Commit `f745a9f` — `feat(i18n): versione inglese di 3 articoli (2026-11-05)`, 3 file, 88 righe aggiunte.
- Push su `main` riuscito (`28d00b5..f745a9f`).
- GitHub Actions `deploy.yml` per `f745a9f`: **success** (il run è rimasto `in_progress` per circa 4 minuti, poi concluso).

## Verifica dal vivo (user-agent browser `Mozilla/5.0 ... Chrome/131`)

Pagine inglesi, tutte **200** con il titolo inglese corretto:

- `/en/2026/11/kimi-k3-1-pro-private-contract-not-cryptography/` → 200
- `/en/2026/11/polygon-rewrites-a-balance-6-8-million-fork/` → 200
- `/en/2026/11/twenty-thousand-dollars-and-one-catalogue-line/` → 200

Pagine italiane corrispondenti, tutte **200** e con il titolo italiano ancora intatto:

- `/2026/11/kimi-k3.1-pro-è-privato-su-venice-una-promessa-contrattuale-non-una-prova-crittografica/` → 200, titolo «Kimi K3.1 Pro è «privato» su Venice: una promessa contrattuale, non una prova crittografica»
- `/2026/11/polygon-riscrive-un-saldo-il-fork-da-68-milioni-e-la-costituzione-delle-eccezioni/` → 200, titolo «Polygon riscrive un saldo: il fork da 6,8 milioni e la costituzione delle eccezioni»
- `/2026/11/ventimila-dollari-e-una-riga-nel-catalogo-il-premio-vero-dellhackathon-di-hermes/` → 200, titolo «Ventimila dollari e una riga nel catalogo: il premio vero dell'hackathon di Hermes»

Accoppiamento bilingue confermato: ogni pagina inglese dichiara i tag `hreflang=it-it`, `hreflang=en-us` e `hreflang=x-default` verso l'URL corretto, quindi il cambio lingua compare.

## Note

- Nessun articolo saltato: tutti e tre hanno `draft: false` e superano abbondantemente le 200 parole (543, 632, 658 parole in inglese).
- Nessun H1 nei corpi; solo `##`, come richiesto.
- Slug italiani generati da Hugo dal titolo: quello di Kimi contiene caratteri non ASCII e viene servito con percent-encoding (`kimi-k3.1-pro-%C3%A8-privato...`), e quello di Polygon normalizza «6,8» in `68` (`...il-fork-da-68-milioni...`). Entrambi funzionano (200), ma sono URL che un lettore non indovina: se in futuro si volesse uno slug italiano stabile e ASCII servirebbe un campo `slug:` nei frontmatter italiani, che è fuori dai file che questo job può toccare. Segnalato, non corretto.
- Nessun problema riscontrato fuori dai file `content/posts/*.en.md`.
