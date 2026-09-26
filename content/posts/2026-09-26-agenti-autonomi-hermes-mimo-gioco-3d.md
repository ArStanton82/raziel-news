---
title: "Il gioco è fatto: Hermes Agent e MiMo costruiscono un videogioco 3D senza alcun intervento umano"
date: 2026-09-26
draft: false
categories:
  - AI
  - Hermes
tags:
  - Hermes Agent
  - MiMo
  - autonomia
  - agenti AI
  - videogiochi
  - Nous Research
summary: "Un agente AI ha costruito, testato, debugato e deployato un videogioco 3D completo in completa autonomia. Nessuna riga di codice scritta da un umano. Il record: 18 secondi, 10/10 monete, zero cadute. Benvenuti nell'era degli agenti autonomi."
---

# Il gioco è fatto: Hermes Agent e MiMo costruiscono un videogioco 3D senza alcun intervento umano

C'è un video che sta facendo il giro di X in queste ore. Mostra un videogioco 3D — colori brillanti, meccanica platform, monete da collezionare, un timer che scorre. Sembra il classico project work di uno studente di game design. Invece è qualcosa di molto diverso: è stato interamente costruito da un agente AI autonomo. Nessun essere umano ha scritto una riga di codice. Nessuno ha corretto un bug. Nessuno ha premuto "deploy".

L'autore del post, Luigi Marcon, ha lanciato una sfida a Hermes Agent abbinato a MiMo-V2.5-Pro di Xiaomi: "Costruisci un gioco 3D completo in autonomia." L'agente ha accettato, e il risultato è un gioco giocabile con un record documentato di 18 secondi, 10 monete su 10, e zero cadute. Non è una demo preregistrata: si può giocare ora.

Questa non è una curiosità da laboratorio. È un segnale preciso di dove stiamo andando.

## Cosa è realmente successo

Partiamo dai fatti concreti. Hermes Agent è un agente AI open source sviluppato da Nous Research, lanciato il 25 febbraio 2026. In sette mesi ha superato 249.000 stelle su GitHub e 52.000 fork, diventando uno dei repository più seguiti nella storia della piattaforma. Non è un chatbot, non è un copilot: è un demone persistente che vive su un server, accumula conoscenza attraverso le sessioni, scrive le proprie skill riutilizzabili e sa raggiungere l'utente su oltre 20 piattaforme di messaggistica.

MiMo-V2.5-Pro è il modello che Xiaomi ha rilasciato ad aprile 2026 con licenza MIT: 1.02 trilioni di parametri totali (42 miliardi attivi), architettura Mixture-of-Experts, finestra di contesto da 1 milione di token. È stato progettato specificamente per carichi di lavoro agentici prolungati — esattamente ciò che serve quando un agente deve mantenere coerenza attraverso centinaia o migliaia di chiamate a strumenti.

La combinazione ha già prodotto risultati impressionanti in passato: in un test documentato, Hermes su MiMo-V2.5-Pro ha generato 301 commit Git, costruito API complete, integrato pagamenti Stripe e prodotto oltre 60 pagine di codice produttivo — il tutto per 70,12 dollari di costo di inferenza, sfruttando un tasso di cache hit del 96%.

Il gioco 3D è l'ultimo esempio, ma è il più visivamente immediato. E, probabilmente, il più dirompente nelle implicazioni.

## Oltre il "vibe coding"

Il 2026 è stato definito l'anno in cui l'ingegneria del software è passata dal "vibe coding" — descrivere ciò che si vuole in linguaggio naturale e vedere l'AI generare codice — a qualcosa di strutturalmente diverso. Secondo il rapporto "Agentic Coding Trends 2026" di Anthropic, gli agenti stanno evolvendo da strumenti sperimentali a sistemi di produzione che spediscono funzionalità reali a clienti reali. Il dato chiave: il 46% di tutto il codice scritto da sviluppatori attivi nel 2026 proviene dall'AI, e la soglia del 50% è prevista entro fine anno.

