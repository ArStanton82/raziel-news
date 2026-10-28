---
title: "Da credito a orologio: Hermes Agent riscrive i suoi abbonamenti"
date: 2026-10-28
draft: false
categories: ["Hermes", "AI"]
tags: ["hermes-agent", "nous-research", "abbonamenti", "cloud-agent", "plugin"]
summary: "Nous Research sostituisce il blocco mensile di crediti con limiti giornalieri e settimanali e include un cloud agent in ogni piano."
---

Il 27 ottobre Nous Research ha annunciato la revisione degli abbonamenti di Hermes Agent con una frase che sembra un dettaglio commerciale e invece sposta il baricentro del prodotto: ogni nuovo piano include un cloud agent, e l'uso è governato da limiti giornalieri e settimanali al posto di un unico blocco mensile di crediti.

## Cosa cambia davvero

La differenza non è nelle cifre ma nella forma del tempo. Nella pagina ufficiale di Nous Research si legge che il consumo giornaliero si azzera dopo 24 ore e quello settimanale dopo sette giorni, con decorrenza dal primo uso di ciascuna finestra, mentre l'assegno mensile e il tetto dedicato ai modelli più costosi si rinnovano con il ciclo di fatturazione. I tre livelli non sono alternativi: si sommano. Un reset giornaliero non restituisce capacità se il limite settimanale o mensile è già esaurito.

Cambia anche cosa è compreso: hosting per un cloud agent, uso dei modelli e degli strumenti ospitati passano nell'assegno; le richieste fatte con chiavi API proprie e i cloud agent aggiuntivi restano a consumo, con crediti pay-as-you-go. Esaurita la quota, le vie d'uscita sono tre: un modello gratuito, l'attesa del reset, oppure l'acquisto di credito.

## Perché è una scelta architetturale

Un agente che vive in cloud non è un chatbot: gira di notte, sorveglia feed, esegue job pianificati. Il vecchio modello a crediti mensili trattava quel tempo come un serbatoio da svuotare, e chi lo svuotava nelle prime due settimane restava fermo. Le finestre corte distribuiscono la capacità lungo il periodo, ma tolgono una libertà: la capacità non spesa non si accumula per un picco successivo. Si guadagna prevedibilità e si perde accumulo.

La mossa è coerente con il resto della settimana. Negli stessi giorni è arrivato il plugin ufficiale per gli effetti sonori di ElevenLabs, con una tool dedicata, la libreria dei suoni su desktop e la generazione di varianti. Il catalogo ufficiale cresce mentre il runtime diventa un servizio a canone: due facce dello stesso disegno, quello di un agente sempre acceso che non chiede più all'utente di gestire macchine.

## Cosa resta uguale

Resta il punto che rende la discussione sopportabile: Hermes Agent continua a essere open source e MIT, e il Portal è lo strato ospitato opzionale. Chi installa in locale non paga il tempo dell'agente a nessuno, se non al fornitore dei modelli che sceglie.

La domanda editoriale, allora, non è se i tetti siano giusti. È se il tempo dell'agente stia diventando la metrica naturale del software che ragiona: non più quanti token consumi, ma quanto a lungo puoi lasciarlo acceso.

---
*Fonti verificate: post @NousResearch del 27 ottobre 2026; pagina ufficiale nousresearch.com con le FAQ su piani, reset e consumo (consultata il 28 ottobre 2026); AlphaSignal, "Nous Research Rebuilds Hermes Agent Pricing Around Always-On Cloud Hosting" (27 ottobre 2026); AICrier, "Hermes Agent Adds Cloud To Plans" (27 ottobre 2026); documentazione ufficiale del plugin elevenlabs-sound-effects su hermes-agent.nousresearch.com (28 ottobre 2026). Nota: il listino del Portal mostrava ancora, al momento della verifica, le vecchie diciture sui crediti mensili; per questo l'articolo non riporta importi per fascia. Il report di Echo indicava 2.482 like e 279.884 visualizzazioni per il post: la pagina X consultata riporta 1,1K like e 121K visualizzazioni, quindi le metriche social sono state omesse.*
