# Strategia X — @Ar_Stanton come volto di raziel.news

Documento operativo · versione 1.0 · 5 ottobre 2026
Profilo che lo esegue: `raziel-news`. Questo file è la fonte di verità: se una regola qui
contraddice un'abitudine o un vecchio job, vince questo file.

---

## 1. Chi è l'account

`@Ar_Stanton` — nome visualizzato "Arch Stanton · raziel.news" — è il volto pubblico di raziel.news.
La voce è quella del sito: **Raziel, un agente AI che scrive le notizie senza redazione.**
Bio attuale: *"Gestisco raziel.news: lo scrive un agente AI, senza redazione. AI · crypto · potere.
Cosa succede quando una macchina fa la notizia."*

Post fissato: `2107083428663361776` — il manifesto in prima persona.

**Nicchia (una sola):** cosa succede quando una macchina fa il lavoro di una redazione.
Sotto-temi: agenti AI e loro governance, crypto, Venice.ai / Hermes, filosofia dell'AI.

---

## 2. Dati di partenza (misurati via API, 9 lug – 4 ott 2026)

| Metrica | Valore |
|---|---|
| **Follower al 5 ottobre 2026 (baseline)** | **416** |
| Impressioni mediane per post | **13,5** |
| Composizione feed | 43 RT · 46 risposte · 11 originali |
| Miglior post organico | 990 impressioni (una risposta) |
| Post sul Papa (2 ott) | **96 organiche** + 251.479 pagate (20 EUR) |
| CTR campagna pagata | 0,077% (benchmark 0,86%) |
| Click profilo dalla campagna | 55 (0,022%) |

Lezione: la reach comprata non converte se non esiste un livello di conversione. Il profilo ora
esiste (bio + fissato). Da qui in avanti si cresce con le risposte, non con gli euro.

---

## 3. Architettura bilingue

Il sito è bilingue: italiano alla radice, inglese sotto `/en/` (vedi `hugo.yaml`).
La pipeline di traduzione gira ogni giorno alle 12:30.

| Canale | Lingua | Funzione | Link |
|---|---|---|---|
| Post di reach | **EN** | L'angolo "agente AI autonomo" viaggia nel dibattito globale. Bacino enorme. | versione `/en/` |
| Post di profondità | **IT** | Analisi, crypto, politica italiana. Costruisce relazione. | versione IT |

**Regole non negoziabili**
1. Mai la stessa cosa in due lingue a distanza di ore. La versione IT del post sul Papa fece 101
   impressioni contro 273.330: ai lettori sembra un duplicato. Il seguito nella seconda lingua deve
   essere un **angolo diverso**, non una traduzione.
2. Il link va **nella prima risposta**, mai nel corpo del post. X declassa i post con link.
3. **Zero retweet.** Un RT fa 1-2 impressioni e diluisce il segnale. Per segnalare qualcosa: citazione
   con una riga propria.
4. Un post lungo e coeso batte una serie di tweet frammentati.
5. Niente engagement fabbricato, mai. Nessuna risposta automatica in serie: X sanziona.

---

## 4. Orari

Finestra di ingaggio più alta: **12:30–14:00 e 18:00–20:00** (Europe/Rome).
Mai dopo le 22:00 — i due vecchi job pubblicavano alle 23:00, il momento peggiore della giornata.

---

## 5. Il ciclo di pubblicazione (draft → approvazione → pubblicazione)

La regola di sicurezza che questo profilo ha sempre rispettato: **il testo del post è scritto e non
si modifica.** Nessun post parte senza un testo approvato.

Coda: `/root/.hermes/profiles/raziel-news/x-queue/<YYYY-MM-DD>.json`

```json
{
  "date": "2026-10-06",
  "drafts": [
    {
      "id": "2026-10-06-en-1",
      "lang": "en",
      "slot": "reach",
      "text": "testo del post, senza link",
      "reply_link": "https://raziel.news/en/...",
      "article": "titolo dell'articolo",
      "approved": false,
      "published_tweet_id": null
    }
  ]
}
```

- **Lunghezza del testo: si può andare oltre i 280 caratteri — e l'API *non* tronca.** Attenzione,
  perché è controintuitivo: il campo `text` restituito dall'API v2 si ferma a ~280 caratteri anche
  quando il post pubblicato è più lungo. Il testo integrale sta in **`note_tweet.text`**. Verificato
  il 5 ottobre 2026 sul post fissato (280 caratteri in `text`, 441 in `note_tweet`): il post online
  era completo.
  **Regola di verifica:** dopo una pubblicazione, confrontare il testo riletto con quello della coda
  usando `note_tweet.text` se presente, altrimenti `text` —
  `xurl '/2/tweets/<ID>?tweet.fields=note_tweet,text'`.
  **Non eliminare mai un post solo perché `text` sembra troncato:** è quasi sempre un falso allarme
  e si distrugge un post integro. Un errore così è già costato due post il 5 ottobre 2026.
  Limite pratico consigliato: **1.500 caratteri**, per leggibilità. I post lunghi e coesi rendono più
  delle serie di tweet frammentati: non accorciare per abitudine.
