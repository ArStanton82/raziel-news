---
title: "Hermes 0.22.5: il computer che si condivide"
date: 2026-10-23
draft: false
categories: ["Hermes", "AI"]
tags: ["hermes-agent", "nous-research", "plugin", "agentic-ai"]
summary: "Patch 0.22.5 con 81 PR e note rinviate a v0.23.0; intanto il plugin Spaces di Trycua allarga l'ecosistema Hermes."
---

Il 23 ottobre alle 05:28 UTC teknium1 ha taggato la v0.22.5 di Hermes Agent. La data dichiarata nel corpo della release è il 22 ottobre, il commit è bf0203a: la distanza tra le due date racconta il senso dell'uscita, un roll-up tecnico e non una presentazione. Le note curate arriveranno con la v0.23.0, che coprirà tutto il periodo dalla v0.22.0 in avanti. È una scelta dichiarata, non una dimenticanza.

## Cosa c'è dentro la finestra

I numeri sono quelli che un manutentore guarda prima di firmare: 231 commit non-merge su 804 file, +35.212 e −17.885 righe, 81 pull request e 30 issue chiuse. Dentro ci sono cambiamenti che toccano il modo in cui l'agente si installa e si governa: il sign-in Nous diventa un device login unico e l'utente free-tier passa dall'ospite al proprio account; arrivano i piani a finestra di utilizzo; i backend di delega diventano sostituibili, così i subagent si instradano per model map o per profilo. Poi i dettagli che dicono quanto il prodotto si stia separando dal nucleo: `hermes mcp serve` e il backend Singularity escono dal core e diventano plugin, mentre Electron 44 chiude il conto delle dipendenze.

## Il computer che si condivide

Il pezzo più interessante della settimana non è nella release. È il plugin Spaces di Trycua, annunciato il 22 ottobre: dà a Hermes un ambiente Linux, macOS o Windows sull'hardware che il team già possiede. Chiunque può aprirlo, guardare in tempo reale, intervenire e poi restituire il controllo mentre l'agente continua a lavorare. Vale una precisazione che il post ufficiale non contiene e che Teknium ha aggiunto nei commenti: il plugin è mantenuto da Trycua, non da Nous. È la stessa logica della release — il core si alleggerisce, l'ecosistema si assume il peso.

## Un plugin, anche commerciale

Sul fronte opposto c'è Meshy, che nell'annuncio offre un mese di piano Pro a un dollaro: accesso API e mille crediti, contro i venti dollari indicati come listino. L'installazione passa da `hermes plugins install meshy` e da una chiave incollata nelle impostazioni. Non è una notizia tecnica, ma dice dove va il progetto: i plugin sono anche un canale distributivo, e l'agente diventa il punto di accesso a servizi terzi.

## La sovranità, detta ad alta voce

Chiude il quadro la conversazione tra Dillon Rolnick e Matthew Prince, ospitata da USV: agenti, futuro di internet, sovranità digitale. Non risultano trascrizioni né sintesi pubblicate dalle due aziende, quindi il contenuto resta il video allegato al post. È però il tema che tiene insieme il resto — un computer condiviso con il team, un plugin che porta dentro servizi commerciali, un core che si svuota. La domanda non è più cosa sappia fare Hermes, ma dove finisca la sua giurisdizione.

La v0.22.5 è una release minore che dice una cosa grande: il progetto sta spostando complessità fuori dal nucleo e responsabilità dentro l'ecosistema. Le note di v0.23.0 saranno il primo bilancio, e converrà leggerle guardando a cosa è uscito, non solo a cosa è entrato.

---
*Fonti verificate: GitHub, release v0.22.5 di NousResearch/hermes-agent (23 ottobre 2026); post @NousResearch su X del 22 ottobre 2026 (plugin Spaces, offerta Meshy, conversazione Rolnick-Prince); post @Teknium su X del 22 ottobre 2026 (manutenzione del plugin affidata a Trycua). Nota: la qualifica di "plugin ufficiale" per il plugin X Chat, riportata da @HermesWatcher, non ha trovato conferma sulla pagina Announcements di nousresearch.com e non è stata inclusa; il progetto OSINT di @adolandev è escluso perché amatoriale.*
