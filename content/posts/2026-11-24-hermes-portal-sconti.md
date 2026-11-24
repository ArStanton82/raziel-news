---
title: "Ottanta per cento da una parte, venti dall'altra: la geografia degli sconti nel Nous Portal"
date: 2026-11-24
draft: false
categories: ["Hermes", "AI"]
tags: ["Nous Portal", "prezzi", "DeepSeek", "Claude", "Arachne Flow"]
summary: "Nous Portal sconta dell'80% DeepSeek V4.1 Flash 1017 e del 20% i modelli di frontiera: la distanza tra i due sconti dice dove sta il margine."
---

Nella notte del 24 novembre Nous Research ha annunciato che DeepSeek V4.1 Flash 1017 costa l'80% in meno per dieci giorni, «grazie a DigitalOcean». La sera prima prometteva i modelli più recenti di Anthropic e OpenAI al 20% di sconto per una settimana. Due ordini di sconto diversi: non è un dettaglio commerciale, è una mappa dei margini.

## La forbice, in dollari

La pagina dei modelli del Portal rende i numeri verificabili e sono più netti dei post. DeepSeek V4.1 Flash 1017 sta a 0,03 dollari per milione di token in input e 0,12 in output, contro un listino di 0,15 e 0,60: il 20% del prezzo pieno. Claude Opus 5.5 sta a 3,20 e 16,00 contro 4,00 e 20,00; GPT-6.2 Sol a 1,60 e 8,00 contro 2,00 e 10,00. Tra il modello scontato dell'80% e quello scontato del 20% corre un fattore 107 sull'input e 133 sull'output: un milione di token in uscita costa dodici centesimi da una parte e sedici dollari dall'altra. Nella stessa tabella convivono sconti del 50% e un altro 80%: la scala non è binaria.

## Chi paga lo sconto

Il post attribuisce la promozione DeepSeek a un contributo di DigitalOcean, senza spiegare il meccanismo: capacità di calcolo donata, credito, o semplice copertura della differenza. È il dettaglio che distingue un ribasso strutturale da una campagna. Che sia campagna lo dicono le finestre — dieci giorni, una settimana — e lo dice la storia del Portal: un tracker indipendente di listini (tokenplans.dev) documenta su Nous Portal una promozione del 20% su tutti i modelli attiva da luglio e un -90% su DeepSeek V4 Flash da agosto. Il prezzo promozionale, insomma, è l'eccezione stabile di questo catalogo, non il suo listino. Per chi sceglie un modello conviene guardare la colonna non barrata: è quella che si paga quando la campagna finisce.

## Il catalogo come fossato

Il catalogo dei plugin ha intanto assorbito Arachne Flow, canvas a nodi per Hermes Desktop: la pull request (#153240) è mergiata il 12 novembre, l'autore è un terzo (EmotionalThrifty) e la scheda ufficiale descrive un editor con trigger (schedule, RSS, webhook), nodi LLM, strumenti Hermes e server MCP. Teknium, in una risposta, ha aggiunto che «un mercato dei bot» sta arrivando su Hermes Market: dichiarazione, non annuncio con data. Il punto però resta: se il tuo lavoro vive in un grafo di nodi salvato in un catalogo, cambiare fornitore costa più di quanto lo sconto faccia risparmiare.

Gli sconti dicono che l'inferenza sui modelli commodity sta diventando una voce di costo quasi irrilevante, e che sui modelli di frontiera i prezzi sono ancora rigidi. Il catalogo dice che la competizione si è spostata altrove: da quanto costa un token a dove resta il lavoro che quel token lo consuma. Le due notizie, lette insieme, raccontano la stessa strategia — entrare dal prezzo, restare con l'ecosistema — e vale la pena ricordare che il primo dei due numeri ha una data di scadenza.

---
*Fonti verificate: portal.nousresearch.com/models (consultata il 24/11/2026: prezzi e sconti puntuali, inclusi listini barrati); post @NousResearch del 23/11/2026 (19:19) e del 24/11/2026 (00:28), ripresi da nousresearch.com; tokenplans.dev/changelog (consultato il 24/11/2026: storico delle promozioni del Portal); hermes-agent.nousresearch.com/marketplace/arachne-flow (consultata il 24/11/2026); PR NousResearch/hermes-agent #153240, mergiata il 12/11/2026 (verificata via API GitHub); post @Teknium del 23/11/2026 sul mercato dei bot (dal report di Echo, non verificato in modo indipendente).*
