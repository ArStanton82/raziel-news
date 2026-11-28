---
title: "Trecentotrentotto PR, nessuna nota: la patch che rimanda il racconto"
date: 2026-11-28
draft: false
categories: ["Hermes", "AI"]
tags: ["hermes agent", "release", "agenti", "open source"]
summary: "Hermes v0.23.5 allinea CLI, Store, Docker e Cloud su 338 PR unite, ma le note curate slittano a v0.24.0: il changelog lo scrivono i terzi."
---
Alle 03:20 UTC di oggi è uscita Hermes Agent v0.23.5. Il corpo della release la data 27 novembre, il tag arriva il 28: è il primo dettaglio di una versione che sembra voler passare inosservata. Dentro la finestra da v0.23.4 ci sono 338 pull request unite, 1.262 commit non-merge, 1.146 file cambiati (+57.989 / −5.346) e 92 issue chiuse, misurati al commit `a428f5344f77`. Le note curate, però, arriveranno con la v0.24.0. Tradotto: si aggiorna adesso, si capisce dopo.

## Il terminale ricorda
La voce più interessante non è nelle note, ed è dichiarata «undocumented here on purpose»: la CLI e la TUI supportano il protocollo di ripresa OSC 7577. Ora Hermes comunica al terminale il comando per riaprire la sessione — `hermes -p PROFILO --cli --resume SESSION_ID` — autenticato con un token del riquadro, e lo cancella solo su `/quit` o Ctrl+D. Il record sopravvive a crash, perdita del terminale e riavvii da `/update`: proprio i casi in cui una sessione va offerta indietro. La persistenza smette di essere una funzione dell'applicazione e diventa una convenzione del terminale.

## L'agente lavora a finestra chiusa
Il secondo cambiamento è silenzioso: il gateway compatta in background le chat inattive. Prima se ne accorgeva solo al messaggio successivo, che aspettava la summarizzazione; ora il tick di manutenzione che già gira ogni cinque minuti prende in carico la conversazione scaduta. La soglia è `compression.idle_compact_after_seconds`, default `0`, quindi spenta, e si può fissare per singolo canale. Nel test dell'autore su un endpoint personalizzato: da 16 a 8 messaggi, da circa 8.611 a 3.665 token, e il prompt successivo sceso da 28.310 a 5.865.

## Il profilo è il confine
Poi c'è la voce che conta per chi installa plugin: una serie di correzioni lega il lavoro dei plugin al nome del profilo con cui è stato aperto (`owner_home`), non alla directory risolta. Quando `profiles/<nome>` è un symlink fuori dalla radice, prima si poteva avviare il launcher indicato nel `config.yaml` di quel profilo e far arrivare un `PYTHONPATH` dal suo `.env` al processo figlio dell'host dei plugin. Ora, se nessun nome porta più a quella directory, il lavoro viene rifiutato con un errore di home spostata. È un fix di sicurezza raccontato come manutenzione.

## Il prezzo e il desktop
Sullo sfondo commerciale, il Black Friday di Nous: 50% sul primo mese di un piano Portal nuovo o aggiornato con il codice FIFTYFIFTY, per 24 ore dal post del 27 novembre, con una pagina promozionale dietro login. Sul desktop, il merge `d71a657` delle 04:35 UTC porta gli aggiornamenti in-app degli AppImage Linux, con due correzioni sulla ricerca dell'aggiornamento.

Il punto editoriale è il versioning come atto di comunicazione. Una patch che allinea CLI, Microsoft Store, Docker e Hermes Cloud sullo stesso codice è una scelta di igiene, ma rimandare le note significa chiedere fiducia: aggiorna senza sapere cosa cambia, te lo diciamo alla prossima minor. Nel frattempo il changelog lo scrivono i terzi, e per una volta la documentazione più utile è fuori dal repository.
---
*Fonti verificate: release GitHub v0.23.5 e API GitHub del 28/11/2026 (pubblicazione 03:20 UTC, commit `a428f5344f77`, conteggi della finestra); changelog indipendente hermes-agent-lab.com/releases/v0-23-5 (28/11/2026, dettagli su OSC 7577, compaction e owner_home); post @NousResearch del 27/11/2026 e pagina promozionale portal.nousresearch.com/promos/fiftyfifty; API GitHub per il commit `d71a657` (merge 28/11/2026, 04:35 UTC).*
