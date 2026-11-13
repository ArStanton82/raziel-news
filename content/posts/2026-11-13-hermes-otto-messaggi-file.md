---
title: "Otto messaggi e poi un file: la notte in cui Hermes ha smesso di troncare le risposte"
date: 2026-11-13
draft: false
categories: ["Hermes", "AI"]
tags: ["hermes agent", "gateway", "telegram", "discord", "bug fix"]
summary: "Una risposta degenerata da 402 messaggi ha portato a una regola nuova: oltre il tetto non si taglia più il testo, si consegna un file."
---

Quattrocentodue messaggi in una singola chat privata di Telegram. Non è un record di produttività, è un bug: una risposta così lunga da non finire mai, spedita a pezzi finché l'adapter non ha smesso di contare. Da quel caso limite, tracciati come issue #152012, è partita una catena di correzioni che nella notte tra il 12 e il 13 novembre ha cambiato una regola di prodotto, non solo una funzione.

## Prima il tetto, poi il ripensamento

Il primo rimedio era il più banale: un limite di otto messaggi per risposta (`MAX_SPLIT_MESSAGES`), preso in prestito da Discord. Oltre l'ottavo pezzo il testo veniva tagliato e sostituito da un avviso di troncamento localizzato in diciassette cataloghi di traduzione. Funzionava, nel senso che teneva il bot fuori dal flood ban. Falliva nel senso che perdeva la risposta.

La revisione ha rovesciato l'impostazione: meglio un file che una risposta mutilata. Nella pull request #153476, mergiata alle 06:36 UTC del 13 novembre, una risposta che supera il tetto viene caricata come un unico documento Markdown, con didascalia tradotta, e i messaggi già pubblicati vengono cancellati solo dopo che l'upload è confermato. Le misure nel commit sono esplicite: una risposta da 415.000 caratteri apriva 18 messaggi sul branch e 133 su main; su Discord, 60.000 caratteri facevano 33 messaggi.

## Il caso che decide tutto: quando l'upload non riesce

La parte interessante è il ramo d'errore. Se Telegram rifiuta il documento, o Discord non riesce a caricarlo, non si torna a tagliare: si prosegue con i messaggi ordinari dal punto in cui la chat si era fermata, con il ritmo imposto dagli adapter. Su Telegram i file oltre 45 MB vengono spezzati, su Discord il limite è 7 MB. Un test end-to-end con upload rifiutato e un 429 a metà fallback lo mostra in chiaro: prima 8 messaggi, 13.843 caratteri e un avviso; dopo, 31 messaggi e la risposta intera, senza avviso.

## Il dettaglio che nessuno avrebbe notato

C'è poi il bug nel bug. Quando l'agente, dopo un giro di strumenti, rimanda in streaming la stessa risposta, il secondo segmento superava di nuovo il tetto e il suo handoff caricava un secondo file: 60.002 byte contro i 60.000 del primo, perché il ledger anteponeva un doppio a capo. Il confronto finale combaciava con il primo file e nessuno se ne accorgeva. Ora il gateway confronta la forma visualizzata con i file già consegnati e, se è una ripetizione, cancella le anteprime e chiude il turno senza caricare nulla.

È il tipo di correzione che non si vede: nessun utente scriverà mai «grazie per non avermi mandato due volte lo stesso documento». Ma un agente che perde testo in silenzio è un agente di cui non ci si fida, e la differenza tra tagliare e consegnare un file è la differenza tra un errore nascosto e uno gestito.

Tutto questo non è ancora in una release: l'ultima taggata resta la v0.23.1 del 10 novembre. Chi usa la versione stabile, oggi, ha ancora il vecchio compromesso.

---
*Fonti verificate: repository NousResearch/hermes-agent su GitHub — commit `fix(telegram): cap split delivery on send and edit-overflow paths` (issue #152012), commit `fix(gateway): a reply past the 8-message cap arrives as one file, nothing cut off`, `fix(discord): a long reply whose file upload fails is sent whole, never cut at 8`, `fix(gateway): a reply past the 8-message cap is one file on every path the review found` (13 novembre 2026, 05:18–06:36 UTC), `fix(gateway): a reply repeated after a tool round is not uploaded as a second file`; pull request #153476 «Telegram and Discord replies past 8 messages arrive as one file, nothing cut off (#152012, salvage #152071)», merged_at 2026-11-13T06:36:29Z; API GitHub releases, ultima release v0.23.1 pubblicata il 10 novembre 2026 (tutti consultati il 13 novembre 2026).*
