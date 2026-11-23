# Traduzione inglese — 2026-11-21

Coda: 3 articoli senza gemello `.en.md` (tutti i precedenti risultano già tradotti). Tradotti tutti e 3, nessuno saltato.

## Articoli tradotti

1. «VVV tra due nuovi listini e la scommessa di Hayes» → «VVV lands on two exchanges while Hayes places his bet»
   percorso inglese: `/en/2026/11/vvv-lands-on-two-exchanges-while-hayes-places-his-bet/`
2. «Hermes, i plugin che vincono sono quelli che frenano l'agente» → «Hermes: the plugins that win are the ones that slow the agent down»
   percorso inglese: `/en/2026/11/hermes-the-plugins-that-win-are-the-ones-that-slow-the-agent/`
3. «Bitcoin sotto i 58.000 dollari: il ribasso non parla di cripto» → «Bitcoin below $58,000: this slump is not about crypto»
   percorso inglese: `/en/2026/11/bitcoin-below-58000-this-slump-is-not-about-crypto/`

## Link interni

`python3 scripts/lingua_link_inglesi.py --scrivi`: 182 coppie italiano→inglese riconosciute, 0 link interni da riscrivere (saltato solo `_index.en.md`, privo di `url:`). Nessuna modifica aggiuntiva al commit.

## Commit e deploy

- commit `40111f9` — `feat(i18n): versione inglese di 3 articoli (2026-11-21)` — 3 file, 98 righe aggiunte, push su `main` riuscito.
- GitHub Actions `deploy.yml` sul commit `40111f9`: **success** (circa 4 minuti, attesa + polling).

## Controlli dal vivo (curl con UA da browser desktop)

Pagine inglesi, tutte `200`:

- `/en/2026/11/vvv-lands-on-two-exchanges-while-hayes-places-his-bet/` → 200, `<title>` «VVV lands on two exchanges while Hayes places his bet»
- `/en/2026/11/hermes-the-plugins-that-win-are-the-ones-that-slow-the-agent/` → 200, `<title>` «Hermes: the plugins that win are the ones that slow the agent down»
- `/en/2026/11/bitcoin-below-58000-this-slump-is-not-about-crypto/` → 200, `<title>` «Bitcoin below $58,000: this slump is not about crypto»

Pagine italiane corrispondenti, tutte `200` e con il titolo italiano intatto:

- `/2026/11/vvv-tra-due-nuovi-listini-e-la-scommessa-di-hayes/` → 200, «VVV tra due nuovi listini e la scommessa di Hayes»
- `/2026/11/hermes-i-plugin-che-vincono-sono-quelli-che-frenano-lagente/` → 200, «Hermes, i plugin che vincono sono quelli che frenano l'agente»
- `/2026/11/bitcoin-sotto-i-58.000-dollari-il-ribasso-non-parla-di-cripto/` → 200, «Bitcoin sotto i 58.000 dollari: il ribasso non parla di cripto»

I tre URL inglesi compaiono anche in `https://raziel.news/en/sitemap.xml`.

## Note (fuori dai file di mia competenza, non corrette)

- `https://raziel.news/sitemap.xml` (indice) risponde alla sfida Cloudflare se si usa un UA ridotto (`-A "Mozilla/5.0"`): serve un UA completo da browser Chrome per ottenere 200. Vale per tutti i controllo curl, non è un guasto del sito.
- Le pagine inglesi non emettono né `hreflang` né un link visibile alla versione italiana (e viceversa): il markup non contiene alcun riferimento incrociato, quindi il cambio lingua non è cliccabile dalla pagina. È un limite dei template, non della coppia di file, e va corretto fuori dal job di traduzione.
