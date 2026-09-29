---
title: "Hermes e il perimetro degli agenti: NVIDIA detta le regole, i modelli arrivano prima"
date: 2026-09-29
draft: false
categories: ["Hermes", "AI"]
tags: ["Hermes Agent", "Nous Research", "NVIDIA", "OpenShell", "Claude Sonnet 5.5"]
summary: "NVIDIA lancia la piattaforma aperta per la sicurezza degli agenti e cita Hermes tra i runtime supportati: cosa cambia davvero."
---
Negli ultimi giorni di settembre la conversazione sugli agenti autonomi ha smesso di essere una questione di capacità e ne è diventata una di contenimento. Non è un cambio di tema: è un cambio di fase.

## Un perimetro, non una promessa

NVIDIA ha presentato la Open Agent Safety Platform, con oltre cento partner dichiarati. L'architettura si appoggia a due pezzi: OpenShell, runtime isolato a livello kernel distribuito in licenza Apache 2.0, e Sentry, un watchdog fuori banda che gira su BlueField-4 e può mettere in quarantena un agente che esce dai propri confini in millisecondi. Hermes non è un ospite occasionale: la pagina NemoClaw parla esplicitamente di "run self-improving Hermes agents", combinando il ciclo skill-e-memoria di Nous Research con i controlli runtime di OpenShell. Il punto è più sottile di quanto sembri: il meccanismo che rende Hermes utile — imparare e conservare — viene trattato come carico da confinare, non come virtù da applaudire.

## Modelli nuovi, regole vecchie

Il 24 settembre la release v0.21.5 (v2026.9.24) porta nei cataloghi Claude Opus 5.5 e GPT-6. Il 28 settembre Anthropic lancia Claude Sonnet 5.5 e la community di Hermes ne annuncia la disponibilità nel runtime: la casa madre non ha ancora pubblicato una nota dedicata, quindi il dato va preso per quello che è, un annuncio di community coerente con la tempistica. La sostanza non cambia: i modelli arrivano nei client prima che qualcuno abbia deciso come limitarli.

## Il desktop come identità

Hermes Desktop si personalizza profilo per profilo: font della chat e del terminale, temi importabili dal Marketplace di VS Code, layout di finestra, tutto salvato nel config del singolo profilo. Il selettore "Applies to" permette di modificare le impostazioni di un altro profilo senza cambiare applicazione. Un agente di ricerca e uno di produzione possono avere due volti, due palette e due densità diverse. È estetica, ma è anche la prima volta che il confine tra agenti diventa visibile a colpo d'occhio.

## Conclusione

La settimana dice una cosa semplice: la sicurezza non è più un accessorio del prodotto, è il terreno su cui si gioca la fiducia. NVIDIA lo ha capito e ha comprato l'attenzione di cento partner. Nous, dal canto suo, si è assicurata che Hermes fosse dentro il recinto — non fuori a chiedere il permesso. Per chi costruisce agenti, la domanda non è più "cosa sa fare", ma "dove gli è permesso andare".

---
*Fonti verificate: NVIDIA Newsroom e GlobeNewswire, lancio Open Agent Safety Platform (28/09/2026); MarkTechPost (28/09/2026); pagina NVIDIA NemoClaw e docs.nvidia.com/nemoclaw (consultate 29/09/2026); GitHub NousResearch/hermes-agent, release v0.21.5 (24/09/2026); docs Hermes Agent "Hermes Desktop" (consultate 29/09/2026); Anthropic release notes e anthropic.com/claude/sonnet (28/09/2026).*
