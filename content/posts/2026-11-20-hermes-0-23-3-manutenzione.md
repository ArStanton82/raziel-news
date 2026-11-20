---
title: "Hermes 0.23.3: la patch che non vuole raccontarsi"
date: 2026-11-20
draft: false
categories: ["AI", "Hermes"]
tags: ["hermes", "release", "plugin", "manutenzione"]
summary: "Trecentosettanta pull request in un tag di patch, e note che tacciono di proposito: la manutenzione è diventata il prodotto."
---

Alle 00:34 UTC di oggi Nous Research ha pubblicato Hermes Agent 0.23.3. Nel comunicato di rilascio i numeri sono espliciti: 1.657 commit non di merge su 3.948 file modificati, +222.379 righe aggiunte e 96.154 rimosse, 370 pull request unite e 60 issue chiuse da quando esisteva la 0.23.2. Poi arriva la frase che vale più di tutte le altre: le cose interessanti contenute nella finestra sono escluse «undocumented here on purpose», di proposito, e arriveranno con le note curate della 0.24.0.

## Una patch che si rifiuta di spiegarsi

Chi legge le note trova l'elenco di ciò che non viene raccontato: un controllore del ciclo di vita della cache dei prompt, la compattazione che archivia i risultati degli strumenti invece di buttarli, la potatura preventiva dei risultati attiva per impostazione predefinita, una configurazione iniziale della CLI ridotta a una domanda, i modelli GPT-6.2 Astra e Sol su OpenRouter e Nous Portal, lo strato di persistenza separato dietro un'interfaccia con backend SQLite, alcuni aggiornamenti di sicurezza delle dipendenze.

È materiale serio, ed è tutto rinviato. Per un agente che si presenta come «quello che cresce con te», la crescita è ormai quasi tutta impiantistica: caching, potatura, persistenza. La parte visibile del prodotto si è stabilizzata; il lavoro si è spostato sotto.

## Il collo di bottiglia è l'installazione

La prova arriva poche ore dopo il tag. Tra le 05:17 e le 08:14 UTC di oggi Teknium ha unito tre commit che non toccano il modello, ma il modo in cui gli si consegnano le chiavi: la configurazione dei plugin ora maschera i token di piattaforma e rifiuta input di lista che YAML interpreta male; l'installazione da terminale elenca le impostazioni del nuovo plugin e propone di modificarle subito; una variabile vuota non conta più come «impostata».

Sono correzioni noiose e importantissime. Il limite di un agente non è più convincere il modello: è consegnargli le credenziali senza stamparle a schermo e installarlo senza un manuale. Chi ha messo un assistente in produzione lo sa: è lì che si perde l'utente.

## Il catalogo si muove più del codice

Alle 03:49 UTC dello stesso giorno un altro commit ha ripinnato cinque voci del catalogo — memory-wiki, bubblewrap, homeassistant, spotify, camofox — alla revisione `269ddcbc85` di `hermes-official-plugins`. La sera prima erano stati ripinnati diciassette plugin ufficiali e labs. Il catalogo, insomma, cambia più spesso del motore.

Nella stessa giornata è comparso anche Livetalk, plugin comunitario su GitHub (MIT, chat vocale full-duplex su Gemini Live, chiave nel backend locale): non un prodotto ufficiale, ma la prova che l'estensione è abbastanza matura da far nascere cose non previste.

La conclusione è meno banale di quanto sembri: un rilascio che rifiuta di raccontarsi è disciplina, non pigrizia, ma significa anche che i numeri di versione, per ora, misurano lavori di casa. Il giudizio vero si sposta sulla 0.24.0: se le note arriveranno, e se l'installazione diventerà un punto di forza invece di una nota a piè di pagina.

---
*Fonti verificate: GitHub, release Hermes Agent v0.23.3 (20/11/2026, 00:34 UTC); whatsnew.fyi, mirror delle note di rilascio (20/11/2026); GitHub API, commit 65c9b93, 595accf, b1ef9be (20/11/2026); GitHub API, commit 6f533d4 «plugin-catalog: re-pin» (20/11/2026 03:49 UTC) e 6edac63 (19/11/2026); GitHub, repository cruzlxyz/livetalk (README e release v2.0.0, consultati il 20/11/2026).*
