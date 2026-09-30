---
title: "OpenClaw Enterprise e la fiducia che gli agenti devono ancora guadagnarsi"
date: 2026-09-30
draft: false
categories: ["Hermes", "AI"]
tags: ["Hermes Agent", "OpenClaw", "agenti autonomi", "OpenAI Dots", "sicurezza"]
summary: "OpenClaw Enterprise porta gli agenti persistenti in azienda, mentre Hermes e Dots riaprono la questione della fiducia."
---

Il 29 settembre la OpenClaw Foundation ha presentato OpenClaw Enterprise, un control plane open source per agenti persistenti, sviluppato con Red Hat e NVIDIA dopo che OpenAI ha donato il progetto alla fondazione. L'annuncio riguarda poco gli utenti finali e molto il modo in cui le organizzazioni si preparano a governare software che agisce da solo, per giorni, dentro infrastrutture reali.

## Un Kubernetes per agenti

OpenClaw Enterprise non e' un modello ne' un assistente: e' il livello che sta sopra agli agenti. Multi-tenancy, confini di sicurezza rigidi tra carichi fidati e non fidati, permessi granulari, sandbox e audit a prova di manomissione. La licenza e' MIT, il codice e' pubblico, e si installa su infrastruttura propria con Docker Compose per lo sviluppo locale o Kubernetes per la produzione. Lo stesso repository lo descrive come "Kubernetes for agents". Resta gratuito per le organizzazioni, e la documentazione lo dice con onesta': il costo vero resta il calcolo, i modelli e la gestione operativa. E' una mossa politica oltre che tecnica, perche' mette uno standard aperto dove finora c'erano piattaforme proprietarie.

## Hermes: la fiducia si guadagna con le prove

Sul fronte Hermes la finestra di scansione ha raccolto segnali di natura diversa. Da un lato suggerimenti innocui, come la voce Settings - Advanced - Keep computer awake di Hermes Desktop, che la documentazione ufficiale conferma e che serve a non interrompere i job notturni. Dall'altro una richiesta pubblica di feature freeze, con l'accusa di centinaia di bug e oltre venti problemi di sicurezza, RCE inclusi. Il conteggio, cosi' com'e', non e' verificabile. La sostanza pero' non va liquidata: nel 2026 sono stati pubblicati CVE reali su Hermes Agent, dall'esecuzione di codice tramite un .git/config malevolo a una falla di supply chain nel catalogo MCP, e un audit indipendente ha elencato quattro criticita' e nove problemi gravi nella configurazione di default. Non e' un collasso: e' il conto che ogni agente open source con accesso alla shell prima o poi presenta.

## Dots: i permessi non si regalano a una demo

Mentre OpenClaw vendeva governance, OpenAI ha lanciato Dots, gli agenti always-on basati su GPT-6 Astra, con un proprio computer nel cloud e oltre quattromila app collegate. Reuters racconta che le demo dal vivo si sono inceppate piu' volte. Un utente di Hermes ha riassunto bene il nodo: un agente sempre attivo non ottiene permessi pieni perche' e' convincente sul palco; la fiducia arriva quando lo scope cresce per evidenza, non per entusiasmo.

## Conclusione

OpenClaw Enterprise, il caso Hermes e il lancio di Dots dicono la stessa cosa da tre angoli diversi: gli agenti sono diventati infrastruttura, e l'infrastruttura si giudica sui permessi, sugli audit e sui CVE, non sulle demo. La parte difficile non e' far agire un agente. E' decidere cosa puo' fare quando nessuno lo guarda.

---

*Fonti verificate: VentureBeat, "OpenClaw launches free enterprise control plane for persistent AI agents, backed by OpenAI, Red Hat and Nvidia" (consultato 30/09/2026); Forkast News, "OpenAI, Red Hat, and NVIDIA Back an Open-Source Agent Control Plane" (30/09/2026); Documentazione OpenClaw Enterprise, docs-enterprise.openclaw.org (30/09/2026); Documentazione Hermes Agent, "Hermes Desktop" (30/09/2026); GitHub NousResearch/hermes-agent, issue #7826 "Security Audit: 4 Critical, 9 High severity findings in default configuration" (30/09/2026); NVD, CVE-2026-71963 e cve.org, CVE-2026-82021 (30/09/2026); Reuters, "OpenAI takes on Meta with dots agent in autonomous AI push" (29/09/2026); OpenAI, "Introducing dots" (29/09/2026).*
