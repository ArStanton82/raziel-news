---
title: "Asahi va al copyleft, Omarchy paga il fork: chi controlla il livello sotto il Mac"
date: 2026-11-23
draft: false
categories: ["Omarchy"]
tags: ["Asahi Linux", "Aurora Silicon", "Omacom Foundation", "copyleft", "GPLv2", "Apple Silicon", "driver"]
url: /2026/11/asahi-copyleft-omarchy-paga-il-fork/
summary: "La fondazione di Omarchy paga due manutentori del fork Aurora mentre Asahi passa al copyleft: la lotta per il livello sotto il Mac."
---

Il 20 novembre la Omacom Foundation ha annunciato che finanzia Aurora Silicon: hardware e token per chi ci lavora, e tre mesi a tempo pieno per due manutentori, Dj e Ryan Murray, a partire dalle serie M3 e M4. Aurora è il progetto che tiene in piedi Linux sui Mac con chip Apple al livello che non si vede: kernel, driver grafici, catena di avvio. Tredici giorni prima, il 7 novembre, Asahi Linux aveva annunciato che tutti i suoi repository passano alla GPLv2 o successiva. Le due notizie, lette insieme, sono la fotografia di chi sta prendendo il controllo di un livello che due anni fa non esisteva.

## I fatti, con le date

Il progress report di Asahi per Linux 7.3, firmato il 7 novembre, è esplicito: «il nostro licenziamento permissivo non è più sostenibile». Asahi era MIT per scelta, perché i driver potessero essere adottati anche dai BSD; ora passa al copyleft forte. Il bootloader m1n1 è già migrato, copyleft dalla 2.0.0, con le versioni precedenti che restano MIT. I driver del kernel erano già GPL, perché il kernel è GPL: la stretta riguarda il resto.

Il 20 novembre la fondazione ha risposto con i soldi: hardware per chi fa reverse engineering, token per i modelli che usa, tre mesi di stipendio per due persone. Il post ringrazia Asahi in modo esplicito e riconosce che l'albero di Aurora — bootloader, kernel, installer — nasce come fork del lavoro di Asahi. Lo stesso giorno è arrivato anche Beelink come patron societario con centomila dollari l'anno per tre anni, e un mini PC con Omarchy preinstallato: il totale dei sostegni dichiarati dalla fondazione arriva a circa 24 milioni di dollari, in buona parte in token di laboratori di AI più che in contanti.

## La licenza serve per la restituzione, non per il codice

Asahi non fa nomi, ma gli indizi sono tutti lì: «diversi tentativi di sfruttare il nostro licenziamento permissivo per dirottare il nostro lavoro, con l'obiettivo dichiarato di sostituire il progetto e monetizzare in modo aggressivo Linux su Apple Silicon». In alcuni casi, scrive Calligeros, codice di funzioni ancora in sviluppo è stato preso direttamente dai fork personali degli sviluppatori e pubblicato senza attribuzione, o «riscritto pigramente con l'aiuto di un LLM per nasconderne l'origine». Il precedente citato è Wine, che passò da MIT a LGPL nel 2002 per gli stessi motivi.

E va detto cosa la licenza non fa: il diritto d'autore protegge la forma, non l'idea, se una parafrasi di un modello sia opera derivata è questione aperta, e la GPL si fa valere solo con una causa. Il copyleft di Asahi è più una dichiarazione di aspettative che un rimedio. Nessuno ha ancora dimostrato che sia stata proprio Omarchy o Aurora a prendere codice senza attribuire.

La risposta di David Heinemeier Hansson è stata breve: la GPLv2 non cambia nulla, il kernel era già GPL, i driver sono già disponibili; «Asahi rifiuta l'upstreaming», ha aggiunto, e Omarchy è MIT. Il punto è tutto in quella frase.

## Il fork che non parla più a monte

Il regolamento di Aurora Silicon lo dice: «non contattate i progetti a monte», mai, per nessun motivo — niente bug, niente pull request, niente segnalazioni. Il motivo dichiarato è che l'approccio di Aurora ai modelli linguistici e alla decompilazione è diverso da quello di Asahi, e che quindi tutto ciò che nasce in Aurora va considerato «inutilizzabile» dal punto di vista di monte. Non è segretezza: è contaminazione. Aurora pretende solo che l'uso di un modello sia dichiarato in ogni pull request con una riga `Assisted-by:`.

Il paradosso: due progetti sullo stesso hardware, con lo stesso codice di partenza, che hanno smesso di scambiarsi i bug.

## Cosa cambia per chi usa la macchina

Per chi vuole Linux su un Mac la notizia buona è concreta: la via d'installazione senza chiavetta e senza terminale esiste da inizio novembre, e ora c'è una fondazione che paga chi la rende possibile.

La notizia cattiva è che il sapere sull'hardware Apple si sta scindendo in due tronconi che hanno deciso di non parlarsi, proprio mentre il codice si può riscrivere con un modello e nasconderne la provenienza. Chi compra un Mac per metterci Linux sceglie un ramo senza saperlo, e nessuno dei due è al sicuro: a monte ci sono anni di reverse engineering volontario, a valle una struttura finanziata che dipende da patrocini e assegnazioni di token.

## Il punto

Non c'è un cattivo in questa storia: c'è un modello nuovo. Fondazione più agenti più fork pagato compra velocità, e la mette su un albero che ha rinunciato a tornare a monte. Chi controlla il livello sotto il Mac, da qui in avanti, lo decide chi paga due stipendi e chi sceglie una licenza — non chi scrive il driver.

---
*Fonti verificate: omarchy.org/news/2026/11/omacom-foundation-to-sponsor-aurora-silicon/ (consultata il 23/11/2026: sponsorizzazione Aurora, hardware, token, tre mesi a tempo pieno per Dj e Ryan Murray, ringraziamento ad Asahi); omarchy.org/news/2026/11/beelink-joins-as-a-distinguished-corporate-patron/ (23/11/2026: 100.000 dollari l'anno per tre anni, mini PC Omarchy Edition, totale sostegni circa 24 milioni); asahilinux.org/2026/11/progress-report-7-3/ (23/11/2026, firmato James Calligeros il 7/11/2026: passaggio di tutti i repository a GPLv2+, citazioni sui tentativi di dirottamento e sulla riscrittura con LLM, precedente Wine, m1n1 copyleft dalla 2.0.0); aurorasilicon.org/docs/policies/ (23/11/2026: divieto di contattare i progetti a monte, riga Assisted-by nelle pull request); heise.de/en/news/Asahi-Linux-changes-license-to-stop-forks-from-taking-its-code-11519257.html (23/11/2026, 10/11/2026: quadro giuridico MIT contro GPLv2, questione aperta dell'opera derivata da modello, dichiarazione di DHH su X dell'8/11/2026 «Asahi changing to GPLv2 changes nothing» e «thanks to agent acceleration, Asahi rejects upstreaming», nessuna prova pubblica contro Omarchy o Aurora); omarchycentral.com (21 e 23/11/2026: ricostruzione della sponsorizzazione e richiamo al cambio di licenza di Asahi); X, ricerca «Omarchy» (23/11/2026: @tylenolburrito il 22/11 «20+ million dollars is actually absurd», @techmore_edu il 23/11 sull'appello a sostenere i manutentori di Aurora). Non verificato: Asahi non nomina Omarchy o Aurora nel report, quindi l'attribuzione resta indiziaria.*
