---
title: "Polygon riscrive un saldo: il fork da 6,8 milioni e la costituzione delle eccezioni"
date: 2026-11-05
draft: false
categories: ["Crypto", "Blockchain"]
tags: ["Polygon", "POL", "hard fork", "Binance", "Polymarket", "governance"]
summary: "Un PIP chiede di azzerare cinque indirizzi a un blocco fissato e accreditare i fondi rubati ai proprietari, con sei condizioni scritte prima."
---

Oggi alle 14:30 UTC la governance di Polygon discute una proposta che, se approvata, cambierà il software della rete per fare una cosa che le blockchain dichiarano impossibile: riscrivere un saldo. A un blocco predeterminato, cinque indirizzi controllati da un attaccante verrebbero azzerati e la stessa quantità di POL accreditata su wallet di recupero verificati da Polymarket e Binance. La supply totale non cambia: cambia chi la possiede.

## Cosa c'è dentro il fork

Il conto è preciso: 70,49 milioni di POL, di cui 23,86 milioni su quattro indirizzi legati all'incidente Polymarket del 29 ottobre e 46,63 milioni su un solo indirizzo legato a Binance. Il PIP ricostruisce il passaggio: nella notte tra il 29 e il 30 ottobre un hot wallet di Binance aveva inviato a quell'indirizzo 46.626.589,6 POL e 6.185.900,1 USDT, e Tether ha poi congelato gli USDT lasciando il POL nativo come unica parte ancora a rischio. La valorizzazione oscilla con il prezzo usato: circa 6,5 milioni ai 0,0924 dollari del 29 ottobre indicati nella proposta, 6,8 milioni ai prezzi correnti.

## La blacklist non basta, ed è già un potere

I produttori di blocco hanno inserito gli indirizzi nella lista di esclusione delle transazioni su richiesta delle parti offese, e nessuna via di aggiramento è stata trovata. Ma la proposta è onesta sui limiti: ogni produttore legge la lista solo all'avvio, quindi ogni modifica richiede un rilascio e un riavvio; le voci non scadono mai; il filtro copre solo i mittenti esterni e le autorizzazioni EIP-7702, quindi non è un congelamento completo. L'attaccante ha continuato a provarci, con una transazione che offriva circa 219.450 POL di commissione, e ha contattato i validatori offrendo denaro per sbloccare un trasferimento. Polymarket ha aperto un canale di recupero on-chain tramite il safe SEAL Safe Harbor, senza risposta.

Vale la pena fermarsi qui: la blacklist era già un atto di controllo centrale, solo silenzioso. Il fork rende quel potere visibile.

## Sei condizioni scritte prima

La parte più interessante del documento non è il meccanismo, è la tabella che lo precede. I proponenti elencano sei condizioni verificabili: incidenti riconosciuti pubblicamente dalle vittime, blocco applicato da ogni produttore, somma significativa, tracciamento on-chain chiaro verso parti rispettabili, richiesta esplicita delle vittime, assenza di pretese concorrenti dopo la divulgazione. E aggiungono che si tratta di un'azione estrema, da non riprodurre comunemente, non di uno strumento generale di congelamento e recupero. Il testo chiarisce anche di non essere consulenza legale e che nessuno promette l'esito del voto.

È il modo giusto di porre la questione, e resta il problema di fondo: l'immutabilità non è una proprietà fisica, è una soglia di governance. Scritta così, la soglia è alta e costosa. Ma la cifra in gioco è piccola, e una cifra piccola è esattamente ciò che rende un precedente a buon mercato.

---
*Fonti verificate: Polygon Community Forum, testo integrale del PIP «Recovery of Funds Held in Blocked Addresses following the Polymarket and Binance Incidents», autore Parvez03 del Validator Support Team di Polygon Labs, pubblicato il 2026-11-04 (letto il 2026-11-05); agenda PPGC-47 del 5 novembre 2026; Cointelegraph, articolo del 2026-11-05 su importi, ripartizione e tempi; crypto.news e Cryptopolitan, articoli del 2026-11-05 con la stessa ripartizione e il prezzo di riferimento del 29 ottobre; FXStreet, 2026-11-05, per le condizioni e i tempi di implementazione. Prezzo di Bitcoin usato solo come contesto: 80.445 $ secondo l'API CoinGecko e 80.533 $ secondo il ticker Cointelegraph, rilevati il 2026-11-05.*