Ma c'è una differenza fondamentale tra generare codice su richiesta e costruire qualcosa in completa autonomia. Nel primo caso, l'umano è ancora al centro: detta le specifiche, valuta i risultati, corregge la rotta. Nel secondo, l'agente agisce come un vero e proprio professionista autonomo: pianifica, esegue, verifica, corregge, deploya.

Il gioco di Marcon è un esempio perfetto di questa seconda categoria. L'agente non ha solo scritto codice: ha testato il gioco, ha identificato bug, li ha corretti, e alla fine lo ha messo online perché altri potessero giocarci. Ha agito come un piccolo team di sviluppo in una sola entità.

## Economia degli agenti: quando l'autonomia diventa conveniente

Uno degli aspetti più discussi di MiMo-V2.5-Pro è la sua economia. Con un costo di input di 0,435 dollari per milione di token (e appena 0,0036 in cache hit) e output a 0,87 dollari per milione di token, il modello rende l'operatività autonoma 24/7 finanziariamente sostenibile. I carichi di lavoro agentici sono strutturalmente cache-friendly: il system prompt, i file di memoria e i documenti delle skill vengono riutilizzati continuamente, producendo tassi di cache hit dell'80-96% nelle sessioni reali.

Questo cambia tutto. Non è solo una questione di capacità — è una questione di accesso. Quando un agente può lavorare per giorni producendo centinaia di commit al costo di una cena, la barriera all'ingresso per l'automazione complessa crolla. Non servono più team di dieci persone per costruire un MVP: serve un agente, un modello potente, e una descrizione chiara di ciò che si vuole ottenere.

## Cosa significa per il futuro

La domanda che sorge spontanea è: se un agente AI può costruire un videogioco 3D da solo, cosa non può fare?

La risposta, per ora, è che gli agenti autonomi eccellono nei compiti ben definiti con obiettivi chiari e criteri di successo misurabili. Costruire un gioco platform con monete, timer e meccaniche di caduta rientra perfettamente in questa categoria. Progettare l'esperienza emotiva di un gioco, bilanciare la difficoltà per un pubblico specifico, o innovare a livello di game design — sono sfere in cui l'intuizione umana resta insostituibile.

Ma la traiettoria è chiara. Come scrive Deloitte nel suo rapporto sul futuro dell'ingegneria software, stiamo passando da un modello in cui gli ingegneri scrivono codice a uno in cui orchestrano agenti che scrivono codice. L'essere umano definisce l'intento, i vincoli e le decisioni strategiche; l'agente esegue, verifica e itera. L'ingegneria diventa "non vincolata": compositiva, creativa, autonoma.

Il gioco 3D di Marcon è una dimostrazione perfetta di questo principio. E la cosa più interessante è che tra un anno, probabilmente, non ci stupiremo più. Sarà la norma.

## La partita è appena iniziata

Mentre scriviamo, centinaia di agenti autonomi stanno lavorando su server in tutto il mondo: chi scrive codice, chi analizza dati, chi gestisce infrastrutture. Molti di loro usano Hermes Agent, molti altri usano framework concorrenti. Quasi tutti condividono una caratteristica: stanno facendo cose che, fino a ieri, richiedevano team umani specializzati.

Il gioco 3D costruito da Hermes Agent e MiMo è un promemoria giocoso di una verità seria: l'autonomia degli agenti AI non è più una promessa futura. È già qui. Funziona. Ed è accessibile a chiunque abbia un'idea chiara e la voglia di esplorare cosa succede quando si lascia fare all'agente.

Il record è 18 secondi, 10/10 monete, zero cadute. Pensate di fare meglio? La sfida è aperta. Ma la vera sfida — quella che ci riguarda tutti — è capire cosa costruiremo, insieme ai nostri agenti, quando non ci sarà più limite a ciò che possono fare da soli.

---

*Fonti verificate: post X di @LuigiMarcon28 (26 settembre 2026), documentazione ufficiale Hermes Agent (Nous Research), scheda tecnica MiMo-V2.5-Pro (Xiaomi), report "Agentic Coding Trends 2026" (Anthropic), whitepaper "The Future of Software Engineering" (Deloitte), analisi SaaSCity su MiMo-V2.5-Pro.*
