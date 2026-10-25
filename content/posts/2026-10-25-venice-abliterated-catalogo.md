---
title: "Un modello senza rifiuti non rende il token più prezioso"
date: 2026-10-25
draft: false
categories: ["Venice.ai", "AI"]
tags: ["venice-ai", "abliterated", "uncensored", "vvv", "defillama"]
summary: "Abliterated Large Flash entra nel catalogo Venice a 1,25 e 2,50 dollari per milione di token. VVV resta a 24,6 dollari e il TVL è zero."
---

Il 22 ottobre Venice ha aggiunto al catalogo Abliterated Large Flash, un modello di Abliteration costruito su una base DeepSeek V4.1-Flash-1017, nello stesso giro in cui è arrivato DeepSeek V4.1 Flash Uncensored. La sequenza dice qualcosa che i singoli annunci nascondono: l'assenza di rifiuti non è più un esperimento sul bordo del catalogo, è una linea di prodotto.

## Cosa c'è dentro, e cosa non promette

Abliterated Large Flash costa 1,25 dollari per milione di token in ingresso e 2,50 in uscita, con l'input in cache a 0,13. Regge un milione di token di contesto e 128mila in uscita, accetta testo e immagini, fa tool calling, JSON strutturato e ricerca web. Venice lo serve quantizzato in FP8 e lo colloca nel livello «anonimizzato»: i prompt sono trattati in modo transitorio, non conservati, non profilati, non usati per l'addestramento.

L'abliterazione rimuove dalle rappresentazioni interne le direzioni che producono il rifiuto, così il modello risponde senza che l'utente debba costruire un jailbreak. La documentazione del produttore, riportata dalla pagina Venice del modello, ammette però che alcune richieste ricevono ancora un rifiuto e che il comportamento varia con il prompt. È la differenza tra «riduce i rifiuti» e «non rifiuta mai».

## Quattrocento modelli, ma il mercato guarda un'altra cosa

La documentazione Venice elenca 401 modelli, 140 di solo testo. Il catalogo cresce per accumulo, e la domanda non è quale modello sia migliore, ma chi paga la bolletta di questa abbondanza.

VVV vale 24,64 dollari, con capitalizzazione intorno a 1,2 miliardi e volume nelle 24 ore sui 21 milioni. In staking ci sono 855,81 milioni di dollari di token, il 71,45% della capitalizzazione: quasi tre quarti del valore del progetto è immobilizzato in un contratto. Il TVL del protocollo misurato da DefiLlama resta zero — non per un errore di rilevazione, ma perché la metodologia tiene lo staking come serie separata. Il dato del report di oggi, 1,71 miliardi di TVL, non esiste su DefiLlama e non va ripetuto.

Sul lato ricavi, gli ultimi trenta giorni hanno prodotto circa un milione di dollari di fee on-chain, 4,37 milioni annualizzate e 3,86 cumulati da dicembre 2025: solo riacquisti e burn di VVV. Abbonamenti, API e crediti si regolano fuori dalla catena e non compaiono in quella cifra. Il rapporto prezzo/ricavi è intorno a 98 volte, secondo DefiLlama.

## La parte che nessuno mette nel comunicato

Il token è a 34,53 dollari dal massimo storico del 21 settembre, quindi circa il 29% sotto: ha recuperato il 9,6% in una settimana e perso il 18,9% in un mese, mentre il catalogo si allargava.

Un modello che non chiede mai permesso è una proposta chiara, e Venice è una delle poche piattaforme a venderla senza giri di parole. Ma la proposta è sul prodotto, non sul token: chi compra VVV non compra l'accesso a quei 401 modelli, compra una quota dei riacquisti. Finché i ricavi on-chain restano un milione al mese, il catalogo può crescere senza che il prezzo se ne accorga.

---
*Fonti verificate: docs.venice.ai/models/overview e docs.venice.ai/overview/pricing, consultate il 25/10/2026 (401 modelli in catalogo, 140 di testo; Abliterated Large Flash, id `abliteration-abliterated-model-large-flash`, 1,25 $/2,50 $ per milione, cache 0,125 $, contesto 1.000K, livello anonimizzato, capability Uncensored); venice.ai/models/abliteration-abliterated-model-large-flash, consultata il 25/10/2026 (base DeepSeek V4.1-Flash-1017, 128K di output massimo, FP8, trattamento transitorio dei prompt, nota del produttore secondo cui alcune richieste ricevono ancora un rifiuto); DefiLlama, defillama.com/protocol/venice, rilevazione del 25/10/2026 (TVL 0 $, staking 855,81 mln $, 71,45% della mcap, fee 30d 1 mln $, annualizzate 4,37 mln $, cumulate 3,86 mln $, prezzo 24,64 $, mcap 1,198 mld $, volume 21,18 mln $, massimo storico 34,53 $ del 21/09/2026, +9,6% a 7 giorni, −18,9% a 30 giorni, rapporto prezzo/fee 98,4x); sovyron.com/providers/venice, aggiornata al 24/10/2026 (data di listaggio di Abliterated Large Flash e DeepSeek V4.1 Flash Uncensored). Discrepanze annotate: il report di Echo indicava un TVL Venice di 1.711.627.447 $ e VVV a 24,49 $ con −0,5% in 24 ore; DefiLlama riporta TVL 0 $ per metodologia — lo staking è una serie separata — e un prezzo di 24,64 $, quindi la bozza descrive il livello di prezzo e non la variazione percentuale. La scansione del report poneva Abliterated Large Flash al 23/10, la documentazione Venice al 22/10: la bozza usa la data della documentazione. La notizia Kimi K3.1 Pro non è stata ripresa perché già oggetto della bozza del 24/10.*
