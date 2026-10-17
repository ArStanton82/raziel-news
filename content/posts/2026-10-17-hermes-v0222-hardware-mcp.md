---
title: "Hermes 0.22.2: la release che ammette di essere un errore corretto"
date: 2026-10-17
draft: false
categories: ["Hermes", "AI"]
tags: ["Hermes Agent", "Nous Research", "open hardware", "MCP", "sicurezza"]
summary: "Nous pubblica la 0.22.2 che ripara la 0.22.1, apre una pagina di idee hardware e chiarisce che Hermes non compra posizionamenti."
---

Ci sono settimane in cui un progetto si giudica dalle funzioni che aggiunge, e settimane in cui si giudica da come parla dei propri errori. Nell'ecosistema Hermes quella appena trascorsa appartiene alla seconda categoria.

## La patch che ammette l'errore
Il 15 ottobre Nous Research ha pubblicato Hermes Agent v0.22.2, e le note di rilascio sono insolitamente franche: «v0.22.1 è stata costruita dal commit sbagliato». La versione precedente aveva spedito lavoro sul gateway non ancora rilasciato, e l'app del Microsoft Store poteva restare bloccata su "Connecting". La 0.22.2, si legge, è la release che la 0.22.1 avrebbe dovuto essere. I due interventi dichiarati sono concreti: il gateway supervisionato riparte dopo un reboot — Linux può assegnare un PID precoce a un processo estraneo, scambiato per un gateway vivo, e Hermes ora registra il boot da cui è partito — e i turni lunghi con modelli locali sopravvivono sui laptop, con i timer di stallo che ignorano il tempo in cui la macchina è stata sospesa. Resta un known issue dichiarato, non nascosto: le sessioni avviate sotto il gateway 0.22.1 non sono cancellabili nella 0.22.2. Chi aggiorna via CLI o installer usa `hermes update`.

## Non si comprano i posizionamenti
Il 16 ottobre l'account ufficiale di Nous Research ha pubblicato una nota editoriale: un post del social intern era satira, Hermes non era stato selezionato per una lista perché «non facciamo PR a pagamento». Il testo compare anche nella sezione Announcements di nousresearch.com. È un dettaglio piccolo, ma dice come un'azienda sceglie di costruire la propria reputazione: con il prodotto, non con le collocazioni.

## L'hardware come banco di prova
Il co-fondatore Teknium ha segnalato un nuovo dispositivo IoT basato su Hermes e ha pubblicato una pagina con centinaia di idee di progetto per l'incontro tra l'agente e l'open hardware: nodi di sensori alimentati a batteria, bridge Zigbee, banchi di test, persino un core FPGA. Non è un catalogo di prodotti ma di ipotesi: l'agente come strato che scrive firmware, interpreta log e orchestra dispositivi che non hanno mai avuto un'interfaccia conversazionale.

## Il rischio che arriva dal protocollo
Il 15 ottobre è stato reso pubblico l'advisory per CVE-2026-59951, che riguarda l'SDK Python di MCP: i server Streamable HTTP in modalità stateful — quella predefinita — non recuperavano le sessioni. Non scadevano mai, un DELETE lasciava la voce registrata e il numero di sessioni non aveva tetto, così un client in grado di raggiungere l'endpoint poteva far crescere la memoria senza limite fino a un riavvio. Le versioni interessate vanno dalla 1.8.0 alla 1.29.1 e dalla 2.0.0 alla 2.1.1; il fix arriva in 1.30.0 e 2.2.0, con `session_idle_timeout` e `max_sessions`. Per chi espone strumenti via MCP, è una nota da leggere prima di aprire la porta.

Tre storie diverse, la stessa lezione: la manutenzione è una forma di credibilità, e l'ecosistema attorno a un agente vale quanto la cura dei suoi punti di contatto.

---
*Fonti verificate: GitHub NousResearch/hermes-agent, release v0.22.2 (15 ottobre 2026); nousresearch.com, sezione Announcements (16 ottobre 2026); teknium.io/hermes-devices (17 ottobre 2026); Red Hat Customer Portal e Kodem Security, CVE-2026-59951 (15 ottobre 2026).*
