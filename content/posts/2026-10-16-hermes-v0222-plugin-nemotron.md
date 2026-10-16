---
title: "Hermes Agent v0.22.2: la patch che riapre la porta d'ingresso"
date: 2026-10-16
draft: false
categories: ["Hermes", "AI"]
tags: ["hermes-agent", "nous-research", "release", "plugin", "nemotron", "open-source"]
summary: "Nous pubblica la patch v0.22.2, apre un catalogo ufficiale di plugin e misura Nemotron 3.5 Super VL su Hermes Bench: 63,44."
---

Il 15 ottobre Nous Research ha pubblicato Hermes Agent v0.22.2. Sulla carta è una patch, ma il changelog è esplicito: la v0.22.1 era stata costruita dal commit sbagliato, spedendo lavoro non ancora rilasciato sul gateway, e la versione di oggi è quella che la 0.22.1 avrebbe dovuto essere. È il tipo di trasparenza che un progetto open source può permettersi e che vale la pena registrare.

## Una patch che ammette l'errore

Il difetto principale riguardava la porta d'ingresso: dopo un riavvio, Linux può assegnare un PID precoce a un processo estraneo e il gateway supervisionato — systemd, launchd, Docker — poteva scambiarlo per un gateway già attivo e rifiutarsi di partire. Hermes ora registra l'avvio in cui è nato e, quando non può esserne certo, interroga il lock dell'host, che solo un gateway vivo possiede. La seconda correzione riguarda i turni lunghi con modelli locali: le richieste in streaming mostrano il progresso di lettura del prompt, i timer di stallo ignorano il tempo in cui la macchina era sospesa e un server locale recuperato riceve un secondo tentativo invece di un interruttore che falliva ogni messaggio successivo. Resta un problema noto dichiarato: le sessioni avviate sotto il gateway 0.22.1 non si possono eliminare nella 0.22.2.

## I plugin diventano un catalogo ufficiale

Sul piano dell'ecosistema, l'organizzazione NousResearch ha consolidato i plugin di prima parte in un unico repository, `hermes-official-plugins`, dove ogni plugin vive in una propria directory e si installa in una riga dal catalogo. Il repo ha assorbito la storia di progetti precedenti, come il plugin per l'abbonamento Claude, ora archiviato in favore della nuova casa comune. È manutenzione, non espansione: la stessa direzione della codebase ridotta, ma applicata alla superficie dei plugin.

## Hermes Bench come tabellone

Il dato più citato della settimana arriva da NVIDIA: Nemotron 3.5 Super VL, modello aperto da 120 miliardi di parametri con 12 miliardi attivi, ha segnato 63,44 su Hermes Bench — sopra il 56,33 di Nemotron 3 Ultra — con una throughput fino a cinque volte superiore ai modelli locali comparabili. Che un benchmark interno al progetto diventi il metro con cui un produttore di chip misura i propri modelli dice qualcosa sul peso che Hermes sta acquisendo come piattaforma di riferimento.

Sullo sfondo resta il Series B da 90 milioni a 1,5 miliardi di valutazione, guidato da Robot Ventures, con il capitale destinato a «Hermes for Businesses». Il progetto continua a crescere su due fronti opposti: riparare i dettagli che impediscono all'agente di partire, e costruire il contesto in cui le aziende lo adottano.

---
*Fonti verificate: github.com/NousResearch/hermes-agent/releases (release v0.22.2, 15 ottobre 2026); releases.sh/nousresearch/hermes-agent e hermes-agent.ai/changelog (consultati il 2026-10-16); github.com/NousResearch/hermes-official-plugins e github.com/orgs/NousResearch/repositories (catalogo plugin, aggiornato il 15 ottobre 2026); developer.nvidia.com/blog/nvidia-nemotron-3-5-super-vl-powers-specialized-agents-with-multimodal-reasoning (Hermes Bench 63,44); nousresearch.com (annuncio Nemotron 3.5 Super VL); sidley.com, techcrunch.com, startupfortune.com e techfundingnews.com (Series B 90 M$ a 1,5 mld $, 7 ottobre 2026).*
