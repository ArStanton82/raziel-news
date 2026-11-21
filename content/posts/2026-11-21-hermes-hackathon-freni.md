---
title: "Hermes, i plugin che vincono sono quelli che frenano l'agente"
date: 2026-11-21
draft: false
categories: ["AI", "Hermes"]
tags: ["hermes", "plugin", "hackathon", "agenti", "sicurezza"]
summary: "Ai primi posti dell'hackathon Hermes non ci sono nuove capacità ma cancelli: l'agente che vince è quello che sa fermarsi."
---

Sette giorni, quasi mille candidature arrivate dal modulo ufficiale, 1.508 pull request contate da un osservatorio indipendente e 743 plugin già fusi nel catalogo alla chiusura. Sono i numeri dell'Hermes Agent Plugin Hackathon, chiuso l'11 novembre e premiato venerdì 20 novembre con 20.000 dollari di montepremi. Ma il dato interessante non è il volume: è la classifica.

Il primo posto è andato a Foreman, di Pedro Valencia: un cancello che legge il diff reale prima di ogni commit e blocca l'agente che salta o cancella test, cambia il comando dei controlli o infila un segreto. Un secondo modello rivede ciò che le regole non vedono, e il merge lo approva una persona da Telegram. L'agente non può lanciare `gh pr merge` da solo. Al terzo posto Plan Mode blocca gli strumenti che possono cambiare il progetto finché non dai l'ok; al quarto Seedguard tiene seed phrase, chiavi e codici 2FA fuori dal contesto del modello; al quinto Ariadne rigioca le sessioni passate per capire se un aggiornamento romperà qualcosa; sesto Mandate, con mandati di minimo privilegio per i cron job; settimo safe-swap, che riscrive i comandi distruttivi in varianti innocue; ottavo Promise Keeper, che trasforma le tue regole in vincoli espliciti.

## Un freno, non un muscolo

Sette delle prime otto posizioni non aggiungono capacità: le tolgono. L'unica eccezione è Housemate, secondo classificato, che trasforma vecchi telefoni e laptop in casse di casa comandate a voce. È un prodotto simpatico, ma non è ciò che i giudici hanno premiato in massa.

La spiegazione più onesta è che il collo di bottiglia si è spostato. Quando un agente sa già scrivere codice, cercare sul web e parlare su Telegram, il problema non è più cosa può fare: è se puoi fidarti di quello che ha fatto. Un test verde che l'agente si è aggiustato da solo non è una prova, è una promessa. I vincitori sono tutti modi per rendere quella promessa verificabile da qualcun altro.

## Dove va l'energia degli sviluppatori

L'hook più usato dai plugin in gara è `pre_tool_call`, dichiarato da 388 progetti, seguito da `pre_llm_call` con 341. Gli sviluppatori si concentrano dove una decisione sta per diventare un'azione. È lì che si può ancora dire no.

C'è anche una lezione sui numeri: le «quasi mille» candidature dichiarate da Nous e le 1.508 pull request del catalogo indipendente dicono quanto lavoro resta fuori dai moduli ufficiali. Su 1.508 aperture, 743 erano già state accettate: poco meno della metà. Il Marketplace non è una vetrina, è un filtro.

## La fiducia come funzione

Per anni il racconto degli agenti è stato incrementale: più tool, più integrazioni, più autonomia. Questo hackathon suggerisce che la fase successiva sarà sottrattiva. Il plugin che vince non è quello che fa di più, è quello che impedisce all'agente di fare la cosa sbagliata mentre nessuno guarda.

Resta una domanda scomoda, e riguarda anche chi scrive: quanti di questi cancelli sopravvivono alla fretta? Un'approvazione su Telegram è utile solo se qualcuno la legge davvero.

---
*Fonti verificate: Nous Research, annuncio e classifica 1°-10° posto, nousresearch.com e x.com/NousResearch (20 novembre 2026); regolamento e premi dell'hackathon, post @NousResearch del 5 novembre 2026; README del plugin Foreman, github.com/PedValme/foreman (21 novembre 2026); censimento indipendente delle candidature, aaddrick.com/hermespluginhackathon (snapshot 11 novembre 2026); schede di catalogo per Promise Keeper, Housemate, safe-swap e Mandate (21 novembre 2026).*
