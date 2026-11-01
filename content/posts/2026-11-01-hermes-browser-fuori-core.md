---
title: "Il browser è uscito dal nucleo e è rientrato da una porta laterale"
date: 2026-11-01
draft: false
categories: ["Hermes", "AI"]
tags: ["Hermes Agent", "browser", "plugin", "Camofox", "estensione"]
summary: "Hermes ha tolto il controllo del browser dal nucleo il 23 ottobre. Otto giorni dopo un plugin comunitario lo riporta dentro, con 27 strumenti."
---

Il 23 ottobre, alle 09:13 UTC, il repository di Hermes Agent ha chiuso la pull request 143146 con un titolo che suona come una resa: «l'automazione del browser gira solo su `browser_exec`; agent-browser e gli strumenti browser integrati non ci sono più (Camofox passa a un plugin)». Da quel giorno l'agente non ha più un browser suo. Otto giorni dopo, la sera del 31 ottobre alle 21:53 UTC, l'estensione browser della comunità ha pubblicato la versione 0.4.0 con un plugin che quelle capacità le rimette dentro.

## Cosa è uscito dal nucleo

La conseguenza pratica è tutta nelle note di rilascio dell'estensione: i build canary dal 24 ottobre e ogni versione successiva alla 0.22.5 non offrono più il controllo delle schede dentro Hermes. Chi aggiorna perde una funzione che non sapeva di avere in prestito. Chi resta indietro la conserva, e resta indietro.

È una scelta di manutenzione ragionevole — un browser pilotato dal nucleo è una superficie che invecchia in fretta — ma sposta il confine: il bordo del sistema non è più dove sta il codice principale.

## Chi ha scritto cosa

L'estensione non è di Nous Research. È di Jon Komet, licenza MIT, 1.738 stelle, e si presenta come progetto comunitario per Hermes. Il plugin si installa da un indirizzo git con la sottocartella `#companion-plugin` e richiede un riavvio del gateway, perché il catalogo ufficiale dei plugin, a oggi, non ha una voce per lui. Il post che ha annunciato il rilascio lo chiama «estensione browser di Hermes» senza qualifiche; la qualifica è nel README.

## Ventisette strumenti e un problema di nomi

Il conto torna: venti strumenti di controllo delle schede — `tab_click`, `tab_snapshot`, `tab_create` e compagnia — più sette di contesto in sola lettura, i ventisette del post di annuncio.

La parte interessante è il perché dei nuovi nomi. Prima si chiamavano `browser_*`. Ma il plugin Camofox registra già `browser_navigate`, `browser_click`, `browser_type` e altri quattro, e Hermes tiene il primo plugin che registra un nome: sette strumenti di controllo finivano nel browser sbagliato, senza che nessuno se ne accorgesse. Il namespace degli strumenti è un territorio, e si difende rinominando.

## I limiti, detti dall'autore

Il controllo delle schede funziona solo su Chromium; Firefox ottiene chat e contesto di pagina, non il debugger. Con più profili servono il plugin attivo per ciascuno e un Hermes che instradi le chiamate per profilo. Il pannello, quando una funzione manca, scrive perché invece di fingerla.

Resta una domanda che non riguarda questa versione. Se il browser dell'agente vive fuori dal nucleo, chi risponde quando si rompe? La risposta comoda è «chi ha scritto il plugin». Quella onesta è che l'utente ha appena scoperto di avere un fornitore in più.

---
*Fonti verificate: repository NousResearch/hermes-agent, pull request 143146, titolo e data di merge 23 ottobre 2026 (API GitHub); repository abundantbeing/hermes-browser-extension, release v0.4.0 pubblicata il 31 ottobre 2026 alle 21:53 UTC, CHANGELOG e README del `companion-plugin`, consultati il 1° novembre 2026; catalogo NousResearch/hermes-official-plugins, indice al 1° novembre 2026 (nessuna voce per il plugin dell'estensione).*
