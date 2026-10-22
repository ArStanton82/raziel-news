---
title: "Hermes chiude il keynote di Nvidia, e il catalogo diventa il prodotto"
date: 2026-10-22
draft: false
categories: ["Hermes", "AI"]
tags: ["hermes-agent", "nous-research", "nvidia", "gtc-berlin", "plugin", "meshy"]
summary: "Jensen Huang chiude GTC Berlin con una demo di Hermes Agent, mentre Nous rilascia la v0.22.4 e il plugin 3D Meshy."
---
C'è un momento, in ogni tecnologia, in cui smette di essere una cosa che si mostra e diventa una cosa su cui si costruisce. Per Hermes Agent quel momento potrebbe essere la scena finale del keynote di Jensen Huang a GTC Berlin, il 21 ottobre: non un annuncio di prodotto, ma una dimostrazione usata come chiusura, con il capo di Nvidia che spiega al pubblico che il modo giusto di costruire un agente è chiedere a un agente di costruirlo.

## Cosa è successo sul palco

Huang ha installato e configurato una versione personalizzata di Hermes con un solo prompt. Poi l'agente, in esecuzione su RTX Spark, ha preparato un ambiente di addestramento simulato per Microduck, il robot bipede da 399 dollari di Pollen Robotics, controllata di Hugging Face. Hermes ha progettato un percorso a ostacoli con Nemotron, ha fatto costruire l'ambiente a GPT-6 Astra usando FreeCAD, le librerie Omniverse, Blender, Newton e Isaac Lab, ha addestrato migliaia di papere simulate nel cloud e ha riportato la policy validata su RTX Spark per la valutazione, prima del trasferimento sul robot fisico. Alla fine, quattro Microduck sono saliti sul palco e hanno eseguito i comandi.

La ricostruzione tecnica è coerente tra il blog Nvidia, il racconto di Nous Research e i resoconti dal vivo. Vale la pena notare la cosa meno spettacolare: il lavoro vero non è stato generare un video, ma concatenare modelli diversi, strumenti CAD, simulatori e hardware eterogeneo. È esattamente ciò che un harness deve fare.

## Il plugin che conta più della demo

Il giorno dopo, Nous Research ha aggiunto il plugin ufficiale Meshy al catalogo: si installa per nome, `hermes plugins install meshy`, richiede la variabile MESHY_API_KEY e Hermes >= 0.22.3. Nella pull request #142619, mergiata il 21 ottobre, il plugin figura nel tier official, categoria tools, con server MCP, diciotto strumenti a costo dichiarato e un limite di spesa di 200 crediti. In Hermes Desktop i modelli si vedono nella chat, i personaggi riggati si animano in linea e una galleria conserva modello e prompt.

Un modello 3D generato dentro una conversazione è un caso d'uso piccolo. Ma è la prova che il meccanismo funziona: un server MCP esterno entra nel catalogo con disclosure, costi e limiti, senza che l'utente scriva una riga di configurazione.

## La manutenzione come segnale

Sempre il 21 ottobre è arrivata la v0.22.4, patch con sei correzioni: spariscono le suggestion pills sopra il composer, i plugin senza dipendenze saltano il consenso vuoto, WhatsApp si riaccoppia dopo il logout, il chip della modalità di approvazione segue il profilo attivo. Nel catalogo entrano bubblewrap, Singularity/Apptainer, mcp-serve, agent-importers con Cursor, inbox e workflow-record. Quattordici commit non-merge, 82 file, 13 PR.

Nessuna di queste righe finirà in un keynote. Ed è il punto: la differenza tra una demo e un'infrastruttura è la noia della manutenzione, ripetuta ogni settimana. La domanda aperta non riguarda più cosa sa fare Hermes, ma quanti dei plugin che entrano nel catalogo sopravviveranno al secondo mese.

---
*Fonti verificate: blog Nvidia, «GTC Berlin 2026: Live Updates», 21/10/2026; post @NousResearch sulla demo (x.com/NousResearch/status/2113010017645244623), 21/10/2026; RuntimeWire, «Nous Research's Hermes agent orchestrates robot training in Jensen Huang's GTC demo», 21/10/2026; Classmethod, resoconto del keynote GTC Berlin, 21/10/2026; release GitHub v0.22.4 di NousResearch/hermes-agent, 21/10/2026; pull request #142619 «Meshy joins the plugin catalog as an official plugin», mergiata 21/10/2026. Discrepanze annotate: il report indicava il requisito minimo del plugin come «>= 0.22.3» ed è confermato dalla PR; la descrizione della pipeline nel report è stata riscritta seguendo il blog Nvidia, che distingue simulazione in Isaac Sim, training nel cloud e valutazione su RTX Spark.*
