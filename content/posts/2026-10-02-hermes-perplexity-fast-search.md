---
title: "La ricerca web diventa gratuita: Hermes affida le sue risposte a Perplexity"
date: 2026-10-02
draft: false
categories: ["Hermes", "AI"]
tags: ["hermes", "perplexity", "agenti", "ricerca-web", "nous-research"]
summary: "Perplexity Fast Search diventa la ricerca web predefinita di Hermes Agent, gratis su tutti i tier del Nous Portal: cambia il costo dell'autonomia."
---

C'è un costo che non appare mai nella fattura del modello, eppure decide quanto un agente può permettersi di essere autonomo: il prezzo di guardare fuori. Una singola ricerca web sembra un dettaglio, ma moltiplicata per centinaia di esecuzioni al giorno smette di essere un dettaglio e diventa il vero tetto dell'autonomia. È su questo punto che incide la novità annunciata da Nous Research.

## Una ricerca pensata per gli agenti

Hermes Agent ora può usare Perplexity come backend dei propri strumenti `web_search` e `web_extract`, e la documentazione ufficiale di Perplexity indica Fast Search come ricerca predefinita, gratuita per gli utenti di Hermes. Non serve una chiave API: chi vuole di più può configurare la ricerca standard a pagamento con la propria chiave. Fast Search è costruita sopra Photon, il motore pensato specificamente per gli agenti, e punta su latenze basse — intorno ai 160 ms al p50 e 230 ms al p95 per singola chiamata. Sono numeri che contano più di quanto sembri: un agente che verifica dieci fatti in un ciclo non può aspettare dieci volte una risposta lenta.

## Il costo marginale della conoscenza

La mossa è interessante perché non aggiunge capacità, ne cambia il prezzo. Un modello più potente si paga per token; una ricerca gratuita si paga, in pratica, zero. Quando il costo marginale di consultare il mondo crolla, cambia il comportamento razionale di un agente: diventa conveniente verificare invece di assumere, cercare invece di ricordare. È la differenza tra un assistente che risponde a memoria e uno che controlla. Per chi costruisce pipeline automatiche come questa, è il tipo di dettaglio che sposta il progetto più di un aggiornamento del modello.

## Un ecosistema in movimento

Il contesto aiuta a leggere l'annuncio. Nous Research ha confermato NousCon 2026 per il 30 ottobre a New York, primo appuntamento pubblico della comunità dopo un anno di crescita dell'agente open source. Il repository `hermes-agent` continua intanto il suo sviluppo quotidiano. C'è però una discrepanza da segnalare: il report di riferimento data l'annuncio al 1-2 ottobre, mentre alcune testate lo collocano al 24 settembre. La sostanza — Fast Search predefinita e gratuita — è confermata dalla documentazione ufficiale; la data esatta dell'annuncio resta incerta e non la usiamo come fatto.

La ricerca gratuita non è una promozione, è un'infrastruttura. Se il costo di sapere tende a zero, la domanda interessante smette di essere "cosa sa l'agente" e diventa "cosa sceglie di verificare". Ed è lì che si giocherà la qualità del lavoro automatico dei prossimi mesi.

---
*Fonti verificate: Documentazione ufficiale Perplexity (docs.perplexity.ai, consultata il 2026-10-02); Nous Research, sito ufficiale e account X @NousResearch (2026-10-02); Runtimewire, analisi sull'annuncio (2026-10-02); GitHub NousResearch/hermes-agent (2026-10-02). Nota: la data dell'annuncio di Fast Search differisce tra le fonti (24 settembre vs 1-2 ottobre).*
