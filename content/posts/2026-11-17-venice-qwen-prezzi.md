---
title: "Venice taglia il prezzo il giorno dopo il lancio: la corsa al ribasso dell'intelligenza"
date: 2026-11-17
draft: false
categories: ["Venice.ai", "AI"]
tags: ["Venice", "VVV", "Qwen", "GLM", "inference pricing", "staking"]
summary: "Qwen 4 Max arriva a 1M di contesto e viene scontato dopo 24 ore. Intanto i ricavi on-chain di Venice restano nell'ordine dei milioni"
---

Venice ha aggiunto due famiglie di modelli al proprio catalogo in quarantotto ore e, per uno dei due, ha già corretto il listino. È il tipo di dettaglio che nei comunicati sparisce e che invece dice molto su dove si sta spostando il mercato dell'inferenza privata: la pressione sui prezzi non arriva più dai concorrenti, arriva dalla cadenza con cui i modelli escono.

## Due aggiunte e un ribasso

Il 16 novembre il changelog tecnico registra due ingressi. Il primo è GLM 5.3 Flash Uncensored: contesto da 1.048.576 token, pesi FP8 pubblicati su Hugging Face, esecuzione classificata come privata, a 0,165 dollari per milione di token in ingresso e 0,55 in uscita — la lettura da cache costa 0,033. Il secondo è Qwen 4 Max, contesto da un milione di token, ingresso di testo, immagini e video, fino a 393.216 token di output, privacy dichiarata come anonimizzata.

Il giorno dopo, il 17 novembre, il changelog riporta una voce sola: i prezzi di Qwen 4 Max scendono. Ingresso da 1,875 a 1,50 dollari per milione, uscita da 5,625 a 4,50, lettura da cache a 0,075. Un taglio del venti per cento a ventiquattro ore dal debutto. Sul listino comparativo della documentazione il prezzo misto del modello si attesta a 2,25 dollari per milione, appena sopra i 2,00 di GPT-6.1 Terra e sotto i 2,50 di Muse Spark Open.

## Il confronto che Venice fa con sé stessa

Nel post di annuncio l'azienda sostiene che Qwen 4 Max ha costruito la stessa scena 3D «in meno della metà del tempo e del costo» rispetto a Qwen 3.8 Max. È una misura interna, non un test indipendente, e va letta come tale. Ha però un pregio: sposta l'attenzione dal punteggio di benchmark al costo per lavoro finito.

## Il token, che vive di un'altra cosa

Sul mercato VVV vale poco più di 21 dollari (21,22 su CoinGecko, 21,20 su DefiLlama nelle rilevazioni della mattina), con capitalizzazione intorno a 1,04 miliardi e volume a 51,8 milioni nelle 24 ore; circolano 49 milioni di token su 81,26 milioni emessi. Ma il dato strutturale è un altro: DefiLlama registra 729,23 milioni di dollari in staking, il 70,21 per cento della capitalizzazione. Il TVL del protocollo, per metodologia dichiarata dall'aggregatore, resta zero: lo staking è una serie separata e non va sommato.

Dall'altro lato del bilancio, le commissioni cumulate sono 4,83 milioni di dollari, di cui 855.584 a novembre (il mese include il riacquisto da circa 458 mila dollari del 9 novembre) e 1,06 milioni a ottobre. Sono i VVV ricomprati e bruciati: l'ombra on-chain del fatturato, non il fatturato. Abbonamenti, API e crediti DIEM regolano fuori catena e DefiLlama li esclude per scelta.

Il punto, allora, è questo: la valutazione di Venice non poggia sui ricavi visibili, poggia su quasi tre quarti dell'offerta bloccata in staking. È una scommessa sull'accesso perpetuo al calcolo, non sulla fatturazione. Finché i prezzi per token scendono, quella scommessa diventa più economica da fare e più difficile da misurare.

---
*Fonti verificate: docs.venice.ai/changelog (voci del 16 e 17 novembre 2026, con i prezzi prima e dopo il taglio); docs.venice.ai/models/qwen-4-max e docs.venice.ai/models/glm-5-3-flash-uncensored (schede tecniche, consultate il 17/11/2026); defillama.com/protocol/venice (TVL 0 $, staking 729,23 mln $ = 70,21% della mcap, fee cumulate 4,83 mln $, serie mensile); coingecko.com/en/coins/venice-token (prezzo, capitalizzazione, volume, offerta circolante). Scartato il «TVL Venice» di 1,409 mld $ riportato dal radar: la pagina DefiLlama mostra 0 $ e tiene lo staking come serie a parte. Le percentuali a 24 ore non sono state pubblicate perché le fonti davano valori non coincidenti.*
