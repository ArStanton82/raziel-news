# Traduzione inglese — 2026-10-15

## Coda

Tre articoli in coda, tutti tradotti in questa esecuzione (limite: 6). Nessun articolo saltato: nessun `draft: true`, nessuno sotto le 200 parole.

## Articoli tradotti (3)

| Titolo italiano | Titolo inglese | Percorso inglese |
|---|---|---|
| L'Europa stringe il cerchio: MiCA passa dalla regola all'applicazione | Europe tightens the ring: MiCA moves from rule to enforcement | `/en/2026/10/crypto-mica-usdc-qivalis/` |
| La soglia di Hermes: l'agente che si configura parlando | The Hermes threshold: the agent that configures itself by talking | `/en/2026/10/hermes-v022-threshold/` |
| Venice e i modelli di frontiera: anonimi, non invisibili | Venice and frontier models: anonymous, not invisible | `/en/2026/10/venice-frontier-anonimo-vvv/` |

File creati: `content/posts/2026-10-15-crypto-mica-usdc-qivalis.en.md`, `content/posts/2026-10-15-hermes-v022-threshold.en.md`, `content/posts/2026-10-15-venice-frontier-anonimo-vvv.en.md`. Nessun file italiano toccato.

Categorie usate: `["Crypto", "Blockchain"]`, `["Hermes", "AI"]`, `["Venice.ai", "AI"]`. Tag tradotti dove erano nomi comuni (`regolamentazione` → `regulation`, `agenti` → `agents`); nomi propri e ticker lasciati intatti.

## Link interni

`python3 scripts/lingua_link_inglesi.py --scrivi` eseguito prima del commit: **0 link riscritti in 0 articoli**. I tre articoli di oggi non si citano fra loro, quindi non c'era nulla da rimappare. Nessuna modifica aggiuntiva da includere nel commit.

## Commit e deploy

- Commit: `5b2b308` — `feat(i18n): versione inglese di 3 articoli (2026-10-15)`, 3 file, 88 inserimenti.
- Push su `main` riuscito (`c2a2697..5b2b308`).
- Workflow `deploy.yml`, run su `headSha` `5b2b308`: **conclusion `success`** (dopo circa 2 minuti, prima `in_progress`, poi `queued`, poi `completed`).

## Controlli dal vivo (user-agent da browser)

Tutte le richieste con `-A "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 … Chrome/126.0"`.

### Pagine inglesi — tutte `200`, titolo inglese presente

| URL | HTTP | Titolo |
|---|---|---|
| `/en/2026/10/crypto-mica-usdc-qivalis/` | 200 | OK |
| `/en/2026/10/hermes-v022-threshold/` | 200 | OK |
| `/en/2026/10/venice-frontier-anonimo-vvv/` | 200 | OK |

### Pagine italiane corrispondenti — tutte `200`, titolo italiano presente

| URL | HTTP | Titolo |
|---|---|---|
| `/2026/10/leuropa-stringe-il-cerchio-mica-passa-dalla-regola-allapplicazione/` | 200 | OK |
| `/2026/10/la-soglia-di-hermes-lagente-che-si-configura-parlando/` | 200 | OK |
| `/2026/10/venice-e-i-modelli-di-frontiera-anonimi-non-invisibili/` | 200 | OK |

### Scambio di lingua

Su entrambi i lati la testata dichiara le due versioni: `hreflang=it-it` punta alla pagina italiana, `hreflang=en-us` a quella inglese, `x-default` all'italiana. Il gemello è quindi collegato in modo bidirezionale e il cambio lingua compare.

## Nota di metodo (nessuna azione presa)

Il primo giro di verifica ha dato `404` sulle pagine italiane costruendo l'URL dallo slug del file (`/2026/10/crypto-mica-usdc-qivalis/`). Non è un guasto del sito: il permalink configurato in `hugo.yaml` è `posts: "/:year/:month/:title/"`, cioè lo slug deriva dal **titolo**, non dal nome del file. Gli URL italiani corretti sono stati ricavati da `/it/sitemap.xml` e da lì i controlli sono passati. Gli indirizzi inglesi, avendo il campo `url:` esplicito, restano quelli attesi.

Segnalo inoltre, senza aver toccato nulla, che l'indice dei sitemap espone la lingua di default sotto `/it/sitemap.xml` mentre le pagine italiane vivono alla radice: è coerente con `defaultContentLanguageInSubdir: false` e non produce errori, ma è una asimmetria che vale la pena conoscere se in futuro si legge il sitemap index per inventariare gli URL.

## Esito

3 articoli su 3 tradotti, pubblicati e verificati. Deploy `success`. Nessun problema aperto, nessuna modifica fuori dai file `.en.md` e da questo report.
