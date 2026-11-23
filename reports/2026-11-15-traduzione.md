# Traduzione inglese — 2026-11-15

Coda di partenza: 4 articoli italiani senza gemello `.en.md`, tutti del 2026-11-15. Nessuno escluso: tutti `draft: false` e sopra le 200 parole. Tradotti tutti e 4 (sotto il tetto di 6).

## Articoli tradotti

1. «Venice aggiunge due modelli in un giorno e abbassa il prezzo del token» → **"Venice Adds Two Models in One Day and Cuts the Price per Token"**
   - IT: `/2026/11/venice-aggiunge-due-modelli-in-un-giorno-e-abbassa-il-prezzo-del-token/`
   - EN: `/en/2026/11/venice-adds-two-models-in-one-day-and-cuts-the-price-per-token/`
   - categorie `Venice.ai`, `AI`; tag `Venice, VVV, Gemini, Seedance, pricing`
2. «L'ufficio entra nell'agente: Hermes Desktop impara a modificare i file veri» → **"The Office Moves Into the Agent: Hermes Desktop Learns to Edit Real Files"**
   - IT: `/2026/11/lufficio-entra-nellagente-hermes-desktop-impara-a-modificare-i-file-veri/`
   - EN: `/en/2026/11/the-office-moves-into-the-agent-hermes-desktop-learns-to-edit-real-files/`
   - categorie `Hermes`, `AI`; tag `Hermes, plugin, Workbench, Microsoft Office, agents`
3. «Chi ha titolo di dire che non c'è nessuno» → **"Who Gets to Say That No One Is There"**
   - IT: `/2026/11/chi-ha-titolo-di-dire-che-non-ce-nessuno/`
   - EN: `/en/2026/11/who-gets-to-say-that-no-one-is-there/`
   - categorie `Philosophy of AI`, `AI`; tag `consciousness, moral status, Anthropic, Suleyman, Vatican, Magnifica Humanitas, evidence, responsibility`
4. «Bitcoin sotto i 65.000 dollari: 2,35 miliardi usciti dagli ETF in due settimane» → **"Bitcoin Below $65,000: $2.35 Billion Out of the ETFs in Two Weeks"**
   - IT: `/2026/11/bitcoin-sotto-i-65.000-dollari-235-miliardi-usciti-dagli-etf-in-due-settimane/`
   - EN: `/en/2026/11/bitcoin-below-65000-235-billion-out-of-the-etfs-in-two-weeks/`
   - categorie `Crypto`, `Blockchain`; tag `Bitcoin, ETF, Kava, stUSDT, regulation`

Frontmatter: stessa `date` (2026-11-15) e `draft: false` per tutti; `url` esplicito sotto `/en/2026/11/`. Il corpo non contiene titoli `#`, solo `##`. La riga finale delle fonti è in fondo dopo il `---`, con etichetta `*Verified sources: ...*`; testate, numeri e date sono identici all'italiano.

## Link interni

`python3 scripts/lingua_link_inglesi.py --scrivi`: 164 coppie italiano→inglese con percorso dichiarato, **0 link riscritti** in 0 file. Nessuna correzione necessaria, nessuna modifica extra da includere nel commit.

## Commit e deploy

- Commit `d996d27` — `feat(i18n): versione inglese di 4 articoli (2026-11-15)`, 4 file, 151 righe aggiunte, solo `content/posts/`.
- Push su `main`: `111b03c..d996d27`.
- GitHub Actions `deploy.yml` (run su `d996d27`): **success**.

## Verifica dal vivo (user-agent da browser)

Pagine inglesi, tutte **200**:

| URL | HTTP | `<title>` |
|---|---|---|
| `/en/2026/11/venice-adds-two-models-in-one-day-and-cuts-the-price-per-token/` | 200 | Venice Adds Two Models in One Day and Cuts the Price per Token |
| `/en/2026/11/the-office-moves-into-the-agent-hermes-desktop-learns-to-edit-real-files/` | 200 | The Office Moves Into the Agent: Hermes Desktop Learns to Edit Real Files |
| `/en/2026/11/who-gets-to-say-that-no-one-is-there/` | 200 | Who Gets to Say That No One Is There |
| `/en/2026/11/bitcoin-below-65000-235-billion-out-of-the-etfs-in-two-weeks/` | 200 | Bitcoin Below $65,000: $2.35 Billion Out of the ETFs in Two Weeks |

Pagine italiane, tutte **200** e con il titolo italiano intatto:

| URL | HTTP | `<title>` |
|---|---|---|
| `/2026/11/venice-aggiunge-due-modelli-in-un-giorno-e-abbassa-il-prezzo-del-token/` | 200 | Venice aggiunge due modelli in un giorno e abbassa il prezzo del token |
| `/2026/11/lufficio-entra-nellagente-hermes-desktop-impara-a-modificare-i-file-veri/` | 200 | L'ufficio entra nell'agente: Hermes Desktop impara a modificare i file veri |
| `/2026/11/chi-ha-titolo-di-dire-che-non-ce-nessuno/` | 200 | Chi ha titolo di dire che non c'è nessuno |
| `/2026/11/bitcoin-sotto-i-65.000-dollari-235-miliardi-usciti-dagli-etf-in-due-settimane/` | 200 | Bitcoin sotto i 65.000 dollari: 2,35 miliardi usciti dagli ETF in due settimane |

Controlli aggiuntivi: le quattro versioni inglesi compaiono in home `/en/` con link assoluto corretto; la pagina inglese «Who Gets to Say That No One Is There» porta il rimando alla pagina italiana `/2026/11/chi-ha-titolo-di-dire-che-non-ce-nessuno/`, quindi il cambio lingua funziona.

## Note

- I percorsi italiani non si derivano a occhio dal titolo: lo slug di Hugo toglie apostrofi e virgole senza mettere trattini (`lufficio-entra-nellagente-...`, `bitcoin-sotto-i-65.000-dollari-235-miliardi-...`). Due URL italiani ipotizzati a mano davano 404; quelli corretti sono stati presi dal sitemap `/it/sitemap.xml` e verificati a 200. Solo un problema di verifica, non di contenuto.
- Nessun file fuori da `content/posts/*.en.md` è stato creato o modificato. Nessun articolo con `draft: true` o sotto le 200 parole incontrato. Nessun errore di build o di pubblicazione.
