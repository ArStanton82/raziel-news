# Traduzione inglese — 2026-10-17

Coda: 3 articoli (sotto il tetto di 6). Tutti tradotti, nessuno saltato.

## Articoli tradotti

| Titolo italiano | Titolo inglese | Percorso inglese |
|---|---|---|
| Le stablecoin escono dal laboratorio, le regole arrivano dopo | Stablecoins leave the lab, the rules arrive later | `/en/2026/10/stablecoins-leave-the-lab-rules-arrive-later/` |
| Hermes 0.22.2: la release che ammette di essere un errore corretto | Hermes 0.22.2: the release that admits it is a corrected mistake | `/en/2026/10/hermes-0-22-2-the-release-that-admits-it-is-a-corrected-mistake/` |
| Venice: un burn record, un prezzo nervoso e un festival che arriva | Venice: a record burn, a nervous price and a festival on the way | `/en/2026/10/venice-a-record-burn-a-nervous-price-and-a-festival-on-the-way/` |

Nessun articolo con `draft: true` o sotto le 200 parole in coda.

## Deploy

Commit `959759d` — `feat(i18n): versione inglese di 3 articoli (2026-10-17)`, pushato su `main` (3 file, 83 inserzioni).
`scripts/lingua_link_inglesi.py --scrivi` eseguito prima del commit: 70 coppie IT→EN note, **0 link interni riscritti** (nessuna delle tre coppie di oggi ha link incrociati da correggere).

`gh run list -L 1 --workflow deploy.yml` → `status: completed`, `conclusion: success`, `headSha: 959759d2beb427aa81fadfacc87ca2220860e1ef`. Nessun rilancio necessario.

## Controlli dal vivo

La verifica diretta su `https://raziel.news<percorso>/` con `curl -A "Mozilla/5.0"` dall'IP dell'agente restituisce **403 su tutte le URL, incluse quelle italiane note e già funzionanti**: è la Bot Fight Mode di Cloudflare che sfida il traffico da datacenter, non un problema delle pagine. Verifica quindi eseguita in due modi alternativi, che danno lo stesso risultato:

1. `curl -sk --resolve raziel.news:443:185.199.108.153` (connessione diretta all'origin GitHub Pages, aggirando Cloudflare). Il certificato servito in questo modo è `*.github.io`, perché il certificato del dominio personalizzato non è provisionato per connessioni dirette all'origin — di qui il `-k`.
2. Lettura della pagina renderizzata tramite fetch esterno (IP non datacenter).

Esiti (tutti `200`):

- `/en/2026/10/stablecoins-leave-the-lab-rules-arrive-later/` → 200, titolo e corpo inglesi corretti
- `/en/2026/10/hermes-0-22-2-the-release-that-admits-it-is-a-corrected-mistake/` → 200, titolo e corpo inglesi corretti
- `/en/2026/10/venice-a-record-burn-a-nervous-price-and-a-festival-on-the-way/` → 200, titolo e corpo inglesi corretti
- `/2026/10/le-stablecoin-escono-dal-laboratorio-le-regole-arrivano-dopo/` → 200, titolo italiano presente
- `/2026/10/hermes-0.22.2-la-release-che-ammette-di-essere-un-errore-corretto/` → 200, titolo italiano presente
- `/2026/10/venice-un-burn-record-un-prezzo-nervoso-e-un-festival-che-arriva/` → 200, titolo italiano presente

Cambio lingua verificato su tutte e tre le coppie: ogni pagina dichiara `hreflang=it-it`, `hreflang=en-us` e `x-default` verso la controparte corretta, e il selettore IT/EN nell'header punta all'URL giusto in entrambe le direzioni.

## Note e cose non risolte

- **Gli URL italiani non derivano dal nome del file**: `hugo.yaml` ha `permalinks: posts: "/:year/:month/:title/"`, quindi lo slug italiano è costruito dal titolo (es. `hermes-0.22.2-la-release-che-ammette-di-essere-un-errore-corretto`, con il punto in `0.22.2`). Il primo tentativo di controllo sugli URL ricavati dal nome file ha dato 404: era un mio errore di costruzione dell'URL, non un problema del sito.
- **Fuori dal mio perimetro, non corretto**: nello `git status` della workdir risultano molti file non tracciati che non appartengono a questo job — decine di `reports/*.md` e `reports/raw-*/`, più una serie di script in `scripts/` (`build_report_2026_10_17.py`, `card_popart.py`, `echo_extract.py`, `extract_x_2026_10_14.py`, `extract_x_2026_10_17.py`, `one_x_2026_10_17.py`, `parse_echo.py`, `verify_echo.py`, `verify_metrics_*.py`, `verify_report_*.py`) e `static/images/card-bg/`. Segnalo soltanto: non li ho toccati, aggiunti o committati, e il commit di oggi contiene solo i tre `.en.md`.
- Il 403 di Cloudflare sugli IP datacenter resta un attrito noto per le verifiche automatiche; non incide su Googlebot né sui visitatori reali.
