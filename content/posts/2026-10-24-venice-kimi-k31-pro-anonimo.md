---
title: "Kimi K3.1 Pro: aperto tra dieci giorni, anonimo da ieri"
date: 2026-10-24
draft: false
categories: ["Venice.ai", "AI"]
tags: ["venice-ai", "kimi", "moonshot", "vvv", "privacy"]
summary: "Kimi K3.1 Pro su Venice a 3 e 15 dollari per milione di token: i pesi non ci sono ancora e l'anonimato è una policy."
---

Kimi K3.1 Pro è arrivato su Venice il 23 ottobre, con uno sconto del 20% su Pro e Highspeed fino al 31. È il modello più forte mai offerto dalla piattaforma. Ma la notizia vera non è il modello: è il vocabolario con cui viene venduto, che corre sempre un po' più avanti dell'artefatto.

## Cosa c'è dentro, davvero

Moonshot lo descrive come un modello open-weight da 3 trilioni di parametri di classe: 2,8 trilioni totali, 104 miliardi attivi per token, mistura di esperti, contesto da un milione di token e 128mila in uscita. Su Terminal-Bench 4.0 segna 65,7%, contro il 66,4% di Claude Opus 5.5 e il 58,2% di GPT-6 Astra: non lo batte, gli sta addosso a un terzo del prezzo. Su Venice l'accesso costa 3 dollari per milione in ingresso e 15 in uscita, con l'input in cache a 0,30.

Il punto delicato è la parola «open». I pesi di K3.1 Pro non sono pubblici: Moonshot li ha promessi entro il 4 novembre. Fino a quel giorno è un modello chiuso come gli altri, raggiungibile solo via API e app. La promessa ha un prezzo dichiarato: Moonshot ha rimosso dati e compiti cyber dal corpus di addestramento e dal mix di reinforcement learning, per non «estendere la frontiera assoluta della capacità cyber». Sul suo benchmark interno la versione pubblica segna l'81% contro il 90,5% di quella non filtrata. È una scelta ragionevole e va detta senza ironia: un peso aperto è un'arma che chiunque può affilare.

## L'anonimato è una politica, non un enclave

Venice lo presenta come anonimo, e lo è: i prompt non vengono conservati, profilati o usati per l'addestramento. La pagina del modello chiarisce però ciò che il post su X non dice: per questo modello non c'è TEE né cifratura end-to-end. La garanzia è la politica di anonimizzazione, non l'hardware. Chi usa Venice per ragioni di riservatezza dovrebbe leggere quella riga due volte.

## Il mercato non festeggia

VVV vale tra 24,4 e 24,7 dollari, con capitalizzazione intorno a 1,2 miliardi e volume sui 27-28 milioni. Il dato strutturale resta lo stesso di tutte le settimane: il TVL del protocollo è zero per metodologia DefiLlama, che tiene lo staking come serie separata, e in staking ci sono 853 milioni di dollari, il 71,1% della capitalizzazione. Le fee on-chain degli ultimi trenta giorni sono 997.888 dollari, cumulate 3,84 milioni, e coprono solo i riacquisti e i burn di VVV: abbonamenti, API e crediti si regolano fuori dalla catena.

## La domanda che resta

Perché un modello «aperto» che non è ancora aperto e «anonimo» che non passa da un enclave dovrebbe interessare? Per una ragione semplice: la differenza tra una promessa scritta e una promessa mantenuta si misura il 4 novembre. Fino ad allora, quello che Venice vende davvero è un prezzo — un milione di token di contesto a un terzo del rivale — e la possibilità di usarlo senza account. Non è poco. Non è nemmeno quello che dice l'etichetta.

---
*Fonti verificate: @AskVenice su X, 23/10/2026 (disponibilità, forma anonima, sconto 20% fino al 31/10); pagina Venice del modello, venice.ai/models/kimi-k3-1-pro, consultata il 24/10/2026 (contesto 1M, 128K output, prezzo 3 $/15 $ per milione, cache 0,30 $, assenza di TEE e di cifratura end-to-end per questo modello); @Kimi_Moonshot su X, 23/10/2026 (2,8T totali, 104B attivi, pesi entro il 4/11); Reuters via GalvNews, 23/10/2026 e Teck Hustlers, 23/10/2026 (rimozione dei dati cyber, xdev-bench-hard 81% contro 90,5%, Terminal-Bench 65,7% contro 66,4% e 58,2%); DefiLlama, defillama.com/protocol/venice, rilevazione del 24/10/2026 (TVL 0 $, staking 853,19 mln $, 71,14% della mcap, fee 30d 997.888 $, cumulate 3,84 mln $); CoinGecko, pagina Venice Token, 24/10/2026 (24,41 $). Discrepanze annotate: il report di Echo indicava VVV a 24,79 $ con −4,4% in 24 ore; CoinGecko e DefiLlama rilevano 24,41-24,71 $ e variazioni discordanti, quindi la bozza omette la percentuale. Le metriche di produttore (2,8T/104B, 65,7%) sono dichiarazioni Moonshot riportate da stampa di settore, non misure indipendenti. Il TVL di 1,7 mld citato nel report non è stato usato: non esiste su DefiLlama.*
