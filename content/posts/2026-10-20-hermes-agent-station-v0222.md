---
title: "Hermes impara a mostrarsi: la sala di controllo e la release che ripara la release"
date: 2026-10-20
draft: false
categories: ["Hermes", "AI"]
tags: ["hermes", "plugin", "agent-station", "release", "desktop"]
summary: "Agent Station porta la sala macchine di Hermes Desktop in una pagina; v0.22.2 chiude la linea 0.22 nata da un commit sbagliato."
---

Due modi per raccontare la giornata di Hermes. Il primo piace ai social: un plugin che disegna la sessione come una stazione spaziale, l'agente principale al centro e i subagent come moduli in orbita. Il secondo è più noioso e più importante: la versione stabile è la 0.22.2, pubblicata il 15 ottobre, e corregge una release costruita dal commit sbagliato. Insieme dicono la stessa cosa: Hermes non è più una demo che si aggiorna a sorpresa, ma un prodotto con canali di rilascio e strumenti per guardare dentro ciò che fa.

## Vedere il lavoro dietro la chat

Agent Station è un plugin per Hermes Desktop fatto dalla community, non un prodotto ufficiale Nous: la scheda di catalogo rimanda al repository di Muhammed Enes Alpler, licenza MIT, revisione fissata a un commit. Mostra ciò che accade nella chat in primo piano: una pagina disegna l'agente e i subagent avviati con `delegate_task` — compito, file toccati, risposta, costo —, una scheda elenca i comandi di shell in background, una terza ripercorre le modifiche ai file dopo ogni richiesta. Due dettagli contano più dell'estetica: è in sola lettura, apre il database di stato in modalità read-only e registra solo rotte GET; e richiede Hermes 0.21.7 o superiore, testato fino alla 0.22.2. Chi arriva da Subagent Watch, il vecchio nome del progetto, deve disinstallarlo prima, o si ritrova due voci in sidebar.

## La release che ripara la release

Il comunicato della 0.22.2 è un piccolo documento di igiene ingegneristica. La 0.22.1 era stata compilata dal commit sbagliato: conteneva lavoro sul gateway non ancora rilasciato e l'app del Microsoft Store poteva restare su "Connecting". La 0.22.2 è la release che doveva essere. Due correzioni si notano nell'uso quotidiano: il gateway riparte dopo un riavvio — su Linux un PID riassegnato poteva essere scambiato per un gateway attivo, e un gateway supervisionato da systemd o Docker si rifiutava di partire (PR #138594) — e i turni lunghi con modelli locali sopravvivono alla sospensione di un laptop, con streaming, timer che ignorano il sonno e compressione senza timeout (PR #138560). Resta un difetto noto: le sessioni avviate sotto il gateway 0.22.1 non si cancellano nella 0.22.2.

## Canali, non sorprese

Rispondendo a una segnalazione su una pull request già mergiata, Teknium ha spiegato che i canali esistono per non costringere gli utenti ad aggiornare a ogni cambiamento: chi vuole l'ultimissimo codice passi a `main`, chi vuole stabilità resti sui tag. È la differenza tra un progetto che si segue e un software che si usa: il lavoro di oggi su `main` — una manciata di correzioni, nessun tag nuovo — non arriverà a chi sta sulla stabile prima della 0.23.0. E va bene così.

In questa prospettiva il dungeon crawler da 107.000 righe "generate dagli agenti" è la parte meno interessante della giornata. La parte interessante è che qualcuno ha costruito una finestra per guardare gli agenti lavorare, e che il progetto ha imparato a dire: questa release era sbagliata, ecco quella giusta.

---
*Fonti verificate: GitHub, release v0.22.2 di NousResearch/hermes-agent (15 ottobre 2026); catalogo plugin di Hermes Agent, scheda agent-station, catalogo costruito il 20 ottobre 2026; changelog Hermes, PR #140760 "feat(plugin-catalog): add agent-station plugin", mergiata il 19 ottobre 2026; post di @Teknium su X del 20 ottobre 2026 (dal report di Echo, non verificabile su fonte indipendente).*
