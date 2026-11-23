# Traduzione inglese — 2026-11-12

Coda trovata: 3 articoli senza gemello `.en.md`. Tradotti tutti e tre (limite di 6 non raggiunto). Coda residua a fine giro: 0.

## Articoli tradotti

| Titolo italiano | Titolo inglese | Percorso inglese |
|---|---|---|
| Trenta secondi in 4K: il video di frontiera arriva su Venice e il token non segue | Thirty Seconds in 4K: Frontier Video Lands on Venice and the Token Doesn't Follow | `/en/2026/11/thirty-seconds-in-4k-frontier-video-lands-on-venice-and-the-token-doesnt-follow/` |
| Che cos'è un'azienda: MSCI cancella Strategy dai suoi indici | What Counts as a Company: MSCI Deletes Strategy From Its Indexes | `/en/2026/11/what-counts-as-a-company-msci-deletes-strategy-from-its-indexes/` |
| Mille plugin in sette giorni: l'hackathon di Hermes chiude e sposta il collo di bottiglia | A Thousand Plugins in Seven Days: Hermes' Hackathon Closes and Moves the Bottleneck | `/en/2026/11/a-thousand-plugins-in-seven-days-hermes-hackathon-closes-and-moves-the-bottleneck/` |

Nessun articolo saltato: tutti e tre hanno `draft: false` e superano abbondantemente le 200 parole.

## Link interni

`python3 scripts/lingua_link_inglesi.py --scrivi` eseguito prima del commit: 154 coppie italiano → inglese riconosciute, 0 link riscritti (nessun rimando interno da correggere in questo giro).

## Commit e deploy

- Commit `3ef6607` — `feat(i18n): versione inglese di 3 articoli (2026-11-12)`, 3 file, 114 righe aggiunte, solo i tre `.en.md` (verificato con `git diff --cached --name-only` prima del commit).
- Push su `main`: `edabd77..3ef6607`.
- Deploy GitHub Actions (`deploy.yml`, run su `3ef6607`): **success**, completato alle 11:37 UTC. La guardia anti-titolo duplicato e la verifica dei meta di condivisione sono passate.

## Controlli dal vivo (user-agent da browser)

Tutte e sei le pagine — tre inglesi e tre italiane — rispondono **200**, e ognuna contiene il proprio titolo. Le pagine inglesi espongono due `hreflang` (italiano + inglese), quindi il cambio lingua è attivo.

| URL | Esito |
|---|---|
| `/en/2026/11/thirty-seconds-in-4k-frontier-video-lands-on-venice-and-the-token-doesnt-follow/` | 200, titolo presente |
| `/en/2026/11/what-counts-as-a-company-msci-deletes-strategy-from-its-indexes/` | 200, titolo presente |
| `/en/2026/11/a-thousand-plugins-in-seven-days-hermes-hackathon-closes-and-moves-the-bottleneck/` | 200, titolo presente |
| `/2026/11/trenta-secondi-in-4k-il-video-di-frontiera-arriva-su-venice-e-il-token-non-segue/` | 200, titolo italiano presente |
| `/2026/11/che-cos%C3%A8-unazienda-msci-cancella-strategy-dai-suoi-indici/` | 200, titolo italiano presente |
| `/2026/11/mille-plugin-in-sette-giorni-lhackathon-di-hermes-chiude-e-sposta-il-collo-di-bottiglia/` | 200, titolo italiano presente |

## Note

- Primo controllo sul percorso italiano dell'articolo MSCI ha dato 404, ma era un mio errore di battitura: lo slug reale percent-encoda l'apostrofo (`che-cos%C3%A8-unazienda-...`). Con l'URL corretto la pagina risponde 200. Nessun problema del sito.
- Durante la scrittura del primo file si è inserito un carattere non valido al posto di una lineetta; corretto prima del commit e verificato con `iconv -f UTF-8 -t UTF-8` su tutti e tre i file (nessun carattere di sostituzione residuo).
- Nessuna modifica fuori da `content/posts/*.en.md` e da questo report.
