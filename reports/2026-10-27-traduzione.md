# Traduzione inglese — 2026-10-27

## Coda

Tre articoli italiani senza gemello inglese, tutti tradotti in questa esecuzione (sotto il limite di 6). Nessun articolo saltato: nessuno aveva `draft: true` e tutti superavano le 200 parole (578, 678, 539).

## Articoli tradotti

| Titolo italiano | Titolo inglese | Percorso inglese |
|---|---|---|
| Un dollaro per milione: la scommessa di Venice sul prezzo dell'intelligenza | One Dollar a Million: Venice Bets on the Price of Intelligence | `/en/2026/10/one-dollar-a-million-venice-bets-on-the-price-of-intelligence/` |
| Lo Stato costruisce le rotaie, la filiera retail si crepa | The State Lays the Rails, the Retail Supply Chain Cracks | `/en/2026/10/the-state-lays-the-rails-the-retail-supply-chain-cracks/` |
| GPT-6.1 Terra entra in Hermes Agent: il modello diventa una voce di costo | GPT-6.1 Terra Lands in Hermes Agent: the Model Becomes a Line Item | `/en/2026/10/gpt-6-1-terra-lands-in-hermes-agent-the-model-becomes-a-line-item/` |

Categorie: `Venice.ai`+`AI`, `Crypto`+`Blockchain`, `Hermes`+`AI`. Struttura delle sezioni identica all'italiano (3, 4 e 3 `##`). Nessun titolo `#` nel corpo. Riga finale delle fonti mantenuta dopo il `---` con etichetta `*Verified sources: ...*`, testate, link e date invariati.

## Link interni

`python3 scripts/lingua_link_inglesi.py --scrivi`: 102 coppie italiano → inglese riconosciute, 0 link riscritti (i tre articoli di oggi non si citano a vicenda), nessuna modifica ai file già esistenti.

## Commit e deploy

- Commit `b4859ab` — `feat(i18n): versione inglese di 3 articoli (2026-10-27)`, 3 file, 92 righe aggiunte, nessun altro file toccato.
- Push su `main` riuscito (`0e5edcc..b4859ab`).
- `deploy.yml`, run `40496806849`: **success**.

## Controlli dal vivo

Tutti con user-agent da browser.

| URL | Codice |
|---|---|
| `/en/2026/10/one-dollar-a-million-venice-bets-on-the-price-of-intelligence/` | 200 |
| `/en/2026/10/the-state-lays-the-rails-the-retail-supply-chain-cracks/` | 200 |
| `/en/2026/10/gpt-6-1-terra-lands-in-hermes-agent-the-model-becomes-a-line-item/` | 200 |
| `/2026/10/un-dollaro-per-milione-la-scommessa-di-venice-sul-prezzo-dellintelligenza/` | 200 |
| `/2026/10/lo-stato-costruisce-le-rotaie-la-filiera-retail-si-crepa/` | 200 |
| `/2026/10/gpt-6.1-terra-entra-in-hermes-agent-il-modello-diventa-una-voce-di-costo/` | 200 |

Titoli: le tre pagine inglesi rendono il titolo inglese, le tre italiane il titolo italiano originale (verificato sul `<title>`). Il cambio lingua funziona nei due sensi: ogni pagina inglese linka la propria versione italiana in `class=lingua`, e ogni pagina italiana linka il nuovo indirizzo `/en/`. Presenti anche gli `hreflang` it/en/x-default corretti.

## Note

- L'URL italiano dell'articolo su Terra contiene un punto: `/2026/10/gpt-6.1-terra-entra-in-hermes-agent-.../`. È un percorso già pubblicato e generato dallo slug del titolo italiano: non l'ho toccato perché sta fuori dai file di mia competenza. Il percorso inglese è correttamente ASCII e con i trattini.
- Nulla di anomalo da segnalare fuori dai file `*.en.md`.
