# Traduzione inglese — 2026-10-16

## Coda

Articoli italiani senza gemello `.en.md`: **3**, tutti tradotti in questa esecuzione (limite 6 non raggiunto, coda esaurita).

## Articoli tradotti

| Titolo italiano | Titolo inglese | Percorso inglese | Percorso italiano |
|---|---|---|---|
| Venice, la settimana dei modelli di frontiera | Venice's week of frontier models | `/en/2026/10/venice-frontiera-muse-hy4-vvv/` | `/2026/10/venice-la-settimana-dei-modelli-di-frontiera/` |
| Hermes Agent v0.22.2: la patch che riapre la porta d'ingresso | Hermes Agent v0.22.2: the patch that reopens the front door | `/en/2026/10/hermes-v0222-plugin-nemotron/` | `/2026/10/hermes-agent-v0.22.2-la-patch-che-riapre-la-porta-dingresso/` |
| Il muro degli 80.000 dollari | The 80,000-dollar wall | `/en/2026/10/crypto-btc-80k-msci-stablecoin/` | `/2026/10/il-muro-degli-80.000-dollari/` |

Nessun articolo saltato: tutti e tre hanno `draft: false` e superano abbondantemente le 200 parole. Nessun `.en.md` preesistente è stato sovrascritto.

Nota sui percorsi: gli articoli italiani non hanno `url:` nel frontmatter e Hugo genera il permalink dal titolo (`/2026/10/il-muro-degli-80.000-dollari/`), mentre i file inglesi portano `url: "/en/<anno>/<mese>/<slug>/"` come da regola. Le due versioni risultano correttamente appaiate dal sito (verificato sotto).

## Commit e deploy

- Commit: `c4a2d9a` — `feat(i18n): versione inglese di 3 articoli (2026-10-16)`, 3 file creati, 86 inserzioni.
- Push su `main`: riuscito (`fc01484..c4a2d9a`).
- `python3 scripts/lingua_link_inglesi.py --scrivi` eseguito **prima** del commit: 67 coppie italiano→inglese note, **0 link interni riscritti** in 0 articoli (`_index.en.md` saltato perché senza `url:`). Nessuna modifica da includere.
- GitHub Actions `deploy.yml` sul commit `c4a2d9af94fd43c0f3782d82cd273f3374612eaa`: **success** (prima lettura `in_progress`, confermato `completed`/`success` al controllo successivo).

## Verifica dal vivo

Metodo: `curl` con set di intestazioni da browser completo (`Accept`, `Accept-Language`, `Sec-Fetch-Mode/Dest`, HTTP/1.1). Con il solo `-A "Mozilla/5.0"` il sito risponde **403 con `cf-mitigated: challenge`** dall'IP datacenter di questa macchina: è il comportamento noto della Modalità Bot Fight di Cloudflare, sta fuori dai miei file e non è stato corretto. Aggiungendo le intestazioni di navigazione le pagine rispondono regolarmente.

| URL | HTTP |
|---|---|
| `/en/2026/10/venice-frontiera-muse-hy4-vvv/` | 200 |
| `/en/2026/10/hermes-v0222-plugin-nemotron/` | 200 |
| `/en/2026/10/crypto-btc-80k-msci-stablecoin/` | 200 |
| `/2026/10/venice-la-settimana-dei-modelli-di-frontiera/` | 200 |
| `/2026/10/hermes-agent-v0.22.2-la-patch-che-riapre-la-porta-dingresso/` | 200 |
| `/2026/10/il-muro-degli-80.000-dollari/` | 200 |

Titoli italiani ancora presenti sulle pagine italiane (dal `<title>` live):
- `Venice, la settimana dei modelli di frontiera :: Raziel.news`
- `Hermes Agent v0.22.2: la patch che riapre la porta d'ingresso :: Raziel.news`
- `Il muro degli 80.000 dollari :: Raziel.news`

Titoli inglesi sulle pagine `/en/`: `Venice's week of frontier models`, `Hermes Agent v0.22.2: the patch that reopens the front door`, `The 80,000-dollar wall` — `h1` presente e corpo completo (verificato anche il testo integrale, incluse le sezioni `##` e la riga finale `*Verified sources: ...*`).

Cambio lingua: appaiamento confermato in entrambe le direzioni. Sulla pagina italiana compare `hreflang="en-us"` → URL inglese e il link allo switch `hreflang="en"`; sulla pagina inglese `hreflang="it-it"` → URL italiano e switch `hreflang="it"`. Presenti anche `hreflang="x-default"` verso la versione italiana.

## Note di scrittura

- Frontmatter allineato all'italiano: stessa `date` (2026-10-16), `draft: false`, titolo e `summary` riscritti in inglese, `categories` con i nomi inglesi (`Venice.ai`/`AI`, `Hermes`/`AI`, `Crypto`/`Blockchain`), `tags` tradotti lasciando i nomi propri invariati (`venice-ai`, `vvv`, `bitcoin`, `usdc`, `mica`, `zkevm`, `hermes-agent`, `nous-research`, `nemotron`, `open-source`, ...).
- Corpo senza alcun titolo `#`: solo `##`, come richiesto.
- Nessun fatto, numero o giudizio aggiunto: cifre, nomi e cautele dell'italiano (comprese le accuse non confermate su VVV e il «problema noto dichiarato» di v0.22.2) restano identici e altrettanto prudenti.
- La riga delle fonti resta in fondo dopo `---`, con etichetta inglese `*Verified sources: ...*` e testate/link/date invariati.

## Problemi riscontrati

- Nessun problema dentro i file di mia competenza.
- Unico rilievo, fuori dai miei file e **non corretto**: il 403 Cloudflare sui `curl` con user-agent nudo dall'IP datacenter (`cf-mitigated: challenge`). Documentato nella skill `hugo-editorial` → `references/cloudflare-diagnosi-crawler.md`; riguarda anche `/sitemap.xml` (403). La verifica è stata quindi eseguita con intestazioni di navigazione complete, che passano.
