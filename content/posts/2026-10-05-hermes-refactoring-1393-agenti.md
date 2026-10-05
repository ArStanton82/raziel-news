---
title: "Un milione di righe, 1.393 agenti: Hermes riscrive se stesso"
date: 2026-10-05
draft: false
categories: ["AI", "Hermes"]
tags: ["Hermes", "Nous Research", "agenti autonomi", "refactoring", "plugin"]
summary: "Hermes ha ripulito un milione di righe di codice in 19 ore con 1.393 subagenti: 19.300 dollari per un valore stimato di 1,8 milioni."
---

C'è un modo di raccontare l'automazione che insiste sulla velocità. Ce n'è un altro, più interessante, che insiste su ciò che resta dopo. Nous Research ha appena pubblicato il resoconto di un esperimento che merita di essere letto per entrambe le ragioni.

## Diciannove ore, 1.393 agenti

Il 2 settembre Teknium ha chiesto al suo agente Hermes di ripulire il repository dell'agente stesso. Il run principale è durato circa diciannove ore attive, ha dispiegato 1.393 subagenti e ha toccato un picco di 218 agenti simultanei. L'orchestratore ha diviso il codice in 36 gruppi non sovrapposti, assegnando a ogni worker un git worktree separato, con brief che indicavano cosa semplificare e quali interfacce preservare. Il PR è stato unito il 4 settembre.

I numeri finali: le righe di Python non di test sono passate da 1.063.826 a 698.363, in calo del 34,4 per cento. Il file più grande, gateway/run.py, è sceso da 34.847 a 5.512 righe; le funzioni oltre 300 righe da 192 a 2; la catena di if/elif più lunga da 92 rami a 9. Il costo stimato del modello è di circa 19.300 dollari, circa 25.000 con le sessioni di follow-up. La stima per farlo a mano era tra 150.000 e 1,8 milioni di dollari.

## La lezione che resta

Il punto non è il risparmio, ma il meccanismo. L'agente aveva accumulato una skill — hermes-agent-dev — costruita correggendo errori reali: è da lì che vengono le istruzioni su come preparare un PR e su come verificare una modifica. Il post non nasconde i costi: circa 65 punti di gestione delle eccezioni sono stati riscritti in modo scorretto e corretti solo grazie alla revisione della community; il numero di moduli e le dipendenze di import sono cresciuti; sei file superano ancora le 5.000 righe. A circa cinquanta minuti dall'inizio, la scadenza di un token di autenticazione ha ucciso il run, che è stato ripreso da una sessione separata.

## Un ecosistema in movimento

Attorno a questo nucleo cresce la comunità. Teknium ha confermato su X che il team si allarga di due o tre persone, con tre dedicate all'app mobile; il catalogo dei plugin conta otto voci ufficiali "testate", ma la revisione non è una certificazione di sicurezza: protegge dagli agenti malevoli, non garantisce che un plugin sia robusto. Restano poi le segnalazioni della community: il plugin Oh My Hermes 3.0 sarebbe stato inserito nel catalogo, e qualcuno è riuscito a far girare il runtime di Hermes direttamente su un telefono Android via Termux.

## Conclusione

La domanda utile non è se un agente possa fare il lavoro di un team. È cosa succede quando sbaglia: se esiste una rete — revisione umana, skill scritte, commit verificabili — capace di accorgersene e riparare. Il refactor di Hermes è convincente proprio perché racconta anche i suoi inciampi.

---
*Fonti verificate: Nous Research, "Refactoring Hermes with 1,393 agents" (nousresearch.com, settembre 2026, consultato il 5 ottobre 2026); analisi tecnica del refactor su hermes-agent-lab.com; documentazione ufficiale del Plugin Catalog di Hermes Agent; post su X di @Teknium e @HermesWatcher del 4-5 ottobre 2026. Nota: l'inserimento di Oh My Hermes 3.0 nel catalogo e il runtime su Android sono riportati da fonti di community e non confermati ufficialmente; il conteggio degli otto plugin ufficiali è dichiarato da Teknium su X.*
