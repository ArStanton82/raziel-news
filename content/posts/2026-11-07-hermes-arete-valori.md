---
title: "Il valore di un modello è a un fine-tune di distanza"
date: 2026-11-07
draft: false
categories: ["AI", "Hermes"]
tags: ["Nous Research", "Arete-27B", "open weights", "allineamento"]
summary: "Nous ridisegna i valori di Qwen3.8-27B: le risposte di Stato scendono dal 22% allo 0,9%. Ma chi scrive la rubrica che misura il risultato?"
---

Nous Research ha pubblicato Arete-27B, un Qwen3.8-27B riaddestrato per ridurre le risposte che adottano la linea ufficiale di Pechino su temi sensibili. Non è un modello nuovo: è una dimostrazione. Se il risultato regge, dice qualcosa di scomodo tanto sui modelli cinesi quanto sui nostri: il livello dei valori in un modello aperto è sottile, e si può rifare in poche ore di calcolo.

## Cinquanta milioni di token, nessuna scorciatoia

Il metodo è volutamente modesto: supervised fine-tuning, circa 52,8 milioni di token, 50.000 campioni a 64.000 di contesto, due epoche, 1.202 step. Nessun reinforcement learning, nessuna preference optimization, nessuna modifica architetturale. Il teacher è Inkling, modello aperto, scelto anche per evitare i vincoli contrattuali sul «distillato illecito». Pesi, prompt di valutazione e dati di training sono pubblici.

## Il numero, e che cosa misura

La valutazione interna usa 803 prompt su sette categorie: libertà di espressione, ideologia di Stato, Stato contro mercato, educazione, privacy e sorveglianza, democrazia, ambiente. Il fact score medio passa da 2,32 a 2,98 su 5; la quota di risposte che fanno propria la linea ufficiale scende dal 22% allo 0,9% con thinking spento (0,6% con thinking attivo; il testo del post arrotonda all'1%). Le risposte da zero punti calano da 359 a 216 su 803. Il salto più netto è sulla libertà di espressione: da 0,89 a 2,44, con la propaganda dal 60% all'1%. Sulle capacità non rivendica guadagni: Hermes Bench segna 65,60% contro 65,77% del modello di partenza, differenza che il laboratorio liquida come rumore.

## Chi giudica, e con quale metro

La riserva sta nel perimetro. La rubrica è di Nous, i prompt sono di Nous, il giudice è un modello (Grok 4.7) istruito da Nous, e non risulta una replica indipendente. La metrica misura la conformità a una policy di valori dichiarata, non l'assenza di un punto di vista: è il laboratorio stesso a scriverlo. Se la stratificazione è così superficiale, la conclusione è simmetrica: nessun modello è neutrale, e un modello aperto è un'opzione fra molte, non un oracolo. La possibilità di riallinearlo rende impossibile fidarsi ciecamente di chi lo ha fatto.

## La potenza e il prezzo dell'accesso

Nello stesso giorno Nous lavora anche sull'agente. Il cofondatore Teknium ha scritto su X che il browser in-app potrà ereditare cookie e password, su consenso dell'utente, «nella prossima patch»: una promessa senza data, non una funzione disponibile. Significa che l'assistente navigherà con le sessioni di chi lo usa. Le due notizie stanno bene insieme: più il modello è allineato ai valori di chi lo addestra, più è capace di agire al posto suo. La domanda non è se i valori si possano cambiare, ma chi tiene la chiave, e con quale rubrica.

Arete-27B è un buon esperimento e un cattivo talismano: dice che l'allineamento non è una proprietà stabile dei modelli, ma una scelta editoriale ripetibile. Chi la compie dovrebbe pubblicare il metro, come ha fatto Nous; chi la legge dovrebbe ricordare che il metro è parte dell'opera.

---
*Fonti verificate: Nous Research, «Introducing Arete-27B», 6 novembre 2026 (nousresearch.com/arete); scheda modello NousResearch/Arete-27B su Hugging Face; AlphaSignal, 6 novembre 2026; post @NousResearch del 6 novembre 2026; post @Teknium del 7 novembre 2026 (ripreso da Digg AI il 7 novembre 2026). Nota di verifica: il report indica 0,9% e 1% come lo stesso valore; sono il dato con thinking spento e l'arrotondamento usato nel testo del post.*
