---
title: "Hermes esce dal terminale: il Desktop nel browser e la skill che cancella i data broker"
date: 2026-10-26
draft: false
categories: ["Hermes", "AI"]
tags: ["hermes-agent", "desktop", "unbroker", "privacy", "open-source"]
summary: "Il Desktop di Hermes viene servito dal gateway e si apre nel browser. Nous intanto spinge Unbroker, la skill che rimuove i dati dai broker."
---

Due notizie nello stesso giorno raccontano la stessa traiettoria da due lati. Da una parte Hermes smette di essere una cosa che si apre in una finestra: il Desktop viene servito dal gateway dell'utente e diventa raggiungibile da un browser qualunque. Dall'altra arriva una skill che fa il lavoro opposto, cioè togliere i dati personali dai siti che li rivendono. Un agente che si rende raggiungibile ovunque e che, insieme, impara a far sparire le tracce che gli altri hanno lasciato.

## Il Desktop non ha più un server suo

La documentazione ufficiale descrive già il meccanismo: si abilita con `hermes config set webapp.enabled true`, si riavvia il gateway e `hermes webapp` compila il bundle se necessario, avvia il gateway se non è in esecuzione e apre un link di accesso monouso. Il workspace Desktop — sessioni, profili, Cron, Artifacts, file dell'host, rail del terminale — viene servito su `127.0.0.1:9120`. Non è la Web Dashboard, ed è il punto: non c'è un relay separato, c'è il gateway che già si possiede.

Il dettaglio che conta è la distinzione tra main e release. L'ultima versione pubblicata resta la v0.22.5, del 22 ottobre; nessuna nota di rilascio annuncia la funzione. Chi legge l'annuncio e aggiorna non la troverà. Chi lavora da main, sì.

## Una skill per uscire dai database

Il secondo movimento ha un numero che vale più di un comunicato: il post di Nous Research su Unbroker ha raccolto oltre 1.100 like e 1.172 bookmark. I bookmark, non i like, misurano l'intenzione di fare qualcosa.

Unbroker è una skill opzionale, installabile con `hermes skills install official/security/unbroker`, arrivata nel repo con la pull request 57438 firmata SHL0MS. Cerca nome, indirizzi, telefono, email e parentele sui data broker e sui siti people-search, poi compila le richieste di rimozione. L'automazione è a livelli: dove il modulo si lascia compilare, lo compila; dove serve un CAPTCHA duro, una carta d'identità, una telefonata o un fax, restituisce a fine corsa un elenco di cose da fare a mano. Non aggira i sistemi anti-bot, non agisce su nessuno senza consenso registrato, tiene un registro delle richieste e riscansione con un Cron. Per la California usa il portale statale DROP, dove una sola richiesta copre un registro di circa 545 broker.

## Quello che manca

Manca la parte noiosa e decisiva: una release. Nella notte il repo ha ricevuto commit coerenti su compattazione e telemetria — riepiloghi preparati mentre i tool girano, flush dei dati al pre-esito del processo — ma restano su main, e alcune opzioni sono disattivate di default. La distanza tra «unito» e «rilasciato» è dove si accumulano le aspettative deluse.

Resta una domanda editoriale, non tecnica: un agente che si raggiunge da qualsiasi browser e che parla in nostro nome con i broker è comodo, ma sposta il perimetro della fiducia. Non è più il terminale a proteggerci. È la consapevolezza di cosa abbiamo delegato.

---
*Fonti verificate: documentazione Hermes Agent, pagine Desktop e Webapp (26 ottobre 2026); GitHub NousResearch/hermes-agent, releases e commit su main (26 ottobre 2026); documentazione Hermes Agent, skill opzionale security/unbroker (26 ottobre 2026); pull request #57438 (26 ottobre 2026); post @NousResearch e @HermesWatcher del 26 ottobre 2026.*
