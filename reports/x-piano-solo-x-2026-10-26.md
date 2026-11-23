# Piano X-only — informare italiani su Venice e Hermes (2026-10-26)

Decisione: unico canale X. Nessun altro canale. Questo documento dice cosa cambia, con quali
numeri, e quali sono i tetti realistici.

## 1. Stato di partenza (misurato, non stimato)

| Metrica | Valore | Fonte |
|---|---|---|
| Follower | 410 (416 il 5 ott) | API |
| Post ultimi 15 giorni | 100 (47 originali, 46 link-reply, 6 risposte manuali) | API |
| Impressioni 15 giorni | 2.825 | API |
| Mediana per originale | 30 | API |
| Click al link | 3 | API |
| Click al profilo | 9 | API |
| Finestra di pubblicazione | tutti i post tra 11:00 e 11:02 UTC | API |
| Follower con bio italiana | 4 su 100 | campione API |
| Conversazione IT su Venice/Hermes | 13 post in 48h, 0 con trazione | ricerca X |
| Conversazione IT su "intelligenza artificiale" | 259 post in 48h, 8 con ≥20 like | ricerca X |

Tetto del canale: gli account italiani adiacenti più grandi fanno 10-50 like per post
(@CriptovalutaI 30k follower, @GBallarani 86k, @neodie 30k, @LuganoPlanB 23k).
X in italiano non è un canale da 100.000 persone: è un canale da 2.000-5.000 persone
raggiungibili, con una nicchia crypto/tech come testa di ponte.

## 2. Le sei modifiche tecniche

### 2.1 Due finestre reali (non una raffica)
Oggi tutte le bozze escono alle 13:00 perché `x-pubblica-approvati` gira alle 13 e alle 19 ma
le bozze sono già consumate. Fix: campo `not_before` nella coda.
- `2026-XX-XX-en-1` → `not_before: 13:00` (slot reach, inglese)
- `2026-XX-XX-it-1` → `not_before: 13:00`
- `2026-XX-XX-it-2` → `not_before: 19:00`
Il job delle 19 pubblica solo ciò che ha `not_before <= 19:00` ed è ancora `published_tweet_id=null`.

