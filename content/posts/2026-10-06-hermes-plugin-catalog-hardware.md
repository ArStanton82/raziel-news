---
title: "Hermes e il catalogo dei plugin: la fiducia si costruisce con un commit pinnato"
date: 2026-10-06
draft: false
categories: ["AI", "Hermes"]
tags: ["hermes", "plugin", "open source", "agenti", "gateway"]
summary: "Il Plugin Catalog di Hermes cresce tra revisione umana e commit pinnati, mentre l'ecosistema si allarga dall'hardware ai gateway."
---

C'è una notte di commit dietro l'angolo di ogni progetto open source che vuole durare. Nelle ultime ore il repository `hermes-agent` di Nous Research ha ricevuto una serie di interventi tecnici — copertura dei test sul gateway, la restituzione della coda di messaggi in ingresso quando una riconnessione fallisce, la pulizia del sistema di aggiornamento, un fix sul canale vocale di Discord — e un push sul ramo principale. Sono i lavori noiosi e decisivi che tengono in piedi un agente che parla con Telegram, Discord e Slack senza perdere pezzi per strada.

## Un catalogo che passa dalle mani di un umano

La parte più interessante, però, non è nei commit ma nel modo in cui Hermes distribuisce le estensioni. Il Plugin Catalog è un elenco curato: ogni voce entra tramite una pull request revisionata da un manutentore, e l'installazione è agganciata a un commit esatto — un SHA di quaranta caratteri, non la punta di un ramo. Se l'autore del plugin pubblica nuovo codice, ciò che il catalogo installa non cambia finché qualcuno non riapre la revisione. Il comando resta uno solo, `hermes plugins install <nome>`.

È una scelta di design più politica che tecnica: separa la comodità dell'installazione dalla velocità di aggiornamento, e mette un essere umano nel punto in cui il rischio è maggiore. Nella community il tema è emerso esplicitamente, con la sottolineatura che la revisione è umana e i pin sono immutabili.

## Dall'hardware ai plugin, l'ecosistema si allarga

Sempre restando alla community, nelle ultime ore è circolato un catalogo di hardware e device open platform su cui far girare o integrare un agente, presentato come base per progetti fai-da-te. Accanto a questo, l'annuncio di un plugin di memoria persistente di terze parti, che rivendica un banco di memoria unificato tra dispositivi e agenti: interessante, ma non risulta ancora confermato nel catalogo ufficiale.

## Il gateway come porta d'ingresso

Sul fronte operativo, la connessione a Discord è stata semplificata con un flusso guidato che verifica il token prima di salvarlo. È il tipo di rifinitura che non fa notizia ma decide l'adozione: un agente si giudica da quanto è facile farlo entrare nei luoghi dove le persone già parlano.

La direzione è chiara. Hermes non sta cercando di essere il modello migliore, ma il centro di controllo in cui i modelli si cambiano senza ricostruire nulla. Il catalogo rivisto e i pin immutabili sono la risposta alla domanda che ogni ecosistema aperto prima o poi incontra: come fidarsi di codice che non hai scritto. La risposta, qui, è un umano e un hash.

---
*Fonti verificate: documentazione ufficiale Hermes Agent — Plugin Catalog e Plugins (hermes-agent.nousresearch.com, consultata il 2026-10-06); Hermes Agent Plugin Catalog (352 plugin, aggiornamento in tempo reale, 2026-10-06); commit del repository NousResearch/hermes-agent; post pubblici degli account @Teknium, @HermesWatcher, @witcheer, @YuyunDeng (X, 2026-10-06).*
