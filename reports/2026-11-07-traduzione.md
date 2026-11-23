# Traduzione inglese — 2026-11-07

Coda di partenza: 3 articoli senza gemello `.en.md`, tutti recenti e tradotti in questa esecuzione. Nessun articolo rimandato.

## Articoli tradotti

1. «Venice: TVL zero, settanta per cento in staking» → «Venice: Zero TVL, Seventy Percent Staked»
   - file: `content/posts/2026-11-07-venice-staking-tvl-zero.en.md`
   - percorso inglese: `/en/2026/11/venice-staking-tvl-zero/`

2. «Sedici miliardi di motivi: il Tesoro taglia MEXC dalle banche americane» → «Sixteen Billion Reasons: Treasury Cuts MEXC Off From U.S. Banks»
   - file: `content/posts/2026-11-07-mexc-fincen-tesoro.en.md`
   - percorso inglese: `/en/2026/11/mexc-fincen-tesoro/`

3. «Il valore di un modello è a un fine-tune di distanza» → «A Model's Values Are One Fine-Tune Away»
   - file: `content/posts/2026-11-07-hermes-arete-valori.en.md`
   - percorso inglese: `/en/2026/11/hermes-arete-valori/`

Nessun articolo saltato: tutti e tre con `draft: false` e ben oltre le 200 parole.

## Script link interni

`python3 scripts/lingua_link_inglesi.py --scrivi` eseguito prima del commit: 137 coppie italiano → inglese con percorso dichiarato riconosciute, **0 link riscritti** (unico file saltato: `_index.en.md`, che non ha `url:`). Nessuna modifica da includere nel commit.

## Commit e deploy

- commit `10b6e05` — `feat(i18n): versione inglese di 3 articoli (2026-11-07)`, 3 file, 90 inserzioni; push su `main` riuscito.
- deploy GitHub Actions `deploy.yml` run `42368540300` (sha `10b6e05`): **conclusion `success`**. La corsa è rimasta "in progress" per circa cinque minuti prima di completare, con lo step «Immagini di condivisione per articolo» in esecuzione; nessun errore.

## Controlli dal vivo (user-agent da browser)

Pagine inglesi — tutte `200`:

- `/en/2026/11/venice-staking-tvl-zero/` → 200, titolo «Venice: Zero TVL, Seventy Percent Staked»
- `/en/2026/11/mexc-fincen-tesoro/` → 200, titolo «Sixteen Billion Reasons: Treasury Cuts MEXC Off From U.S. Banks»
- `/en/2026/11/hermes-arete-valori/` → 200, titolo «A Model's Values Are One Fine-Tune Away»

Pagine italiane corrispondenti — tutte `200` e con il titolo italiano intatto:

- `/2026/11/venice-tvl-zero-settanta-per-cento-in-staking/` → 200, «Venice: TVL zero, settanta per cento in staking»
- `/2026/11/sedici-miliardi-di-motivi-il-tesoro-taglia-mexc-dalle-banche-americane/` → 200, «Sedici miliardi di motivi: il Tesoro taglia MEXC dalle banche americane»
- `/2026/11/il-valore-di-un-modello-%C3%A8-a-un-fine-tune-di-distanza/` → 200, «Il valore di un modello è a un fine-tune di distanza»

Accoppiamento lingue verificato sugli `hreflang`: ogni pagina inglese dichiara `it-it` verso l'italiano e `en-us` verso sé stessa, e viceversa. Il cambio lingua è attivo.

## Note

- Lo slug italiano del terzo articolo contiene una `è` percent-encoded (`%C3%A8`) nell'URL: è un comportamento preesistente del permalink ricavato dal titolo, non introdotto da questa esecuzione e non modificabile senza toccare il file italiano. Gli `hreflang` puntano al percorso corretto, quindi la navigazione funziona.
- Nessun problema riscontrato fuori dai file di competenza. Nessuna modifica a script, layout, tema, `hugo.yaml`, `i18n/`, immagini o file italiani.
