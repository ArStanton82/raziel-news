# Traduzione inglese — 2026-10-07

## Coda

Articoli italiani in `content/posts/` senza gemello `.en.md`: **3** (tutti quelli del giorno).
Nessun arretrato: la coda era composta solo dagli articoli di oggi. Tutti `draft: false` e sopra le 200 parole — nessuno saltato. Limite di 6 non raggiunto.

## Articoli tradotti

| Titolo italiano | Titolo inglese | Percorso inglese |
|---|---|---|
| $VVV sbarca su Solana: Venice allarga le rotte e stringe le emissioni | VVV lands on Solana: Venice widens its routes and tightens emissions | `/en/2026/10/vvv-solana-venice-catalogue-emissions/` |
| Hermes Index: misurare gli agenti sul costo reale, non solo sul punteggio | Hermes Index: measuring agents on real cost, not just on score | `/en/2026/10/hermes-index-cost-per-task/` |
| Bitcoin sotto 84.000 dollari, mentre Washington cambia rotta | Bitcoin below 84,000 dollars as Washington changes course | `/en/2026/10/bitcoin-below-84k-cftc-fincen/` |

File creati:
- `content/posts/2026-10-07-venice-vvv-solana-catalogo.en.md`
- `content/posts/2026-10-07-hermes-index-costo-per-task.en.md`
- `content/posts/2026-10-07-bitcoin-liquidazioni-cftc-fincen.en.md`

Nessun altro file del repository toccato; i file italiani non sono stati modificati.

## Riscrittura dei link interni

`python3 scripts/lingua_link_inglesi.py --scrivi` eseguito prima del commit:

```
coppie italiano → inglese con percorso dichiarato: 39
versioni inglesi senza `url:` (saltate): _index.en.md
link interni riscritti: 0 in 0 articoli inglesi
```

Nessun link da correggere: i tre articoli non contengono link interni verso altri articoli.

## Commit e deploy

- Commit `b86be1d` — `feat(i18n): versione inglese di 3 articoli (2026-10-07)` (3 file, 90 inserimenti).
- Push su `main` riuscito (`dd12c6b..b86be1d`).
- Workflow `deploy.yml` sul commit `b86be1db0b38569112d3f3d13f7e6e92f2180dda`: **success** (prima `in_progress`, poi `completed`/`success`).

## Verifica dal vivo

Tutte le richieste con user-agent da browser completo (`Mozilla/5.0 (Windows NT 10.0; Win64; x64) ... Chrome/128.0`) e header `Accept`/`Accept-Language`/`--compressed`.

Versioni inglesi — HTTP 200 e titolo inglese corretto:

| URL | HTTP | Titolo |
|---|---|---|
| `/en/2026/10/vvv-solana-venice-catalogue-emissions/` | 200 | VVV lands on Solana: Venice widens its routes and tightens emissions |
| `/en/2026/10/hermes-index-cost-per-task/` | 200 | Hermes Index: measuring agents on real cost, not just on score |
| `/en/2026/10/bitcoin-below-84k-cftc-fincen/` | 200 | Bitcoin below 84,000 dollars as Washington changes course |

Versioni italiane corrispondenti — HTTP 200 e titolo italiano intatto:

| URL | HTTP | Titolo |
|---|---|---|
| `/2026/10/vvv-sbarca-su-solana-venice-allarga-le-rotte-e-stringe-le-emissioni/` | 200 | $VVV sbarca su Solana: Venice allarga le rotte e stringe le emissioni |
| `/2026/10/hermes-index-misurare-gli-agenti-sul-costo-reale-non-solo-sul-punteggio/` | 200 | Hermes Index: misurare gli agenti sul costo reale, non solo sul punteggio |
| `/2026/10/bitcoin-sotto-84.000-dollari-mentre-washington-cambia-rotta/` | 200 | Bitcoin sotto 84.000 dollari, mentre Washington cambia rotta |

Cambio lingua bidirezionale confermato: ogni pagina inglese dichiara `hreflang=it-it` verso la pagina italiana corretta, e ogni pagina italiana dichiara `hreflang=en-us` verso la pagina inglese corretta.

## Note e cose non risolte

1. **403 con user-agent troncato.** Con il solo `-A "Mozilla/5.0"` tutte e sei le URL restituiscono `403`: è la sfida di Cloudflare (Bot Fight) al traffico da datacenter, già nota. Con lo user-agent da browser completo le pagine rispondono `200`. Non è un problema del sito.
2. **Percorsi italiani non deducibili dal nome file.** I permalink usano `/:year/:month/:title/` e `:title` è il titolo italiano slugificato (es. il file `2026-10-07-venice-vvv-solana-catalogo.md` è servito a `/2026/10/vvv-sbarca-su-solana-venice-allarga-le-rotte-e-stringe-le-emissioni/`). Le URL italiane sono state ricavate leggendo `hreflang=it-it` dalle pagine inglesi.
3. Nessun problema rilevato fuori dai file `content/posts/*.en.md` e da questo report.
