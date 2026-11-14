---
title: "Hermes smette di essere un programma e diventa un catalogo"
date: 2026-11-14
draft: false
categories: ["Hermes", "AI"]
tags: ["hermes agent", "plugin", "marketplace", "home assistant", "modal"]
summary: "Duemilatrecento plugin nel catalogo, Home Assistant passa tra gli ufficiali e Modal entra come provider: Hermes cresce per ecosistema."
---

Il numero che racconta meglio la settimana di Hermes non è una release ma un contatore: al momento in cui scriviamo il marketplace ufficiale dichiara 2.309 plugin, aggiornato poche ore prima. Intorno a quel numero ruotano i tre fatti degli ultimi giorni: un plugin storico che cambia casa, un provider di inference che entra dalla porta principale e un hackathon che si chiude con quasi mille candidature.

## Il codice vecchio cambia indirizzo

Home Assistant non è una novità per Hermes: era parte del core. La scheda ufficiale del catalogo, alla versione 2.0.1, lo dice senza giri di parole — «formerly built into Hermes core; existing users are migrated automatically». Nome della piattaforma, toolset, nomi dei tool, variabili d'ambiente e chiavi di configurazione restano identici; cambia il fatto che ora si installa con `hermes plugins install homeassistant` e richiede Hermes 0.21.5 o superiore. Chi lo usava non deve fare nulla: il primo avvio dopo l'aggiornamento lo installa e lo abilita.

Il post che nei giorni scorsi annunciava che «Hermes ora gestisce tutta la casa» descriveva dunque un uso, non un esordio. La distinzione conta, perché segnala la direzione: ciò che era monolite diventa modulo, e il modulo può essere aggiornato, sostituito, disinstallato senza toccare il resto.

## Un provider firmato da chi lo gestisce

Il 13 novembre Teknium ha annunciato che Modal è disponibile come provider di inference tramite il suo plugin «verified». La scheda conferma la sostanza: `modal`, pubblicato da modal-labs, versione 1.0.0, aggiornata il giorno prima. Il plugin espone gli endpoint Modal compatibili OpenAI, si configura con un token `MODAL_PROXY_TOKEN` e si seleziona da `hermes model`. Non è un wrapper di terzi che finge di essere ufficiale: l'autore è l'azienda che eroga il servizio.

## Mille candidature e un canary che passa i test

Mentre l'ecosistema si allargava, il concorso lo ha fotografato. Le iscrizioni all'Hermes Agent Plugin Hackathon si sono chiuse alle 17:00 EST del 12 novembre con «nearly 1,000 entries»; i giudici stanno selezionando i primi dieci, i vincitori saranno avvisati per email e annunciati «in about a week». Il montepremi era di 20.000 dollari.

Sul fronte delle build, le note di release del 13 e del 14 novembre mostrano un canary v0.23.1 con i test nativi di installazione e chat superati su macOS (DMG arm64) e su Windows (MSIX arm64 e x64), con i bundle Linux disabilitati. Una routine, ma è la routine che tiene in piedi un catalogo che si aggiorna ogni giorno.

## Il problema che arriva con il successo

Duemilatrecento plugin sono una piattaforma, e una piattaforma ha i problemi delle piattaforme: superficie d'attacco, qualità disomogenea, aspettative di manutenzione. Il caso Home Assistant mostra la soluzione più solida — codice che viveva nel core, ripubblicato con gli stessi contratti e migrazione automatica — ma non è quella che si può applicare a tutto. La domanda dei prossimi mesi non sarà quanti plugin ci sono, ma quanti sopravvivono al primo cambio di versione.

---
*Fonti verificate: Hermes Marketplace, pagina plugins e contatore 2.309 (14/11/2026); scheda ufficiale del plugin homeassistant v2.0.1 (14/11/2026); scheda del plugin modal di modal-labs v1.0.0 (14/11/2026); note di release GitHub NousResearch/hermes-agent, canary v0.23.1+canary.20261113T064447Z e .20261114T064334Z, lette via API (13-14/11/2026); annuncio hackathon su nousresearch.com e x.com/NousResearch/status/2120715518243987685 (12/11/2026); post di @Teknium sul provider Modal (13/11/2026).*
