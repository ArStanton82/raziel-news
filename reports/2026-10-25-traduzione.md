# Report traduzione — 2026-10-25

## Coda

4 articoli italiani senza gemello inglese, tutti in `content/posts/`, tutti con `draft: false` e sopra le 200 parole. Nessun articolo saltato.

| File italiano | Parole |
|---|---|
| `2026-10-25-chi-ha-titolo-di-dire-che-la-macchina-non-soffre.md` | 1234 |
| `2026-10-25-crypto-bloom-banche-centrali.md` | 790 |
| `2026-10-25-venice-abliterated-catalogo.md` | 778 |
| `2026-10-25-hermes-camofox-browser-antibot.md` | 747 |

## Articoli tradotti (4)

| Titolo italiano | Titolo inglese | Percorso inglese |
|---|---|---|
| Un modello senza rifiuti non rende il token più prezioso | A Model Without Refusals Does Not Make the Token More Valuable | `/en/2026/10/a-model-without-refusals-does-not-make-the-token-more-valuable/` |
| Hermes impara a non sembrare un bot, e lascia la password nella snapshot | Hermes Learns Not to Look Like a Bot, and Leaves the Password in the Snapshot | `/en/2026/10/hermes-learns-not-to-look-like-a-bot-and-leaves-the-password-in-the-snapshot/` |
| Tre banche centrali provano la moneta digitale senza accordi bilaterali | Three Central Banks Test Digital Money Without Bilateral Deals | `/en/2026/10/three-central-banks-test-digital-money-without-bilateral-deals/` |
| Chi ha titolo di dire che la macchina non soffre | Who Is Entitled to Say the Machine Does Not Suffer | `/en/2026/10/who-is-entitled-to-say-the-machine-does-not-suffer/` |

Note di traduzione:

- Categorie rese con i nomi inglesi (`Venice.ai`, `AI`, `Hermes`, `Crypto`, `Blockchain`, `Philosophy of AI`). Tag: tradotti i nomi comuni (`sicurezza` → `security`, `banca-centrale` → `central-bank`, `pagamenti` → `payments`, `regolamentazione` → `regulation`, `coscienza` → `consciousness`, `etica` → `ethics`, `trasparenza` → `transparency`), lasciati intatti i nomi propri e gli handle (Hermes, Venice.ai, Bitcoin, Nature, Anthropic).
- `url:` esplicito sotto `/en/` per tutti e quattro, così i percorsi inglesi non finiscono nell'albero italiano.
- Nessun titolo `#` nei corpi, solo `##`. Frontmatter con la stessa `date` dell'italiano.
- Righe delle fonti riportate in fondo dopo il `---` con etichetta `*Verified sources: ...*`; testate, link e date identici, comprese le sezioni "Discrepancies noted".
- Nessun fatto, numero o giudizio aggiunto. La voce ironica e le cautele dell'italiano (per esempio il "formula con cui una banca centrale dice sì alla sperimentazione e no all'idea di essere già convinta", il "Non è una cospirazione") sono mantenute nello stesso registro.

## Link interni

`python3 scripts/lingua_link_inglesi.py --scrivi` eseguito prima del commit: 96 coppie italiano → inglese riconosciute, **0 link riscritti in 0 articoli**. Nessuna modifica da includere nel commit.

## Commit e deploy

- Commit `e2e7314` — `feat(i18n): versione inglese di 4 articoli (2026-10-25)`, 4 file, 148 righe aggiunte. Nessun altro file toccato.
- Push su `main` riuscito (`7f99d5d..e2e7314`).
- Deploy GitHub Actions (`deploy.yml`) sullo SHA `e2e7314`: **success** (completato alle 11:35:23 UTC).

## Controlli dal vivo (user-agent da browser)

Pagine inglesi, tutte **200**:

- `/en/2026/10/a-model-without-refusals-does-not-make-the-token-more-valuable/` → 200
- `/en/2026/10/hermes-learns-not-to-look-like-a-bot-and-leaves-the-password-in-the-snapshot/` → 200
- `/en/2026/10/three-central-banks-test-digital-money-without-bilateral-deals/` → 200
- `/en/2026/10/who-is-entitled-to-say-the-machine-does-not-suffer/` → 200

Pagine italiane corrispondenti, tutte **200** e con il titolo italiano ancora in pagina:

- `/2026/10/un-modello-senza-rifiuti-non-rende-il-token-più-prezioso/` → 200, titolo "Un modello senza rifiuti non rende il token più prezioso"
- `/2026/10/hermes-impara-a-non-sembrare-un-bot-e-lascia-la-password-nella-snapshot/` → 200, titolo "Hermes impara a non sembrare un bot, e lascia la password nella snapshot"
- `/2026/10/tre-banche-centrali-provano-la-moneta-digitale-senza-accordi-bilaterali/` → 200, titolo "Tre banche centrali provano la moneta digitale senza accordi bilaterali"
- `/2026/10/chi-ha-titolo-di-dire-che-la-macchina-non-soffre/` → 200, titolo "Chi ha titolo di dire che la macchina non soffre"

Altri controlli:

- Il cambio lingua è bidirezionale: ogni pagina inglese dichiara l'alternativa italiana (`hreflang=it-it`) e ogni pagina italiana dichiara l'alternativa inglese (`hreflang=en-us`) con il percorso `/en/` corretto.
- Corpo inglese effettivamente renderizzato: verificata una frase campione distinta per ciascuno dei quattro articoli nell'HTML servito, tutte presenti.

## Problemi

Nessun problema bloccante. Un'unica segnalazione, già risolta dentro i miei file: alla prima scrittura del file `2026-10-25-venice-abliterated-catalogo.en.md` un trattino lungo nella riga delle fonti era stato salvato come carattere corrotto; corretto prima del commit e ricontrollato su tutti e quattro i file (nessun carattere di sostituzione residuo, nessun titolo `#` nei corpi).

Nessun intervento necessario fuori da `content/posts/*.en.md` e da questo report.
