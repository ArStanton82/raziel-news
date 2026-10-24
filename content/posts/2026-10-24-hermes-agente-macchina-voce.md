---
title: "L'agente si prende una macchina e una voce"
date: 2026-10-24
draft: false
categories: ["Hermes", "AI"]
tags: ["hermes", "plugin", "cua", "voce", "agenti"]
summary: "Hermes esce dal desktop: uno Space isolato da guardare dal vivo e la voce spostano il luogo in cui vive l'agente."
---

Per due giorni la community di Hermes ha discusso di due plugin, non di un modello. È un dettaglio che dice molto: il collo di bottiglia di un agente autonomo non è più quanto bene ragiona, ma dove viene eseguito e da chi può essere interrotto.

## Una macchina che non è la tua

Il plugin cua-spaces, del team trycua, è nel catalogo ufficiale dalla versione 0.4.0, tier verificato, ed è la cosa più interessante della settimana. Sposta terminale, file e codice dentro uno Space: una macchina Linux, macOS o Windows isolata, sull'hardware che già possiedi o nel tuo account cloud. Si attiva con un comando, `hermes config set terminal.backend cua`, e da quel momento ogni comando finisce lì invece che sul tuo portatile.

Due conseguenze contano più delle altre. La prima è la supervisione: lo Space ha una vista dal vivo, chiunque nel team può guardare, intervenire, restituire il controllo e lasciare che l'agente continui. La seconda è la sicurezza: poiché lo Space è già il sandbox, Hermes smette di chiedere conferma per i comandi rischiosi eseguiti al suo interno. È un patto esplicito — meno attrito in cambio di un perimetro — e vale la pena leggerlo come tale.

## La voce come superficie di orchestrazione

Il secondo plugin è hermes-talk, della community, non di Nous. Aggiunge voce bidirezionale in tempo reale: si parla, l'agente risponde a voce e nel frattempo usa i suoi strumenti veri, delega lavoro in background e riporta i risultati quando arrivano. Funziona nel terminale con `hermes talk`, in un canale vocale Discord e nella scheda Talk della dashboard. La trovata pratica è l'autenticazione: può appoggiarsi all'abbonamento ChatGPT via login Codex o a un account X Premium, senza chiave API. Il rovescio della medaglia è nei dettagli del catalogo: la modalità live passa da un endpoint non documentato, fuori dai termini pubblicati del fornitore, e può smettere di funzionare senza preavviso.

## Il rilascio che prepara il terreno

Sullo sfondo, la patch v0.22.5 del 22 ottobre: 81 pull request, 231 commit non-merge su 804 file. Le note curate arriveranno con la 0.23.0, ma l'elenco già segnala la direzione — backend di delegation sostituibili, subagenti instradati per model map o profilo e cambiabili per sessione, `hermes mcp serve` e il backend Singularity spostati dal core ai plugin.

## La domanda che resta

Un agente che ha una macchina propria, una voce con cui essere interrotto e backend che si scambiano a caldo è un agente che assomiglia sempre meno a un chatbot e sempre più a un collega con un accesso di rete. La parte difficile non sarà installare il plugin: sarà decidere chi risponde di ciò che quella macchina fa alle tre di notte.

---
*Fonti verificate: catalogo plugin Hermes, pagina cua-spaces (v0.4.0, tier verificato, backend `terminal.backend cua`, requisiti Hermes ≥0.21.6), consultata il 24/10/2026; annuncio Nous Research del 22/10/2026 su X e su nousresearch.com; repository GitHub TheSmokeDev/hermes-talk e relativo README, consultati il 24/10/2026, più voce di catalogo TheSmokeDev; GitHub, release Hermes Agent v0.22.5 (rilasciata il 23/10/2026 05:28 UTC, data di release 22/10/2026), consultata il 24/10/2026. Nota: il report di Echo attribuiva a hermes-talk licenza MIT; non è stato possibile confermarla sulla pagina del repository, quindi la bozza non la riporta. Il plugin Meshy e la disponibilità di Kimi K3.1 Pro su Nous Portal, presenti nel report, non sono stati usati come notizia principale: il primo è promozionale, il secondo è segnalato solo da account della community.*
