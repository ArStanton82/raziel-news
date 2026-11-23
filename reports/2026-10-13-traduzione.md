# Traduzione inglese — 2026-10-13

Coda di partenza: 3 articoli italiani senza gemello `.en.md` (nessun arretrato: le esecuzioni precedenti avevano già tradotto tutto fino al 12 ottobre). Tradotti tutti e 3, sotto il limite di 6.

## Articoli tradotti

| Titolo italiano | Titolo inglese | Percorso inglese |
|---|---|---|
| Venice mette la privacy al centro, mentre i grandi holder alleggeriscono | Venice puts privacy first while large holders lighten up | `/en/2026/10/venice-privacy-unstaking-whale/` |
| Hermes, l'ecosistema cresce ai margini: connettori, skill e progetti della community | Hermes: the ecosystem grows at the edges — connectors, skills and community projects | `/en/2026/10/hermes-ecosistema-community/` |
| Bitcoin entra nelle banche e nei regolamenti: quando le regole inseguono il mercato | Bitcoin walks into banks and rulebooks: when regulation chases the market | `/en/2026/10/crypto-banche-regolamentazione/` |

Nessun articolo saltato: tutti e tre hanno `draft: false` e sono sopra le 200 parole (607, 650 e 666 parole).

## Commit e deploy

- Commit `67532bf` — `feat(i18n): versione inglese di 3 articoli (2026-10-13)`, 3 file, 98 inserimenti, solo `content/posts/*.en.md`.
- Push su `main` riuscito (`9d83907..67532bf`).
- `python3 scripts/lingua_link_inglesi.py --scrivi`: 58 coppie IT→EN riconosciute, **0 link interni riscritti** (nessuna modifica da includere nel commit).
- Workflow `deploy.yml`: `conclusion: success` sul commit `67532bf` (run creato alle 10:32 UTC, completato).

## Controlli dal vivo (13 ottobre 2026)

Tutte le pagine rispondono **200** e contengono il titolo atteso.

Pagine inglesi:
- `/en/2026/10/venice-privacy-unstaking-whale/` → 200, titolo inglese presente
- `/en/2026/10/hermes-ecosistema-community/` → 200, titolo inglese presente
- `/en/2026/10/crypto-banche-regolamentazione/` → 200, titolo inglese presente

Pagine italiane corrispondenti (invariate, titolo italiano ancora presente):
- `/2026/10/venice-mette-la-privacy-al-centro-mentre-i-grandi-holder-alleggeriscono/` → 200
- `/2026/10/hermes-lecosistema-cresce-ai-margini-connettori-skill-e-progetti-della-community/` → 200
- `/2026/10/bitcoin-entra-nelle-banche-e-nei-regolamenti-quando-le-regole-inseguono-il-mercato/` → 200

Abbinamento bilingue verificato in entrambe le direzioni: gli `alternate hreflang=it-it` / `hreflang=en-us` sono presenti e corretti su tutte e tre le coppie, e il selettore di lingua renderizzato (`layouts/partials/menu.html`) punta dalla pagina inglese alla pagina italiana giusta.

## Note e problemi riscontrati (non corretti: fuori dai miei file)

1. **403 di Cloudflare con la sola `-A "Mozilla/5.0"`.** Le prime chiamate di verifica hanno restituito 403 su *tutte* le URL, compresa una pagina vecchia sicuramente viva usata come controllo: è la Modalità Bot Fight che sfida il traffico da datacenter, non un problema delle pagine. Con un set di header da browser reale (user-agent completo + `Accept` + `Accept-Language`) le stesse URL rispondono 200. Segnalo perché la verifica standard del job (`curl -A "Mozilla/5.0"`) da questo IP è inaffidabile per costruzione.
2. **Gli URL italiani non derivano dal nome del file.** In `hugo.yaml` i permalink sono `posts: "/:year/:month/:title/"`, quindi lo slug italiano è il titolo slugificato, non il nome file: `/2026/10/bitcoin-entra-nelle-banche-e-nei-regolamenti-.../` e non `/2026/10/2026-10-13-crypto-banche-regolamentazione/`. Il primo giro di controllo aveva dato 404 solo per questo. Le pagine inglesi non sono toccate dal problema perché il campo `url:` esplicito vince sul permalink.
3. **`gh-pages`/origine GitHub Pages non è utilizzabile come verifica di riserva**: `https://arstanton82.github.io/raziel-news/...` risponde 301 verso `http://raziel.news/...` (redirect del dominio personalizzato, oltretutto in http).
4. `scripts/lingua_link_inglesi.py` salta `_index.en.md` perché non ha il campo `url:` — comportamento atteso, nessuna azione.
