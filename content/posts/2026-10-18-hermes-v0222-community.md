---
title: "Hermes 0.22.2: la release che ripara la release"
date: 2026-10-18
draft: false
categories: ["Hermes", "AI"]
tags: ["hermes-agent", "release", "gateway", "modelli-locali", "plugin"]
summary: "Nous Research pubblica Hermes Agent 0.22.2, nata per correggere la 0.22.1: gateway, modelli locali e una community che costruisce ai margini."
---

Il 15 ottobre Nous Research ha pubblicato Hermes Agent v0.22.2. La cosa più interessante non è l'elenco delle funzioni, ma la motivazione dichiarata nella nota di rilascio: la v0.22.1 era stata costruita dal commit sbagliato. Aveva spedito lavoro sul gateway non ancora destinato al pubblico, e l'app del Microsoft Store poteva bloccarsi su "Connecting". La 0.22.2 è, nelle parole degli stessi autori, "la release che la 0.22.1 avrebbe dovuto essere".

## Cosa ripara davvero

Il primo fix è quello che interessa chiunque faccia girare Hermes su una macchina sempre accesa: il gateway supervisionato (systemd, launchd, Docker) torna a partire dopo un riavvio. Dopo un reboot, Linux può assegnare un PID anticipato a un processo estraneo, e il gateway lo scambiava per un'istanza già attiva, rifiutandosi di avviarsi. Ora Hermes registra l'epoca di boot in cui è partito e, quando non riesce a confrontarla, interroga il lock dell'host — che solo un gateway vivo possiede.

Il secondo riguarda i turni lunghi sui modelli locali: le richieste locali trasmettono sempre con un indicatore di avanzamento, i timer di stallo saltano il tempo in cui la macchina era sospesa, e un server locale recuperato riceve un altro tentativo invece di finire in un interruttore che faceva fallire ogni messaggio successivo. Resta un problema noto e onesto: le sessioni create sotto il gateway 0.22.1 non sono cancellabili in 0.22.2.

## Il giorno dopo, il lavoro non si ferma

Nella giornata del 18 ottobre il repository ha già ricevuto nuovi commit su TLS e gateway, fra cui un fix che rifiuta una cancellazione in corsa con uno steer in coda invece di riportare un falso successo. È il segno di una linea di sviluppo che usa la release come punto fermo, non come traguardo.

## La community costruisce ai margini

Fuori dal repository ufficiale, l'ecosistema si muove. Un utente ha collegato un robot da scrivania basato su ESP32 a Hermes, usando Parakeet per il riconoscimento vocale e Kokoro per le risposte: si parla con l'agente, lo si ascolta mentre lavora e si delegano i compiti lunghi a helper in background. Un altro ha segnalato un dettaglio pratico: `auto_prune: true` e `retention_days: 90` scritti in un vecchio `config.yaml` restano attivi anche dopo che il pruning è diventato disattivato di default — chi non pulisce il file continua a cancellare chat. E circola un workflow semplice e sensato: quando un modello locale si impunta su un'automazione, pagare pochi centesimi a un modello cloud per capire il blocco, poi insegnarlo al modello locale con un file di skill esplicito.

La maturità di un progetto si misura meno dalle funzioni e più da come gestisce i propri errori. Una release nata per ripararne un'altra, documentata senza giri di parole, dice più di qualunque changelog trionfale.

---
*Fonti verificate: GitHub NousResearch/hermes-agent, release v0.22.2 (15/10/2026); releases.sh/nousresearch, changelog (16/10/2026); post e thread della community su X (@Alacritic_Super, @GodsBoy7777, @joe_ptrkv_ch, 18/10/2026) — consultati il 18/10/2026.*
