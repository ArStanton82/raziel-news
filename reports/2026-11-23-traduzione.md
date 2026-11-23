# Traduzione inglese — 2026-11-23

Coda: 3 articoli senza gemello `.en.md` (tutti del 2026-11-23). Tradotti tutti e 3, sotto il tetto di 6.

## Articoli tradotti

1. `2026-11-23-vvv-crediti-diem.md` → `2026-11-23-vvv-crediti-diem.en.md`
   - titolo: «VVV corre mentre il mercato scende. Il dato interessante non è il +30%» → «VVV runs while the market falls. The interesting number is not the +30%»
   - percorso inglese: `/en/2026/11/vvv-runs-while-the-market-falls-the-interesting-number-is-not-the-30-percent/`
2. `2026-11-23-hermes-gateway-cruscotto.md` → `2026-11-23-hermes-gateway-cruscotto.en.md`
   - titolo: «Hermes cambia casa: il cruscotto va in pensione, il gateway resta» → «Hermes moves house: the dashboard retires, the gateway stays»
   - percorso inglese: `/en/2026/11/hermes-moves-house-the-dashboard-retires-the-gateway-stays/`
3. `2026-11-23-etf-deflussi-strutturali.md` → `2026-11-23-etf-deflussi-strutturali.en.md`
   - titolo: «Gli ETF Bitcoin perdono 1,79 miliardi in una settimana. E c'è chi li chiama «strutturali»» → «Bitcoin ETFs lose 1.79 billion in a week. And some call it «structural»»
   - percorso inglese: `/en/2026/11/bitcoin-etfs-lose-1-79-billion-in-a-week-and-some-call-it-structural/`

Nessun articolo saltato (tutti `draft: false`, tutti sopra le 200 parole).

## Pre-commit

`python3 scripts/lingua_link_inglesi.py --scrivi`: 189 coppie it→en con percorso dichiarato, 0 link interni riscritti in 0 articoli (nessun articolo inglese puntava a una pagina italiana con gemello nuovo). Unico file saltato: `_index.en.md` (senza `url:`).

## Commit e deploy

- commit `280633d` su `main`: `feat(i18n): versione inglese di 3 articoli (2026-11-23)`, 3 file, 98 righe aggiunte.
- push `fcea330..280633d` riuscito.
- GitHub Actions `deploy.yml`: run 45166164952, stato `completed`, conclusione **success**.

## Verifica dal vivo (user-agent browser)

Versioni inglesi:
- `/en/2026/11/vvv-runs-while-the-market-falls-the-interesting-number-is-not-the-30-percent/` → 200, titolo inglese corretto
- `/en/2026/11/hermes-moves-house-the-dashboard-retires-the-gateway-stays/` → 200, titolo inglese corretto
- `/en/2026/11/bitcoin-etfs-lose-1-79-billion-in-a-week-and-some-call-it-structural/` → 200, titolo inglese corretto

Versioni italiane corrispondenti (controllo di non regressione):
- `/2026/11/vvv-corre-mentre-il-mercato-scende.-il-dato-interessante-non-%C3%A8-il-30/` → 200, titolo italiano integro
- `/2026/11/hermes-cambia-casa-il-cruscotto-va-in-pensione-il-gateway-resta/` → 200, titolo italiano integro
- `/2026/11/gli-etf-bitcoin-perdono-179-miliardi-in-una-settimana.-e-c%C3%A8-chi-li-chiama-strutturali/` → 200, titolo italiano integro

## Anomalie

Nessuna. Tutti i controlli superati. Restano invariati i soliti file non tracciati fuori dal perimetro (report storici, script di servizio): non committati, come da vincolo.