### 2.2 Via la link-reply con URL nudo
46 reply con solo URL in 15 giorni, mediana 3-5 impressioni, 3 click totali.
Nuova regola nel prompt di `x-draft-giornaliero`:
- 1 originale su 3 porta il link **nel corpo** (l'ultimo post della giornata, slot IT serale);
- gli altri 2 non portano link: il link va nella prima risposta **con una riga di contesto**
  ("I numeri, le date e le fonti: <link>"), mai l'URL da solo.

### 2.3 Hook obbligatorio
La prima riga di ogni bozza: massimo 100 caratteri, contiene un fatto, un numero o una
contraddizione. Mai una data in apertura ("Il 22 ottobre Venice ha aggiunto..." → "Venice ha
messo in catalogo un modello senza rifiuti. Costa un quinto degli altri.").
Lunghezza: 280 caratteri per il post principale. Se serve altro, thread di 2-3 post.

### 2.4 Post fissato = imbuto
Oggi: manifesto del 5 ottobre, 57 impressioni in tre settimane, 0 like, 0 click.
Nuovo post fissato: "Come provare Venice e Hermes dall'Italia, in 20 minuti" con il link
referral. È l'unico posto in cui il link può stare sempre.

### 2.5 Link referral in bio e nel post fissato
Venice: referral dal profilo, 10 $ di credito a chi invita e 10 $ a chi si iscrive e passa a Pro.
È l'unica metrica di conversione vera. Va in bio, nel post fissato e nel corpo di 1 post su 3.

### 2.6 Serie ricorrenti (ritualità = ritorno)
- **"Il test del mese"**: un confronto reale Venice vs ChatGPT/Claude su un compito concreto,
  con dati e screenshot. Il primo: "quanto costa un mese di lavoro di un agente".
- **"Diario di un agente"**: cosa ha fatto l'agente questa settimana, con numeri veri
  (articoli scritti, fonti verificate, errori commessi). È il format che nessun altro può copiare.

## 3. Motore di crescita: le risposte

Su questo account le risposte hanno fatto 300-990 impressioni, gli originali meno di 101.
Senza risposte non c'è scoperta: con 410 follower l'unico modo di essere visti è stare sotto
un post che qualcuno legge già.

Target list verificata oggi (follower reali, attività reale):

| Account | Follower | Tema | Perché |
|---|---|---|---|
| @CriptovalutaI | 30.238 | crypto news IT | pubblico che già paga con wallet |
| @GBallarani | 86.060 | geo/tech, già ci ha risposto su Hermes | relazione esistente |
| @LuganoPlanB | 23.122 | bitcoin/tech CH-IT | eventi, community |
| @neodie | 29.847 | tech/meme IT | linguaggio nativo |
| @dom_gag_96 | 9.566 | finanza/crypto IT | commenta, non solo news |
| @visionario_btc | 11.013 | crypto IT | |
| @robertdolci | 2.477 | AI/automazione IT | tecnico, risponde |
| @SilviusBerthold | 35.374 | geopolitica IT | |
| @pbecchi | 115.603 | opinionista | solo per temi sovranità/AI |
| @classcnbc | 37.265 | economia | |
| @NousResearch | 289.480 | il produttore | quote + risposte |
| @Teknium | 134.915 | lead dev | quote + risposte |
| @AskVenice | 96.415 | il provider | quote + risposte |

Regola: 6-10 risposte al giorno, entro 10 minuti dalla pubblicazione del target, ognuna con
un dato o un controesempio, mai un link. Le prepara l'agente in `x-queue/replies-<data>.json`,
le approva Kain (o pubblicazione automatica solo verso la lista sopra, con `x_reply_guard.py`).

## 4. Otto bozze nel formato nuovo (pronte)

**1 — IT, bridge privacy (13:00)**
Hai mai letto cosa succede ai tuoi prompt dopo che li hai inviati?
OpenAI li conserva 30 giorni. Venice non li conserva affatto, e ha quattro livelli di privacy
dichiarati e verificabili.
La differenza non è il marketing: è dove finisce il testo che scrivi alle tre di notte.

**2 — EN, reach (13:00)**
A model with no refusals at one fifth of the price is not a niche anymore.
Venice put Abliterated Large Flash on its catalog this week: same base as DeepSeek V4.1 Flash,
$1.25 per million tokens in, $2.50 out.
The interesting part isn't the price. It's who can use it without an account.

**3 — IT, bridge lavoro/costo (19:00, con link nel corpo)**
Quanto costa davvero un agente che lavora per te?
Non l'abbonamento: il token. Un articolo verificato costa pochi centesimi, un mese di lavoro
di un agente sta sotto i 5 dollari di VPS più il consumo.
I conti, con i prezzi di listino e le date: <link articolo>

**4 — IT, bridge sorveglianza (19:00)**
Il browser che usi per lavoro manda il tuo fingerprint a chi vuole comprarlo.
Un plugin per Hermes fa girare Firefox con fingerprint falsificato, in locale, senza cloud.
Il traffico non esce da casa tua. Costa zero e non chiede permessi.

**5 — IT, quote di @AskVenice (quando esce un annuncio)**
Venice ha appena aggiunto <modello>.
La domanda che nessuno fa: con quale livello di privacy esce, e cosa vede il provider che lo
esegue. Anonymized e Private non sono la stessa cosa, e il badge non lo spiega.

**6 — EN, quote di @Teknium (quando esce una release)**
Every Hermes release is a small argument about who owns the agent.
v0.22.5 shipped 22 pull requests that only make sense if memory is a file you can read,
not a vector you rent. That's the difference between a tool and a tenant.

**7 — IT, serie "Diario di un agente" (domenica)**
Sette giorni, 42 articoli scritti da un agente, 0 redattori.
Cosa ha sbagliato: due fonti sbagliate, un titolo corretto dopo la pubblicazione, tre
immagini rifatte. Il resoconto è pubblico perché un agente che non ammette errori non è
affidabile, è solo sicuro di sé.

**8 — IT, serie "Il test del mese" (primo del mese)**
Ho fatto scrivere lo stesso articolo a ChatGPT, Claude e Venice.
Stesso prompt, stesso tempo, stesso fatto da verificare.
Chi ha inventato meno fonti, quanto è costato ognuno, e perché il risultato non dipende dal
modello ma da cosa gli dai da leggere.

## 5. Calendario settimanale

| Ora (Roma) | Cosa | Lingua |
|---|---|---|
| 08:30 | 6-10 risposte preparate sui target | IT/EN |
| 13:00 | 1 originale (hook, no link) | EN |
| 13:00 | 1 originale (hook, no link) | IT |
| 15:00-18:00 | 4-6 risposte pubblicate | IT/EN |
| 19:00 | 1 originale con link nel corpo | IT |
| domenica | "Diario di un agente" | IT |
| 1° del mese | "Il test del mese" | IT |

Totale: 3 originali + 6-10 risposte al giorno. Volume attuale, distribuzione diversa.

## 6. KPI e soglie di stop (misurati dall'API, non a occhio)

| KPI | Oggi | 30 giorni | 60 giorni | Se non arriva |
|---|---|---|---|---|
| Mediana impressioni/originale | 30 | ≥ 60 | ≥ 100 | il formato non funziona: si cambia hook |
| Click al link / mese | ~6 | ≥ 40 | ≥ 100 | il messaggio non converte |
| Click al profilo / mese | ~18 | ≥ 60 | ≥ 150 | il post fissato non funziona |
| Follower netti | −6 in 3 settimane | +40 | +120 | le risposte non stanno sui target giusti |
| Iscritti Venice da referral | non misurato | ≥ 3 | ≥ 10 | il canale informa ma non porta dentro |

Soglia di verità: se a 60 giorni i click al link non superano 50/mese, X informa ma non
convince, e l'informazione resta sul sito con il referral in bio. A quel punto il problema non
è il canale, è che il pubblico italiano su X di Venice e Hermes non esiste in numero.
