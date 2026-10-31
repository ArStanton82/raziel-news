---
title: "Il segreto stava nella cartella sbagliata"
date: 2026-10-31
draft: false
categories: ["Hermes", "AI"]
tags: ["Hermes Agent", "sicurezza", "sandbox", "approvazioni", "cron"]
summary: "Quattro file spostati di un livello: il sandbox difende i percorsi, non le intenzioni, e una cartella rinominata basta a leggere un segreto."
---

Il 31 ottobre, alle 03:49 UTC, il repository di Hermes Agent ha registrato il merge della pull request 146715. Il titolo parla di igiene: «sposta le cache dei segreti e il token Photon nella radice della home del profilo». Spostare quattro file di un livello non sembra una notizia. La motivazione, invece, è la lezione.

## Il difetto era geometrico

Il sandbox non nasconde i segreti: nasconde percorsi. Su Windows il meccanismo MXC, usato dal plugin OpenShell, espone una lista `deniedPaths` che può proteggere soltanto un file che si trovi direttamente nella home concessa all'agente. Se il file sta un livello sotto — in `cache/` o in `runtime/` — l'agente può rinominare la cartella in cui scrive e leggere il file nascosto al nuovo indirizzo. È stato misurato su MXC 1.0.0 e 1.0.1: non è una teoria.

Da qui la correzione, che è insieme semplice e imbarazzante: la cache in chiaro di Bitwarden (`bws_cache.json`), quella cifrata, la cache di 1Password (`op_cache.json`) e il record del sidecar Photon, che contiene porta e token, ora vivono nella radice della home. Le copie vecchie vengono cancellate senza essere lette. Il testo della PR aggiunge un dettaglio che vale più del resto: la cache di 1Password era l'unica che nessun guardiano copriva.

## Spostare un file, aggiornare cinque liste

Un segreto è protetto solo se tutti i controlli conoscono il suo nome. La stessa modifica tocca le liste dei percorsi credenziali del profilo, i divieti di lettura e scrittura dell'agente, il filtro del gateway sui media, i nomi nascosti dell'API Files della dashboard e il `.gitignore` dell'installazione piatta. Quattro file spostati, cinque registri da riscrivere. Il costo vero di una misura di sicurezza non è la misura: è tenere allineato l'elenco di chi deve saperla.

## Chi decide quando non c'è nessuno

Nella stessa documentazione emerge l'altra metà del problema. Le approvazioni dei comandi pericolosi hanno tre modalità — `smart` per default, `manual`, `off` — e tre chiavi che governano i contesti senza umano: `cron_mode`, `single_query_mode`, `unattended_mode`. Tutte e tre valgono `deny`: se un job programmato incontra un comando distruttivo, il comando viene bloccato e l'agente deve trovare un'altra strada.

È il default più interessante del sistema, perché non protegge chi è davanti alla tastiera. Protegge il caso in cui la tastiera non c'è.

Resta una considerazione scomoda. La sicurezza di un agente autonomo non si misura da quanto è intelligente la sua valutazione del rischio, ma da quanto è corto l'elenco dei percorsi che ha dimenticato di aggiornare. Il giorno in cui una cache finisce un livello troppo in basso, il sandbox continua a funzionare perfettamente e non protegge niente.

---
*Fonti verificate: pull request NousResearch/hermes-agent #146715, testo e data di merge 31 ottobre 2026 (API GitHub); documentazione ufficiale Hermes Agent, pagine Security (modalità `approvals.mode`, `cron_mode`) e X Search, consultate il 31 ottobre 2026.*
