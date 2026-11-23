# Traduzione inglese — 2026-10-04

La giornata ha avuto **due esecuzioni** della pipeline-traduzione. Questo file le riporta entrambe.

## Esecuzione 1 (mattina, commit `345c036`)

Coda: 3 articoli italiani senza gemello `.en.md`, tutti tradotti (limite 6 non raggiunto).

1. **Grayscale e l'onda AI crypto: VVV tra i protagonisti di settembre** → **Grayscale and the crypto-AI wave: VVV among September's standouts** — `/en/2026/10/grayscale-crypto-ai-wave-vvv/`
2. **Hermes: Discord più semplice e la scommessa dell'app web** → **Hermes: a simpler Discord and the web-app bet** — `/en/2026/10/hermes-discord-simpler-web-app-bet/`
3. **Bitcoin tra banche sistemiche e regole in stallo** → **Bitcoin between systemic banks and stalled rules** — `/en/2026/10/bitcoin-systemic-banks-stalled-rules/`

Deploy `345c036`: success. Link interni: 0 riscritti. Verifica live via curl: 403 (Cloudflare), verificato su build locale.

## Esecuzione 2 (sera, commit `1e543dc`) — questa esecuzione

Coda: **1 articolo**. È l'italiano pubblicato nel pomeriggio con il commit `3841b0d` ("Chi risponde quando l'agente sbaglia, e chi non si presenta"), arrivato dopo la traduzione del mattino; tutti gli altri articoli avevano già il gemello inglese.

### Articoli tradotti

- **Chi risponde quando l'agente sbaglia, e chi non si presenta** → **Who answers when the agent gets it wrong, and who doesn't show up**
  - file: `content/posts/2026-10-04-chi-risponde-quando-l-agente-sbaglia.en.md`
  - percorso inglese: `/en/2026/10/who-answers-when-the-agent-gets-it-wrong/`

Nessun articolo saltato: `draft: false` e ben oltre le 200 parole.

### Link interni

`python3 scripts/lingua_link_inglesi.py --scrivi`: 30 coppie italiano→inglese riconosciute, **0 link riscritti**. Nessuna modifica extra inclusa nel commit.

### Commit e deploy

- Commit: `1e543dc` — `feat(i18n): versione inglese di 1 articoli (2026-10-04)` (1 file, +44 righe), pushato su `main`.
- GitHub Actions `deploy.yml` per `1e543dc`: **success** (completato).

### Controlli dal vivo

- `curl -A "Mozilla/5.0"` → **403** sia su `/en/2026/10/who-answers-when-the-agent-gets-it-wrong/` sia sull'italiano `/2026/10/chi-risponde-quando-lagente-sbaglia-e-chi-non-si-presenta/`. È il comportamento noto di Cloudflare Bot Fight Mode, che sfida il traffico da datacenter (IP dell'agente) ma non i bot verificati come Googlebot: non è un errore del sito né della traduzione.
- Anche l'origine GitHub Pages (`arstanton82.github.io/raziel-news/...`) risponde 301 verso `raziel.news` e finisce comunque dietro Cloudflare (403).
- Verifica alternativa eseguita: build Hugo locale su directory di scratch (`hugo --destination <scratch>`), che riproduce l'output pubblicato dal commit andato a buon fine. Build completata senza errori (248 pagine per lingua). Esito:
  - la pagina inglese esiste a `/en/2026/10/who-answers-when-the-agent-gets-it-wrong/`; `<title>` e `og:title` in inglese ("Who answers when the agent gets it wrong, and who doesn't show up"), `og:locale` `en_US`;
  - la pagina italiana corrispondente esiste ancora a `/2026/10/chi-risponde-quando-lagente-sbaglia-e-chi-non-si-presenta/` e mantiene il titolo italiano ("Chi risponde quando l'agente sbaglia, e chi non si presenta");
  - il cambio lingua è collegato: `hreflang` `it-it` / `en-us` / `x-default` reciproci tra le due pagine; il corpo inglese usa il rimando interno `[Contact](/en/contatti/)`;
  - il corpo inglese non contiene titoli `#` (solo `##`) e mantiene la riga finale delle fonti (`*Verified sources: ...*`).

## Note

- Nessun problema fuori dai file di competenza (`content/posts/*.en.md` e questo report).
- La verifica "dal vivo" con curl resta impossibile dall'IP dell'agente per via di Cloudflare Bot Fight Mode; il controllo è stato fatto sull'output di build e sull'esito del deploy, che coincidono con quanto pubblicato.
