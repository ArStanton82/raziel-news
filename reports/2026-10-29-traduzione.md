# Traduzione inglese — 2026-10-29

Coda trovata: 3 articoli (tutti pubblicati oggi, `draft: false`, tutti sopra le 200 parole). Nessuno saltato, nessuno escluso per il tetto di 6.

## Articoli tradotti

1. «Venice ha bruciato più di un milione di dollari in un mese. Il prezzo non se n'è accorto»
   → «Venice Burned More Than a Million Dollars in a Month. The Price Did Not Notice»
   percorso inglese: `/en/2026/10/venice-burned-a-million-dollars-in-a-month-the-price-did-not-notice/`
   (italiano: `/2026/10/venice-ha-bruciato-più-di-un-milione-di-dollari-in-un-mese.-il-prezzo-non-se-n'è-accorto/`)

2. «Hermes impara a guardarsi dentro: il plugin inbox»
   → «Hermes Learns to Look Inside Itself: The Inbox Plugin»
   percorso inglese: `/en/2026/10/hermes-learns-to-look-inside-itself-the-inbox-plugin/`
   (italiano: `/2026/10/hermes-impara-a-guardarsi-dentro-il-plugin-inbox/`)

3. «Il DTCC mette i titoli di Wall Street su una blockchain. Con i diritti veri»
   → «The DTCC Puts Wall Street Securities on a Blockchain. With Real Rights»
   percorso inglese: `/en/2026/10/dtcc-puts-wall-street-securities-on-a-blockchain-with-real-rights/`
   (italiano: `/2026/10/il-dtcc-mette-i-titoli-di-wall-street-su-una-blockchain.-con-i-diritti-veri/`)

Frontmatter: `date` identica all'italiano (2026-10-29), `draft: false`, `url` esplicita sotto `/en/`, categorie in inglese (Venice.ai/Crypto, Hermes/AI, Crypto/Blockchain), tag tradotti con i nomi propri intatti (VVV, DIEM, DTCC, Fed). Corpi senza nessun titolo di primo livello, solo `##`. Riga finale delle fonti con etichetta inglese, testate, link e date invariati. Nessun fatto, cifra o giudizio aggiunto rispetto all'italiano: anche la nota metodologica dell'articolo su Venice (dati del report scartati) è riportata in inglese.

## Link interni

`python3 scripts/lingua_link_inglesi.py --scrivi` eseguito prima del commit: 108 coppie it→en con percorso dichiarato, **0 link riscritti** in 0 articoli inglesi. Atteso: i tre articoli di oggi non si citano tra loro e non hanno link interni nel corpo.

## Commit e deploy

- commit `7cc0dcc` — `feat(i18n): versione inglese di 3 articoli (2026-10-29)`, 3 file, 102 righe aggiunte, solo `content/posts/*.en.md`.
- push su `main`: `6adb26c..7cc0dcc`.
- GitHub Actions `deploy.yml`: **success** sullo SHA `7cc0dcc` (controllato dopo l'attesa; il primo controllo dava `in_progress`, il workflow ha impiegato qualche minuto in più dei 90 secondi iniziali).

## Verifiche dal vivo (user-agent da browser)

Pagine inglesi — tutte `200` e con il titolo inglese corretto in `<h1>`:

| pagina | esito |
|---|---|
| `/en/2026/10/venice-burned-a-million-dollars-in-a-month-the-price-did-not-notice/` | 200 |
| `/en/2026/10/hermes-learns-to-look-inside-itself-the-inbox-plugin/` | 200 |
| `/en/2026/10/dtcc-puts-wall-street-securities-on-a-blockchain-with-real-rights/` | 200 |

Pagine italiane corrispondenti — tutte `200` e con il titolo italiano ancora in pagina:

| pagina | esito |
|---|---|
| `.../venice-ha-bruciato-più-di-un-milione-di-dollari-in-un-mese.-il-prezzo-non-se-n'è-accorto/` | 200, titolo italiano presente |
| `/2026/10/hermes-impara-a-guardarsi-dentro-il-plugin-inbox/` | 200, titolo italiano presente |
| `.../il-dtcc-mette-i-titoli-di-wall-street-su-una-blockchain.-con-i-diritti-veri/` | 200, titolo italiano presente |

Cambio lingua: verificato in entrambe le direzioni. Le pagine inglesi dichiarano `hreflang=it-it` con l'URL italiano esatto dei rispettivi gemelli, le pagine italiane espongono il selettore `hreflang=en`. Accoppiamento corretto, nessun articolo appeso alla versione sbagliata.

## Note (fuori dai miei file, non corrette)

- Gli slug italiani generati da Hugo dai titoli contengono un punto prima della seconda frase (`...in-un-mese.-il-prezzo...`, `...una-blockchain.-con-i-diritti-veri/`). Funziona e dà `200`, ma un punto nel percorso è un dettaglio di igiene SEO: si risolverebbe con uno `slug:` esplicito nel frontmatter italiano. Non l'ho toccato, come da vincoli.
- `git status` mostra `reports/` e `scripts/` quasi interamente non tracciati (circa 130 file, incluse cartelle `reports/raw-*` e script di analisi una tantum). Non riguarda questo job e non l'ho committato: il commit di oggi contiene soltanto i tre `.en.md`. Segnalo che, se un giorno si vuole la cronologia dei report anche nel repo, serve una decisione a monte su cosa tracciare.
- Coda residua: zero articoli in attesa di traduzione dopo questo giro.
