---
title: "Un modello da 600 miliardi gratis nell'agente: la settimana in cui Hermes fa i conti con la propria scala"
date: 2026-10-10
draft: false
categories: ["Hermes", "AI"]
tags: ["hermes-agent", "stepfun", "step-5-preview", "nous-portal", "kanban", "v0.21.6"]
summary: "Step 5 Preview gratis per una settimana su Nous Portal, la release stabile v0.21.6 e gli strumenti per governare molti agenti insieme."
---

Per chi segue Hermes Agent, questa settimana ha un sapore diverso dal solito. Non è l'ennesima funzione aggiunta al core, ma il momento in cui il progetto comincia a comportarsi come un'infrastruttura: modelli di frontiera che arrivano nel catalogo, una pipeline di release che si stabilizza e una serie di strumenti che servono a governare la complessità generata dalla propria crescita.

## Un modello di frontiera, in prova gratuita

Nous Research ha reso disponibile Step 5 Preview di StepFun su Nous Portal, gratis per una settimana. I numeri spiegano perché la notizia conti: architettura sparse mixture-of-experts con circa 600 miliardi di parametri totali e 27 miliardi attivi per token, finestra di contesto da un milione di token e input anche visivo. Sul Hermes Index — la classifica che Nous costruisce facendo girare ogni modello attraverso lo stesso harness dell'agente — il punteggio iniziale di 33.89 è stato poi corretto a 32.83, appena dietro GPT-6 Luna (33.89) e GLM 5.3 Flash (34.95). Restano i costi di listino, una volta finita la promozione: 1 dollaro per milione di token in input e 2,70 in output. La mossa dice qualcosa di più ampio: l'agente non è più solo il guscio, ma il banco di prova su cui i laboratori misurano i propri modelli.

## La release impara a essere stabile

L'8 ottobre è arrivata la v0.21.6, la prima tagliata dalla nuova pipeline di release stabile: un'unica referenza di build, un'immagine Docker testata e un tag di ricevuta alla pubblicazione. Racchiude circa 2.100 pull request accumulate dalla versione precedente e tre gruppi di correzioni di sicurezza, tra cui l'irrigidimento dell'autenticazione della dashboard. Le note curate complete arriveranno con la v0.22.0. È il segnale che il progetto vuole smettere di essere un cantiere permanente.

## Governare molti agenti, non uno

Sul fronte operativo, l'attenzione si sposta dalla singola conversazione al coordinamento. Hermes Kanban è una board persistente, condivisa tra profili, in cui ogni attività è una scheda con un assegnatario e uno stato; un dispatcher reclama le schede pronte e avvia worker in workspace separati, con heartbeat e recupero dei task rimasti orfani. Attorno al progetto ufficiale cresce poi un ecosistema di terze parti: Ares, un workbench per chi vuole controllo esplicito sulle release, e HOL Guard, un layer di sicurezza locale che ispeziona comandi e plugin prima dell'esecuzione. Sono iniziative indipendenti e con pochissima trazione — vale la pena ricordarlo — ma indicano dove si sta spostando la domanda: sicurezza e supervisione, non più solo capacità.

## Conclusione

La domanda aperta non è più se Hermes sappia fare cose difficili, ma se sappia restare comprensibile mentre le fa. Un modello da 600 miliardi in prova gratuita, una release che si stabilizza e una board che coordina decine di worker raccontano la stessa transizione: da strumento potente a piattaforma su cui altri costruiscono. La parte difficile comincia adesso.

---
*Fonti verificate: nousresearch.com e X @NousResearch (8-9 ottobre 2026); alphasignal.ai e aipromonow.com su Step 5 Preview e Hermes Index (8-9 ottobre 2026); newreleases.io/project/github/NousResearch/hermes-agent/release/v0.21.6, github.com/NousResearch/hermes-agent/releases e hermes-agent-lab.com/releases (8 ottobre 2026); hermes-agent.nousresearch.com/docs — kanban (9 ottobre 2026); X @HermesWatcher, @RecursiveIntell, @NFTerramike (9-10 ottobre 2026).*
