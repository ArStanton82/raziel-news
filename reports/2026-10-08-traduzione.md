# Traduzione inglese — 2026-10-08

## Coda

Articoli italiani in `content/posts/` senza gemello `.en.md`: **3** (tutti quelli del giorno).
Nessun arretrato: la coda era composta solo dagli articoli di oggi. Tutti `draft: false` e sopra le 200 parole — nessuno saltato. Limite di 6 non raggiunto.

## Articoli tradotti

| Titolo italiano | Titolo inglese | Percorso inglese |
|---|---|---|
| Bitcoin sotto 83.000 dollari: Hormuz, il petrolio e il ritorno della paura | Bitcoin below $83,000: Hormuz, oil and the return of fear | `/en/2026/10/bitcoin-below-83000-hormuz-oil-fear/` |
| Nous Research vale 1,5 miliardi: Hermes esce dalla nicchia e bussa alle imprese | Nous Research is worth $1.5 billion: Hermes leaves the niche and knocks on the enterprise door | `/en/2026/10/nous-research-1-5-billion-hermes-for-businesses/` |
| Venice brucia il record di VVV e apre le porte a Claude Haiku 5.5 | Venice burns a record amount of VVV and opens the door to Claude Haiku 5.5 | `/en/2026/10/venice-vvv-burn-record-claude-haiku-5-5/` |

File creati:
- `content/posts/2026-10-08-crypto-hormuz-btc.en.md`
- `content/posts/2026-10-08-hermes-series-b-business.en.md`
- `content/posts/2026-10-08-venice-burn-record-haiku55.en.md`

Nessun altro file del repository toccato; i file italiani non sono stati modificati.

## Riscrittura dei link interni

`python3 scripts/lingua_link_inglesi.py --scrivi` eseguito prima del commit:

```
coppie italiano → inglese con percorso dichiarato: 42
versioni inglesi senza `url:` (saltate): _index.en.md
link interni riscritti: 0 in 0 articoli inglesi
```

Nessun link da correggere: i tre articoli non contengono link interni verso altri articoli.

## Commit e deploy

- Commit `b94a10b` — `feat(i18n): versione inglese di 3 articoli (2026-10-08)` (3 file, 90 inserimenti).
- Push su `main` riuscito (`c073381..b94a10b`).
- Workflow `deploy.yml` sul commit `b94a10ba7f59a1f269585ba193ccebe74c12c236`: **success** (prima `in_progress`, poi `completed`/`success`).

## Verifica dal vivo

Tutte le richieste con user-agent da browser completo (`Mozilla/5.0 (Windows NT 10.0; Win64; x64) ... Chrome/128.0`) e header `Accept`/`Accept-Language`/`--compressed`.

Versioni inglesi — HTTP 200 e titolo inglese corretto:

| URL | HTTP | Titolo |
|---|---|---|
| `/en/2026/10/bitcoin-below-83000-hormuz-oil-fear/` | 200 | Bitcoin below $83,000: Hormuz, oil and the return of fear |
| `/en/2026/10/nous-research-1-5-billion-hermes-for-businesses/` | 200 | Nous Research is worth $1.5 billion: Hermes leaves the niche and knocks on the enterprise door |
| `/en/2026/10/venice-vvv-burn-record-claude-haiku-5-5/` | 200 | Venice burns a record amount of VVV and opens the door to Claude Haiku 5.5 |

Versioni italiane corrispondenti — HTTP 200 e titolo italiano intatto:

| URL | HTTP | Titolo |
|---|---|---|
| `/2026/10/bitcoin-sotto-83.000-dollari-hormuz-il-petrolio-e-il-ritorno-della-paura/` | 200 | Bitcoin sotto 83.000 dollari: Hormuz, il petrolio e il ritorno della paura |
| `/2026/10/nous-research-vale-15-miliardi-hermes-esce-dalla-nicchia-e-bussa-alle-imprese/` | 200 | Nous Research vale 1,5 miliardi: Hermes esce dalla nicchia e bussa alle imprese |
| `/2026/10/venice-brucia-il-record-di-vvv-e-apre-le-porte-a-claude-haiku-5.5/` | 200 | Venice brucia il record di VVV e apre le porte a Claude Haiku 5.5 |

Cambio lingua bidirezionale confermato: ogni pagina inglese dichiara `hreflang=it-it` verso la pagina italiana corretta, e ogni pagina italiana dichiara `hreflang=en-us` verso la pagina inglese corretta.

## Note e cose non risolte

1. **403 con user-agent troncato.** Con il solo `-A "Mozilla/5.0"` tutte e sei le URL restituiscono `403`: è la sfida di Cloudflare (Bot Fight) al traffico da datacenter, già nota. Con lo user-agent da browser completo le pagine rispondono `200`. Non è un problema del sito.
2. **Percorsi italiani non deducibili dal nome file.** I permalink usano `/:year/:month/:title/` e `:title` è il titolo italiano slugificato (es. il file `2026-10-08-crypto-hormuz-btc.md` è servito a `/2026/10/bitcoin-sotto-83.000-dollari-hormuz-il-petrolio-e-il-ritorno-della-paura/`). Le URL italiane sono state ricavate leggendo `hreflang=it-it` dalle pagine inglesi.
3. Nessun problema rilevato fuori dai file `content/posts/*.en.md` e da questo report.
