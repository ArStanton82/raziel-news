# Traduzione 2026-10-05

## Articoli tradotti (3)

1. "Bitcoin prova il breakout, Wall Street prepara il turno di notte" → "Bitcoin tests a breakout as Wall Street prepares the night shift"
   - EN: `/en/2026/10/bitcoin-breakout-wall-street-night-shift/`
   - IT: `/2026/10/bitcoin-prova-il-breakout-wall-street-prepara-il-turno-di-notte/`
2. "Un milione di righe, 1.393 agenti: Hermes riscrive se stesso" → "A million lines, 1,393 agents: Hermes rewrites itself"
   - EN: `/en/2026/10/million-lines-1393-agents-hermes-rewrites-itself/`
   - IT: `/2026/10/un-milione-di-righe-1.393-agenti-hermes-riscrive-se-stesso/`
3. "VVV verso i 30 dollari: i crediti di AskVenice toccano un massimo" → "VVV heads toward 30 dollars: AskVenice credits hit a record"
   - EN: `/en/2026/10/vvv-toward-30-dollars-askvenice-credits-record/`
   - IT: `/2026/10/vvv-verso-i-30-dollari-i-crediti-di-askvenice-toccano-un-massimo/`

Coda iniziale: 3 articoli senza gemello `.en.md`, tutti tradotti (limite 6 non raggiunto). Nessun articolo saltato.

## Commit e deploy

- Commit `e3d4808` — `feat(i18n): versione inglese di 3 articoli (2026-10-05)` — pushato su `main`.
- `scripts/lingua_link_inglesi.py --scrivi`: 33 coppie IT→EN con percorso dichiarato, 0 link interni riscritti (nessun articolo inglese puntava a una pagina italiana tradotta in questo giro). Nessuna modifica da includere.
- Deploy `deploy.yml` sul commit `e3d4808`: **success**.

## Controlli dal vivo

Tutte le pagine con User-Agent da browser: **200**.

| Pagina | Codice |
| --- | --- |
| EN bitcoin-breakout-wall-street-night-shift | 200 |
| EN million-lines-1393-agents-hermes-rewrites-itself | 200 |
| EN vvv-toward-30-dollars-askvenice-credits-record | 200 |
| IT bitcoin-prova-il-breakout-... | 200 |
| IT un-milione-di-righe-1.393-agenti-... | 200 |
| IT vvv-verso-i-30-dollari-... | 200 |

Verifica del titolo: ogni pagina IT contiene ancora il titolo italiano (presente in `<title>` e `<h1>`) e ogni pagina EN contiene il titolo inglese. Le tre nuove URL inglesi compaiono nel sitemap `/en/sitemap.xml`.

## Note tecniche

- Con il solo header `-A "Mozilla/5.0"` tutte le pagine su `raziel.news` rispondono **403** (sfida di Cloudflare Bot Fight contro gli IP da datacenter). Aggiungendo gli header completi da browser (`Accept`, `Accept-Language`, `Accept-Encoding` + `--compressed`) le pagine rispondono 200. È il comportamento atteso della configurazione Cloudflare, non un errore del sito; nessun intervento richiesto.
- Il percorso italiano degli articoli non deriva dal nome file ma dal titolo (es. `2026-10-05-bitcoin-86k-okxice-zkapi.md` è servito a `/2026/10/bitcoin-prova-il-breakout-.../`). Le URL IT sono state ricavate dal sitemap `/it/sitemap.xml`.
- Nessun problema rilevato fuori dai file `content/posts/*.en.md` e da questo report.
