---
title: "Hermes esce dal terminale: Microsoft Store, plugin di catalogo e una release che si taglia da sola"
date: 2026-10-09
draft: false
categories: ["Hermes", "AI"]
tags: ["hermes-agent", "microsoft-store", "plugin-catalog", "release", "nous-research"]
summary: "Hermes arriva sul Microsoft Store, Spotify esce dal core come plugin di catalogo e debutta la pipeline di release stabile v0.21.6."
---

Per un anno Hermes Agent è stato un oggetto da iniziati: si installava con una riga di comando, si configurava in un file YAML e si spiegava agli amici con una certa aria di complicità. Questa settimana il progetto ha fatto il passo che cambia la platea: esce dai terminali e si mette dove lo trovano tutti.

## Un'installazione a un clic

Nous Research ha annunciato l'8 ottobre che Hermes Agent è ora disponibile — e in evidenza — sul Microsoft Store, con installazione a un clic. Non è un dettaglio cosmetico. Distribuire un agente su uno store significa firmare il pacchetto, gestire gli aggiornamenti e accettare le regole di una piattaforma chiusa, esattamente il contrario della cultura da repository che ha reso popolare il progetto. L'azienda promette altri aggiornamenti per l'ecosistema Windows nelle prossime settimane: la mossa suggerisce che il desktop, non più la CLI, diventa la porta d'ingresso.

## Il core si alleggerisce: Spotify diventa un plugin

Sul repository, i commit del 9 ottobre confermano una scelta architetturale: l'integrazione Spotify esce dal core e diventa un plugin ufficiale del catalogo, mantenuto in un repository separato. Gli utenti esistenti vengono migrati automaticamente, login e dati inclusi. È la logica che Nous ha già applicato altrove: il core resta magro, le funzionalità vivono in moduli che si installano quando servono. Un core più piccolo è un core più facile da aggiornare e da mantenere sicuro.

## v0.21.6 e la pipeline di release

L'8 ottobre è arrivata la release v0.21.6, una patch che raccoglie circa 2.100 pull request accumulate dalla v0.21.5. Il dato interessante non è il numero, ma il come: è la prima release tagliata dalla nuova pipeline stabile, con un'unica referenza di build, un'immagine Docker testata e un tag di ricevuta alla pubblicazione. Docker e Hermes Cloud seguono il canale stable; app desktop, pacchetti Termux e Microsoft Store restano sulla build corrente fino al prossimo rilascio raggruppato. Tra le correzioni di sicurezza, l'irrigidimento dell'autenticazione della dashboard contro header contraffatti.

## La community e i suoi eccessi

Dalla community arrivano i segnali più ambivalenti. Un utente racconta di essersi ritrovato con oltre 200 skill accumulate in due settimane e chiede strumenti per governarle; un altro celebra il caso d'uso di un agente che, ricevuti i requisiti, costruisce da sé un team di bot specializzati, ognuno con il proprio modello. È l'auto-evoluzione che Nous vende come bandiera — e che, senza freni, rischia di diventare rumore.

## Conclusione

La domanda aperta non è più se Hermes sia potente, ma se la potenza regga la popolarità. Uno store semplifica l'ingresso; un core snello lo tiene in ordine. Resta da vedere se l'ecosistema saprà restare leggibile mentre cresce.

---
*Fonti verificate: nousresearch.com e X @NousResearch (8 ottobre 2026); hermesbible.com/changelog e commit GitHub NousResearch/hermes-agent (9 ottobre 2026); api.github.com/repos/NousResearch/hermes-agent/releases/latest e github.com/NousResearch/hermes-agent/releases (8 ottobre 2026); hermes-agent.nousresearch.com/docs — installation, plugin-catalog (9 ottobre 2026); X @HermesWatcher e @junthekey (9 ottobre 2026).*
