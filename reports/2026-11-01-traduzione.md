# Traduzione inglese — 2026-11-01

Coda trovata: 4 articoli senza gemello `.en.md`, tutti del 2026-11-01. Tradotti tutti e 4 (limite di 6 non raggiunto, nessun articolo rinviato). Nessun articolo saltato per `draft: true` o per lunghezza sotto le 200 parole.

## Articoli tradotti

1. **Un milione bruciato, e un terzo dell'offerta che non c'entra** → **A Million Burned, and a Third of the Supply That Has Nothing to Do With It**
   - file: `content/posts/2026-11-01-venice-burn-record.en.md`
   - percorso inglese: `/en/2026/11/venice-burn-record/`
   - italiano: `/2026/11/un-milione-bruciato-e-un-terzo-dellofferta-che-non-centra/`

2. **La scatola era giusta. Il circuito in mezzo no** → **The Box Was Right. The Circuit in the Middle Wasn't**
   - file: `content/posts/2026-11-01-trezor-cryptobilis-impianto.en.md`
   - percorso inglese: `/en/2026/11/trezor-cryptobilis-impianto/`
   - italiano: `/2026/11/la-scatola-era-giusta.-il-circuito-in-mezzo-no/`

3. **La scheda che non si delega** → **The Ballot You Can't Delegate**
   - file: `content/posts/2026-11-01-la-scheda-che-non-si-delega.en.md`
   - percorso inglese: `/en/2026/11/la-scheda-che-non-si-delega/`
   - italiano: `/2026/11/la-scheda-che-non-si-delega/`

4. **Il browser è uscito dal nucleo e è rientrato da una porta laterale** → **The Browser Left the Core and Came Back Through a Side Door**
   - file: `content/posts/2026-11-01-hermes-browser-fuori-core.en.md`
   - percorso inglese: `/en/2026/11/hermes-browser-fuori-core/`
   - italiano: `/2026/11/il-browser-è-uscito-dal-nucleo-e-è-rientrato-da-una-porta-laterale/`

Le date nei frontmatter sono identiche all'italiano (2026-11-01). Categorie tradotte: `Filosofia dell'AI` → `Philosophy of AI`; le altre restano invariate perché già in inglese (`Crypto`, `Blockchain`, `Venice.ai`, `AI`, `Hermes`). Tag: nomi comuni tradotti (`elezioni` → `elections`, `modelli linguistici` → `language models`, `delega` → `delegation`, `responsabilita` → `responsibility`, `estensione` → `extension`), nomi propri invariati (Grok, ChatGPT, Trezor, Ledger, CryptoBilis, VVV, Camofox, Hermes Agent). Nessun titolo `#` nel corpo, solo `##`.

## Link interni inglesi

`python3 scripts/lingua_link_inglesi.py --scrivi`: 119 coppie italiano → inglese con percorso dichiarato, **0 link riscritti in 0 articoli**. Nessuna modifica a file preesistenti.

## Commit e deploy

- commit `e0fb0e6` — `feat(i18n): versione inglese di 4 articoli (2026-11-01)`, 4 file, 172 inserimenti, solo i quattro `.en.md` nuovi.
- push su `main`: `c360d35..e0fb0e6`, riuscito.
- GitHub Actions `deploy.yml` per quel commit: **success**.

## Verifica dal vivo (user-agent da browser)

Tutte le pagine inglesi, HTTP **200**:

- `/en/2026/11/venice-burn-record/` → 200
- `/en/2026/11/trezor-cryptobilis-impianto/` → 200
- `/en/2026/11/la-scheda-che-non-si-delega/` → 200
- `/en/2026/11/hermes-browser-fuori-core/` → 200

Pagine italiane corrispondenti, HTTP **200**, con il titolo italiano ancora presente nell'HTML in tutte e quattro.

Abbinamento bilingue attivo: ogni pagina inglese dichiara `hreflang=it-it` verso il proprio italiano e mostra il cambio lingua; le pagine italiane dichiarano `hreflang=en-us` verso l'inglese. Le quattro URL inglesi compaiono in `/en/sitemap.xml`.

## Note

- Nessun problema riscontrato dentro o fuori dai file di mia competenza. Nessuna correzione necessaria.
- Il repository contiene molti file non tracciati fuori da `content/posts/` (report storici, script, `static/images/card-bg/`, `cache/`): non li ho toccati e non sono entrati nel commit.
