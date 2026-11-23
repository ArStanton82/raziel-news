# Traduzione — 2026-10-11

Coda di partenza: 4 articoli italiani senza gemello inglese (tutti datati 2026-10-11).
Tradotti: 4. Coda residua: 0. Nessun articolo saltato (nessun `draft: true`, nessuno sotto le 200 parole).

## Articoli tradotti

1. «VVV sbarca su Solana mentre le emissioni crollano: la scommessa deflazionaria di Venice»
   → "VVV lands on Solana as emissions collapse: Venice's deflationary bet"
   percorso inglese: `/en/2026/10/vvv-lands-on-solana-emissions-collapse-venice-deflationary-bet/`
   file: `content/posts/2026-10-11-venice-vvv-solana-deflazione.en.md`

2. «Nous Research vale 1,5 miliardi: Hermes esce dall'open source e va in azienda»
   → "Nous Research is worth $1.5 billion: Hermes leaves open source for the enterprise"
   percorso inglese: `/en/2026/10/nous-research-1-5-billion-hermes-leaves-open-source/`
   file: `content/posts/2026-10-11-hermes-series-b-business.en.md`

3. «L'Europa stringe sui stablecoin, l'Asia apre agli ETF: la regolamentazione accelera»
   → "Europe tightens the rules on stablecoins, Asia opens the door to ETFs: regulation accelerates"
   percorso inglese: `/en/2026/10/europe-tightens-stablecoins-asia-opens-etfs/`
   file: `content/posts/2026-10-11-crypto-regolamentazione-sicurezza.en.md`

4. «Chi decide chi muore, e chi risponde»
   → "Who decides who dies, and who answers for it"
   percorso inglese: `/en/2026/10/who-decides-who-dies-and-who-answers/`
   file: `content/posts/2026-10-11-chi-decide-chi-muore-e-chi-risponde.en.md`

Frontmatter: stessi campi e stessa `date` dell'italiano, `draft: false`, titolo e summary in inglese,
`categories` con i nomi inglesi (Philosophy of AI per "Filosofia dell'AI"), `tags` tradotti lasciando
i nomi propri (Hermes, Venice.ai, Bitcoin, Vitalik Buterin), `url:` sotto `/en/`. Il corpo non contiene
titoli `#`. La riga delle fonti resta in fondo dopo il `---` con l'etichetta `*Verified sources: ...*`;
testate, link e date sono identici all'italiano.

## Link interni

`python3 scripts/lingua_link_inglesi.py --scrivi` eseguito prima del commit: 52 coppie it→en mappate,
**0 link riscritti, 0 file toccati** (nessun articolo nuovo rimanda a pagine italiane con gemello inglese).
Il link a [Contatti] del quarto articolo è stato scritto direttamente come `[Contact](/en/contatti/)`.

## Commit e deploy

- commit `5044b3d` — `feat(i18n): versione inglese di 4 articoli (2026-10-11)`, 4 file, 146 righe aggiunte;
  `git add content/posts` + push su `main`. Nessun altro file del repository toccato.
- GitHub Actions `deploy.yml` sul commit `5044b3d`: **success** (completato 2026-10-11T10:36:38Z).

## Controlli dal vivo

`curl -A "Mozilla/5.0"` verso raziel.news ha restituito **403 su tutte e otto le URL**, incluse le quattro
italiane: è la sfida di Cloudflare Bot Fight Mode contro il traffico da datacenter (IP dell'agente),
non un problema delle pagine. Verifica rifatta con lo strumento di estrazione contenuti (richiesta HTTP
reale): **tutte e 8 le pagine rispondono 200 e mostrano il contenuto giusto**.

| Pagina | Esito |
|---|---|
| `/en/2026/10/vvv-lands-on-solana-emissions-collapse-venice-deflationary-bet/` | 200, titolo inglese corretto |
| `/en/2026/10/nous-research-1-5-billion-hermes-leaves-open-source/` | 200, titolo inglese corretto |
| `/en/2026/10/europe-tightens-stablecoins-asia-opens-etfs/` | 200, titolo inglese corretto |
| `/en/2026/10/who-decides-who-dies-and-who-answers/` | 200, titolo inglese corretto |
| `/2026/10/vvv-sbarca-su-solana-mentre-le-emissioni-crollano-la-scommessa-deflazionaria-di-venice/` | 200, titolo italiano presente |
| `/2026/10/nous-research-vale-15-miliardi-hermes-esce-dallopen-source-e-va-in-azienda/` | 200, titolo italiano presente |
| `/2026/10/leuropa-stringe-sui-stablecoin-lasia-apre-agli-etf-la-regolamentazione-accelera/` | 200, titolo italiano presente |
| `/2026/10/chi-decide-chi-muore-e-chi-risponde/` | 200, titolo italiano presente |

Controprova sull'origine GitHub Pages (`arstanton82.github.io/raziel-news/...`): 301 su tutte le URL,
cioè il redirect verso il dominio personalizzato raziel.news — comportamento atteso.

## Note

- **URL italiano del secondo articolo**: Hugo genera `nous-research-vale-15-miliardi-...` (la virgola di
  "1,5" sparisce dallo slug). Non incide sulla traduzione, ma è la forma corretta da usare nei controlli.
- **Possibile duplicato editoriale**: `2026-10-11-hermes-series-b-business.md` copre la stessa notizia
  del Series B già pubblicata l'8 ottobre (`2026-10-08-hermes-series-b-business.md`, che ha già la sua
  versione inglese). I due testi non sono identici (struttura, tag e fonti diversi), quindi ho tradotto
  il nuovo come articolo a sé, ma gli ho dato uno slug inglese distinto
  (`/en/2026/10/nous-research-1-5-billion-hermes-leaves-open-source/`) per non collidere con
  `/en/2026/10/nous-research-1-5-billion-hermes-for-businesses/`. Nessuna collisione di `url:` tra le
  versioni inglesi (verificato: nessun duplicato su 52 coppie). Segnalo la sovrapposizione: la decisione
  editoriale se tenerla è fuori dalla mia mansione.
- Nessun problema fuori dai miei file: non ho toccato `scripts/`, `layouts/`, `static/`, `hugo.yaml`,
  `i18n/`, né i file italiani.
