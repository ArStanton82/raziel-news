---
title: "Hermes accelera, ma i suoi plugin di memoria cercano un proprietario"
date: 2026-10-03
draft: false
categories: ["Hermes", "AI"]
tags: ["hermes", "nous-research", "plugin", "memoria", "open-source", "mcp"]
summary: "Nous Research marca tre plugin di memoria come 'unmaintained' mentre il core di Hermes corre. La manutenzione è la parte meno visibile dell'ecosistema."
---

Il 2 ottobre, l'organizzazione NousResearch su GitHub ha aggiornato tre repository di plugin per la memoria di Hermes Agent — hermes-plugin-holographic, hermes-plugin-byterover e hermes-plugin-retaindb — aggiungendo a ciascuno la stessa descrizione: "Unmaintained — looking for an owner. Not maintained by Nous Research." L'ultimo commit, firmato da teknium1, è esplicito: "Nous Research does not maintain memory providers". Tre piccoli repo, una nota breve, e una domanda che riguarda tutto l'ecosistema: chi tiene accese le luci quando il core va veloce?

## Il core non si ferma

Nella stessa notte, il repository principale hermes-agent ha ricevuto una serie di commit di manutenzione: la correzione dei processi figli di un server MCP morto, un limite all'attesa del lock del resolver del browser, e diverse rifiniture alla roster dei bot su Desktop, con tracce di attribuzione dell'identità per le connessioni multiple. L'ultima release stabile taggata resta v0.21.5 (v2026.9.24), che aveva già raggruppato circa 460 pull request. Il ritmo è quello di un progetto in piena corsa: il catalogo dei plugin è passato da 292 voci al momento di quella release a 349 il 2 ottobre, e l'installazione degli MCP dal catalogo approvato da Nous è ormai una questione di pochi clic.

## Un ecosistema, due velocità

C'è una tensione strutturale in ogni progetto che cresce in fretta. Il nucleo evolve ogni notte, mentre i componenti periferici — i provider di memoria, in questo caso — richiedono un proprietario che li segua nel tempo. Holographic è un archivio locale di fatti in SQLite con retrieval HRR; ByteRover costruisce un albero di conoscenza tramite la CLI brv; RetainDB è un'API cloud con ricerca ibrida. Sono tre approcci diversi allo stesso problema: dare all'agente una memoria che sopravvive alle sessioni. Il fatto che Nous li abbia "liberati" non li rende inutili — li rende orfani. La documentazione ufficiale continua a elencarli tra i provider disponibili, ma la manutenzione è ora responsabilità di qualcun altro.

## La parte noiosa che decide tutto

C'è una lezione ricorrente nel software open source: la differenza tra una demo e un'infrastruttura non è l'idea, è chi risponde alle issue sei mesi dopo. Un agente che ricorda è più utile di uno che dimentica, ma solo se quella memoria continua a funzionare dopo l'aggiornamento del core. Nous Research ha scelto di concentrarsi su ciò che considera il proprio nucleo e di cedere il resto a chi lo vorrà mantenere: una decisione legittima, e persino onesta nel modo in cui è comunicata.

La domanda aperta è per gli utenti. Chi oggi si affida a uno di questi provider sta costruendo su un pezzo che nessuno promette di aggiornare. È il compromesso silenzioso dell'ecosistema Hermes: grande velocità al centro, e alla periferia la necessità — tutta umana — di trovare qualcuno che se ne prenda cura.

---
*Fonti verificate: GitHub, org NousResearch (descrizioni e commit dei repo hermes-plugin-holographic, hermes-plugin-byterover, hermes-plugin-retaindb, 2026-10-02); GitHub, commit e release di NousResearch/hermes-agent (v0.21.5, v2026.9.24; commit del 2026-10-03); documentazione ufficiale Hermes Agent, sezioni Plugin Catalog e Memory Providers; hermesagents.net, stato del catalogo plugin (349 voci al 2026-10-02). Tutte consultate il 2026-10-03.*
