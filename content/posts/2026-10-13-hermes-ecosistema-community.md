---
title: "Hermes, l'ecosistema cresce ai margini: connettori, skill e progetti della community"
date: 2026-10-13
draft: false
categories: ["Hermes", "AI"]
tags: ["hermes-agent", "nous-research", "connettori", "skill", "community", "open-source"]
summary: "Mentre la v0.21.7 consolida le release stabili, l'ecosistema Hermes cresce dal basso: connettori multi-account, la skill Anatomy e progetti come Herald OS."
---

Nelle ultime settimane l'attenzione su Hermes Agent è andata al ciclo di release e al round da 90 milioni di dollari di Nous Research. Ma la parte più interessante, per chi segue il progetto da vicino, sta ai margini: le funzioni piccole, i contributi della community, i progetti di terze parti che usano l'agente come infrastruttura. È lì che si capisce se un ecosistema sta davvero attecchindo.

## Connettori con più account, ora con un nome

Il 12 ottobre il changelog del progetto ha registrato 42 pull request mergiate l'11 ottobre. La più utile riguarda i connettori: ora supportano più account della stessa applicazione, ciascuno con un alias breve come "lavoro" o "personale". Hermes può finalmente distinguere due caselle Gmail diverse e dire sotto quale identità ha eseguito ogni chiamata; la riparazione di un account avviene senza toccare gli altri. È un dettaglio che sembra minore, ma è la differenza tra uno strumento che si usa in demo e uno che si usa al lavoro. Nello stesso ciclo è arrivata anche l'identità "guest": chi non ha un account Nous può usare i connettori, con un token dal solo scopo `connectors:invoke`.

## Una skill ufficiale arrivata dalla community

Sul fronte delle competenze, "Anatomy" è entrata nel catalogo ufficiale delle skill opzionali di Hermes. Nata come strumento per Claude Code, descrive una macchina o un concetto tecnico partendo da una riga di testo e ne costruisce un modello isometrico interattivo, con parti mobili e letture dal vivo. Si installa con `hermes skills install official/creative/anatomy`. Il co-fondatore Teknium l'ha presentata come integrazione ufficiale: un contributo esterno che diventa parte del prodotto è il segno più chiaro di una community attiva.

## Herald OS e l'ufficio 3D: si costruisce sopra Hermes

Attorno all'agente crescono poi progetti indipendenti. Herald OS, di Luke The Dev, è un sistema operativo "agent-native" che usa Hermes come interfaccia: ha superato le 400 stelle su GitHub e aggiunge un editor fotografico (Herald Canvas) e una suite documenti (Herald Docs, Sheets e Slides) su cui si può chiedere a Hermes di lavorare direttamente. È un progetto non affiliato a Nous Research — l'autore lo ripete con chiarezza — ma è anche una prova di come l'agente venga usato come strato di base. Sulla stessa linea, un utente ha costruito un "ufficio 3D" per i propri agenti, con reparti separati e una vista in tempo reale di chi lavora e chi è inattivo.

## Conclusione

Hermes ha ormai un ciclo di rilascio disciplinato — la v0.21.7 di inizio ottobre ha spostato gli aggiornamenti da sorgente sulle release taggate — e un'offerta enterprise in arrivo. Ma la sua tenuta nel tempo si misura altrove: nella capacità di assorbire contributi esterni e di diventare piattaforma per altri. I segnali di questa settimana vanno in quella direzione.

---
*Fonti verificate: github.com/NousResearch/hermes-agent (release v0.21.7, 11-12 ottobre 2026); hermes-agent-lab.com/blog ("Two Gmails, One Hermes: Connector Accounts Finally Get Names", 12 ottobre 2026) e hermesbible.com/changelog (12 ottobre 2026) sui connettori multi-account e l'identità guest; x.com/HermesWatcher sul roll-up di 42 PR (12 ottobre 2026); hermes-agent.nousresearch.com/docs/reference/optional-skills-catalog e aihub.com/briefing sulla skill Anatomy (12-13 ottobre 2026); github.com/iamlukethedev/Herald-OS e trendshift.io (6-13 ottobre 2026) su Herald OS; x.com/HermesWatcher sul progetto "ufficio 3D" (13 ottobre 2026). Nota: il report segnalava per la skill Anatomy nessuna conferma da canali ufficiali; il catalogo ufficiale delle skill opzionali e l'annuncio di Teknium confermano invece l'integrazione.*
