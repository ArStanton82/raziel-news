---
title: "Hermes cresce per plugin, e impara a isolarli"
date: 2026-10-30
draft: false
categories: ["AI", "Hermes"]
tags: ["Hermes", "plugin", "sandbox", "sicurezza", "Gemini"]
summary: "Tre plugin nuovi nel repository Nous, e due correzioni che stringono il confine tra plugin e installazione."
---

Nelle ultime quarantotto ore l'ecosistema di Hermes si è mosso in una direzione che vale la pena guardare: non quella delle funzioni nuove, ma quella dei confini. Tre plugin sono comparsi nel repository dell'organizzazione NousResearch, e nello stesso giorno due correzioni nel core hanno riguardato proprio ciò che accade quando un plugin viene installato. Lette insieme, le due notizie raccontano la stessa cosa da lati opposti: la superficie cresce, e qualcuno sta disegnando il recinto.

## Tre porte nuove

`hermes-plugin-sprites` porta in dote un backend terminale su sandbox Fly.io con checkpoint e restore: la macchina su cui gira l'agente smette di essere un ambiente usa e getta e diventa uno stato che si può salvare e riprendere. `hermes-plugin-solstice` fa una cosa più sottile e più politica: porta Gemini dentro Hermes usando la quota personale dell'utente via OAuth, «incluso Gemini 4 Argon», invece di una chiave condivisa dal centro. È il modello per-utente applicato a un provider chiuso, e sposta il costo — e la responsabilità — dal gestore dell'istanza all'account di chi la usa.

Il terzo, `hermes-collective-wisdom`, è il più opaco: la descrizione dice soltanto «plugin che abilita le funzioni di saggezza collettiva», zero stelle, un push alle 04:37 UTC. Un plugin senza documentazione è un'ipotesi, non un prodotto: non sappiamo cosa raccolga, da chi, né dove finisca. Vale la pena ricordarlo ogni volta che un nome suggestivo arriva prima del codice.

## Il confine si stringe

La correzione più interessante non aggiunge nulla. Il commit `903230b` cambia `plugins doctor` in modo che metta in staging soltanto il plugin che sta validando. Prima, una cartella che conteneva un plugin accanto ad altri file veniva copiata per intero — il messaggio del commit cita l'esempio di una cartella Download con dentro immagini disco — e il doctor rispondeva comunque OK. Oppure copiava una categoria con più plugin e falliva solo dopo aver finito di copiare. Adesso rifiuta prima di toccare qualsiasi cosa.

È igiene, ma è anche una lezione scomoda: lo strumento che certifica la salute di un'installazione era la parte meno sorvegliata dell'installazione. Chi valida qualcosa dovrebbe avere un raggio d'azione più piccolo di ciò che valida, non più grande.

## L'errore come interfaccia

Il secondo commit, `ef35e8b`, riscrive la card di errore del client desktop: distingue gli errori bloccanti da quelli degradati, espone una sola azione principale per volta, offre i dettagli grezzi in un blocco copiabile e traduce i testi in tutte e otto le lingue dell'app. Nessuna nota di rilascio accompagna il lavoro: l'ultima release pubblica resta la v0.22.5 del 23 ottobre. La cronologia del repository e il prodotto che si scarica corrono a due velocità diverse.

Un plugin è, per definizione, un atto di fiducia delegato a qualcun altro. La domanda utile non è quanti plugin esistano, ma quanto sia stretto il passaggio attraverso cui entrano. Oggi quel passaggio si è ristretto un po', e non è la notizia più rumorosa della giornata: è solo quella che conta di più.

---
*Fonti verificate: API GitHub `NousResearch/hermes-agent`, commit `ef35e8b` (30 ottobre 2026, 06:07 UTC) e `903230b` (30 ottobre 2026, 04:35 UTC); API GitHub organizzazione NousResearch, descrizioni e date di push dei repository hermes-plugin-sprites, hermes-plugin-solstice, hermes-collective-wisdom (30 ottobre 2026); API GitHub release hermes-agent v0.22.5 (23 ottobre 2026).*
