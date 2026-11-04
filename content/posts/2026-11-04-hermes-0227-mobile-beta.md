---
title: "Hermes cresce di notte: la 0.22.7, una beta mobile già piena e i plugin che arrivano da fuori"
date: 2026-11-04
draft: false
categories: ["Hermes", "AI"]
tags: ["Hermes Agent", "Nous Research", "Hermes Mobile", "plugin", "open source"]
summary: "Patch 0.22.7 con 174 PR, la beta mobile esaurita in poche ore a NousCon e un ecosistema di plugin che cresce fuori dal perimetro ufficiale."
---

C'è un modo di misurare la salute di un progetto open source che non passa dalle stelle su GitHub né dai comunicati: guardare cosa succede nei giorni in cui nessuno annuncia niente. La notte del 3 novembre Hermes Agent ha pubblicato la versione 0.22.7, un aggiornamento che l'etichetta definisce «patch» e che però, se si aprono i numeri, racconta altro.

## Una patch che non è una patch

Nella finestra da v0.22.6 a v0.22.7 il repository registra 581 commit non-merge su 554 file modificati, con un saldo di +24.012 e −3.144 righe, 174 pull request unite e 29 issue chiuse, sul commit `b200f5b`. La release, firmata da teknium1, arriva su CLI, Microsoft Store, Docker e Hermes Cloud, ma le note curate sono rimandate alla 0.23.0: quello che leggiamo oggi è un riassunto volutamente incompleto. Tra le voci non documentate figurano il lead routing opzionale nelle Group Chat di Desktop, i cron job che pubblicano nelle stanze condivise e il rendering di diagrammi mermaid e TeX.

174 PR in poche settimane non sono un caso: sono una direzione. Chi insegue ogni numero rischia di confondere il ritmo con la sostanza, ma qui il ritmo è la sostanza.

## La beta mobile si è riempita in poche ore

Il giorno prima, il 3 novembre, Nous aveva ringraziato chi ha attraversato il mondo per NousCon 2026 ricordando che la beta di Hermes Mobile, presentata all'evento, «si è riempita rapidamente, come previsto». L'azienda dice di stare liberando nuovi posti e di voler portare l'app in produzione per un rilascio più ampio; nel frattempo resta la lista d'attesa. Il post ha raccolto oltre 900 like e più di 63.000 visualizzazioni.

Vale la pena leggerlo per quello che è: una beta chiusa che si esaurisce è un segnale di domanda, non una misura di prodotto. La differenza tra le due cose è esattamente quella che separa un evento da una tabella di marcia.

## Il plugin non lo scrive più solo Nous

Il fronte più interessante è laterale. Un account di tracking della community ha presentato «Office 3D», plugin che trasforma ogni profilo Hermes in una persona seduta alla scrivania dentro un ufficio isometrico, con statistiche reali di sessione, token e costo. Il codice esiste — `oslook/hermes-desktop-plugin-office-3d`, costruito con l'SDK dei plugin di Desktop — ma non è un prodotto ufficiale, ed è bene dirlo. Nello stesso giorno il repository `hermes-plugin-sprites`, backend di terminale su sandbox Fly.io, risultava aggiornato.

La conclusione è meno entusiasta di quanto sembri. Hermes non sta vincendo perché ha più funzioni: sta vincendo perché la sua superficie è abbastanza aperta da rendere conveniente costruirci sopra, anche a chi non fa parte della casa. Il rischio, come sempre nei ecosistemi giovani, è che l'abbondanza diventi rumore: plugin non documentati, fork che duplicano, aspettative create da account che non rappresentano il progetto. La qualità della selezione, nei prossimi mesi, conterà più della quantità dei commit.

---
*Fonti verificate: GitHub, release Hermes Agent v0.22.7 (pubblicata 2026-11-03T21:53Z, commit b200f5b); nousresearch.com, announcement del 2026-11-03 su NousCon e beta Hermes Mobile; API GitHub, ricerca `hermes-desktop-plugin-office-3d` e repository dell'organizzazione NousResearch (letti il 2026-11-04).*
