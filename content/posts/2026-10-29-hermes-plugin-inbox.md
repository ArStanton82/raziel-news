---
title: "Hermes impara a guardarsi dentro: il plugin inbox"
date: 2026-10-29
draft: false
categories: ["Hermes", "AI"]
tags: ["hermes", "plugin", "osservabilita", "agenti"]
summary: "Il comando hermes inbox mette in una sola schermata cron falliti, delegazioni bloccate e processi appesi. È un plugin labs, non un pezzo del core."
---

Un agente autonomo ha un problema di visibilità che assomiglia a quello di un cantiere: il lavoro procede, ma nessuno sa dire a colpo d'occhio quante impalcature sono ancora in piedi e quali sono vuote. Hermes ha aggiunto un modo per rispondere: il plugin `inbox`, che si installa con `hermes plugins install inbox` e aggiunge un solo comando, `hermes inbox`.

## Cosa si vede in una schermata

La vista è divisa in cinque sezioni. In «Needs attention» finiscono le cose che chiedono attenzione: cron con l'ultima esecuzione fallita, cron in pausa con un motivo, delegazioni ferme o senza esito, processi in background il cui PID non esiste più, task kanban bloccati. «In progress» elenca processi vivi, delegazioni asincrone in corso e task in lavorazione. Poi c'è la sezione più interessante, «Finished, result not yet delivered»: le delegazioni che hanno finito ma il cui risultato non è ancora arrivato alla conversazione che lo aspettava. Chiudono l'elenco i job schedulati con le prossime cinque esecuzioni e le superfici di chat aperte, con il titolo della sessione.

Tutto è in sola lettura: i file JSON vengono letti come file, i database SQLite aperti con `mode=ro`, e il comando non ripara né pota nulla. Esiste anche `hermes inbox --json`, per chi vuole mettere il snapshot in una dashboard.

## Perché è un plugin «labs»

Il dettaglio che conta più della funzione: il comando nasce dentro il core di Hermes, dalla pull request 81507, e da lì è stato spostato fuori in un plugin. La pagina del catalogo ufficiale lo dice senza giri di parole: «funziona, ma non è supportato», Nous Research lo ha scritto e non lo mantiene. Non è un caso isolato: altri plugin del catalogo, come il backend browser camofox o l'importatore da altri agenti, dichiarano di essere vissuti nel core prima di uscirne.

È una scelta architetturale con un prezzo. Il vantaggio è un core più magro, dove ciò che non è essenziale non entra nella superficie di manutenzione. Il prezzo è che una funzione che usi ogni giorno può smettere di funzionare senza che nessuno abbia il compito di accorgersene.

## Il buco dichiarato

L'inbox non mostra le approvazioni in sospeso e le domande di chiarimento. Non è una dimenticanza: quei prompt vivono nella memoria del processo che li ha emessi, e non esistono in uno store che un altro processo possa leggere. Quindi la schermata non è un pannello di controllo dell'agente, è un inventario di ciò che è stato scritto su disco. La differenza conta: un cron fallito lo vedi, un agente che aspetta un permesso no.

Per chi fa girare agenti di continuo, però, il passo è giusto. La maggior parte dei guasti non è misteriosa: è un processo che è morto tre ore fa e un risultato che nessuno ha mai ritirato. Vederli in una lista, invece di scoprirli per caso, cambia il modo in cui si progetta il lavoro.

---
*Fonti verificate: catalogo ufficiale dei plugin di Hermes Agent, pagina `inbox`, catalogo aggiornato al 28 ottobre 2026 (letta il 29 ottobre 2026); README del plugin sul repository `NousResearch/hermes-labs-plugins`, commit 62dbc16 (letto il 29 ottobre 2026). Il report di Echo citava anche un post su X di @HermesWatcher: usato solo come segnalazione, non come fonte.*
