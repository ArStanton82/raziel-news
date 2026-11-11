---
title: "Il plugin è diventato il prodotto: l'hackathon di Hermes chiude stasera"
date: 2026-11-11
draft: false
categories: ["Hermes", "AI"]
tags: ["hermes agent", "plugin", "hackathon", "nous research", "ecosistema"]
summary: "Chiude oggi l'hackathon plugin di Hermes: 20mila dollari in premi, centinaia di progetti. E un bug da 14 MiB spiega perché."
---

Alle 17 di New York, le 23 in Italia, si chiudono le sottomissioni del Plugin Hackathon di Hermes Agent. Nous Research lo aveva aperto il 4 novembre con una settimana di tempo, 20.000 dollari in premi e una promessa: i plugin accettati sarebbero finiti nel nuovo Hermes Marketplace, dove chiunque usa l'agente può installarli. Ieri sera l'account ufficiale ha scritto che le candidature sono già «centinaia» e che la giuria sta per mettersi al lavoro. Non è una notizia finanziaria. È però il segno che per Hermes il confine del prodotto si è spostato: non è più il modello che risponde, è ciò che gli si aggancia intorno.

## Un catalogo, non una vetrina

Le regole dell'hackathon dicono molto su come Nous immagina l'ecosistema. Per partecipare non basta un video: bisogna aprire una pull request che aggiunge il plugin al catalogo ufficiale, pubblicare una demo sotto i 90 secondi e inviare entrambi i link. I giudici valutano utilità, affidabilità, rifinitura e creatività, e — parola del bando — «favoriscono i plugin che fanno più di quanto potrebbe fare un prompt o una skill». Il premio vero non è il denaro: è l'ingresso in un indice che gli utenti possono consultare.

## Il bug che spiega perché i tubi contano

Mentre le demo si accumulavano, martedì è arrivata la patch v0.23.1: circa 618 pull request arrotolate in una release di stabilità, ma con un intervento che vale la pena leggere. Dal 9 novembre il `plugin-catalog.json` pubblicato aveva superato il tetto di 2 MiB che i client accettano; risultato, ogni installazione ricadeva silenziosamente sul catalogo incluso nella release. I plugin aggiunti dopo l'ultimo aggiornamento sparivano, si installavano pin vecchi, le voci «rimosse» non arrivavano. La correzione alza il limite a 16 MiB, così il catalogo live torna utilizzabile.

È il dettaglio che decide se un ecosistema esiste o sembra esistere. Un hackathon produce idee; un catalogo che si aggiorna le rende installabili. Chi è rimasto alla v0.23.0 o precedente continua a vedere la copia vecchia finché non aggiorna — e questa è, in miniatura, la storia di ogni distribuzione software.

## La coda che non si vede

Intanto l'altra metà del racconto è mobile. La lista d'attesa della beta è aperta sul sito ufficiale di Nous. Le stime che circolano sono però di community, non dell'azienda: l'account HermesWatcher parla di circa 100.000 persone in attesa e di una release completa tra il Giorno del Ringraziamento e Natale, con la beta limitata dai tetti di tester imposti da Apple e Google. Lo stesso account indica in una o due settimane l'arrivo del redesign di Desktop e web app, senza beta intermedia. Sono indicazioni plausibili e non confermate: vanno lette come tali.

La cosa certa è che l'ecosistema si sta organizzando su tre piani — plugin, catalogo, client — e che il collo di bottiglia non è più la fantasia degli sviluppatori. Centinaia di progetti in sette giorni lo dimostrano. Il problema, come sempre, è la manutenzione: chi rivede, chi rompe, chi aggiorna il pin. Il martedì di v0.23.1 è lì a ricordarlo.

---
*Fonti verificate: thread ufficiale @NousResearch sull'hackathon (4 e 10 novembre 2026); note di release Hermes Agent v0.23.1 su GitHub (pubblicata 10 novembre 2026, release date 9 novembre); pagina di iscrizione alla beta mobile di Hermes Agent, hermes-agent.nousresearch.com/mobile (consultata 11 novembre 2026); post @HermesWatcher su lista d'attesa e redesign Desktop (11 novembre 2026, fonte di community, non confermata da Nous Research).*