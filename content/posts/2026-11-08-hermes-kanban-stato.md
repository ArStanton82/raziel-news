---
title: "Un database, una coda e una riga UNVERIFIED: Hermes dà uno stato agli agenti"
date: 2026-11-08
draft: false
categories: ["Hermes", "AI"]
tags: ["hermes agent", "kanban", "compaction", "plugin", "open source"]
summary: "Le novità meno spettacolari di Hermes sono le più importanti: ogni attività diventa una riga, ogni dubbio un'etichetta."
---

La funzione di cui si parla di più, in questi giorni, fa immagini con un modello di Google e video con un altro. Ma la novità che cambia il modo in cui un agente lavora non si vede in un post: è una tabella. Hermes Kanban, il sistema di bacheche di progetto di Hermes Agent, tratta ogni attività come una riga in un database SQLite, ogni passaggio di consegne come una riga che chiunque può leggere e scrivere, ogni lavoratore come un processo del sistema operativo.

## La fine dello sciame in memoria

Fino a ieri la collaborazione tra agenti si faceva con i subagent: creature nate dentro il processo del padre, che sparivano con lui. La documentazione ufficiale descrive la bacheca come l'alternativa agli «sciami di subagent in processo, fragili». Il cambio non è cosmetico. Un'assegnazione che vive in un database sopravvive al riavvio, si può ispezionare da fuori, si può sbloccare a mano. I lavoratori avviati dal dispatcher non vedono nemmeno le altre bacheche: la variabile d'ambiente che li avvia è fissata sulla loro, e la documentazione dice che «fisicamente non possono vedere» le altre.

C'è anche una concessione al realismo: chi lavora riceve un avviso intorno al 90% del proprio budget di iterazioni, e la documentazione precisa che è «un'occasione di rendicontazione», non una garanzia che il modello lo ascolti.

## L'incertezza ha una riga tutta sua

La seconda novità è più sottile e, per chi usa questi strumenti ogni giorno, più importante. Dalla versione 0.23 «The Hearth», del 5 novembre, i riassunti di compattazione elencano le affermazioni incerte su righe `UNVERIFIED:`, ciascuna con la base su cui è formulata. La pull request che lo introduce spiega il problema meglio di un comunicato: quando una conversazione lunga viene compressa, le parole come «sospetto» o «probabilmente» sono le prime a sparire, e una congettura torna indietro dopo la compressione sotto forma di fatto accertato.

È il punto in cui un agente si autoinganna, e non è un dettaglio da ingegneri. Un assistente che perde traccia di ciò che non sa non è più affidabile di uno che sbaglia: è solo più difficile da correggere. Lo affianca una compattazione «preparata» che scrive il riassunto in anticipo, e che invece è spenta di default.

## La periferia che cresce

Intorno al nucleo si muove il catalogo. Il plugin `gemini-media`, di un maintainer della community, collega i tool immagine e video dell'agente ai modelli Google: Nano Banana fino a 14 immagini di riferimento e output 4K, Gemini Omni per video da 3 a 10 secondi con audio nativo. C'è poi `serpapi`, che porta dentro ricerca web, mappe e notizie. Nessuno dei due è firmato da Nous.

La domanda editoriale, allora, non è quanti agenti si possono far girare insieme. È dove vive il loro stato e chi può leggerlo. Una coda persistente e un'etichetta per i dubbi valgono più di un modello in più nell'elenco, perché sono le due cose che rendono un sistema automatico correggibile da una persona.

---
*Fonti verificate: documentazione ufficiale Hermes Agent, pagina Kanban e riferimento CLI, consultate l'8 novembre 2026 (bacheca per progetto, database SQLite separato per bacheca, dispatcher, toolset `kanban_*`, checkpoint al 90% del budget, isolamento dei worker); note di rilascio Hermes Agent v0.23.0 su GitHub, 5 novembre 2026 (righe `UNVERIFIED:`, compattazione preparata spenta di default); pull request NousResearch/hermes-agent #86019, letta l'8 novembre 2026; scheda del plugin gemini-media nel catalogo ufficiale e repository bytecakelake/hermes-gemini-media-generation, 8 novembre 2026 (Nano Banana fino a 14 riferimenti, 1K-4K; Gemini Omni 3-10 s, audio nativo, tier community); scheda del plugin serpapi nel catalogo, 8 novembre 2026. Escluso dal pezzo il plugin Signal Dog per l'accessibilità: un solo post dell'autore su X, 18 visualizzazioni, nessuna seconda fonte.*
