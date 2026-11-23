# Traduzione inglese — 2026-10-14

Coda di partenza: 3 articoli italiani senza gemello `.en.md`, tutti pubblicati oggi (nessun arretrato: le esecuzioni precedenti avevano già tradotto tutto fino al 13 ottobre). Tradotti tutti e 3, sotto il limite di 6.

## Articoli tradotti

| Titolo italiano | Titolo inglese | Percorso inglese |
|---|---|---|
| Il cripto che entra nei bilanci: da Bitcoin a 84.000 dollari al collaterale tokenizzato | Crypto walks onto the balance sheet: from bitcoin at $84,000 to tokenized collateral | `/en/2026/10/crypto-btc-istituzioni/` |
| Il plugin come interfaccia: l'ecosistema Hermes cresce ai margini del core | The plugin as interface: the Hermes ecosystem grows at the edges of the core | `/en/2026/10/hermes-ecosistema-plugin/` |
| Prezzo giù, consumi su: il paradosso di Venice nella settimana 41 | Price down, usage up: Venice's paradox in week 41 | `/en/2026/10/venice-consumi-prezzo/` |

Nessun articolo saltato: tutti e tre hanno `draft: false` e sono sopra le 200 parole (669, 530 e 563 parole).

## Commit e deploy

- Commit `b79b7ca` — `feat(i18n): versione inglese di 3 articoli (2026-10-14)`, 3 file, 92 inserimenti, solo `content/posts/*.en.md` (più il presente report).
- Push su `main` riuscito (`e1d06d2..b79b7ca`).
- `python3 scripts/lingua_link_inglesi.py --scrivi`: 61 coppie IT→EN riconosciute, **0 link interni riscritti** (nessuna modifica da includere nel commit). Salta `_index.en.md` perché priva di `url:` — comportamento atteso.
- Workflow `deploy.yml`: `conclusion: success` sul commit `b79b7ca` (run creato alle 10:32 UTC, completato).

## Controlli dal vivo (14 ottobre 2026)

Tutte le pagine rispondono **200** e contengono il titolo atteso.

Pagine inglesi:
- `/en/2026/10/crypto-btc-istituzioni/` → 200, titolo inglese presente
- `/en/2026/10/hermes-ecosistema-plugin/` → 200, titolo inglese presente
- `/en/2026/10/venice-consumi-prezzo/` → 200, titolo inglese presente

Pagine italiane corrispondenti (invariate, titolo italiano ancora presente):
- `/2026/10/il-cripto-che-entra-nei-bilanci-da-bitcoin-a-84.000-dollari-al-collaterale-tokenizzato/` → 200
- `/2026/10/il-plugin-come-interfaccia-lecosistema-hermes-cresce-ai-margini-del-core/` → 200
- `/2026/10/prezzo-gi%C3%B9-consumi-su-il-paradosso-di-venice-nella-settimana-41/` → 200

Abbinamento bilingue verificato in entrambe le direzioni: gli `alternate hreflang=it-it` / `hreflang=en-us` / `hreflang=x-default` sono presenti e corretti sulla coppia crypto (controllata come campione), e le tre URL inglesi compaiono nel sitemap `/en/sitemap.xml` mentre le tre italiane restano nel sitemap `/it/sitemap.xml`.

## Note e problemi riscontrati (non corretti: fuori dai miei file)

1. **403 di Cloudflare con la sola `-A "Mozilla/5.0"`.** Il comando di verifica previsto dal job (`curl -A "Mozilla/5.0"`) restituisce 403 su *tutte* le URL, incluse le pagine italiane già online da giorni: è la Modalità Bot Fight che sfida il traffico da datacenter, non un problema delle pagine. Con un set di header da browser reale (user-agent completo + `Accept` + `Accept-Language`) le stesse URL rispondono 200. Segnalo perché la verifica standard del job da questo IP è inaffidabile per costruzione.
2. **Gli URL italiani non derivano dal nome del file.** In `hugo.yaml` i permalink sono `posts: "/:year/:month/:title/"`, quindi lo slug italiano è il titolo slugificato, non il nome file. Le pagine inglesi non sono toccate dal problema perché il campo `url:` esplicito vince sul permalink. Le URL italiane corrette sono state ricavate da `https://raziel.news/it/sitemap.xml`.
3. **`gh-pages`/origine GitHub Pages non è utilizzabile come verifica di riserva**: `https://arstanton82.github.io/raziel-news/...` risponde 301 verso `http://raziel.news/...` (redirect del dominio personalizzato, oltretutto in http).
4. Nessuna modifica a script, layout, tema, `hugo.yaml` o immagini: l'unico file creato oltre ai tre `.en.md` è questo report.