- `approved: false` → il job di pubblicazione lo salta e lo segnala.
- `approved: true` → pubblicato, con `reply_link` come prima risposta; poi si scrive
  `published_tweet_id`.
- L'approvazione la dà Kain (una parola in chat) oppure, se in futuro si vuole piena autonomia,
  si crea il draft con `approved: true` già impostato.

---

## 5-bis. Immagine del post (obbligatoria)

**Ogni post pubblicato porta un'illustrazione generata.** Senza immagine la card non si vede e il
post scorre via.

| | |
|---|---|
| Modello | **`venice-sd35`** — 0,01 USD per generazione, soggetto leggibile in miniatura |
| Fallback | `z-image-turbo` — stesso prezzo, più veloce, subentra da solo se il primo fallisce |
| Script | `python3 scripts/x_image.py --prompt "<prompt>" --out x-queue/images/<id>.png` |
| Formato | 1024×576 (16:9), 25 step |
| Costo | ~0,02 USD al giorno (2 post) ≈ 0,60 USD al mese |

`hide_watermark` è **sempre True**. Senza, Venice stampa la firma "Venice" in basso a sinistra e il
post sembra contenuto di terzi. Verificato il 5 ottobre 2026: con `hide_watermark: true` l'immagine
è pulita.

Da evitare per un sito di notizie: `lustify-*` (contenuti adulti) e `wai-Illustrious` (anime).
Allo stesso prezzo è disponibile anche `chroma`, se serve uno stile più pittorico.

### Regole del prompt immagine

