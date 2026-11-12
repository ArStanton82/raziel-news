---
title: "Mille plugin in sette giorni: l'hackathon di Hermes chiude e sposta il collo di bottiglia"
date: 2026-11-12
draft: false
categories: ["Hermes", "AI"]
tags: ["hermes agent", "plugin", "hackathon", "nous research", "catalogo"]
summary: "Quasi mille plugin in una settimana per 20mila dollari di premi: ora il problema non è inventarli, è revisionarli."
---

Le candidature si sono chiuse alle 17 di New York, le 23 in Italia, e il conto è arrivato poche ore dopo: «quasi 1.000 voci». Ventiquattro ore prima Nous Research parlava ancora di «centinaia». La giuria sta selezionando i dieci finalisti e i vincitori arriveranno per email «tra circa una settimana».

Quel numero va letto per quello che è: non mille prodotti, ma mille domande di accesso a un indice.

## Un premio da ventimila dollari e una regola sola

Il bando era lineare: 20.000 dollari complessivi, distribuiti in cinque posizioni (10.000, 5, 2.500, 1.500 e 1.000 dollari) più cinque menzioni. Per partecipare non bastava un video: bisognava aprire una pull request che aggiungeva il plugin al catalogo ufficiale, pubblicare una demo sotto i 90 secondi e inviare entrambi i link.

Due dettagli dicono più dei premi. Le posizioni premiate sono dieci, esattamente quante le voci che la giuria sta selezionando. E la candidatura coincide con la pubblicazione nel catalogo: non si vince un concorso e poi si entra nel marketplace, si entra nel marketplace e la giuria decide quanto vale.

## Il collo di bottiglia si è spostato

Mille progetti in sette giorni non misurano la fantasia degli sviluppatori. Misurano la capacità di revisione di chi li deve accogliere. Con un rapporto di uno a cento tra finalisti e candidature, la selezione è il vero prodotto dell'hackathon.

Il catalogo, intanto, ha già dato segni di sforzo. Il plugin comunitario Hermes Multiplayer è stato aggiunto l'11 novembre e ri-pinnato quattro volte nell'arco di una giornata: prima per un cambio di nome degli strumenti, poi per due test obsoleti, infine per la rimozione del relay integrato — un pezzo di infrastruttura che non era più suo. La release v0.23.1 (618 pull request arrotolate in un patch) ha invece alzato da 2 a 16 MiB il tetto del catalogo: il file pubblicato lo aveva superato, e ogni installazione ricadeva in silenzio sulla copia inclusa nel client.

Sono dettagli di manutenzione, e sono la parte che nessun hackathon premia.

## Chi paga i conti del plugin

C'è poi la domanda che i mille progetti lasciano aperta: chi sostiene il costo di esercizio. Il nuovo plugin di comunità X Bookmarks — che trasforma i segnalibri di X in un digest settimanale su Hermes — richiede una propria app sviluppatore X, in regime di pagamento a consumo, oltre a Hermes v0.23.0 o superiore. Funziona, ma sposta sull'utente una chiave e una bolletta.

È lo stesso schema del relay rimosso da Multiplayer: quando il plugin cresce, le parti che costano denaro o responsabilità tendono a uscire dal codice e a tornare all'utente. Un ecosistema che passa da centinaia a mille voci in sette giorni non ha risolto questo punto. Lo ha moltiplicato.

La domanda giusta, alla fine, non è quanti plugin siano stati scritti. È quanti saranno ancora installabili tra sei mesi, con un pin aggiornato e qualcuno che risponda alle issue. La risposta arriva tra una settimana, quando la giuria pubblicherà dieci nomi su mille.

---
*Fonti verificate: annuncio @NousResearch sulla chiusura delle candidature e sui «quasi 1.000» invii (12 novembre 2026), ripreso dalla sezione Announcements di nousresearch.com; bando dell'Hermes Agent Plugin Hackathon con premi e requisiti di partecipazione (4 novembre 2026); API GitHub NousResearch/hermes-agent, commit `feat(catalog): add the hermes-multiplayer plugin entry`, `bump … pin to a60c87a`, `bump … to a744368`, `Re-pin … to 8dee088 (built-in relay removed)` (11 novembre 2026); release Hermes Agent v0.23.1, pubblicata il 10 novembre 2026, 618 PR e tetto del catalogo portato da 2 a 16 MiB (#151860, corregge #151856); post @HermesWatcher sul plugin X Bookmarks e sui requisiti di accesso (12 novembre 2026, fonte di comunità).*
