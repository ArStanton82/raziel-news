---
title: "Cento fix in un fine settimana: la sicurezza di Hermes si fa manutenzione"
date: 2026-11-16
draft: false
categories: ["Hermes", "AI"]
tags: ["hermes agent", "sicurezza", "release", "plugin"]
summary: "Oltre cento correzioni in un weekend, la 0.23.2 ancora in release candidate e un interruttore per la revisione automatica."
---

Mentre il resto del settore misura le novità in modelli annunciati, Hermes ha passato il fine settimana a fare l'unica cosa che non si può raccontare in un post di lancio: correggere. Un blocco di oltre cento fix, secondo il canale che segue il progetto, ha toccato il modo in cui i segreti vengono trattati dentro l'agente — negli errori, nell'output dei tool e nei log.

Non è una nota di prodotto, è il tipo di lavoro che si vede solo quando manca.

## Cosa è cambiato davvero

La descrizione pubblica parla di nuove chiavi riconosciute e mascherate: formati recenti di Gemini, Tavily, SendGrid, Slack, Discord, Teams. Il riscontro nel repository è coerente: tra il 13 e il 16 novembre risultano 178 commit che citano la redazione dei segreti e 21 pull request unite con il prefisso di lavoro `sec3/`, tra cui una sulla redazione dei file di credenziali e una sulle righe che contengono segreti. In parallelo la raffica `fix(approval)` ha chiuso falle nello scanner dei comandi: heredoc, script scritti e poi eseguiti, sink verso interpreti con redirect.

È un dettaglio poco glamour e molto concreto: la maggior parte delle fughe di credenziali non passa da un attacco esotico, passa da una riga di log che nessuno aveva previsto.

## La release non insegue i commit

La linea 0.23.2 resta ferma alle release candidate: la rc.8 è stata taggata il 14 novembre alle 18:53 UTC con un corpo generato dall'automazione, senza note prodotto, e non è stata promossa. L'ultima versione stabile rimane la v0.23.1 del 9 novembre, che aveva un solo compito dichiarato — alzare il tetto del catalogo plugin da 2 a 16 MiB, perché il file pubblicato era cresciuto oltre il limite accettato dai client e ogni installazione ricadeva silenziosamente sul catalogo incluso nella release.

Nel frattempo le canary continuano a uscire ogni mattina: quella di oggi è stata pubblicata alle 07:59 UTC. Le note curate per l'intera finestra, si legge nella release, arriveranno con la v0.24.0.

## L'interruttore che resta in mano all'operatore

Un dettaglio utile a chi usa l'agente più che a chi lo sviluppa: la revisione automatica in background — quella che rivede la conversazione per proporre memoria e skill — si spegne con una riga di configurazione, `auxiliary.background_review.enabled: false`, senza toccare la memoria e senza azzerare gli intervalli dei promemoria. La documentazione conferma che la chiave va letta sotto il blocco `auxiliary:`; un blocco `background_review:` di primo livello non viene considerato.

La lezione del weekend è sobria. La sicurezza non si annuncia, si accumula: cento correzioni invisibili valgono più di una feature in vetrina, e il fatto che la linea stabile non sia stata forzata per inseguirle è, in questo caso, un segnale di disciplina e non di ritardo.

---
*Fonti verificate: API GitHub NousResearch/hermes-agent, releases (16/11/2026, ultima canary v0.23.1+canary.20261116T070005Z delle 07:59 UTC); note di release v0.23.1 (9/11/2026); pagina release rc.8-v0.23.2 (14/11/2026, 18:53 UTC); ricerca commit e pull request sul repository (13-16/11/2026); documentazione Hermes, /docs/user-guide/features/memory (16/11/2026); post @HermesWatcher e @Teknium su X (16/11/2026) come dichiarazioni di parte. Esclusa la segnalazione di una falsa app «Hermes Agent - AI» sul Play Store: unica fonte, nessuna conferma ufficiale.*
