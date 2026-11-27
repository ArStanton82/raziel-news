---
title: "Il vault resta tuo. Le note, forse no"
date: 2026-11-27
draft: false
categories: ["Hermes", "AI"]
tags: ["hermes agent", "obsidian", "plugin", "privacy"]
summary: "Obsidian porta sette skill ufficiali nel catalogo Hermes: i file restano in locale, il contenuto delle note viaggia verso il modello."
---
Mercoledì Obsidian ha annunciato di avere «connettori ufficiali per ogni agente». Giovedì mattina, ora del Pacifico, Nous Research ha detto che Hermes Agent li usa. In mezzo c'è una frase da leggere due volte: «le tue note restano locali, private e sotto il tuo controllo». È vera per i file. Non lo è per quello che chiedi all'agente di farci.

## Sette istruzioni, nessun server
Il connettore non è software: è un pacchetto di istruzioni, licenza MIT, senza server MCP, hook o processi in background. Dentro ci sono sette skill — Markdown in stile Obsidian, viste Bases, tavole Canvas, la riga di comando di Obsidian, Obsidian Headless per Sync e Publish, Defuddle per convertire pagine web, Knap per i template. Per questo funziona in sei agenti diversi, da Claude a Cursor, da Grok Bot a Kiro: si installa con `hermes plugins install obsidian`. La skill che cerca e modifica le note passa dalla app desktop aperta, e può spostare e cancellare file. La scheda del catalogo lo dichiara; il post promozionale no.

## «Locale» vuol dire un'altra cosa
La differenza tra il comunicato e la disclosure è tutta qui: restano locali i file, non l'elaborazione. Quando chiedi all'agente di riassumere una nota, il contenuto di quella nota viene inviato al modello che stai usando, come nota la stessa scheda del marketplace. Non è un inganno: è la fisica di un agente che pensa altrove. Ma è la ragione per cui «privato» andrebbe sempre accompagnato dal nome di chi riceve il testo.

## La delega si vede
Nella stessa settimana sono arrivati due plugin comunitari che mostrano l'altra faccia del problema, la visibilità. Panoptes disegna una mappa live di ciò che l'agente legge, esegue e delega: è un puro renderer, senza rete né credenziali. Hermes Warden porta Bitwarden dentro l'agente e promette che le password non entrano mai nella chat: escono solo verso gli appunti o un comando approvato. La disclosure, però, aggiunge i dettagli che contano — `bw serve` espone il vault sbloccato su 127.0.0.1 senza autenticazione finché resta attivo, e `warden_run` esegue il comando approvato fuori da qualsiasi sandbox. Nessuno dei due è un audit: il badge «Verified» del catalogo dice che l'autore ha compilato la scheda, non che qualcuno ha verificato il codice.

Sullo sfondo, la manutenzione notturna del gateway: i commit del 27 novembre fanno compattare in background le chat inattive su ogni rotta, perché una conversazione ferma non deve consumare contesto. È il ritratto esatto di questa fase: agenti che lavorano anche a finestra chiusa, e una fiducia che si amministra leggendo le note in piccolo. Il catalogo, più che un negozio, è il luogo dove il contratto di delega viene scritto. Conviene leggerlo prima di premere installa.

---
*Fonti verificate: catalogo Hermes, schede obsidian (v1.2.3), hermes-warden (v0.1.6) e panoptes (v0.1.0), lette il 27 novembre 2026; repository obsidianmd/obsidian-skills, commit «README: Link the Hermes Marketplace» del 26 novembre 2026; MODEL, «Hermes Agent adds Obsidian's official agent skills», 26 novembre 2026; post @NousResearch del 26 novembre 2026; commit NousResearch/hermes-agent 170d9637ea del 27 novembre 2026.*
