---
title: "DeepSeek 1017 su Venice: lo stesso modello, un altro conto"
date: 2026-10-19
draft: false
categories: ["Venice.ai", "AI"]
tags: ["deepseek", "privacy", "vvv", "modelli"]
summary: "La build 1017 di DeepSeek V4.1 Flash debutta su Venice a 0,30 dollari per milione di token, mentre VVV scende e gli abbonamenti salgono."
---
Il 17 ottobre DeepSeek ha pubblicato la build 1017 di V4.1 Flash. Il 18 Venice l'ha resa disponibile nell'app e via API con l'identificativo `deepseek-v4-1-flash-1017`. La parte interessante è cosa cambia per chi lo usa, e a che prezzo.

## Cosa c'è dentro la build 1017

La scheda tecnica di Venice descrive un Mixture-of-Experts da 552 miliardi di parametri con architettura Causal Encoder-Decoder, 8 miliardi attivi in prefill e 16 in decode, contesto da un milione di token, visione nativa e pesi aperti su Hugging Face. La versione originale era uscita il 10 settembre: la 1017 è un aggiornamento, non un nuovo modello. Il dato che conta per chi paga è il listino: 0,30 dollari per milione di token in ingresso e 1,20 in uscita, con input in cache a 0,01, contro i 3,75 e 18,75 di Kimi K3 sulla stessa piattaforma. Venice stessa ammette il limite: sui lavori lunghi e autonomi in terminale il modello resta dietro i migliori chiusi.

## La privacy ha livelli, e conviene leggerli

Il punto delicato è la parola «privato». Venice colloca il modello nel tier a ritenzione zero: prompt, immagini e output non vengono conservati, profilati o usati per l'addestramento. Ma la FAQ della stessa pagina è esplicita: il modello non gira dentro un TEE e il traffico non è cifrato end-to-end; la garanzia è la politica di non registrazione, non l'isolamento hardware. È una distinzione tecnica che diventa politica nel momento in cui si sceglie dove far passare dati sensibili. «Non lo conserviamo» e «non possiamo leggerlo» sono due promesse diverse, anche quando il marketing le impila nella stessa riga di badge.

## Il prezzo scende, l'uso sale

Nel frattempo il token del protocollo racconta una storia opposta. Il report settimanale W42 di VeniceStats, pubblicato oggi, registra VVV a 22,77 dollari, meno 8,0% su sette giorni, con le iscrizioni Pro in crescita del 18,4% a 21.935 — ottava settimana consecutiva di aumento, più 3.406 abbonati — e acquisti di crediti a un nuovo massimo giornaliero di circa 276.814 dollari. Lo stesso report segnala una quota Pro+ scesa al minimo di otto settimane, al 6,0%. Nelle ultime 24 ore il prezzo ha rimbalzato: circa 24,1 dollari, più 7,8%, capitalizzazione 1,17 miliardi, 842 milioni di VVV in staking, il 71,8% della capitalizzazione.

## La metrica che non c'è

DefiLlama indica per Venice un TVL di zero dollari: lo staking è tracciato come serie separata, fuori dal TVL. Il valore di 1,68 miliardi circolato nelle prime versioni di questa storia non trova riscontro nella fonte citata. In un settore dove le metriche sono anche argomenti di vendita, la differenza tra «locked» e «TVL» è la differenza tra una tesi e un numero.

Resta il quadro: un modello più economico e più capace, un token che perde prezzo mentre l'utilizzo cresce, e una piattaforma che dichiara con onestà i propri limiti. È un mercato che comincia a distinguere tra chi possiede il modello e chi possiede la relazione con chi lo usa.

---
*Fonti verificate: pagina modello venice.ai/models/deepseek-v4-1-flash-1017 e FAQ (19/10/2026); tabella prezzi docs.venice.ai/overview/pricing (19/10/2026); report settimanale VeniceStats W42 del 19/10/2026 (venicestats.com/insights e post @venicestats); CoinGecko, pagina Venice Token (19/10/2026); DefiLlama, pagina protocollo Venice (19/10/2026). Discrepanza rilevata: il TVL di 1,68 mld $ indicato nel report di Echo non corrisponde a DefiLlama, che riporta TVL 0 $ e lo staking come serie separata; nel testo è usato il dato verificato.*
