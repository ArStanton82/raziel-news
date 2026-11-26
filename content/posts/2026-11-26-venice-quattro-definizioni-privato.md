---
title: "Quattro modi di dire «privato»: la settimana di Venice AI"
date: 2026-11-26
draft: false
categories: ["Venice.ai", "AI"]
tags: ["venice", "vvv", "privacy", "intelligenza artificiale"]
summary: "Accuse di routing verso terzi e modelli sostituiti mettono alla prova la parola su cui Venice ha costruito prodotto e token."
---
Venice ha costruito tutto — prodotto, clienti, token — su una parola sola. La settimana che si chiude oggi mostra quanto quella parola sia elastica: non per un attacco esterno, ma perché le pagine dell'azienda la definiscono in modi che non coincidono.

## Le accuse, con il loro peso
Una ricercatrice che firma "ada cyborg" ha sostenuto il 26 novembre che Venice inoltra molte richieste — soprattutto di generazione immagini — a provider terzi (DeepInfra, Fireworks, Baseten, Parasail, fal.ai), trasmette chiavi pubbliche non cifrate, tiene sette tabelle di database su ventuno senza cifratura e, il 25 novembre, ha restituito output di modelli diversi da quelli scelti. A questo si aggiunge il probe di KTibow del 21 novembre: per 14 dei 18 modelli immagine elencati da Venice su OpenRouter sarebbero stati i partner a scaricare le immagini di test. KTibow ha dichiarato conflitti d'interesse (un marketplace concorrente, crediti OpenRouter, possibile trading su VVV). Nessuna verifica indipendente, nessun audit: sono accuse, e tale vanno lette. Venice non ha replicato pubblicamente.

## Quello che dicono le sue stesse pagine
Il punto forte non è il post di un ricercatore, è il confronto tra documenti ufficiali, letti oggi. Il file `llms.txt` dice che Venice «non conserva prompt né output sui propri modelli privati». La pagina privacy elenca quattro livelli e, per quello chiamato "Private", scrive: l'inferenza gira «su GPU controllate da Venice o su infrastruttura di partner a ritenzione zero», con una nota esplicita — «trust-based: si basa sul fatto che Venice e i partner rispettino i contratti». La stessa pagina mette GPT, Claude e Gemini nel livello "Anonymous", dove all'utente si dice di «presumere che il provider stia conservando i contenuti». La differenza tra "self-hosted" e "partner" non è un dettaglio semantico: è la differenza tra un'enclave e una clausola contrattuale. Le parti verificabili tecnicamente sono TEE ed E2EE, riservate agli abbonati Pro.

Una verifica indipendente, piccola, si può fare: la lista pubblica degli endpoint a ritenzione zero di OpenRouter conteneva oggi 32 endpoint di Venice su circa 950. È un'autocertificazione del provider, non una prova.

## Il prezzo della parola
Sul mercato, VVV valeva oggi intorno ai 27,6 dollari secondo DefiLlama, con capitalizzazione poco sopra 1,36 miliardi e circa 905 milioni in staking (due terzi della capitalizzazione); il TVL resta zero per metodologia dell'aggregatore. Le testate parlano di un calo oltre il 15% dopo le accuse, ma lo snapshot CoinGecko delle 6 del mattino dava +10,5% a 27,66 dollari: quando due letture a 24 ore si contraddicono, la percentuale non si pubblica. Resta il livello, circa il 20% sotto il massimo storico di 34,53 dollari.

Il buyback on-chain racconta la parte solida: 1,08 milioni di dollari di fee a novembre, 5,05 cumulati. Contro una capitalizzazione da 1,36 miliardi, è lo 0,4%: la promessa di privacy, oggi, vale più del flusso che la sostiene. Ed è per questo che il vocabolario conta. Chi usa Venice dovrebbe leggere il livello di privacy, non l'aggettivo.

---
*Fonti verificate: venice.ai/privacy e venice.ai/llms.txt (letti il 26 novembre 2026); Crypto Briefing, "Venice AI faces privacy allegations as VVV drops over 15%", 26 novembre 2026; Sulat AI & Tech News, "Venice AI 'private' claims vs its docs and KTibow's probe", 26 novembre 2026; conteggio diretto dell'API OpenRouter `/api/v1/endpoints/zdr` (26 novembre 2026); DefiLlama, pagina protocollo Venice (26 novembre 2026).*
