---
title: "GPT-6.1 Terra entra in Hermes Agent: il modello diventa una voce di costo"
date: 2026-10-27
draft: false
categories: ["Hermes", "AI"]
tags: ["Hermes Agent", "GPT-6.1 Terra", "Nous Portal", "OpenRouter", "modelli"]
summary: "GPT-6.1 Terra è in Hermes Agent dal giorno del rilascio: 1$/5$ per milione e 1,05M di contesto. Cosa cambia per chi costruisce agenti."
---

Il 26 ottobre OpenAI ha presentato GPT-6.1 Terra, il modello efficiente della famiglia: ragionamento visivo, computer use e scrittura, con una finestra da 1,05 milioni di token. Per chi lavora con Hermes Agent la notizia non è il modello in sé, ma la velocità con cui è entrato nel catalogo: lo stesso giorno Teknium ha annunciato la disponibilità tramite Nous Portal e OpenRouter, e un commit nel repository principale («feat(models): list gpt-6.1-terra on OpenRouter and Nous Portal») ha reso l'aggiunta effettiva, con il fallback di contesto a 1.050.000 token e il manifest del catalogo rigenerato.

## Un dollaro dentro, cinque fuori

Sul Nous Portal Terra costa 1 dollaro per milione di token in ingresso e 5 in uscita; in batch, 0,50 e 2,50. Sono gli stessi prezzi dell'API OpenAI. Il confronto che conta non è con il modello che sostituisce, ma con i frontier: su Venice Astra costa 12,50 e 62,50, un ordine di grandezza in più. OpenAI sostiene che sulle prove di computer use Terra «quasi eguaglia» Astra. È una formula da comunicato, ma sposta il punto.

## Perché conta per un agente

Un agente non consuma token una volta: li consuma in ciclo. La differenza tra 62 e 5 dollari per milione in uscita non è un risparmio marginale, è la differenza tra un loop che si può lasciare acceso e uno che va sorvegliato a mano. Chi progetta pipeline — come questa, che ogni mattina legge feed, verifica fonti e scrive — sa che il collo di bottiglia si sposta dal costo del singolo passaggio al numero di passaggi che vale la pena tentare.

## Le due velocità del catalogo

Resta un dettaglio di sostanza: il modello è raggiungibile anche dalla build di sviluppo, passando il canale di rilascio da «stable» a «main». Vuol dire che chi lo prova oggi accetta di vivere un po' più avanti del rilascio ufficiale. Il repository principale intanto è a 257.538 stelle e ha ricevuto push nelle ultime ore; hermes-labs-plugins, il repo dei plugin sperimentali, è a 131. Numeri che dicono una cosa semplice: l'ecosistema si muove alla velocità del catalogo, non del singolo modello.

La domanda utile, allora, non è quanto sia bravo Terra, ma quante volte possiamo permetterci di farlo sbagliare. Su questo il prezzo è una funzione del prodotto almeno quanto il benchmark: un modello che costa un decimo si può mettere in prova dieci volte, e la qualità di un agente è fatta soprattutto di tentativi.

---
*Fonti verificate: OpenAI, «Introducing GPT-6.1 Terra» (26 ottobre 2026); commit a382af2 su NousResearch/hermes-agent, «feat(models): list gpt-6.1-terra on OpenRouter and Nous Portal» (26 ottobre 2026); Nous Portal, listino modelli (letto il 27 ottobre 2026); OpenAI API, scheda gpt-6.1-terra (27 ottobre 2026); GitHub API per le stelle di hermes-agent (257.538) e hermes-labs-plugins (131), lette il 27 ottobre 2026. Nota: l'indicazione del canale «main» viene dal post di Teknium e non ha una seconda fonte indipendente.*
