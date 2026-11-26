---
title: "Il cookie che non doveva esistere: Hermes chiude la porta di 127.0.0.1"
date: 2026-11-26
draft: false
categories: ["Hermes", "AI"]
tags: ["hermes", "sicurezza", "webapp", "loopback", "cookie"]
summary: "Un fix notturno nel repository di Hermes: sulla webapp in loopback i login via cookie sono rifiutati, perché 127.0.0.1 non isola le porte."
---
C'è un'idea che quasi tutti diamo per buona: se un servizio gira su 127.0.0.1, è al sicuro perché è "solo locale". Il commit che Nous Research ha pubblicato questa notte sul repository di Hermes Agent (3e33ec2a, 05:29 UTC) mostra che quell'idea ha una falla precisa, e che la falla non stava nel codice dell'agente ma in una specifica del browser.

## Cosa succede davvero su localhost
La RFC 6265, al paragrafo 8.5, stabilisce che i cookie non sono isolati per porta su 127.0.0.1. In pratica: un cookie emesso da un servizio in ascolto sulla porta 9119 viene inviato dal browser anche a qualunque altro servizio locale visitato su una porta diversa — un server di sviluppo, una pagina di test, l'ennesimo pannello di un'altra applicazione. Se la webapp di Hermes avesse accettato un login via cookie in loopback, chiunque controllasse una di quelle pagine avrebbe potuto catturare il cookie e rigiocarlo contro le API REST e contro il ticket del terminale host (`/api/webapp/socket-ticket?socket=host-terminal`), aggirando il meccanismo che tiene il token di sessione fuori dall'HTML.

## La scelta: solo link di lancio
La correzione (PR #160226, che chiude la segnalazione #159500) prende la strada più netta: su loopback la webapp resta "launch-link-only", cioè si apre con `hermes webapp`. La pagina `/login` ora spiega questo invece di mostrare un modulo; `/auth/password-login`, `/auth/login` e `/auth/callback` rispondono 403 senza impostare alcun cookie; `/api/auth/providers` restituisce una lista vuota. Il pull request dichiara tredici test di regressione nuovi e 319 test verdi su diciotto file.

## Perché è una lezione, non un incidente
La documentazione del dashboard dice già che in loopback non serve alcun login e che un bind non-loopback attiva il gate di autenticazione, fallendo chiuso se manca un provider. Il difetto non rompeva quel modello: ne creava una credenziale che nessun middleware accettava, ma che il browser avrebbe potuto rigiocare altrove. La sicurezza dello spazio locale non è un permesso concesso una volta, è un'assunzione da verificare ogni volta che si emette un segreto.

Due dettagli pratici. Il fix è su main ma non in una release taggata: l'ultima stabile resta la v0.23.4 del 24 novembre, la canary più recente è del 25. E intanto il catalogo ufficiale dei plugin ha promosso Mission Control, dashboard in sola lettura con metri di token e costo per Desktop: versione 1.0.0, richiede Hermes 0.21.6, aggiornata quattordici giorni fa. Non è una novità di prodotto, è una vetrina: guardare quanto costa un agente mentre lavora resta, però, il modo più onesto di usarlo.

---
*Fonti verificate: commit 3e33ec2a e PR #160226 (NousResearch/hermes-agent, 25-26 novembre 2026); issue #159500; documentazione Hermes Web Dashboard, sezione autenticazione e note su `--insecure` e bind loopback (letta il 26 novembre 2026); API GitHub delle release, ultima stabile v0.23.4 del 24 novembre 2026; scheda mission-control nel catalogo plugin di hermes-agent.nousresearch.com (26 novembre 2026).*
