---
title: "Hermes SEO: quarantacinque competenze in cerca di un catalogo"
date: 2026-10-19
draft: false
categories: ["Hermes", "AI"]
tags: ["plugin", "seo", "community", "mcp"]
summary: "Un plugin community porta in Hermes 45 skill SEO e 19 ruoli specialistici: potente, ma la pull request per il catalogo è ancora aperta."
---
C'è un modo di leggere l'ecosistema degli agenti che non passa dai benchmark, ma da come il lavoro viene diviso. La notizia di ieri sera è piccola e significativa insieme: «Hermes SEO», port nativo del toolkit Claude SEO, è arrivato come plugin community con 45 skill e 19 ruoli specialistici. Non è un prompt più lungo. È un'organizzazione del lavoro importata dentro l'agente.

## Un reparto, non un comando

Il repository parla chiaro: 25 skill di workflow, un router `seo`, 19 skill di ruolo, 56 script di utilità e i template Schema.org. Il port è dichiarato dalla versione 2.4.2 di Claude SEO, progetto di Daniel Agrici, e richiede Hermes Agent 0.22.2 o superiore. La release v0.1.0 è del 16 ottobre. La differenza rispetto a un singolo skill sta nella catena: audit del sito, tecnico, pagina, brief, dati strutturati, visibilità sui motori generativi, locale, strategia. Chiunque abbia provato a far fare un audit serio a un agente sa che il collo di bottiglia non è la scrittura, è la sequenza.

## «Nel catalogo» è un'altra cosa

L'annuncio circolato su X parlava del plugin «nel catalogo Hermes». Il README del progetto, aggiornato il 17 ottobre, dice qualcosa di più sobrio: è un progetto indipendente, separato dai plugin ufficiali Nous Research, e la pull request per il catalogo community (#139998) è ancora aperta. Il repository ha 48 stelle; le 15.000 appartengono al progetto upstream, non al port. Non è una polemica, è una distinzione che conta per chi installa: al momento l'installazione avviene da GitHub con un riferimento bloccato al commit della release, non con un comando preso dal catalogo. Resta anche un limite dichiarato dagli autori: i flussi con Google OAuth sono disabilitati perché Hermes non offre ancora un percorso di autorizzazione legato al profilo.

## Intanto il core rattoppa l'MCP

Nella stessa giornata, due commit nel repository principale mostrano dove si sta lavorando davvero: la configurazione MCP. Il primo, `5fc490e`, fa sì che una variabile `${VAR}` non impostata non ricada più sul valore ereditato dal processo padre. Il secondo, `43c9e0a`, esclude dall'ambiente di un server MCP stdio le voci rimaste come segnaposto letterale. Sembra igiene interna, ed è esattamente il tipo di dettaglio che decide se un plugin con credenziali opzionali parte o si spegne. L'ultima release pubblicata resta la v0.22.2 del 15 ottobre: questi sono lavori di manutenzione, non un annuncio.

La lezione è doppia. Da un lato, il valore di un agente comincia a misurarsi in competenze confezionate, ruoli e responsabilità: il plugin SEO è interessante perché prova a insegnare un mestiere, non a rispondere a una domanda. Dall'altro, un ecosistema che cresce in fretta ha bisogno di fondamenta noiose — variabili d'ambiente, permessi, cataloghi — che nessuno twitta e che tutti notano quando mancano.

---
*Fonti verificate: repository GitHub yuzushi-dev/hermes-seo, README e release v0.1.0 (consultato il 19/10/2026); commit NousResearch/hermes-agent 5fc490e e 43c9e0a (19/10/2026); pagina releases NousResearch/hermes-agent, v0.22.2 del 15/10/2026; post @HermesWatcher del 19/10/2026. Discrepanza rilevata: il post annuncia il plugin «nel catalogo», mentre il README indica la pull request #139998 ancora aperta — nel testo è riportata la versione del repository.*
