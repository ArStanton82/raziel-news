# Traduzione inglese — 2026-10-24

## Coda
3 articoli senza gemello `.en.md` (tutti del 2026-10-24), sotto il limite di 6. Nessun `draft: true`, nessun articolo sotto le 200 parole: nessuno saltato. Dopo questo giro la coda è vuota.

## Articoli tradotti (3)

| Titolo italiano | Titolo inglese | Percorso inglese |
|---|---|---|
| La stablecoin scende allo sportello, il capitale esce dalla porta | Stablecoins Reach the Counter While Capital Slips Out the Door | /en/2026/10/stablecoins-reach-the-counter-while-capital-slips-out-the-door/ |
| L'agente si prende una macchina e una voce | The Agent Takes a Machine and a Voice | /en/2026/10/the-agent-takes-a-machine-and-a-voice/ |
| Kimi K3.1 Pro: aperto tra dieci giorni, anonimo da ieri | Kimi K3.1 Pro: Open in Ten Days, Anonymous Since Yesterday | /en/2026/10/kimi-k3-1-pro-open-in-ten-days-anonymous-since-yesterday/ |

Frontmatter allineato all'italiano per `date` (2026-10-24), `draft: false`; `categories` con i nomi inglesi, `tags` tradotti con i nomi propri intatti (`hermes`, `cua`, `kimi`, `moonshot`, `vvv`, `venice-ai` restano; `regolamentazione` → `regulation`, `voce` → `voice`, `agenti` → `agents`). Corpi senza H1, solo `##`. Riga fonti in fondo con etichetta `*Verified sources: ...*`, testate, link e date identici all'italiano. Nessun fatto, numero o giudizio aggiunto.

## Link interni
`python3 scripts/lingua_link_inglesi.py --scrivi` eseguito prima del commit: 92 coppie it→en riconosciute, **0 link riscritti** in 0 articoli (i tre pezzi non hanno link interni da rimappare). Nessuna modifica da includere nel commit oltre ai tre file.

## Commit e deploy
- Commit `073b83f` — `feat(i18n): versione inglese di 3 articoli (2026-10-24)`, 3 file, 102 inserzioni; push su `main` (`0e92f05..073b83f`).
- Workflow `deploy.yml`: **success** (ultima esecuzione collegata al commit). Nessun rilancio.

## Verifica dal vivo (UA browser, curl)
Pagine inglesi, tutte `200`:
- /en/2026/10/stablecoins-reach-the-counter-while-capital-slips-out-the-door/ → 200
- /en/2026/10/the-agent-takes-a-machine-and-a-voice/ → 200
- /en/2026/10/kimi-k3-1-pro-open-in-ten-days-anonymous-since-yesterday/ → 200

Pagine italiane, tutte `200` e con il titolo italiano intatto:
- /2026/10/la-stablecoin-scende-allo-sportello-il-capitale-esce-dalla-porta/ → 200, «La stablecoin scende allo sportello, il capitale esce dalla porta»
- /2026/10/lagente-si-prende-una-macchina-e-una-voce/ → 200, «L'agente si prende una macchina e una voce»
- /2026/10/kimi-k3.1-pro-aperto-tra-dieci-giorni-anonimo-da-ieri/ → 200, «Kimi K3.1 Pro: aperto tra dieci giorni, anonimo da ieri»

Accoppiamento bilingue confermato: ogni pagina italiana dichiara `<link rel=alternate hreflang=en-us>` verso il proprio URL inglese, e le inglesi il corrispondente `it-it`.

## Note
- Lo slug italiano del pezzo Kimi conserva il punto (`kimi-k3.1-pro-...`): il primo controllo, fatto con lo slug a trattini, ha dato 404. Lo slug reale è stato ricavato da `https://raziel.news/it/sitemap.xml`. L'URL inglese invece è a trattini, come richiesto dal brief. Non è un errore del sito, solo una cosa da ricordare in verifica: non dedurre gli URL italiani togliendo la punteggiatura, leggerli dal sitemap.
- Il `<title>` delle pagine inglesi riporta correttamente i titoli inglesi, senza prefisso di lingua.
- Nessun problema fuori dai file di mia competenza: niente da segnalare su layout, script o configurazione.
