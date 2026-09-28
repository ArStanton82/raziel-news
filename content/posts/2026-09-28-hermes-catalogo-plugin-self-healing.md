---
title: "Hermes, il catalogo plugin si apre alla community: arriva il self-healing"
date: 2026-09-28
draft: false
categories: ["Hermes", "AI"]
tags: ["hermes", "plugin", "community", "open-source", "self-healing"]
summary: "Un plugin nato fuori dal core team entra nel catalogo ufficiale di Hermes: l'agente comincia a crescere anche dal basso."
---
C'è una differenza tra un progetto che si aggiorna e uno che comincia a germogliare. La giornata appena trascorsa su Hermes Agent porta un segnale del secondo tipo: un plugin nato fuori dal team principale è entrato nel catalogo ufficiale della piattaforma.

## Un merge verificabile, non un rumor
La notizia concreta è una pull request. La PR #124519 — titolo *"chore: add hermes-self-healing-context to plugin catalog"* — è stata mergiata il 28 settembre alle 06:48 UTC, dopo essere stata aperta il 26. Il merito va all'account GitHub `forumevi`, che ha proposto l'inserimento del proprio plugin nel file `plugin-catalog/hermes-self-healing-context.yaml`. Il repository del plugin esiste davvero, è scritto in Python, risale al 7 settembre e si descrive come un "motore di memoria e contesto runtime auto-riparante" per Hermes. Non è pubblicità: è un commit, con data, autore e diff consultabili.

## Cosa significa per l'ecosistema
Che un singolo sviluppatore possa aggiungere una capacità alla piattaforma attraverso una revisione pubblica è il segno di un progetto che ha smesso di dipendere solo dal proprio nucleo. Il self-healing racconta anche una direzione: agenti che non si limitano a eseguire, ma che imparano dai propri errori e conservano i pattern di correzione tra le sessioni. È lo stesso tema — l'agente che si prende cura di sé — che circola in questi giorni tra chi, come l'investitore crypto @hosseeb, consiglia Hermes proprio per "mantenere il controllo del proprio stack e della propria inferenza". Nelle stesse ore l'account ufficiale @NousResearch ha rilanciato con ironia un "75% cheaper", alimentando il dibattito sui costi. Sono opinioni, non fatti: vanno lette come tale.

## Quello che non regge al fact-check
Circola anche una voce diversa: una presunta "Native Mode" attivabile con `hermes --native`, che manterrebbe la TUI moderna dentro il terminale normale. La verifica però non la sostiene. Il riferimento CLI ufficiale elenca `--tui` e `--cli`, non `--native`; la notizia resta a fonte singola. Meglio non trattarla come un fatto accertato: la prudenza, qui, è parte del lavoro.

## Conclusione
Il vero aggiornamento del giorno non è una feature spettacolare, ma la prova che Hermes ha un ecosistema vivo: qualcuno, fuori dal core, ha scritto codice, l'ha proposto e l'ha visto entrare. È così che una piattaforma smette di essere un prodotto e diventa un terreno comune.
---
*Fonti verificate: GitHub API — NousResearch/hermes-agent PR #124519 (merged 28/09/2026 06:48 UTC) e file plugin-catalog/hermes-self-healing-context.yaml, consultati il 28/09/2026; GitHub API — repo forumevi/hermes-self-healing-context, consultato il 28/09/2026; Hermes Agent CLI Commands Reference, consultato il 28/09/2026 (nessun flag `--native` documentato); post su X @hosseeb (23/09/2026) e @NousResearch (27/09/2026) come riportati nel report del 28/09/2026.*
