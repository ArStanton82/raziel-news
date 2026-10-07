---
title: "Hermes Index: misurare gli agenti sul costo reale, non solo sul punteggio"
date: 2026-10-07
draft: false
categories: ["Hermes", "AI"]
tags: ["hermes-agent", "benchmark", "nous-research", "costo-per-task", "agenti"]
summary: "Nous Research pubblica Hermes Index: quattro benchmark dentro Hermes Agent, con il costo medio per task accanto al punteggio."
---

Quando si sceglie un modello per un agente, il punteggio da solo dice poco. Conta quanto quel punteggio costa, task dopo task. È la premessa di Hermes Index, l'indice pubblicato il 6 ottobre da Nous Research: quattro suite di valutazione eseguite dentro lo stesso harness di Hermes Agent, con il costo medio per task accanto alla media dei risultati.

## Quattro prove, un solo banco di lavoro

Hermes Index media quattro suite: Hermes Bench, un benchmark nuovo dello stesso team, TerminalBench 4, TerminalBench Science e SkillsBench. Ogni modello gira con le stesse regole — pass@1, una sola possibilità per task — e con il ragionamento impostato su "high" dove disponibile. Il risultato non è una classifica di intelligenza astratta, ma una misura di quanto bene un modello si comporta quando gli si affida lavoro vero dentro un agente. In testa c'è Claude Opus 5.5, con 63,31 punti a 4,99 dollari per task; seguono GPT 6 Astra (56,25 punti, ma 11,61 dollari per task) e Claude Sonnet 5.5 (53,14 a 2,82 dollari).

## Il punto interessante è la coda della classifica

Il dato più utile sta più in basso. DeepSeek V4.1 Flash segna 36,91 a 0,259 dollari per task; Ling 3.0 Flash arriva a 21,56 con circa 5 centesimi. Nous indica sei modelli sulla frontiera di Pareto — quelli che, a parità di costo, nessun altro batte — e la lista racconta una cosa semplice: per molte attività di un agente un modello economico e veloce è la scelta razionale, mentre il modello "migliore" resta per i compiti difficili. È esattamente il motivo per cui Hermes distingue un modello principale dai modelli ausiliari, usati per compiti di lato come la visione, i titoli di sessione o la compressione del contesto.

## Skill e plugin dalla chat, memoria fuori dal core

Nella stessa finestra arrivano altre due novità. Hermes Desktop può ora cercare e installare plugin e skill direttamente dalla conversazione, senza passare dal terminale: la ricerca nel Plugin Catalog e nello Skills Hub avviene in chat, con una scheda di conferma prima dell'installazione. E i provider di memoria continuano a uscire dal core: holographic e byterover hanno repository standalone marcati "unmaintained", con l'uscita fissata al 15 ottobre 2026, quando chi li usa dovrà passare ai plugin corrispondenti.

## Un indice, una domanda

Hermes Index non dice quale modello sia il migliore in assoluto. Dice una cosa più scomoda e più utile: che nel lavoro agentico il costo fa parte del risultato. La domanda non è più "quanto è bravo", ma "quanto è bravo per quello che costa".

---
*Fonti verificate: portal.nousresearch.com/bench (consultato 7 ottobre 2026); nousresearch.com (7 ottobre 2026); alphasignal.ai/news/nous-research-s-hermes-index-ranks-ai-agents-by-score-and-real-cost (7 ottobre 2026); documentazione Hermes Agent — Plugin Catalog, Skills, Memory Providers, Configuration (7 ottobre 2026); github.com/NousResearch/hermes-plugin-holographic e hermes-plugin-byterover (7 ottobre 2026).*
