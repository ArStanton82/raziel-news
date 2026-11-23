# Traduzione inglese — 2026-11-06

Coda iniziale: 3 articoli senza gemello `.en.md`. Tradotti tutti e 3 (limite di 6 non raggiunto).

## Articoli tradotti

1. "Venice mette il turbo: DeepSeek V4.1 Flash arriva in versione Ultrafast"
   → "Venice Hits the Turbo: DeepSeek V4.1 Flash Arrives in an Ultrafast Build"
   → `/en/2026/11/venice-deepseek-ultrafast-burn/`
   → file: `content/posts/2026-11-06-venice-deepseek-ultrafast-burn.en.md`

2. "Hermes 0.23: il desktop diventa una scheda del browser"
   → "Hermes 0.23: the desktop becomes a browser tab"
   → `/en/2026/11/hermes-hearth-webapp/`
   → file: `content/posts/2026-11-06-hermes-hearth-webapp.en.md`

3. "Bitcoin sotto i 76.000 dollari: la correzione arriva dai data center"
   → "Bitcoin below $76,000: the correction arrives from the data centers"
   → `/en/2026/11/bitcoin-76000-miner-ai/`
   → file: `content/posts/2026-11-06-bitcoin-76000-miner-ai.en.md`

Nessun articolo saltato: tutti `draft: false` e sopra le 200 parole (693, 583, 680 parole).

## Script link interni

`python3 scripts/lingua_link_inglesi.py --scrivi` eseguito prima del commit: 134 coppie italiano→inglese riconosciute, **0 link riscritti in 0 articoli**. Include solo `_index.en.md` fra le versioni inglesi saltate (priva di `url:`). Nessuna modifica da includere nel commit.

## Commit e deploy

- Commit `3d7a118` — "feat(i18n): versione inglese di 3 articoli (2026-11-06)", 3 file, 94 inserimenti.
- Push su `main` riuscito (`22694b8..3d7a118`).
- GitHub Actions `deploy.yml` sul commit `3d7a118`: **success** (attesa ~5 minuti, il run è rimasto `in_progress` per circa quattro minuti e mezzo prima di concludere).

## Controlli dal vivo

Fatti con user-agent Chrome completo (`Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36`).

| URL inglese | HTTP | corpo EN | fonti EN |
|---|---|---|---|
| /en/2026/11/venice-deepseek-ultrafast-burn/ | 200 | presente | presente |
| /en/2026/11/hermes-hearth-webapp/ | 200 | presente | presente |
| /en/2026/11/bitcoin-76000-miner-ai/ | 200 | presente | presente |

| URL italiana corrispondente | HTTP | titolo italiano |
|---|---|---|
| /2026/11/venice-mette-il-turbo-deepseek-v4.1-flash-arriva-in-versione-ultrafast/ | 200 | presente |
| /2026/11/hermes-0.23-il-desktop-diventa-una-scheda-del-browser/ | 200 | presente |
| /2026/11/bitcoin-sotto-i-76.000-dollari-la-correzione-arriva-dai-data-center/ | 200 | presente |

Il cambio lingua è correttamente esposto: su ogni pagina inglese l'`hreflang=it-it` punta alla pagina italiana e il canonical inglese resta sotto `/en/`.

## Note e cose non funzionate

- **403 di Cloudflare sulla prima verifica.** Il primo giro di curl con `-A "Mozilla/5.0"` (user-agent corto) ha restituito `403` su tutti e sei gli URL, inglesi e italiani, comprese pagine che sono online. Con lo user-agent Chrome completo si ottiene `200`. Non è un problema del sito: è la Bot Fight Mode che scatta sull'UA troncato. Da tenere presente per le verifiche future, perché un 403 con UA corto non significa pagina assente.
- **Slug italiani non deducibili dal titolo a occhio.** Hugo conserva i punti negli slug (`hermes-0.23-...`, `v4.1-flash`, `76.000-dollari`), quindi i primi URL italiani che avevo costruito a mano davano `404`. Gli URL corretti sono stati letti dall'`hreflang` delle pagine inglesi. Nessuna correzione fatta al sito: gli slug sono giusti così.
- Il primo controllo testuale sul corpo dell'articolo Venice ha dato esito negativo per un falso allarme: il testo in HTML è spezzato su più righe, quindi `grep -F` su una frase intera non combacia. Verificato con una sottostringa più corta: il corpo è presente e completo.
- Nessun problema fuori dai file di mia competenza. Nessuna modifica a `scripts/`, `layouts/`, `static/`, `hugo.yaml`, `i18n/` o ai file italiani.
