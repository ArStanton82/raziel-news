# Traduzione inglese — 2026-10-10

## Coda

`content/posts/` conteneva **3 articoli italiani senza gemello `.en.md`**, tutti datati 2026-10-10. Erano gli unici in coda: nessun arretrato, nessun articolo forzato (limite di 6 non raggiunto). Tutti e tre hanno passato i controlli di ammissibilità (`draft: false`, oltre 200 parole), nessuno è stato saltato.

## Articoli tradotti (3)

| Titolo italiano | Titolo inglese | Percorso inglese |
|---|---|---|
| La regolamentazione diventa infrastruttura: Thailandia, ESMA e SEC ridisegnano il perimetro crypto | Regulation becomes infrastructure: Thailand, ESMA and the SEC redraw the crypto perimeter | `/en/2026/10/crypto-regulation-becomes-infrastructure/` |
| Un modello da 600 miliardi gratis nell'agente: la settimana in cui Hermes fa i conti con la propria scala | A 600-billion-parameter model free inside the agent: the week Hermes reckons with its own scale | `/en/2026/10/hermes-reckons-with-its-own-scale/` |
| Venice spinge sull'agente: chat multi-passo, modelli di frontiera a basso costo e un token che si restringe | Venice bets on the agent: multi-step chat, cheap frontier models and a token that shrinks | `/en/2026/10/venice-bets-on-the-agent-shrinking-token/` |

File creati:
- `content/posts/2026-10-10-crypto-regolamentazione-ledger.en.md`
- `content/posts/2026-10-10-hermes-step5-kanban.en.md`
- `content/posts/2026-10-10-venice-agentic-chat-vvv.en.md`

Frontmatter allineato all'italiano: stessa `date` (2026-10-10), `draft: false`, `categories` con i nomi inglesi (`Crypto`, `Blockchain`, `Hermes`, `AI`, `Venice.ai`), `tags` tradotti (nomi propri invariati: `hermes-agent`, `stepfun`, `step-5-preview`, `nous-portal`, `kanban`, `venice-ai`, `vvv`, `esma`, `sec`, `mica`, `ledger`), `url:` sotto `/en/` in ASCII minuscolo. Corpi con soli `##`, nessun `#`, riga finale `*Verified sources: ...*` con testate, link e date identici all'italiano.

## Link interni

`python3 scripts/lingua_link_inglesi.py --scrivi` eseguito prima del commit: **0 link riscritti in 0 articoli** (48 coppie it→en riconosciute, `_index.en.md` saltato perché privo di `url:`). Nessuna modifica aggiuntiva da includere nel commit.

## Commit e deploy

- Commit: `b6f604d` — `feat(i18n): versione inglese di 3 articoli (2026-10-10)` (3 file, 94 inserzioni).
- Push su `main`: `b7e3f73..b6f604d`, riuscito.
- GitHub Actions `deploy.yml`: **success** (run su `b6f604dca14694912ec4145eed3554e7959e8346`, completato dopo circa 2 minuti). Nessun rilancio necessario.

## Verifica dal vivo

Tutte e 6 le pagine (3 inglesi + 3 italiane) rispondono **200** e mostrano il titolo corretto:

| Pagina | HTTP | Titolo letto dal vivo |
|---|---|---|
| `/2026/10/la-regolamentazione-diventa-infrastruttura-thailandia-esma-e-sec-ridisegnano-il-perimetro-crypto/` | 200 | La regolamentazione diventa infrastruttura: Thailandia, ESMA e SEC ridisegnano il perimetro crypto |
| `/en/2026/10/crypto-regulation-becomes-infrastructure/` | 200 | Regulation becomes infrastructure: Thailand, ESMA and the SEC redraw the crypto perimeter |
| `/2026/10/un-modello-da-600-miliardi-gratis-nellagente-la-settimana-in-cui-hermes-fa-i-conti-con-la-propria-scala/` | 200 | Un modello da 600 miliardi gratis nell'agente: la settimana in cui Hermes fa i conti con la propria scala |
| `/en/2026/10/hermes-reckons-with-its-own-scale/` | 200 | A 600-billion-parameter model free inside the agent: the week Hermes reckons with its own scale |
| `/2026/10/venice-spinge-sullagente-chat-multi-passo-modelli-di-frontiera-a-basso-costo-e-un-token-che-si-restringe/` | 200 | Venice spinge sull'agente: chat multi-passo, modelli di frontiera a basso costo e un token che si restringe |
| `/en/2026/10/venice-bets-on-the-agent-shrinking-token/` | 200 | Venice bets on the agent: multi-step chat, cheap frontier models and a token that shrinks |

Le pagine italiane contengono ancora il titolo italiano e il testo italiano. Cambio lingua verificato dal vivo in entrambe le direzioni su un campione (la pagina inglese linka lo slug italiano e viceversa), con tag `hreflang` presenti nell'head.

## Note operative (nessuna correzione applicata)

- **Cloudflare Bot Fight sfida i curl "nudi".** Con il solo `-A "Mozilla/5.0"` tutte le URL, comprese pagine pubblicate da giorni, restituiscono **403**. Con un set completo di header da browser (`Accept`, `Accept-Language`, `Sec-Fetch-*`, `Upgrade-Insecure-Requests`) le stesse URL rispondono **200**: è il comportamento noto della zona verso gli IP da datacenter, non un problema delle pagine nuove. La verifica sopra è stata fatta in quel modo e incrociata con una lettura indipendente delle pagine (titolo e corpo resi correttamente). Non ho toccato la configurazione Cloudflare (fuori dai miei file).
- **Lo slug italiano non deriva dal nome del file.** I permalink italiani sono costruiti dal titolo, non dal nome file: `/2026/10/<slug-del-titolo>/`. Un primo controllo costruito sullo slug del filename (`/2026/10/venice-agentic-chat-vvv/`) dava 404 — è il comportamento normale del sito, non un errore introdotto da questa esecuzione. Gli URL italiani sopra sono quelli reali, presi dalla pagina 404 del sito stesso.
- L'accesso all'origine `arstanton82.github.io/raziel-news/...` risponde **301** (redirect al dominio personalizzato): atteso, nessuna azione.
- Nessun problema riscontrato nel build Hugo: i tre percorsi inglesi e i tre italiani vengono generati come attesi.
- Nessun file fuori da `content/posts/*.en.md` è stato creato o modificato. Nessun file italiano toccato, nessun articolo già tradotto sovrascritto.
