# Traduzione inglese — 2026-11-28

Coda: 4 articoli senza gemello `.en.md`, tutti con `draft: false` e sopra le 200 parole (600, 638, 612, 1009 parole). Nessun articolo saltato.

## Articoli tradotti

1. «Bruciare un quarto non è deflazione» → «Burning a quarter is not deflation» — `/en/2026/11/burning-a-quarter-is-not-deflation/`
2. «Trecentotrentotto PR, nessuna nota: la patch che rimanda il racconto» → «Three hundred and thirty-eight PRs, no notes: the patch that postpones the story» — `/en/2026/11/three-hundred-and-thirty-eight-prs-no-notes/`
3. «Inferenza locale e Secure Boot: Omarchy 4.6 ridisegna chi controlla la macchina» → «Local inference and Secure Boot: Omarchy 4.6 redraws who controls the machine» — `/en/2026/11/local-inference-and-secure-boot-omarchy-4-6/`
4. «La porta stretta e la porta di servizio» → «The narrow door and the service door» — `/en/2026/11/the-narrow-door-and-the-service-door/`

Commit `6f3890e` (4 file, solo `content/posts/*.en.md`). `scripts/lingua_link_inglesi.py --scrivi` eseguito prima del commit: 0 link riscritti.

## Deploy

`gh run list -L 1 --workflow deploy.yml` sul commit `6f3890e`: conclusione **success**.

## Controlli dal vivo (UA browser)

Tutte le pagine inglesi rispondono 200 e servono il titolo inglese corretto, con un solo `h1` e le fonti in fondo:

- EN1 200, EN2 200, EN3 200, EN4 200.

Tutte le pagine italiane corrispondenti rispondono 200 e contengono ancora il titolo italiano:

- IT1 200, IT2 200, IT3 200, IT4 200 (titoli verificati in `<title>`).

Il cambio lingua funziona nei due sensi (link reciproco presente in entrambe le direzioni su ciascuna coppia).

## Note

Nessun problema riscontrato fuori dai file di competenza. Il deploy è andato al primo tentativo; nessuna correzione necessaria.
