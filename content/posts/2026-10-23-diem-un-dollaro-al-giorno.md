---
title: "DIEM, un dollaro di calcolo al giorno"
date: 2026-10-23
draft: false
categories: ["Venice.ai", "Blockchain"]
tags: ["diem", "vvv", "venice-ai", "staking", "token"]
summary: "Un DIEM in stake vale un dollaro di credito al giorno. Il walkthrough ufficiale e i numeri veri di VVV: TVL a zero, 70% in staking."
---

Il 22 ottobre, tra le 19:02:26 e le 19:02:43 UTC, l'account @AskVenice ha pubblicato un thread in otto post che fa una cosa semplice e rara: spiega un token senza promettere rendimenti. La documentazione ufficiale, interrogata oggi, conferma ogni passaggio. DIEM è un ERC-20 su Base; messo in stake, ogni token vale un dollaro di credito Venice al giorno.

## Un dollaro al giorno, non un interesse

La meccanica è lineare. Un DIEM in stake genera un dollaro di credito per epoch, cento crediti per dollaro, e l'assegnazione si rinnova alle 00:00 UTC. Il DIEM non speso non si riporta al giorno dopo; servono almeno 0,1 DIEM in stake perché il saldo sia spendibile; l'ordine di consumo è DIEM, poi i crediti guadagnati, poi quelli inclusi nel piano, poi i dollari. Non è un rendimento sul capitale, è capacità di calcolo prepagata che si azzera ogni notte. Definirlo «inferenza tokenizzata», come ha fatto Jon ShapeShift, è più preciso che chiamarlo staking.

## Due strade, un vincolo

Si può comprare DIEM sul mercato, su Aerodrome o Uniswap, e metterlo in stake. Oppure si stake VVV, si ricevono sVVV e si minta DIEM al Mint Rate corrente: una curva che sale con l'offerta di DIEM. Il VVV resta bloccato finché non si brucia la stessa quantità di DIEM mintata. I tempi: un giorno di cooldown per lo unstake di DIEM, sette giorni per l'sVVV liberato dopo il burn. Chi entra per speculare sul prezzo del token trova qui il primo attrito.

## I numeri, senza gonfiarli

Il mercato, intanto, non premia. VVV vale circa 26 dollari — 25,96 su DefiLlama, 26,04 su CoinGecko — con capitalizzazione intorno a 1,26 miliardi e volume giornaliero di circa 43 milioni. Resta un quarto sotto il massimo storico di 34,53 dollari, toccato il 21 settembre.

E qui va corretta una cifra che circola: il TVL del protocollo è zero. DefiLlama lo scrive in chiaro e spiega perché — il grafico tiene lo staking come serie separata, fuori dal TVL. Quello che conta è l'altro numero: 888,49 milioni di dollari in VVV stakeati, il 70,4% della capitalizzazione. Quasi tre quarti del valore del token è già dentro il meccanismo. Le fee on-chain degli ultimi trenta giorni sono 991.539 dollari, cumulate 3,82 milioni: il protocollo compra e brucia VVV con una quota degli abbonamenti. Il resto del fatturato — abbonamenti, API, crediti DIEM — si regola fuori dalla catena e DefiLlama non lo conta.

## La domanda che resta

Se un DIEM è un dollaro di calcolo al giorno, il valore del token diventa una scommessa su quanto calcolo servirà davvero e sull'ipotesi che l'inferenza resti un bene scarso, vendibile a prezzo pieno. Il 70% in staking dice che molti ci credono. Il TVL a zero dice che, per ora, è una scommessa interna al token: nessun altro capitale è entrato a sostenerla.

---
*Fonti verificate: thread ufficiale @AskVenice su X del 22 ottobre 2026; documentazione Venice, docs.venice.ai/overview/vvv-diem, consultata il 23 ottobre 2026 (spend order, cooldown 1 e 7 giorni, Mint Rate); DefiLlama, defillama.com/protocol/venice, rilevazione del 23 ottobre 2026 (TVL 0 $, staking 888,49 mln $, fee 30d 991.539 $); CoinGecko, pagina Venice Token, 23 ottobre 2026; post @JonShapeShift del 22 ottobre 2026. Nota: il report di Echo indicava un TVL di 1.776.984.472 $ e un calo del 5,6% in 24 ore; DefiLlama riporta TVL 0 $ con lo staking come serie separata e, nella rilevazione odierna, il token è poco sopra i 26 dollari dopo una seduta debole. La bozza usa i dati verificati e omette la variazione percentuale giornaliera, troppo sensibile alla finestra di rilevazione.*
