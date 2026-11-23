---
title: "Hermes cambia casa: il cruscotto va in pensione, il gateway resta"
date: 2026-11-23
draft: false
categories: ["Hermes", "AI"]
tags: ["Hermes Agent", "Nous Research", "gateway", "dashboard", "MCP", "open source"]
summary: "Il vecchio cruscotto di Hermes lascia il posto alla web app del gateway: una sola sessione, molte finestre. E il mercato ci mette un po' di troppo."
---

Nelle ultime ore su X qualcuno ha chiesto a Nous Research se Microsoft l'avesse comprata. La risposta dell'account ufficiale è stata secca: «We weren't acquired lol». Fa sorridere, ma è la notizia meno interessante della settimana. Quella vera è più quieta e riguarda l'architettura: il cruscotto locale di Hermes esce di scena, e al suo posto resta il gateway.

## Una sola sessione, molte finestre

La direzione è scritta nella release v0.23.0, la «Hearth Release» del 5 novembre: la nuova Webapp serve l'intero workspace di Desktop dal gateway dell'utente — stesse chat, stessi plugin e impostazioni — in qualunque browser, in rete locale o dietro un accesso autenticato. È spenta per default e si accende con `webapp.enabled`. Sotto c'è il cambio concettuale: ogni macchina esegue un solo gateway che possiede tutte le sessioni, e le superfici (CLI, TUI, Desktop, editor, bot, cron) vi si agganciano come client. Una chat aperta ovunque è la stessa chat, con una coda e una storia sola. Il patch v0.23.3 del 20 novembre ha arrotolato 370 pull request in una release stabile.

## Il cruscotto esce di scena

Il 22 novembre l'account di monitoraggio @HermesWatcher ha annunciato che il vecchio dashboard «is on its way out»: un comando sposta l'utente sulla web app del gateway, stesso indirizzo e stesso accesso (131 like, 10.333 visualizzazioni). La frase di Teknium citata ieri — «the dashboard is being deprecated» — va nella stessa direzione. Anche la documentazione ha già il linguaggio del trasloco: parla di «Move to a single Hermes» quando un vecchio `hermes dashboard` o `hermes serve` serve ancora la home di un profilo. Manca però una nota di release ufficiale che descriva la dismissione: finché non arriva, è un annuncio, non un contratto.

## La periferia si muove più del centro

Intorno al gateway crescono le superfici. Un utente ha collegato un agente vocale di terze parti (JooVoice) via MCP, con una riga di comando e un'auth OAuth, per farsi chiamare quando un bug è stato corretto. Un altro account descrive Imagination Studio, uno studio di produzione dentro un messaggio Telegram: miniature, voiceover, musica d'intro. Nessuno dei due è un annuncio ufficiale, ma indicano dove si sposta l'interesse: meno demo del modello, più superfici in cui l'agente lavora.

## Il mercato, intanto

Il partenariato con Microsoft resta quello del 18-19 novembre: Hermes Enterprise dentro Teams, Microsoft Store e Azure, con M12 tra gli investitori. La smentita di stanotte è una risposta a utenti, non un comunicato. Serve però a ricordare una distinzione che il rumore confonde: distribuzione e proprietà non sono la stessa cosa.

La lezione della settimana è piccola e concreta. Quando un prodotto matura non si annuncia con un tweet: si annuncia con una migrazione che qualcuno deve fare. Il cruscotto che sparisce è il segno che Hermes sta diventando infrastruttura, e le infrastrutture si giudicano da quanto è indolore restare.

---
*Fonti verificate: changelog ufficiale Hermes Agent v0.23.0 (5/11/2026) e v0.23.3 (20/11/2026) su hermes-ai.net/changelog e API GitHub releases (23/11/2026); documentazione Hermes, «Hermes Web Dashboard» (23/11/2026); post @HermesWatcher 22-23/11/2026 e @NousResearch/@Teknium 22/11/2026 (come riportati nel report di Echo, metriche incluse); post @NousResearch sul partenariato Microsoft 19/11/2026.*
