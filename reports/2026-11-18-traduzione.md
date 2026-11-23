# Traduzione inglese — 2026-11-18

Coda di oggi: 3 articoli italiani senza gemello `.en.md` (tutti e tre del 18/11, nessun arretrato). Tutti tradotti: limite di 6 non raggiunto.

## Articoli tradotti

1. «La Banca Mondiale prova l'USDC per gli aiuti: la notizia noiosa che conta» → «The World Bank Tries USDC for Aid: The Boring News That Matters»
   - percorso inglese: `/en/2026/11/the-world-bank-tries-usdc-for-aid-the-boring-news-that-matters/`
2. «L'agente che si porta via: Hermes impara a traslocare nel cloud» → «The Agent You Can Carry: Hermes Learns to Move House in the Cloud»
   - percorso inglese: `/en/2026/11/the-agent-you-can-carry-hermes-learns-to-move-house-in-the-cloud/`
3. «Mind Market: Venice non vende il modello, vende il compito» → «Mind Market: Venice Doesn't Sell the Model, It Sells the Task»
   - percorso inglese: `/en/2026/11/mind-market-venice-doesnt-sell-the-model-it-sells-the-task/`

Nessun articolo saltato: tutti `draft: false`, tutti sopra le 200 parole.

## Link interni

`python3 scripts/lingua_link_inglesi.py --scrivi` eseguito prima del commit: 173 coppie italiano→inglese riconosciute, 0 link riscritti (nessun articolo inglese puntava a una pagina italiana con gemello appena creato). Nessuna modifica da includere.

## Commit e deploy

- Commit `c7b63ed` — `feat(i18n): versione inglese di 3 articoli (2026-11-18)`, push su `main` (bc14380..c7b63ed).
- Run GitHub Actions `deploy.yml` 44295489625: job `build` success (incluso lo step «Immagini di condivisione per articolo»), job `deploy` success. Conclusione complessiva: **success**.

## Verifica dal vivo (user-agent da browser)

Pagine inglesi, tutte `200`:

- `/en/2026/11/the-world-bank-tries-usdc-for-aid-the-boring-news-that-matters/` → 200, `<title>` «The World Bank Tries USDC for Aid: The Boring News That Matters»
- `/en/2026/11/the-agent-you-can-carry-hermes-learns-to-move-house-in-the-cloud/` → 200, `<title>` «The Agent You Can Carry: Hermes Learns to Move House in the Cloud»
- `/en/2026/11/mind-market-venice-doesnt-sell-the-model-it-sells-the-task/` → 200, `<title>` «Mind Market: Venice Doesn't Sell the Model, It Sells the Task»

Pagine italiane corrispondenti, tutte `200` e con il titolo italiano intatto:

- `/2026/11/la-banca-mondiale-prova-lusdc-per-gli-aiuti-la-notizia-noiosa-che-conta/` → 200, titolo «La Banca Mondiale prova l'USDC per gli aiuti: la notizia noiosa che conta»
- `/2026/11/lagente-che-si-porta-via-hermes-impara-a-traslocare-nel-cloud/` → 200, titolo «L'agente che si porta via: Hermes impara a traslocare nel cloud»
- `/2026/11/mind-market-venice-non-vende-il-modello-vende-il-compito/` → 200, titolo «Mind Market: Venice non vende il modello, vende il compito»

Corpo delle pagine inglesi renderizzato correttamente (controllo testuale: «restore point» / «punto di ripristino» presenti su entrambe le versioni dell'articolo Hermes), `<html lang=en>` sulle pagine inglesi e `lang=it` sulle italiane.

## Note

- Nessun problema bloccante, nessuna correzione fuori dai file di mia competenza.
- Il markup delle pagine non emette link `hreflang` né un collegamento diretto fra gemelli (verificato anche su coppie di giorni precedenti, es. 17/11): è il comportamento attuale del tema, non un effetto di queste traduzioni. Se il cambio lingua sulle pagine articolo deve essere visibile nei template, va trattato fuori da questo job.
- Non sono stati toccati file italiani, script, layout, `hugo.yaml`, `i18n/` o immagini.
