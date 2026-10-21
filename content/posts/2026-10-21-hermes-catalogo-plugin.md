---
title: "Il catalogo di Hermes ha 644 plugin, non 700: la differenza conta"
date: 2026-10-21
draft: false
categories: ["Hermes", "AI"]
tags: ["hermes-agent", "plugin", "game-dev", "nvidia", "asus"]
summary: "Il catalogo plugin di Hermes supera le 640 voci revisionate. Intorno crescono uno studio di videogiochi e i laptop RTX Spark."
---
Nella stessa giornata in cui il co-fondatore di Nous Research annunciava poteri da studio di videogiochi per Hermes Agent, il dato più interessante era un altro, e stava in fondo a una pagina di documentazione: il contatore del catalogo plugin.

## Il numero che i social gonfiano

Sui social circolava «oltre 700 plugin». La pagina ufficiale del catalogo, interrogata il 21 ottobre, ne dichiara 644, divisi in nove categorie: 13 ufficiali e 631 della community. Le note di rilascio della v0.22.0, datate 13 ottobre, parlavano di 600 voci. Quarantaquattro aggiunte in otto giorni sono un ritmo credibile per un catalogo vivo; un salto a 700 non lo è. Non è pignoleria da redattori: in un ecosistema di estensioni il numero è anche la misura della superficie esposta, e gonfiarlo non aiuta nessuno.

## Un catalogo, non un app store

La cosa notevole non è la quantità, ma il meccanismo. Ogni voce è bloccata a un commit revisionato: quello che si installa è esattamente ciò che è stato esaminato, e un aggiornamento arriva solo quando un nuovo pin passa la revisione. Le regole del catalogo vietano ai plugin di modificare le interiora di Hermes o di distribuire binari non scansionabili.

È una scelta di governance travestita da funzione. Un ecosistema che cresce di oltre il sette per cento in una settimana ha bisogno di un collo di bottiglia, non di un cancello aperto. Il catalogo è quel collo di bottiglia, e la sua lentezza dichiarata è il prodotto.

## Lo studio di videogiochi resta un piano

Ryan Teknium ha indicato le capacità mancanti per trasformare l'agente in un piccolo studio: generazione di modelli 3D, animazioni, effetti sonori, connettori a Unity e Godot. Tutto via plugin, senza toccare il core. La stampa specializzata è stata esplicita: gli strumenti non sono ancora stati aggiunti, e la proposta è una roadmap. Un plugin comunitario per il game dev esiste come pull request nel catalogo, non come voce installabile.

Vale la pena ricordare la direzione: l'agent framework non prova a diventare un motore grafico. Prova a orchestrare quelli che esistono già.

## Il laptop come canale di distribuzione

Il terzo movimento è più silenzioso e forse più decisivo. Il 16 ottobre Nous Research ha confermato di essere partner di lancio di RTX Spark, la piattaforma NVIDIA per PC con agenti locali. ASUS la porta sui ProArt P16 e P14 e sul mini PC GR1X, con pre-ordini dal 7 ottobre e disponibilità dal 16. Hermes arriva insieme a ComfyUI, e la sicurezza passa dal runtime OpenShell di NVIDIA.

«Abbiamo costruito Hermes per dare un'intelligenza che puoi davvero possedere, invece di affittarla», ha detto il CEO Dillon Rolnick. È una frase di marketing, ma descrive una strategia coerente: prima il catalogo rende l'agente estendibile da altri, poi l'hardware lo rende presente sulla scrivania.

Tre mosse che convergono. Il numero da seguire non è quello gridato sui social, ma quello revisionato nella pagina del catalogo.

---
*Fonti verificate: catalogo plugin Hermes Agent, hermes-agent.nousresearch.com/docs/plugins (letto il 21/10/2026); note di rilascio v0.22.0 del 13/10/2026 (GitHub NousResearch/hermes-agent); TokenPost, «Nous Research Co-Founder Plans Game Studio Tools for Hermes Agent», 20-21/10/2026; Nous Research, annuncio RTX Spark, 16/10/2026; NVIDIA, comunicato RTX Spark, 01/06/2026; ASUS, comunicato ProArt P16/P14 e GR1X, 08/10/2026. Discrepanza annotata: il «oltre 700 plugin» diffuso sui social non corrisponde al conteggio ufficiale di 644.*
