# Traduzione inglese — 2026-10-18

Coda: 4 articoli italiani senza gemello `.en.md` (tutti del 2026-10-18). Tradotti tutti e 4, nessuno saltato (nessun `draft: true`, tutti sopra le 200 parole).

## Articoli tradotti

| Titolo italiano | Titolo inglese | Percorso inglese |
|---|---|---|
| Venice: Halloween, il festival Lumara e il burn che non si vede | Venice: Halloween, the Lumara festival and the burn nobody sees | `/en/2026/10/venice-halloween-the-lumara-festival-and-the-invisible-burn/` |
| Hermes 0.22.2: la release che ripara la release | Hermes 0.22.2: the release that fixes the release | `/en/2026/10/hermes-0222-the-release-that-fixes-the-release/` |
| La Francia tassa le stablecoin, l'OCC smonta il debanking: chi scrive le regole | France taxes stablecoins, the OCC dismantles debanking: who writes the rules | `/en/2026/10/france-taxes-stablecoins-occ-dismantles-debanking/` |
| Chi impara a giudicare | Who learns to judge | `/en/2026/10/who-learns-to-judge/` |

File creati: `content/posts/2026-10-18-venice-halloween-lumara.en.md`, `2026-10-18-hermes-v0222-community.en.md`, `2026-10-18-crypto-francia-stablecoin-occ.en.md`, `2026-10-18-chi-impara-a-giudicare.en.md`.

## Lingua dei link interni

`python3 scripts/lingua_link_inglesi.py --scrivi` eseguito prima del commit: 74 coppie it→en riconosciute, **0 link riscritti** (nessuno degli articoli di oggi conteneva link interni verso pagine italiane). Nessuna modifica da includere nel commit.

## Commit e deploy

- Commit `9184c0c` — `feat(i18n): versione inglese di 4 articoli (2026-10-18)` (4 file, 138 inserimenti), push su `main` riuscito.
- Workflow `deploy.yml` (run 39119629385, headSha `9184c0c`): `completed` / **success**.

## Verifiche dal vivo

Cloudflare (Bot Fight Mode) risponde a raffica alle richieste da datacenter con `403` e pagina di challenge JS: le prime curl sono state respinte così, non era un problema del sito. Ripetendo la richiesta con user-agent da browser e retry la pagina arriva con `200` e contenuto corretto. Verifica di controllo: anche un articolo vecchio e noto funzionante dà lo stesso `403` intermittente, quindi è comportamento noto dell'infrastruttura, non una regressione.

Pagine inglesi — tutte `200`:

| Percorso | HTTP | Titolo servito |
|---|---|---|
| `/en/2026/10/venice-halloween-the-lumara-festival-and-the-invisible-burn/` | 200 | Venice: Halloween, the Lumara festival and the burn nobody sees |
| `/en/2026/10/hermes-0222-the-release-that-fixes-the-release/` | 200 | Hermes 0.22.2: the release that fixes the release |
| `/en/2026/10/france-taxes-stablecoins-occ-dismantles-debanking/` | 200 | France taxes stablecoins, the OCC dismantles debanking: who writes the rules |
| `/en/2026/10/who-learns-to-judge/` | 200 | Who learns to judge |

Pagine italiane corrispondenti — tutte `200` e con il titolo italiano intatto:

| Percorso | HTTP | Titolo servito |
|---|---|---|
| `/2026/10/venice-halloween-il-festival-lumara-e-il-burn-che-non-si-vede/` | 200 | Venice: Halloween, il festival Lumara e il burn che non si vede |
| `/2026/10/hermes-0.22.2-la-release-che-ripara-la-release/` | 200 | Hermes 0.22.2: la release che ripara la release |
| `/2026/10/la-francia-tassa-le-stablecoin-locc-smonta-il-debanking-chi-scrive-le-regole/` | 200 | La Francia tassa le stablecoin, l'OCC smonta il debanking: chi scrive le regole |
| `/2026/10/chi-impara-a-giudicare/` | 200 | Chi impara a giudicare |

Cambio lingua verificato in entrambe le direzioni: ogni pagina italiana di oggi contiene il link al gemello `/en/...`, e ogni pagina inglese dichiara `hreflang=it-it` verso l'italiano e `hreflang=en-us` verso sé stessa.

Nota: i percorsi italiani non derivano dal nome del file ma dal `title` (in `hugo.yaml` i permalink sono `/:year/:month/:title/`), quindi gli URL italiani vanno letti dal titolo — per esempio `hermes-0.22.2-la-release-che-ripara-la-release`. I primi controlli a `/2026/10/hermes-v0222-community/` davano `404` per questo motivo, non per un errore di pubblicazione.

## Altro

- Verifica incrociata sull'artifact `github-pages` del run di deploy: tutti e quattro i file `index.html` inglesi e i quattro italiani sono presenti nel sito costruito.
- Nessun problema riscontrato fuori dai file di mia competenza; nessuna modifica fatta a script, layout, configurazione o immagini.
