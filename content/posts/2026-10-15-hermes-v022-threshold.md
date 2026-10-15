---
title: "La soglia di Hermes: l'agente che si configura parlando"
date: 2026-10-15
draft: false
categories: ["Hermes", "AI"]
tags: ["hermes-agent", "nous-research", "release", "plugin", "agenti"]
summary: "Hermes Agent v0.22 «The Threshold Release» si presenta da solo in chat e taglia un terzo della codebase; il giorno dopo arriva la patch v0.22.1."
---

Il 13 ottobre Nous Research ha pubblicato Hermes Agent v0.22.0, «The Threshold Release», diffuso il giorno successivo. Il nome è una dichiarazione di intenti: dopo aver montato il pantheon con la v0.21, la v0.22 vuole far passare l'utente attraverso la porta. Il changelog ufficiale descrive il ciclo più ampio mai spedito dal progetto: circa 24.200 commit e 6.080 pull request unite da v0.21.0, 15.600 file modificati, 7.180 issue chiuse e circa 2.520 contributori.

## La prima conversazione non è con il modello

La novità più significativa non è tecnica, è di esperienza. Una nuova installazione desktop si apre su una chat di configurazione guidata che gira su un modello di prova gratuito: chi arriva non deve procurarsi una chiave API prima di poter parlare con l'agente. Nella stessa direzione vanno i Connectors, che portano Hermes dentro applicazioni ospitate come Linear e Notion senza richiedere un account Nous per iniziare, e i modelli locali con un runtime llama.cpp a un clic. L'onboarding smette di essere una procedura e diventa una conversazione.

## Un terzo di codice in meno

Il dato che colpisce è la direzione opposta alla crescita: la codebase è più piccola di circa un terzo. Ridurre la superficie mentre si aggiungono funzioni è un segnale di manutenzione, non di espansione. Attorno a questa spina dorsale il rilascio mette pacchetti desktop firmati, compreso il Microsoft Store, un solo package manager sotto tutto e un catalogo da 600 plugin. Il giorno dopo arriva la patch v0.22.1: correzioni per Windows Store e aggiornamenti dei plugin, parametri di default per Nemotron Super 3.5 e il pacchetto lingua coreano per il desktop.

## Quello che resta fuori

Alcune cose restano dichiarazioni, non annunci. Il co-fondatore Teknium ha detto che l'app mobile «non è lontana» e che l'accesso ad alcuni modelli attende ancora lavoro legale con Google e Microsoft. Gli account di terze parti che raccontano Hermes — l'onboarding, il login che non espone le password al modello — descrivono funzioni confermate dal changelog ufficiale, ma vanno letti come cronaca, non come voce del progetto.

Il punto è che Hermes sta smettendo di chiedere all'utente di essere un installatore. Se la soglia funziona, il progetto non si misurerà più in commit ma in quante persone riescono ad attraversarla.

---
*Fonti verificate: GitHub NousResearch/hermes-agent, release v0.22.0 «The Threshold Release» (13 ottobre 2026) e v0.22.1 (14 ottobre 2026); nousresearch.com, annuncio del 14 ottobre 2026; releasebot.io/updates/nousresearch/hermes-agent e releases.sh/nousresearch/hermes-agent (consultati il 2026-10-15); post X @NousResearch e @Teknium (14-15 ottobre 2026).*
