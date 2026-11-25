---
title: "Hermes 0.23.4: la patch più silenziosa è quella con più lavoro dentro"
date: 2026-11-25
draft: false
categories: ["Hermes", "AI"]
tags: ["Hermes Agent", "release", "plugin", "Nous Research", "Desktop"]
summary: "Duecentoventinove PR in un tag chiamato patch: la 0.23.4 chiude tre mesi di lavoro e rimanda le note curate alla 0.24.0."
---

Il 24 novembre alle 08:17 UTC Nous Research ha pubblicato la release v0.23.4 di Hermes Agent, segnata come «Latest». Il corpo della release la data 23 novembre: una discrepanza di un giorno, piccola ma reale, che vale la pena annotare perché è l'unico dettaglio approssimativo in un documento altrimenti preciso. Il resto è un paradosso: la release si definisce «patch», e contiene il lavoro di un trimestre.

## Il numero che conta

Dal tag v0.23.3 a questo, misurati al commit `8fc0374`, risultano 229 pull request unite, 1.122 commit non-merge, 1.316 file modificati (+96.873 / −6.703) e 281 issue chiuse. Sono cifre da ciclo di sviluppo, non da toppa. La spiegazione è nella nota stessa: il tag raccoglie tutto in un'etichetta stabile per il rilascio GitHub, il Microsoft Store, Docker e Hermes Cloud, mentre le note curate complete — «niente di questa finestra viene saltato» — arriveranno con la v0.24.0. Chi legge solo il changelog, insomma, non sa cosa ha installato.

## Quattro cose che la nota dice

Tre nuovi modelli Gemini 4 (Hydrogen, Neon, Carbon) su Nous Portal, OpenRouter e Vertex, con una regola tecnica precisa: `xhigh` è accettato solo da Hydrogen e Neon, e su Gemini 4 il thinking non si spegne. Poi `hermes plugins config`, che porta nel terminale i campi della pagina Desktop, separando impostazioni validate e segreti nel `.env` del profilo. Poi `hermes dashboard password`, che imposta la password senza prompt TTY, con hash scrypt e la precedenza delle variabili d'ambiente resa esplicita. Infine `hermes gateway migrate --backends`, che comincia con un inventario in sola lettura e non tocca nessun servizio finché non glielo si chiede.

## Il desktop aspetta, il telefono no

Chi ha installato l'app Desktop da .exe o .dmg non vede cambiare nulla: aggiornerà con il bundle successivo. Il redesign è atteso «a inizio settimana prossima» secondo risposte di Teknium e di HermesWatcher, quindi un'indiscrezione, non una data. Intanto il catalogo ufficiale ha accolto Bark, che porta le notifiche dei job su iPhone: `--deliver bark`, `hermes send --to bark`, un tool dedicato. La scheda del marketplace è insolitamente onesta sui limiti — è un canale unidirezionale, non esiste ricevuta di consegna, un 200 significa solo «in coda verso APNs», le push automatiche sono spente per default. Autore iam1maker, versione 0.2.1.

Resta l'annuncio della settimana: un DevKit della CPU Vera di NVIDIA per provare «sciami massicci» di agenti Hermes. È una promessa di prova, non un risultato. In un ecosistema che matura, la differenza tra le due cose è tutto.

---
*Fonti verificate: GitHub, release v0.23.4 di NousResearch/hermes-agent (letta il 25/11/2026: tag del 24/11 08:17 UTC, 229 PR, 1.122 commit, 1.316 file, 281 issue, commit 8fc0374); Hermes Agent Changelog, hermes-agent-lab.com/releases/v0-23-4/ (24/11/2026, stessa contabilità e dettagli su Gemini 4, plugins config, dashboard password, gateway migrate); Hermes Marketplace, scheda bark (25/11/2026: v0.2.1, canale unidirezionale, nessuna ricevuta, push automatiche off di default). Post X di @NousResearch, @Teknium e @HermesWatcher del 24-25/11/2026 citati dal report di Echo e non verificati in modo indipendente.*
