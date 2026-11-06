---
title: "Hermes 0.23: il desktop diventa una scheda del browser"
date: 2026-11-06
draft: false
categories: ["Hermes", "AI"]
tags: ["hermes agent", "webapp", "gateway", "plugin", "open source"]
summary: "La release Hearth porta la workspace Desktop in un tab del browser e affida ogni conversazione a un solo gateway."
---

C'è un momento, in ogni progetto che cresce, in cui l'interfaccia smette di essere una finestra e diventa un'abitudine. Hermes Agent arriva a quel momento con la v0.23.0, ribattezzata The Hearth: il focolare attorno a cui si raccolgono le superfici che fino a ieri vivevano ognuna per conto proprio.

## Il desktop in una scheda
La novità che dà il nome alla release è la Webapp: il gateway serve l'intera workspace Desktop, con chat, Group Chats, plugin e impostazioni, dentro qualunque browser della rete o dietro un URL pubblico con accesso autenticato. È spenta di default e si accende con `webapp.enabled`, oppure da Impostazioni, alla voce Web Access. L'immagine Docker e il pacchetto Nix la includono già. La promessa è sobria e per questo credibile: nessun clone, nessuna chat alleggerita, le stesse sessioni su ogni schermo.

## Un solo gateway, una sola verità
Sotto la superficie c'è una correzione architetturale più importante della funzione visibile. Prima, CLI, TUI, Desktop, editor via ACP, bot di messaggistica e cron potevano avviare ciascuno la propria copia dell'agente sulla stessa conversazione: è così che i messaggi venivano scritti due volte o sparivano tra una superficie e l'altra. Ora ogni macchina esegue un gateway che possiede tutte le sessioni, e ogni interfaccia vi si collega come client. Il desktop può anche modificare un prompt in coda senza che parta due volte.

## Il resto del carico
Il contorno non è folklore. Il catalogo plugin passa da circa 600 a oltre 1.050 voci, con un livello Verified per quelli firmati dal fornitore; i tool MCP a pagamento possono dichiarare un prezzo, mostrato nel prompt di approvazione insieme al totale della chat; `/rewind` riporta la conversazione a un messaggio precedente e permette di diramare una nuova sessione; il terminale disegna finalmente le immagini inline. Le skill integrate scendono da 58 a 44, con Word, PowerPoint ed Excel fusi in un'unica skill.

Il conto da pagare sta nelle note di aggiornamento: i dieci vecchi tool `browser_*` sono stati rimossi e l'automazione passa solo da `browser_exec`; il Desktop richiede macOS 13 o Windows a 64 bit; `hermes mcp serve` diventa `hermes mcp-serve`; GLM-5.3 sostituisce GLM-5.2 come default silenzioso.

## Quello che resta aperto
Su una cosa il comunicato tace: la dashboard. In risposta a un utente, Teknium ha scritto che «andrà via tra due mesi, una volta sicuri che funzioni», senza annuncio ufficiale né data. È una dichiarazione informale, e come tale va letta: la direzione è chiara, il calendario no.

La lezione della release è più interessante del changelog. Dopo aver fatto entrare le persone dalla porta, questo progetto prova a costruire il focolare: un luogo unico in cui le sessioni si incontrano, invece di tanti agenti che si contendono la stessa conversazione.

---
*Fonti verificate: release notes v0.23.0 su GitHub, NousResearch/hermes-agent, consultata il 6 novembre 2026 (10.080 commit, 1.950 PR, 666 contributor, 850 issue chiuse, Webapp, gateway unico, catalogo 600→1.050, note di aggiornamento); changelog mirror hermes-ai.net e sintesi releases.sh, 5-6 novembre 2026; post di lancio su nousresearch.com, 5 novembre 2026; dichiarazione di Teknium sulla dashboard, reply del 6 novembre 2026 (fonte unica, informale). Non incluso nel pezzo: il Plugin Hackathon da 20.000 dollari, perché l'unica fonte disponibile è l'annuncio sul sito ufficiale.*
