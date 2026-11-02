---
title: "Hermes vuole che il tuo setup non sappia su quante macchine vive"
date: 2026-11-02
draft: false
categories: ["Hermes", "AI"]
tags: ["Hermes Agent", "gateway", "plugin", "migrazione", "desktop"]
summary: "Un commit di test disegna un desktop in cui ogni macchina tiene il suo gateway, mentre il catalogo impara a importare anche Grok Bot."
---

C'è un momento preciso in cui uno strumento smette di essere un programma e diventa un'infrastruttura personale: quando lo usi su due macchine e non vuoi più sapere quale delle due stia facendo cosa. Hermes si sta muovendo verso quel momento, e lo sta facendo con una modifica poco appariscente: un commit di test, non una nota di rilascio.

## Ogni macchina tiene il suo gateway

Il commit «test(desktop): remote-topology allows This device's kept gateway; the chat still goes remote», mergiato nella notte tra l'1 e il 2 novembre, descrive una topologia in cui la pull request 147681 «tiene connesso ogni gateway registrato per la durata della finestra, compreso quello di questa macchina quando il primario è remoto». In pratica: un desktop in modalità remota che ha Hermes installato avvia adesso un gateway locale proprio, mentre la chat continua ad andare al server remoto. Il commit esiste perché la specifica di collaudo affermava il contrario, e faceva fallire i test end-to-end su Linux.

È un dettaglio di ingegneria, ma dice la direzione: non un'app che si connette a un server, bensì un insieme di nodi equivalenti che si riconoscono. L'account di monitoraggio @HermesWatcher ha rilanciato il 2 novembre che la prossima release desktop sarà «grossa» e che usare Hermes su più macchine sembrerà «un solo setup»: ogni gateway registrato si connette all'avvio, resta connesso, si riconnette da solo se cade, e il passaggio da uno all'altro è istantaneo. Va detto che è un annuncio di community: al momento della verifica non risultano note di rilascio ufficiali.

## Il catalogo che importa anche Grok Bot

La seconda metà del lavoro è la porta d'ingresso. Alle 06:23 UTC del 2 novembre il repository principale ha pinnato `agent-importers` 1.2.1, che aggiunge l'importazione da Grok Bot a quelle già presenti per OpenClaw, Claude Code, Codex CLI, Cursor e OpenBot. Il README del plugin, un tempo parte del nucleo (`hermes_cli/agent_import.py`), documenta un comando per ciascun bersaglio: il Bot scrive un export JSON e `hermes import-agent grok-bot` lo porta dentro, con anteprima voce per voce e `--dry-run` che non tocca il disco. Chiavi API e credenziali non vengono importate, con una sola eccezione esplicita: i segreti in allowlist di OpenClaw, e solo passando `--migrate-secrets`.

La pagina del catalogo, ripinnata al commit `ba4f8c9`, elenca ormai sei bersagli: la copertura Grok Bot non è più solo su `main`.

## Perché conta

Le due cose insieme raccontano una strategia che non passa dalla pubblicità: abbassare il costo di cambiare idea. Chi arriva da un altro agente trova un comando; chi ha già due computer trova un solo pannello. È un modo di crescere meno rumoroso di un lancio, e più difficile da imitare, perché richiede che il prodotto regga la complessità al posto dell'utente.

Resta un'avvertenza. Un commit di test che adegua una specifica non è una promessa commerciale, e un post di monitoraggio non è una release. La topologia multi-gateway esiste nel codice e nei test; la data in cui la vedrai nel desktop, no.

---
*Fonti verificate: GitHub NousResearch/hermes-agent — commit `30ee54e` e storia di `main`, incluse «test(desktop): remote-topology allows This device's kept gateway» e «chore: plugin catalog pins agent-importers 1.2.1» (2 novembre 2026); README di agent-importers su `main` e pagina del catalogo plugin, pinnata a `ba4f8c9` (2 novembre 2026); post di @HermesWatcher sulla prossima release desktop (2 novembre 2026, annuncio di community, non confermato da note ufficiali). Nota: il report indicava il catalogo ancora fermo a quattro importer; la pagina risulta ripinnata e documenta già Grok Bot e OpenBot.*
