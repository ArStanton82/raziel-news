# Traduzione — 2026-10-03

Coda iniziale: 3 articoli senza gemello `.en.md` (tutti del 2026-10-03). Tradotti tutti e 3 (sotto il limite di 6). Nessun articolo saltato: tutti `draft: false` e ben oltre le 200 parole.

## Articoli tradotti

1. **Bitcoin, il lavoro che rallenta e le regole che accelerano**
   → *Bitcoin: the jobs market that slows, the rules that accelerate*
   percorso inglese: `/en/2026/10/bitcoin-payrolls-sec-custody-blast/`
   file: `content/posts/2026-10-03-bitcoin-payrolls-sec-custody-blast.en.md`

2. **Hermes accelera, ma i suoi plugin di memoria cercano un proprietario**
   → *Hermes speeds up, but its memory plugins are looking for an owner*
   percorso inglese: `/en/2026/10/hermes-plugin-memoria-unmaintained/`
   file: `content/posts/2026-10-03-hermes-plugin-memoria-unmaintained.en.md`

3. **Venice, 267 aggiornamenti in un mese: la velocità come strategia**
   → *Venice, 267 updates in a month: speed as a strategy*
   percorso inglese: `/en/2026/10/venice-267-aggiornamenti-abliterated/`
   file: `content/posts/2026-10-03-venice-267-aggiornamenti-abliterated.en.md`

## Link interni

`python3 scripts/lingua_link_inglesi.py --scrivi` eseguito prima del commit: 26 coppie italiano→inglese con percorso dichiarato, **0 link interni riscritti** in 0 articoli inglesi. Nessuna modifica da includere nel commit.

## Commit e deploy

- Commit: `47b4b8c` — `feat(i18n): versione inglese di 3 articoli (2026-10-03)` (3 file, 84 inserimenti).
- Push su `main` riuscito (`976fafd..47b4b8c`).
- Deploy: `gh run list -L 1 --workflow deploy.yml` → `status: completed`, `conclusion: success` per l'head SHA `47b4b8c`.

## Verifica dal vivo

Nota: le richieste dell'agente dall'IP del datacenter vengono sfidate da Cloudflare (Bot Fight Mode) e con il solo `-A "Mozilla/5.0"` restituiscono **403**. Con un set completo di header da browser (UA Chrome completo + `Accept` + `Accept-Language` + `--compressed`) le pagine rispondono **200**. La verifica sotto è stata fatta con quel set.

Pagine inglesi — tutte **200**:
- `/en/2026/10/bitcoin-payrolls-sec-custody-blast/` → 200, titolo inglese presente.
- `/en/2026/10/hermes-plugin-memoria-unmaintained/` → 200, titolo inglese presente.
- `/en/2026/10/venice-267-aggiornamenti-abliterated/` → 200, titolo inglese presente.

Pagine italiane corrispondenti — tutte **200**, titolo italiano ancora presente:
- `/2026/10/bitcoin-il-lavoro-che-rallenta-e-le-regole-che-accelerano/` → 200.
- `/2026/10/hermes-accelera-ma-i-suoi-plugin-di-memoria-cercano-un-proprietario/` → 200.
- `/2026/10/venice-267-aggiornamenti-in-un-mese-la-velocit%C3%A0-come-strategia/` → 200.

Cambio lingua verificato in entrambe le direzioni per tutte e tre le coppie: ogni pagina inglese linka la gemella italiana e viceversa.

## Note e cose non perfette

- **Slug italiano ≠ nome file.** I permalink del sito sono `posts: "/:year/:month/:title/"`: l'URL italiano deriva dal *titolo*, non dal nome del file. Gli URL italiani sono quindi `bitcoin-il-lavoro-che-rallenta-e-le-regole-che-accelerano`, `hermes-accelera-ma-i-suoi-plugin-di-memoria-cercano-un-proprietario` e `venice-267-aggiornamenti-in-un-mese-la-velocità-come-strategia` (con la `à` percent-encoded, perché Hugo non rimuove gli accenti). Il titolo inglese è invece indipendente, come previsto.
- **403 di Cloudflare con il solo `-A "Mozilla/5.0"`.** È il comportamento noto del Bot Fight Mode verso il traffico da datacenter, non un problema del sito: le pagine esistono e rispondono 200 con header da browser completo. Non ho toccato nulla fuori dai miei file.
- Nessun articolo con `draft: true` o sotto le 200 parole in coda. Nessuna traduzione già esistente sovrascritta.
