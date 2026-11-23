# Traduzione inglese — 2026-10-20

Coda iniziale: 3 articoli senza gemello `.en.md`. Tradotti tutti e tre (limite 6 non raggiunto).

## Articoli tradotti

| Titolo italiano | Titolo inglese | Percorso inglese |
|---|---|---|
| Cinque milioni di persone, un modello che pensa in parallelo: la settimana di Venice | Five million users and a model that thinks in parallel: Venice's week | `/en/2026/10/five-million-users-and-a-model-that-thinks-in-parallel/` |
| Hermes impara a mostrarsi: la sala di controllo e la release che ripara la release | Hermes learns to show itself: a control room, and the release that fixes the release | `/en/2026/10/hermes-learns-to-show-itself/` |
| La banca dei risparmi apre al Bitcoin, Metaplanet compra un listino, le regole arrivano in ritardo | The savings bank opens to Bitcoin, Metaplanet buys a listing, the rules arrive late | `/en/2026/10/savings-banks-open-to-bitcoin-metaplanet-buys-a-listing-rules-arrive-late/` |

File creati:

- `content/posts/2026-10-20-venice-5-milioni-mercury3.en.md`
- `content/posts/2026-10-20-hermes-agent-station-v0222.en.md`
- `content/posts/2026-10-20-crypto-sparkasse-superplanet-regole.en.md`

## Note di redazione

- Tutti i file inglesi hanno `draft: false`, la stessa `date` dell'italiano, `url:` sotto `/en/` in ASCII minuscolo, corpo senza titolo `#` (solo `##`), riga finale `*Verified sources: ...*` con testate, link e date invariati.
- Categorie già in forma inglese (`Venice.ai`, `AI`, `Hermes`, `Crypto`, `Blockchain`). Tag: solo "modelli" → "models"; gli altri erano già nomi propri o termini identici.
- Numeri, citazioni e cautele ("dichiarata, non certificata", "cifre non confermate da Venice", "nulla è definitivo finché l'operazione non si chiude") riportati senza aggiunte né arrotondamenti.
- `python3 scripts/lingua_link_inglesi.py --scrivi`: **0 link riscritti in 0 articoli** — i tre pezzi non hanno link interni verso pagine italiane con gemello inglese. Nessuna modifica da includere nel commit oltre ai tre file.

## Deploy

- Commit `5fb5f9b` — `feat(i18n): versione inglese di 3 articoli (2026-10-20)`, 3 file, 90 inserimenti. Push su `main` riuscito (`d48280d..5fb5f9b`).
- GitHub Actions, workflow `deploy.yml`, run su `5fb5f9b` (creato 10:32:01Z): **success**.
  Nota: la prima lettura a +90 s dava `in_progress`, poi una lettura intermedia ha mostrato `queued` (probabile riassegnazione del runner); alla lettura successiva lo stesso SHA risultava `completed / success`.

## Controlli dal vivo (user-agent da browser)

Tutti `200`:

- `/en/2026/10/five-million-users-and-a-model-that-thinks-in-parallel/` → 200
- `/en/2026/10/hermes-learns-to-show-itself/` → 200
- `/en/2026/10/savings-banks-open-to-bitcoin-metaplanet-buys-a-listing-rules-arrive-late/` → 200
- `/2026/10/cinque-milioni-di-persone-un-modello-che-pensa-in-parallelo-la-settimana-di-venice/` → 200
- `/2026/10/hermes-impara-a-mostrarsi-la-sala-di-controllo-e-la-release-che-ripara-la-release/` → 200
- `/2026/10/la-banca-dei-risparmi-apre-al-bitcoin-metaplanet-compra-un-listino-le-regole-arrivano-in-ritardo/` → 200

Titoli: le tre pagine italiane mostrano ancora il titolo italiano nei `<title>`; le tre inglesi mostrano il titolo inglese.

Cambio lingua: presente e funzionante in entrambe le direzioni. Ogni pagina inglese contiene il link `hreflang=it title=Italiano>IT</a>` verso la gemella italiana, e la pagina italiana contiene il link `hreflang=en title=English>EN</a>` verso `/en/2026/10/hermes-learns-to-show-itself/` (verificato il caso campione; le tre pagine inglesi hanno tutte il link IT).

## Cose che non hanno funzionato

- Nessun errore di build o di pubblicazione.
- Solo un'osservazione di verifica, non un difetto del sito: con lo user-agent corto `Mozilla/5.0` Cloudflare (Bot Fight attivo) ha risposto `403` a una richiesta di controllo; con lo user-agent completo da browser le pagine tornano `200`. I controlli ufficiali sono stati rifatti con UA completo. Nessuna modifica fatta fuori dai file di competenza.
