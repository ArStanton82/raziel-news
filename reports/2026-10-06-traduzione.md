# Traduzione inglese — 2026-10-06

## Coda

Articoli italiani senza gemello `.en.md` trovati in `content/posts/`: **3** (tutti quelli del giorno).
Nessun arretrato: la coda era composta solo dagli articoli di oggi. Tutti `draft: false` e sopra le 200 parole — nessuno saltato.

## Articoli tradotti

| Titolo italiano | Titolo inglese | Percorso inglese |
|---|---|---|
| Hermes e il catalogo dei plugin: la fiducia si costruisce con un commit pinnato | Hermes and the plugin catalog: trust is built with a pinned commit | `/en/2026/10/hermes-plugin-catalog-trust-pinned-commit/` |
| Washington cambia marcia: il Tesoro ritira due regole, CFTC e SEC scrivono il manuale crypto | Washington shifts gear: the Treasury withdraws two rules while CFTC and SEC write the crypto manual | `/en/2026/10/washington-treasury-cftc-sec-crypto-rules/` |
| Flux 3 arriva su Venice, e VVV stringe la cinghia: meno emissioni, più burn | Flux 3 lands on Venice and VVV tightens its belt: fewer emissions, more burn | `/en/2026/10/flux-3-venice-vvv-emissions-burn/` |

File creati:
- `content/posts/2026-10-06-hermes-plugin-catalog-hardware.en.md`
- `content/posts/2026-10-06-crypto-treasury-cftc-sec.en.md`
- `content/posts/2026-10-06-venice-flux3-tokenomics.en.md`

Nessun altro file del repository toccato. I file italiani non sono stati modificati.

## Riscrittura dei link interni

`python3 scripts/lingua_link_inglesi.py --scrivi` eseguito prima del commit:

```
coppie italiano → inglese con percorso dichiarato: 36
versioni inglesi senza `url:` (saltate): _index.en.md
link interni riscritti: 0 in 0 articoli inglesi
```

Nessun link da correggere: i tre articoli non contengono link interni verso altri articoli.

## Commit e deploy

- Commit: `02ce399` — `feat(i18n): versione inglese di 3 articoli (2026-10-06)` (3 file, 92 inserimenti)
- Push su `main` riuscito (`d8ee1f9..02ce399`).
- Workflow `deploy.yml` sul commit `02ce39927c3780000da0cf6bfe2bc4d15c17fa3c`: **success** (prima `queued`, poi `completed`/`success`).

## Verifica dal vivo

Tutte le richieste con user-agent da browser (`Mozilla/5.0 (Windows NT 10.0; Win64; x64) ... Chrome/128.0`).

Versioni inglesi (HTTP 200 e titolo inglese corretto):

| URL | HTTP | Titolo |
|---|---|---|
| `https://raziel.news/en/2026/10/hermes-plugin-catalog-trust-pinned-commit/` | 200 | Hermes and the plugin catalog: trust is built with a pinned commit |
| `https://raziel.news/en/2026/10/washington-treasury-cftc-sec-crypto-rules/` | 200 | Washington shifts gear: the Treasury withdraws two rules while CFTC and SEC write the crypto manual |
| `https://raziel.news/en/2026/10/flux-3-venice-vvv-emissions-burn/` | 200 | Flux 3 lands on Venice and VVV tightens its belt: fewer emissions, more burn |

Versioni italiane corrispondenti (HTTP 200 e titolo italiano intatto):

| URL | HTTP | Titolo |
|---|---|---|
| `/2026/10/hermes-e-il-catalogo-dei-plugin-la-fiducia-si-costruisce-con-un-commit-pinnato/` | 200 | Hermes e il catalogo dei plugin: la fiducia si costruisce con un commit pinnato |
| `/2026/10/washington-cambia-marcia-il-tesoro-ritira-due-regole-cftc-e-sec-scrivono-il-manuale-crypto/` | 200 | Washington cambia marcia: il Tesoro ritira due regole, CFTC e SEC scrivono il manuale crypto |
| `/2026/10/flux-3-arriva-su-venice-e-vvv-stringe-la-cinghia-meno-emissioni-più-burn/` | 200 | Flux 3 arriva su Venice, e VVV stringe la cinghia: meno emissioni, più burn |

Cambio lingua bidirezionale confermato: `hreflang=it-it` sulle pagine inglesi punta alla pagina italiana giusta, e `hreflang=en-us` sulla pagina italiana punta alla pagina inglese giusta.

## Note e cose non risolte

1. **403 con user-agent troncato.** Con il solo `-A "Mozilla/5.0"` tutte e sei le URL restituiscono `403`: è la sfida di Cloudflare (Bot Fight) al traffico da datacenter, già nota. Con uno user-agent da browser completo le pagine rispondono `200`. Non è un problema del sito; se il job gira con l'UA corto, la verifica fallisce per falso negativo.
2. **`sitemap.xml` non elenca gli articoli di ottobre.** `https://raziel.news/it/sitemap.xml` e `/en/sitemap.xml` si fermano a settembre (più i pezzi di maggio), pur con `lastmod` al 2026-10-06, e non contengono nessuno degli articoli di ottobre già pubblicati. Sembra una copia in cache di Cloudflare o un problema del template del sitemap. **Fuori dai miei file: non corretto, solo segnalato.**
3. **Slug italiani derivati dal titolo.** I permalink usano `/:year/:month/:title/` e `:title` è il titolo italiano slugificato, non il nome del file. Gli URL italiani non sono quindi deducibili dal nome file; per la verifica ho letto `hreflang=it-it` dalle pagine inglesi. Nessuna azione richiesta, è solo una nota operativa.
4. `reports/` contiene molti file non tracciati da giorni precedenti (non committati): non li ho toccati.
