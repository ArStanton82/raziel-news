# Pubblicazione straordinaria — articoli estemporanei del 2026-09-29

Run: 2026-09-30 (cron, profilo raziel-news) — pubblicazione una tantum fuori dalla pipeline a 4 stadi.
Repo: /root/.hermes/profiles/raziel-news/workspace/raziel-news (origin: ArStanton82/raziel-news, branch main).

## Esito

Tutti e tre gli articoli sono pubblicati, deployati e verificati online (HTTP 200).

### 1. Il settembre che non doveva esistere
- File: `content/posts/2026-09-29-bitcoin-settembre-stablecoin-ipo.md` (da `drafts/2026-09-29-bitcoin-settembre-stablecoin-ipo.md`, `draft: false`)
- URL verificata: https://raziel.news/2026/09/il-settembre-che-non-doveva-esistere/
- HTTP: **200** — H1 renderizzato una sola volta (valore 1)

### 2. ChatGPT entra nel portico di Hermes: l'identità diventa l'interfaccia
- File: `content/posts/2026-09-29-chatgpt-hermes-identita.md` (da `drafts/2026-09-29-chatgpt-hermes-identita.md`, `draft: false`)
- URL verificata: https://raziel.news/2026/09/chatgpt-entra-nel-portico-di-hermes-identita-diventa-linterfaccia/
- HTTP: **200** — H1 renderizzato una sola volta (valore 1); `<title>` corretto; riga "*Fonti verificate*" presente
- Nota: il permalink dedotto dal titolo con accento (`/2026/09/chatgpt-entra-nel-portico-di-hermes-lidentità-diventa-linterfaccia/`) rispondeva **404**. Dettagli e correzione nella sezione "Problema rilevato".

### 3. Venice, la settimana in cui il prezzo ha smesso di raccontare la storia
- File: `content/posts/2026-09-29-venice-gpt61-vvv-tokenomics.md` (da `drafts/2026-09-29-venice-gpt61-vvv-tokenomics.md`, `draft: false`)
- URL verificata: https://raziel.news/2026/09/venice-la-settimana-in-cui-il-prezzo-ha-smesso-di-raccontare-la-storia/
- HTTP: **200** — H1 renderizzato una sola volta (valore 1)

Frontmatter e corpo copiati dalle bozze senza modifiche; le tre bozze in `drafts/` non sono state toccate.

## Idempotenza

Nessuno dei tre file era già presente in `content/posts/` prima di questa run: pubblicati tutti e tre.
Gli articoli del 2026-09-29 della pipeline (`bitcoin-chiusura-massimo-istituzioni`, `hermes-nvidia-sicurezza-agenti`, `venice-sonnet-55-vvv-emissioni`) non sono stati modificati.

## Deploy (GitHub Actions "Deploy to GitHub Pages")

| Run | Evento | Commit | Esito |
|---|---|---|---|
| 36684185343 | push | 67367df `feat(posts): articoli estemporanei del 2026-09-29` | success |
| 36684935512 | workflow_dispatch (test diagnostico) | 67367df | success |
| 36685249724 | push | 4b12b74 `fix(posts): url ASCII per ChatGPT/Hermes (permalink accentato non servito)` | success |

Commit di pubblicazione: `67367dfbbf3e6c9981d9d918d49a45d2e8ef313e`
Commit di correzione: `4b12b7499d5881a3788acafcdf9ae9aa7f009b59`

## Problema rilevato e correzione (permalink con accento non servito)

L'articolo 2 ha una "à" nel titolo (`l'identità`), quindi Hugo generava il permalink `/2026/09/chatgpt-entra-nel-portico-di-hermes-lidentità-diventa-linterfaccia/`.

- Quell'URL, pur presente in `sitemap.xml` e in `index.json` e pur presente (verificato scaricando l'artefatto `github-pages` della run 36684185343) come cartella `2026/09/chatgpt-entra-nel-portico-di-hermes-lidentità-diventa-linterfaccia/index.html`, rispondeva **404** sia in `/` sia in `/index.html`.
- Non è un problema di cache (testato anche con query di cache-busting, `cf-cache-status: DYNAMIC`), né di codifica della richiesta (testate le forme `%C3%A0`, `%c3%a0`, NFD `a+U+0300`, byte UTF-8 grezzi: sempre 404), né del renderer Hugo (la pagina 404 del sito stesso elencava quel link).
- Controllo di comparazione: i permalink accentati pubblicati nelle run precedenti (`.../il-clarity-act-è-affondato-...`, `.../vvv-e-diem-venice-vende-capacità-...`, `.../il-gioco-è-fatto-...`) rispondono **200**.
- Un secondo deploy identico (`workflow_dispatch`, run 36684935512) non ha modificato l'esito: 404.

Correzione applicata (chirurgica, contenuto invariato): aggiunto `url:` ASCII nel frontmatter dell'articolo 2. Un semplice `slug:` non basta perché `hugo.yaml` definisce `permalinks.posts: "/:year/:month/:title/"` e ignora lo slug. Non è stata toccata nessuna impostazione globale (es. `removePathAccents`), che avrebbe cambiato retroattivamente le URL accentate già funzionanti.

Conseguenza: l'articolo 2 è pubblicato e raggiungibile all'URL ASCII indicata sopra (200); il percorso accentato derivato dal titolo non esiste più.

Nota per le prossime pubblicazioni: i titoli con accenti generano permalink che GitHub Pages non riesce a servire per i file nuovi di questo deploy; usare `url:` (o un titolo senza accenti nel permalink) prima del push.

<!-- estemporanei-status: 2026-09-30 complete -->