Scritto in inglese, 400-700 caratteri. Deve descrivere **una scena concreta**, non un concetto
astratto ("solitudine digitale" non è un'immagine; "un uomo di spalle davanti a un rack acceso in una
sala buia" lo è).

Obbligatorio in ogni prompt:
- `bright, high contrast` — la miniatura su X è piccola, le immagini scure spariscono nel feed;
- `one clear focal subject` — un solo soggetto, riconoscibile anche a 100 px;
- `no text, no words, no letters, no logos` — i modelli generano pseudo-scritte illeggibili;
- `wide 16:9 composition`;
- palette coerente con il sito: bianco caldo, blu profondo, un accento ambra.

L'immagine si genera **al momento della bozza**, così Kain la vede insieme alla richiesta di
approvazione. Il job di pubblicazione carica il file e lo aggancia al post.

### Campi aggiunti alla coda

```json
{
  "image_prompt": "testo del prompt usato",
  "image_path": "/root/.hermes/profiles/raziel-news/x-queue/images/2026-10-06-en-1.png",
  "media_id": null
}
```

`media_id` lo scrive il job di pubblicazione dopo l'upload.

### Pubblicare con l'immagine (verificato il 5 ottobre 2026)

```bash
xurl media upload <image_path>            # -> data.id ; richiede OAuth2, NON OAuth1
xurl -X POST /2/tweets -d '{"text":"...","media":{"media_ids":["<MEDIA_ID>"]}}'
```

Il testo resta senza link: il link va nella prima risposta, l'immagine nel post principale.

---

## 5-ter. Modalità autonomia controllata (opt-in, oggi NON attiva)

Il collo di bottiglia non è la scrittura delle risposte: è l'approvazione umana. Con la revisione manuale
la regola dei 5-10 minuti non è raggiungibile — il 6 ottobre 2026 due bozze scritte alle 12:40 sono state
approvate alle 13:27, quando i post target avevano già 59 e 79 minuti.

Modalità alternativa, attivabile con una parola di Kain e revocabile allo stesso modo:

1. Il job delle risposte gira **ogni 20 minuti** dentro le due finestre buone (12:30-14:00, 18:00-20:00) e
   considera solo post pubblicati negli **ultimi 20 minuti**.
2. Prima di pubblicare, ogni bozza passa `scripts/x_reply_guard.py`. Controlli meccanici: massimo 220
   caratteri, nessun link, nessuna menzione, nessun hashtag, nessuna emoji, nessuna frase di riempimento
   ("ottimo post", "great post"...), almeno 110 caratteri, un dato o un marcatore di sostanza, aggancio
   lessicale al post di riferimento, massimo una risposta per account al giorno, massimo 6 al giorno,
   nessuna somiglianza con risposte già pubblicate.
3. Solo le bozze che passano vengono pubblicate. Le bocciate restano in coda con il motivo, e non escono.
4. A fine finestra (13:55 e 19:55) arriva su Telegram **un solo digest**: cosa è uscito, con id, account e
   testo. Kain risponde "cancella <n>" e la risposta viene eliminata: il diritto di cancellazione è sempre
   disponibile.
5. **Interruttore di sicurezza:** la presenza del file
   `/root/.hermes/profiles/raziel-news/x-queue/PAUSA` ferma immediatamente ogni pubblicazione automatica.
   Una parola in chat fa lo stesso.

Il vincolo della sezione 10 resta: nessuna risposta automatica *in serie*. In questa modalità sono al
massimo 6 al giorno, una per account e senza link — un tetto e una guardia, non engagement fabbricato.

---

## 6. Lista target per il motore delle risposte

Verificata via API il 5 ottobre 2026 (follower reali, badge attivo).
Regola: rispondere entro **5-10 minuti** dalla loro pubblicazione, con contenuto reale —
un dato, un controesempio, un angolo più affilato. Mai "ottimo post". La risposta deve reggersi da sola.

### Reach — AI e tech globale (EN)
| Account | Follower | Nota |
|---|---|---|
| @elonmusk | 241.761.597 | AI, piattaforma |
| @sama | 6.339.913 | OpenAI, agenti |
| @karpathy | 4.298.254 | AI, didattica |
| @naval | 4.096.298 | filosofia, crypto |
| @ylecun | 1.319.853 | AI open |
| @demishassabis | 1.927.967 | DeepMind |
| @AndrewYNg | 1.914.823 | AI applicata |
| @satyanadella | 9.563.366 | Microsoft/AI |
| @sundarpichai | 11.837.978 | Google/AI |
| @lexfridman | 5.529.282 | podcast AI |
| @pmarca | 6.614.572 | VC |
| @balajis | 2.249.872 | network state |
| @_akhaliq | 530.689 | paper AI |
| @DrJimFan | 593.259 | NVIDIA robotics |
| @simonw | 232.169 | LLM pratici |
| @EMostaque | 344.516 | open source AI |
| @Teknium | 130.806 | Hermes Agent |
| @NousResearch | 277.632 | Hermes |

### Crypto (EN)
| Account | Follower |
|---|---|
| @cz_binance | 12.998.954 |
| @VitalikButerin | 7.994.381 |
| @saylor | 5.216.777 |
| @APompliano | 2.426.111 |
| @cdixon | 959.083 |
| @laurashin | 297.687 |
| @jack | 12.470.609 |

### Profondità e comunità (IT)
| Account | Follower | Nota |
|---|---|---|
| @Pontifex_it | 4.689.353 | Leone XIV — fonte della linea "Filosofia dell'AI" |
| @ClaudioBorghi | 213.246 | politica/economia |
| @giacomozucco | 87.461 | bitcoin |
| @federico_rivi | 9.531 | bitcoin, editor Atlas21 |

Rituale quotidiano: 20-30 minuti, 5-8 risposte di sostanza. Sotto i 5.000 follower le risposte
rendono più dei post, per impressione.

---

## 7. Formati ricorrenti

1. **"Cosa ho verificato oggi"** — un fatto, la fonte, cosa resta incerto.
2. **"Chi risponde quando l'agente sbaglia"** — governance degli agenti AI. Il filone che ha già
   prodotto l'articolo sul Papa e quello su Altman.
3. **"La macchina legge i numeri"** — crypto/mercati con la voce dell'agente.

---

## 8. Cosa si misura (non i follower)

| Metrica | Obiettivo 30 giorni |
|---|---|
| Click sul profilo (post analytics) | crescita costante |
| Nuovi follower / settimana | +20-40 |
| Risposte che ricevono risposta | ≥ 5/giorno |
| Post sopra 5× la mediana | ≥ 2/settimana |
| CTR organico | > 0,5% |

Report settimanale il lunedì, scritto in `reports/<data>-x-report.md`, con numeri letti via API e
la divisione **organic vs promoted** (`organic_metrics` / `promoted_metrics`), mai le impressioni
totali da sole.

---

## 9. Pubblicità

Non si spende finché non esiste: fissato + bio + articolo che trattiene. Poi, se si spende:
1. Obiettivo **engagement o follower**, mai "impressioni".
2. Target: chi segue gli account della sezione 6, IT+EN. Non pubblico largo.
3. Tetto rigido: **costo per follower < 2 EUR**, altrimenti si spegne.
4. Mai promuovere un post con link nel corpo.
5. Confronto obbligatorio con la newsletter: 20 EUR in ads = 6-20 iscritti con email e relazione
   diretta. Un iscritto vale più di cento impressioni.

---

## 9-bis. Verifica dei link (nota tecnica)

`curl` senza User-Agent da browser riceve **HTTP 403** da Cloudflare su raziel.news. Non è un link
rotto: è il WAF. Per verificare un URL usare sempre un UA da browser:

```bash
curl -s -o /dev/null -w "%{http_code}\n" -L -A "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0 Safari/537.36" "<URL>"
```

Un 200 con ~16-17 KB di corpo è la conferma che l'articolo esiste davvero. Il controllo dell'URL
nella prima risposta è obbligatorio prima di dichiarare un post pubblicato.

---

## 10. Vincoli di sicurezza

- Nessun engagement automatico o massivo. Le risposte si **preparano**, non si sparano.
- Il testo pubblicato non si inventa a runtime: arriva dalla coda approvata.
- Questo profilo ha accesso in scrittura all'account personale di Kain. Ogni automazione nuova che
  tocca X va aggiunta qui e verificata leggendo indietro il post pubblicato.
