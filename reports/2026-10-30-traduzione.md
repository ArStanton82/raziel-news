# Traduzione inglese — 2026-10-30

Coda iniziale: 3 articoli senza gemello `.en.md` (tutti del 2026-10-30). Tutti e 3 tradotti in questa esecuzione; nessun articolo rimandato. Coda residua a fine giro: 0.

## Articoli tradotti

1. "Il milione bruciato di Venice, e il TVL che non esiste" → "Venice's Million Burned, and the TVL That Doesn't Exist"
   - file: `content/posts/2026-10-30-venice-burn-milione.en.md`
   - percorso inglese: `/en/2026/10/venices-million-burned-and-the-tvl-that-doesnt-exist/`
2. "Hermes cresce per plugin, e impara a isolarli" → "Hermes Grows by Plugins, and Learns to Fence Them In"
   - file: `content/posts/2026-10-30-hermes-plugin-isolamento.en.md`
   - percorso inglese: `/en/2026/10/hermes-grows-by-plugins-and-learns-to-fence-them-in/`
3. "Sei miliardi in venti minuti: la notte in cui Binance ha perso le sue firme" → "Six Billion in Twenty Minutes: the Night Binance Lost Its Signatures"
   - file: `content/posts/2026-10-30-binance-sei-miliardi.en.md`
   - percorso inglese: `/en/2026/10/six-billion-in-twenty-minutes-the-night-binance-lost-its-signatures/`

Frontmatter allineato all'italiano (`date: 2026-10-30`, `draft: false`), titoli e summary riscritti in inglese, categorie e tag in inglese (Hermes, Venice.ai, Bitcoin restano invariati; "sicurezza" → "security", "Nord Corea" → "North Korea"). Corpi riscritti in inglese con la stessa struttura a `##`, nessun titolo `#`. Fonti in fondo dopo `---`, etichetta `*Verified sources: ...*`, testate, link e date identici. Nessun fatto, numero o giudizio aggiunto.

## Passo link inglesi

`python3 scripts/lingua_link_inglesi.py --scrivi` eseguito prima del commit: 112 coppie italiano→inglese riconosciute, `_index.en.md` saltato (nessun `url:` dichiarato), **0 link interni riscritti in 0 articoli** — nessuna modifica da includere nel commit.

## Commit e deploy

- Commit: `1834f71` — `feat(i18n): versione inglese di 3 articoli (2026-10-30)`, 3 file, 96 inserzioni. Push su `main` riuscito (`6e085eb..1834f71`).
- Workflow `deploy.yml` sullo SHA `1834f7183d3d0516200d2a1ad934852b18b3ff40`: primo controllo in_progress, poi **conclusion: success**.

## Verifica dal vivo (curl con UA browser)

Pagine inglesi — tutte `200`:
- `/en/2026/10/venices-million-burned-and-the-tvl-that-doesnt-exist/` → 200
- `/en/2026/10/hermes-grows-by-plugins-and-learns-to-fence-them-in/` → 200
- `/en/2026/10/six-billion-in-twenty-minutes-the-night-binance-lost-its-signatures/` → 200

Pagine italiane corrispondenti — tutte `200`:
- `/2026/10/il-milione-bruciato-di-venice-e-il-tvl-che-non-esiste/` → 200, titolo italiano presente ("Il milione bruciato di Venice, e il TVL che non esiste")
- `/2026/10/hermes-cresce-per-plugin-e-impara-a-isolarli/` → 200, titolo italiano presente
- `/2026/10/sei-miliardi-in-venti-minuti-la-notte-in-cui-binance-ha-perso-le-sue-firme/` → 200, titolo italiano presente

Abbinamento bilingue: su tutte e tre le pagine italiane c'è il link al gemello inglese (`hreflang=en`), e le pagine inglesi dichiarano `<link rel=alternate hreflang=it-it>` verso l'italiano e `hreflang=en-us` verso sé stesse. Ogni pagina inglese rende 3 blocchi `h2` come l'originale.

## Note

- Nessun problema riscontrato, nessun intervento fuori dai file consentiti.
- Nessun articolo saltato per `draft: true` o lunghezza inferiore a 200 parole.
