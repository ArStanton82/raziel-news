---
title: "Hermes 0.22.6 e il trasloco degli altri: la migrazione come funzione"
date: 2026-11-03
draft: false
categories: ["Hermes", "AI"]
tags: ["hermes", "migrazione", "grok-bot", "openbot", "cli"]
summary: "Con la 0.22.6 Hermes importa routine, skill e memorie da Grok Bot e OpenBot: un trasloco, non una clonazione."
---

Per mesi, per chi lasciava un agente conversazionale, la domanda era una sola: cosa resta dei miei automatismi? La risposta che Hermes dà da ieri è un comando. Con la versione 0.22.6, pubblicata il 2 novembre, `hermes migrate` e la procedura di primo avvio possono importare un'utenza Grok Bot o OpenBot: le routine diventano job cron, le skill restano skill, le memorie diventano memoria del profilo, e con loro arriva il ruolo del bot.

## Un trasloco con le etichette

La pull request che ha introdotto la funzione racconta bene il vuoto che colma: fino a quel momento solo il plugin agent-importers conosceva gli altri agenti, e nessuno conosceva Grok Bot. Ora il setup iniziale propone Grok Bot e OpenBot accanto a OpenClaw, Claude Code, Codex e Cursor, mentre `hermes migrate <agent>` installa l'importer quando manca e lo esegue.

Il dettaglio che merita attenzione è un altro: le routine importate arrivano in pausa. Nessun job parte due volte mentre l'originale è ancora acceso. È la differenza tra un'importazione e un incidente, e dice molto su come il progetto intende la parola "migrazione": non un fork silenzioso, ma un passaggio di consegne con il motore spento.

## 776 PR in una patch

Il numero che accompagna la release è più grande della notizia. Il rilascio è dichiaratamente una patch, ma la finestra da v0.22.5 contiene 3.448 commit non di merge su 4.316 file, 776 pull request e 385 issue chiuse. Le note curate arriveranno con la 0.23.0: qui il progetto ha scelto di elencare tutto in una riga per voce, rinunciando alla gerarchia pur di non perdere pezzi.

Vale la pena leggerlo come un segnale di metodo. Un agente che cresce a questo ritmo ha un problema di racconto, non di codice: chi lo usa ha bisogno di sapere cosa è cambiato senza dover leggere un changelog di seimila righe. La scelta di rimandare la curatela è onesta, ma sposta il lavoro di sintesi su chi adotta.

## Cosa non passa

La mappatura è esplicita e vale la pena ripeterla: routine, skill, memorie, ruolo. Non è una clonazione, è una ricostruzione dell'identità operativa. Chi si aspettava di ritrovare la cronologia delle conversazioni resterà deluso, e forse è giusto così: un agente non è il suo transcript.

C'è poi un limite pratico che il comunicato non nasconde. L'app desktop installata da pacchetto non cambia con questa release e si aggiornerà col prossimo bundle; chi usa la CLI aggiorna con `hermes update`. La migrazione, insomma, arriva prima a chi lavora in terminale.

Che un progetto giovane investa sull'importazione dagli altri è, in fondo, un atto di fiducia: presuppone che il valore di un agente stia nelle procedure che ha accumulato e non nella piattaforma che le ospita. Se il trasloco funziona, la fedeltà diventa una scelta rinnovabile ogni giorno. Ed è un modo più sobrio, e più difficile, di competere.

---
*Fonti verificate: release GitHub v0.22.6, NousResearch/hermes-agent, pubblicata il 2 novembre 2026 alle 17:18 UTC (letta il 3 novembre 2026); pull request #147724 "Grok Bot and OpenBot users can move to Hermes from setup and hermes migrate" (letta il 3 novembre 2026); documentazione CLI e import-from-other-agents citata nella PR. Non verificati e perciò esclusi: il conteggio delle modifiche della beta mobile e i numeri di build iOS/Android, assenti da fonti ufficiali; il caso d'uso Olares, di natura promozionale.*
