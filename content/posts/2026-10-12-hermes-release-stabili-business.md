---
title: "Hermes Agent v0.21.7 e la scelta delle release stabili: il progetto entra nella fase adulta"
date: 2026-10-12
draft: false
categories: ["Hermes", "AI"]
tags: ["hermes-agent", "nous-research", "open-source", "release", "plugin", "missingno"]
summary: "Hermes Agent pubblica la v0.21.7 e passa alle release taggate: il progetto open source di Nous Research sceglie la stabilità."
---

Il 12 ottobre, alle 05:53 UTC, Nous Research ha pubblicato Hermes Agent v0.21.7. Letta così è una normale patch release, la seconda tagliata dalla nuova pipeline di distribuzione. Ma il dettaglio più interessante non è nel numero di versione: è nella regola che introduce. Da oggi un'installazione da sorgente del repository ufficiale si aggiorna all'ultima release taggata `vX.Y.Z`, non più a ogni commit su `main`. Chi vuole continuare a seguire lo sviluppo quotidiano deve chiederlo esplicitamente.

## Dal ritmo del commit al ritmo della release

Per un progetto nato come strumento per sviluppatori, è un cambio di postura. Aggiornarsi a ogni commit significa vivere sul filo del rasoio: si ottengono le novità subito, ma anche i difetti non ancora filtrati. Passare alle release taggate introduce un ritmo più lento e prevedibile, lo stesso che adottano i software che qualcuno usa per lavorare, non solo per sperimentare. La v0.21.7 non porta grandi funzionalità — il roll-up di circa 204 pull request servirà alla v0.22.0 — ma consolida questa infrastruttura di distribuzione: un interruttore in Settings ▸ About ▸ Updates, un dialogo che dice su quale canale ti trovi, e aggiornamenti che non falliscono più dietro certi firewall. Anche il "reasoning" firmato ora sopravvive a `hermes chat --resume`.

## Open source e business non sono opposti

Il contesto in cui arriva questa release è significativo. Il 7 ottobre Nous ha confermato il round Series B da 90 milioni di dollari a una valutazione di 1,5 miliardi, guidato da Robot Ventures con Nvidia, Microsoft M12, Samsung, Union Square Ventures, Y Combinator e Menlo Ventures tra i partecipanti. Il funding totale sale a 158 milioni e il capitale finanzia l'ingresso enterprise con "Hermes for Businesses". Il messaggio che circola è chiaro: dare via il software può essere il modo in cui il business comincia, non il suo contrario. Il WSJ riporta un run-rate di circa 36 milioni di dollari a metà settembre, con l'obiettivo di superare i 100 milioni entro fine anno.

## Solo plugin ufficiali, e un modello gratuito

Sul fronte operativo, il co-fondatore Teknium ha precisato che nel repository `hermes-official-plugins` finiranno solo i plugin ufficiali mantenuti da Nous, non quelli della community: "We are only putting official, nous maintained plugins in that repo". Intanto è ancora disponibile, per tempo limitato, MISSINGNO: un modello per coding e ragionamento agentico che Nous descrive come molto efficiente in token e offre gratis su Nous Portal. Un annuncio di mercato, ma anche un test di adozione.

## Conclusione

Hermes sta diventando un prodotto con un ciclo di rilascio disciplinato, un'offerta enterprise e un ecosistema di plugin con regole chiare. È il passaggio dall'entusiasmo alla manutenzione: meno spettacolare, ma è la fase in cui un progetto open source dimostra di poter durare oltre la curiosità iniziale.

---
*Fonti verificate: github.com/NousResearch/hermes-agent (release v0.21.7, pubblicata 12 ottobre 2026, 05:53 UTC) e releasebot.io (12 ottobre 2026); techcrunch.com, startupfortune.com, techfundingnews.com, digg.com e zetik.com sul Series B da 90 milioni e "Hermes for Businesses" (7 ottobre 2026); nousresearch.com e portal.nousresearch.com su MISSINGNO (10 ottobre 2026); github.com/NousResearch/hermes-official-plugins (push 11 ottobre 2026); x.com/Teknium sui plugin ufficiali e il tier Ultrafast (12 ottobre 2026). Nota: TechCrunch cita "oltre 24 milioni di cloni", il WSJ "oltre 22 milioni di download"; la differenza dipende dalla metrica usata.*
