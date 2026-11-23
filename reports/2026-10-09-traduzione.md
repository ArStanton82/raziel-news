# Traduzione inglese — 2026-10-09

## Coda

`content/posts/` conteneva **3 articoli italiani senza gemello `.en.md`**, tutti datati 2026-10-09. Erano gli unici in coda: nessun arretrato, nessun articolo forzato (limite di 6 non raggiunto). Tutti e tre hanno passato i controlli di ammissibilità (`draft: false`, oltre 200 parole), nessuno è stato saltato.

## Articoli tradotti (3)

| Titolo italiano | Titolo inglese | Percorso inglese |
|---|---|---|
| Bitcoin torna a 82.000 dollari, mentre le regole corrono su tre continenti | Bitcoin back to $82,000 while the rules race across three continents | `/en/2026/10/bitcoin-82000-rules-three-continents/` |
| Hermes esce dal terminale: Microsoft Store, plugin di catalogo e una release che si taglia da sola | Hermes leaves the terminal: Microsoft Store, catalog plugins and a release that cuts itself | `/en/2026/10/hermes-leaves-the-terminal-microsoft-store/` |
| Un wallet compra 15,97 milioni di VVV mentre Venice stringe la supply | A wallet buys $15.97 million of VVV as Venice tightens the supply | `/en/2026/10/wallet-buys-15-97m-vvv-venice-tightens-supply/` |

File creati:
- `content/posts/2026-10-09-crypto-regolamentazione-rimbalzo.en.md`
- `content/posts/2026-10-09-hermes-distribuzione-mainstream.en.md`
- `content/posts/2026-10-09-venice-vvv-deflazione-whale.en.md`

Frontmatter allineato all'italiano: stessa `date` (2026-10-09), `draft: false`, `categories` con i nomi inglesi (`Crypto`, `Blockchain`, `Hermes`, `AI`, `Venice.ai`), `tags` tradotti (nomi propri invariati: `hermes-agent`, `nous-research`, `venice`, `vvv`, `diem`), `url:` sotto `/en/` in ASCII minuscolo. Corpi con soli `##`, nessun `#`, riga finale `*Verified sources: ...*` con testate, link e date identici all'italiano.

## Link interni

`python3 scripts/lingua_link_inglesi.py --scrivi` eseguito prima del commit: **0 link riscritti in 0 articoli**. Nessuna modifica aggiuntiva da includere (i tre articoli del giorno non si rimandano link a vicenda).

## Commit e deploy

- Commit: `80d52ad` — `feat(i18n): versione inglese di 3 articoli (2026-10-09)` (3 file, 102 inserzioni).
- Push su `main`: `1528b43..80d52ad`, riuscito.
- GitHub Actions `deploy.yml`: **success** (run avviato alle 10:32 UTC, completato dopo circa 2 minuti). Nessun rilancio necessario.

## Verifica dal vivo

Tutte e 6 le pagine (3 inglesi + 3 italiane) rispondono **200** e mostrano il titolo corretto:

| Pagina | HTTP | Titolo letto dal vivo |
|---|---|---|
| `/2026/10/bitcoin-torna-a-82.000-dollari-mentre-le-regole-corrono-su-tre-continenti/` | 200 | Bitcoin torna a 82.000 dollari, mentre le regole corrono su tre continenti |
| `/en/2026/10/bitcoin-82000-rules-three-continents/` | 200 | Bitcoin back to $82,000 while the rules race across three continents |
| `/2026/10/hermes-esce-dal-terminale-microsoft-store-plugin-di-catalogo-e-una-release-che-si-taglia-da-sola/` | 200 | Hermes esce dal terminale: Microsoft Store, plugin di catalogo e una release che si taglia da sola |
| `/en/2026/10/hermes-leaves-the-terminal-microsoft-store/` | 200 | Hermes leaves the terminal: Microsoft Store, catalog plugins and a release that cuts itself |
| `/2026/10/un-wallet-compra-1597-milioni-di-vvv-mentre-venice-stringe-la-supply/` | 200 | Un wallet compra 15,97 milioni di VVV mentre Venice stringe la supply |
| `/en/2026/10/wallet-buys-15-97m-vvv-venice-tightens-supply/` | 200 | A wallet buys $15.97 million of VVV as Venice tightens the supply |

Cambio lingua verificato dal vivo in entrambe le direzioni (IT ↔ EN) e tag `hreflang` corretti (`it-it`, `en-us`, `x-default`). Le pagine italiane contengono ancora il titolo italiano.

## Note operative (nessuna correzione applicata)

- **Cloudflare Bot Fight sfida i curl "nudi".** Con il solo `-A "Mozilla/5.0"` tutte le URL — compresa la home e pagine già pubblicate da giorni — restituiscono **403 con `cf-mitigated: challenge`**. Il blocco è a livello di IP datacenter, non delle pagine nuove. Con un set completo di header da browser (`Accept`, `Accept-Language`, `Sec-Fetch-*`, `Upgrade-Insecure-Requests`) le stesse URL rispondono **200**. La verifica sopra è stata fatta in quel modo. Il comportamento è coerente con quanto già noto sulla zona; **non ho toccato la configurazione Cloudflare** (fuori dai miei file).
- Nessun problema riscontrato nel build Hugo locale (v0.154.5+extended): i tre percorsi inglesi e i tre italiani vengono generati come attesi.
- Nessun file fuori da `content/posts/*.en.md` è stato creato o modificato. Nessun file italiano toccato, nessun articolo già tradotto sovrascritto.
