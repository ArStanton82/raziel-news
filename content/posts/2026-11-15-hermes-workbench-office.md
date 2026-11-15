---
title: "L'ufficio entra nell'agente: Hermes Desktop impara a modificare i file veri"
date: 2026-11-15
draft: false
categories: ["Hermes", "AI"]
tags: ["Hermes", "plugin", "Workbench", "Microsoft Office", "agenti"]
summary: "Un plugin comunitario porta Word, Excel e PowerPoint dentro Hermes Desktop. Il catalogo cresce a un ritmo che chiede regole, non entusiasmo."
---

Il catalogo dei plugin di Hermes ha smesso di essere una raccolta di curiosità. La canary pubblicata questa mattina — v0.23.1+canary.20261115T064406Z, alle 07:52 UTC — è per gran parte un elenco di voci di catalogo: decine di plugin aggiunti o ripinnati, da dosbox-mcp a video-xray, da hermes-eye-memory a progression. Il numero che conta però non è la quantità: è che tra quelle voci ce n'è una che tocca i file con cui le persone lavorano davvero.

## Office dentro Desktop

La scheda si chiama hermes-office-desktop e la descrizione la firma «Workbench by Atlas Omnia»: apre e modifica Word, Excel, PowerPoint, OneNote e Outlook per il web dentro Hermes Desktop. Due dettagli valgono più del titolo. I sistemi supportati sono macOS e Windows, quindi si parla dell'app desktop e non della riga di comando. E ogni modifica passa da un'approvazione esplicita di Hermes. Il plugin è entrato in catalogo il 13 novembre, è di livello «community» — non è un prodotto Nous — e il repository che lo ospita ha due stelle su GitHub. Non è una condanna: è la misura di quanto sia giovane tutto questo.

## La domanda che arriva prima della funzione

Un plugin che scrive in un file reale sposta il problema dal modello ai permessi. Nella stessa canary compare permission-tiers, che assegna a ogni schema di nome di tool un livello allow, ask o block e intercetta la chiamata prima che parta, tenendo un registro locale delle decisioni. È il contrappeso naturale di Workbench, e spiega perché convenga guardare l'ordine degli eventi più che le feature: prima l'accesso ai file, poi il modo per limitarlo.

## Il costo di un ecosistema veloce

Il catalogo viene ripinnato più volte al giorno e il repository ha superato le 263 mila stelle. La velocità è insieme la promessa e il rischio: un plugin che nessuno ha ancora usato in produzione entra in una lista che, ai più, sembra una garanzia. La distinzione tra «ufficiale» e «community» nelle schede non è burocrazia, è il livello di promessa. Anche voci arrivate in questi giorni, come own-compute, si presentano nel changelog come candidature all'hackathon: materiale fresco, non necessariamente stagionato.

## Conclusione

Che un agente apra un foglio di calcolo e ci scriva dentro è, tecnicamente, un piccolo evento; editorialmente è il punto in cui la chat smette di essere un'interfaccia e diventa un collega con accesso alle cartelle. La domanda utile non è più «cosa può fare», ma «chi approva, cosa resta scritto, come si torna indietro». Workbench risponde con un prompt di conferma per ogni modifica. È un inizio ragionevole — e il fatto che sia un plugin comunitario, con due stelle, dice quanto lavoro di fiducia resti da fare.

---
*Fonti verificate: GitHub, release NousResearch/hermes-agent v0.23.1+canary.20261115T064406Z (15/11); GitHub API, repos/NousResearch/hermes-agent (15/11); catalogo plugin hermes-agent.nousresearch.com/marketplace, schede hermes-office-desktop e permission-tiers (15/11); repository github.com/AtlasOmnia/workbench (15/11). Nota: la pagina X di @HermesWatcher annunciava il plugin come «Workbench nel catalogo»; il contenuto è stato verificato sulla scheda del catalogo ufficiale, che precisa «Outlook per il web» e il solo supporto macOS/Windows.*
