# Traduzione EN — 2026-11-24

Coda iniziale: 4 articoli senza gemello inglese (tutti sopra le 200 parole, nessuno `draft: true`). Tradotti tutti e 4, sotto il tetto di 6.

## Articoli tradotti

| Titolo IT | Titolo EN | Percorso EN |
|---|---|---|
| Asahi va al copyleft, Omarchy paga il fork: chi controlla il livello sotto il Mac | Asahi goes copyleft, Omarchy pays for the fork: who controls the layer under the Mac | /en/2026/11/asahi-goes-copyleft-omarchy-pays-for-the-fork/ |
| Un dollaro di bitcoin vale ottanta centesimi: la CFTC scrive il prezzo del collaterale | A dollar of bitcoin is worth eighty cents: the CFTC writes the price of collateral | /en/2026/11/a-dollar-of-bitcoin-is-worth-eighty-cents-the-cftc-writes-the-price-of-collateral/ |
| Ottanta per cento da una parte, venti dall'altra: la geografia degli sconti nel Nous Portal | Eighty per cent on one side, twenty on the other: the geography of discounts in the Nous Portal | /en/2026/11/eighty-per-cent-on-one-side-twenty-on-the-other-the-geography-of-discounts-in-the-nous-portal/ |
| VVV sale mentre il bitcoin scende: cosa si può verificare del movimento | VVV rises while bitcoin falls: what can actually be verified about the move | /en/2026/11/vvv-rises-while-bitcoin-falls-what-can-actually-be-verified-about-the-move/ |

Commit: `2597704` — `feat(i18n): versione inglese di 4 articoli (2026-11-24)`. Push su `main` riuscito.

`scripts/lingua_link_inglesi.py --scrivi`: eseguito prima del commit, 0 link riscritti (nessun file inglese modificato dallo script).

## Deploy

`gh run list -L 1 --workflow deploy.yml`: run su `259770483c76...` concluso con `success`.

## Verifica dal vivo (user-agent browser)

Pagine inglesi — tutte `200`:
- /en/2026/11/asahi-goes-copyleft-omarchy-pays-for-the-fork/ → 200 (title EN corretto)
- /en/2026/11/a-dollar-of-bitcoin-is-worth-eighty-cents-the-cftc-writes-the-price-of-collateral/ → 200
- /en/2026/11/eighty-per-cent-on-one-side-twenty-on-the-other-the-geography-of-discounts-in-the-nous-portal/ → 200
- /en/2026/11/vvv-rises-while-bitcoin-falls-what-can-actually-be-verified-about-the-move/ → 200

Pagine italiane corrispondenti — tutte `200`, titolo italiano ancora presente:
- /2026/11/asahi-copyleft-omarchy-paga-il-fork/ → 200, «Asahi va al copyleft…»
- /2026/11/un-dollaro-di-bitcoin-vale-ottanta-centesimi-la-cftc-scrive-il-prezzo-del-collaterale/ → 200, «Un dollaro di bitcoin vale ottanta centesimi…»
- /2026/11/ottanta-per-cento-da-una-parte-venti-dallaltra-la-geografia-degli-sconti-nel-nous-portal/ → 200, «Ottanta per cento da una parte…»
- /2026/11/vvv-sale-mentre-il-bitcoin-scende-cosa-si-pu%C3%B2-verificare-del-movimento/ → 200, «VVV sale mentre il bitcoin scende…»

## Note

- Il primo `curl` con solo `-A "Mozilla/5.0"` ha preso la challenge Cloudflare («Just a moment…») sul sitemap.xml; con UA completo Chrome/131 tutto ok, come da prassi.
- Nessun problema fuori dai file `content/posts/*.en.md`: niente da segnalare per correzioni esterne.
- Coda residua a fine giro: 0 articoli in attesa di traduzione.
