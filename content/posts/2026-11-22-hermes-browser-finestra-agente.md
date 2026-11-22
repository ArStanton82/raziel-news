---
title: "Hermes esce dalla chat: il browser diventa una finestra sull'agente"
date: 2026-11-22
draft: false
categories: ["AI", "Hermes"]
tags: ["hermes", "browser extension", "plugin", "proattività", "dashboard"]
summary: "Un plugin comunitario porta Hermes nella barra laterale del browser; intanto Teknium parla di proattività con approvazione e di dashboard in dismissione."
---

Il modo in cui un agente entra nella nostra giornata conta quanto quello che sa fare. Per mesi Hermes è vissuto in una finestra di terminale o in una chat. Le tre notizie di questo fine settimana raccontano lo stesso spostamento, dal dentro verso il fuori.

## La pagina come contesto

Il tassello più concreto è un'estensione del browser firmata Jon Komet, plugin comunitario e non ufficiale di Nous Research: licenza MIT, pannello laterale su Chromium e barra laterale su Firefox, codice pubblico su GitHub. L'agente non riceve più una pagina incollata a mano: legge quella che stai guardando, con titoli, link, moduli e testo selezionato.

I limiti sono dichiarati dall'autore. Su Firefox il controllo è ridotto: l'estensione legge le pagine, apre indirizzi e gestisce le schede, ma non può cliccare né digitare. Sui browser Chromium il controllo è completo. Serve inoltre il plugin complementare sui build di Hermes successivi al 24 ottobre 2026, e un riavvio del gateway. Non è un chatbot nel browser: è una porta sul runtime che hai già configurato, con i tuoi modelli, strumenti e memoria.

## Proattività con il freno a mano

Il secondo indizio viene dalle risposte di Teknium, co-fondatore di Nous Research, in un thread del 21 novembre: «non c'era proattività in Hermes, questo sarebbe il passo successivo» e, poco dopo, la speranza che «chiedere approvazione per alcuni di questi tentativi proattivi permetta all'utente di arginare le assurdità». Sono battute di conversazione, non un annuncio, e nel changelog pubblico non c'è ancora traccia di una funzione del genere.

Il punto editoriale però resta: un agente che agisce senza chiedere è più utile e più rischioso nello stesso gesto. Spostare il consenso dentro il flusso, invece di affidarlo a una configurazione iniziale, è la scelta matura. Chi ha usato agenti autonomi sa che il problema non è il rifiuto, è l'iniziativa a sproposito.

## Il dashboard si sposta nel gateway

Il terzo segnale è tecnico e per ora informale. Sempre il 22 novembre Teknium ha scritto, rispondendo a due utenti, che «il dashboard è in dismissione». Il changelog del 21 novembre mostra la direzione coerente: pull request che spostano il vecchio backend del dashboard dentro il gateway, con una scheda di sistema dedicata alla migrazione. Non è una rimozione annunciata con un comunicato, ma la fine di un pezzo di architettura.

Messaggio implicito: l'interfaccia non è più un'applicazione separata da amministrare, ma una superficie del gateway. Meno componenti, meno credenziali da tenere allineate, meno modi di sbagliare.

## Il confine, non la funzione

La tentazione è leggere tutto come un elenco di feature. È più interessante notare che browser, proattività e dashboard convergono sullo stesso problema: dove finisce l'agente e dove comincia l'utente. Un'estensione che legge la pagina, un permesso chiesto prima di agire, un cruscotto che smette di essere un mondo a parte. Nessuna delle tre cose è spettacolare. Insieme descrivono un prodotto che sta imparando a stare al bordo dell'attenzione, invece che al centro.

---
*Fonti verificate: repository github.com/abundantbeing/hermes-browser-extension e scheda su addons.mozilla.org (consultati il 22/11/2026, licenza MIT, autore Jon Komet, limiti di Hermes Control su Firefox); hermesatlas.com/projects/abundantbeing/hermes-browser-extension (22/11/2026); post @Teknium del 21-22/11/2026 su proattività e dashboard (dichiarazioni informali, nessuna voce nel changelog); changelog hermesbible.com del 21/11/2026 e gradually.ai/changelogs/hermes-agent (v0.23.3 del 20/11/2026). Discrepanza annotata: il report indica il catalogo plugin ufficiale come non leggibile in questa esecuzione (`plugin-catalog.json` vuoto), quindi lo stato «ufficiale» del plugin non è confermato né escluso; il post @HermesWatcher lo presenta come installabile con `hermes plugins install`, mentre il README parla di plugin comunitario.*
