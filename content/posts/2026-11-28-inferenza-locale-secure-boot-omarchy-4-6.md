---
title: "Inferenza locale e Secure Boot: Omarchy 4.6 ridisegna chi controlla la macchina"
date: 2026-11-28
draft: false
categories: ["Omarchy", "AI"]
tags: ["Omarchy 4.6", "modelli locali", "systemd-boot", "Secure Boot", "polkit", "Tailscale", "DGX Spark", "Chrome"]
url: /2026/11/inferenza-locale-secure-boot-omarchy-4-6/
summary: "La release candidate 4.6 porta i modelli locali nel sistema e sposta il boot: la macchina cambia padrone, e lo dice."
---

Il 27 novembre è uscita la release candidate 4.6 di Omarchy. Le note avvertono che non è una release finale e consigliano una macchina di test o uno snapshot da cui tornare indietro; poi mettono in chiaro la tesi: «Omarchy 4.6 porta i modelli aperti a casa». È il primo giro in cui il sistema si riorganizza intorno all'ipotesi che sulla macchina girino agenti, e nella stessa release consegna tre pezzi dello stack a qualcun altro: il catalogo dei modelli al progetto, la firma del boot a Microsoft, il browser a Google.

## Tre modifiche, tre date

Sono merged tra il 21 e il 25 novembre, tutte già dentro la RC. La prima è una barra dei modelli locali, separata dal pannello degli agenti, che compare solo su una macchina in grado di eseguire un modello e divide la RAM in scala tra sistema, modello e spazio libero, con etichette come «32 GB short». La seconda è il prompt della password di root: mostra l'icona dell'agente che ha chiesto, o la riga «Authorize Claude to run …». Tra gli agenti riconosciuti ci sono Claude, Codex, Copilot, Hermes. La terza fa passare le nuove installazioni UEFI da Limine a systemd-boot.

## La barra mostra il prezzo

`omarchy models use best` installa un modello di catalogo che sta nelle misure della macchina, dentro un container chiuso e senza rete. Il «senza rete» è nelle note ed è più rigoroso del solito: i modelli si possono condividere via tailnet, quindi l'isolamento vale per il processo che fa inferenza, non per la portata dell'agente. Due DGX Spark collegati con un cavo possono reggere un modello insieme; un `qwen3.8-27b-gufo` vuole circa 40 GiB su una macchina da 128, un Flash Next circa 100 con la finestra intera da 256K.

La barra rende visibile che «quale modello» lo decide l'hardware: l'inferenza esce dalle mani del fornitore, ma il catalogo è curato da altri e il modello che ci sta è un vincolo fisico.

## Il lucchetto adesso ha un nome

Il cambio sul prompt polkit vale più degli altri. La merge request lo dice con la frase che è anche il limite: «È un indizio, non una prova: qualunque cosa può chiamarsi claude». Se due richieste si contraddicono non mostra nessun agente, se la ricerca si impunta torna il lucchetto dopo un secondo. La PR è scritta con Claude Opus 5.5, DHH ha aggiunto due commit propri prima di unire, e il giorno prima la stessa shell aveva chiuso una falla sui manifest dei plugin che si spacciavano per first-party.

Un agente che chiede root è la prima cosa che rende la macchina una macchina amministrata da un agente, e il sistema comincia ad ammetterlo invece di nasconderlo dietro un lucchetto anonimo.

## Il boot passa per Microsoft

Systemd-boot arriva per una ragione dichiarata: «Secure Boot su hardware consumer di serie richiede uno shim firmato da Microsoft», e lo shim review accetta GRUB e systemd-boot come second stage, non Limine. Secure Boot però non è acceso da questa modifica: mancano lo shim di Omarchy, il kernel lockdown e la firma dei moduli. Chi ha già installato non riceve nessun invito, solo `omarchy-boot-switch`, a stadi reversibili. Gli snapshot presi prima del passaggio non si avviano più. E si perde velocità: 9,6 secondi contro 4,6 sull'installazione, misura dello stesso PR, con la promessa di scendere sotto i 5 dalla RC2.

Nello stesso rilascio: Chrome al posto di Chromium sulle nuove installazioni, Folio e Omaview al posto di Nautilus e mpv, e alcuni di questi pezzi scritti da `@omarchybot`, un agente che scrive il sistema su cui gireranno gli agenti.

## Cosa cambia per chi usa la macchina

La riduzione di zram a 8 GiB e lo swappiness a 1, con gli stalli peggiori da 162 a 17 millisecondi, confermano che il desktop è già tarato sul modello. DHH racconta di aver ottimizzato Omarchy per un tetto di 4 GB di RAM e di usare Neon come driver predefinito «per tutto ciò che riguarda il lavoro di sistema»; su X c'è già chi segnala venti raccoglitori di statistiche degli agenti che occupano dieci thread su dodici ogni quarto d'ora.

Per chi la installa: non è roba da macchina di lavoro in questa forma. La RC è dichiaratamente instabile e chi ha snapshot importanti dovrebbe aspettare la finale, perché il boot nuovo li rende non avviabili. Chi invece vuole sapere se il proprio portatile regge un modello locale ha adesso il modo più economico di scoprirlo.

## Il punto

La 4.6 sposta la catena di inferenza a casa e insieme mostra i manici nuovi: il catalogo lo sceglie il progetto, il boot lo firma Microsoft, l'icona del lucchetto la disegna chi chiede il permesso. Chi controlla la macchina non è più una questione astratta: da ieri è scritta in tre punti dell'interfaccia, e uno dei tre è un indizio, non una prova.

---
*Fonti verificate: github.com/omacom/omarchy/releases/tag/v4.6.0-rc1 (28/11/2026, pubblicata il 27/11: modelli locali, container senza rete, catalogo, DGX Spark, Chrome, zram, @omarchybot autore di PR); github.com/omacom/omarchy/pull/20103 (28/11/2026: prompt polkit, lista agenti, «it's a hint, not proof: anything can call itself claude», PR scritta con Claude Opus 5.5); github.com/omacom/omarchy/pull/19667 (28/11/2026: shim firmato Microsoft, systemd-boot, Secure Boot non attivo, snapshot precedenti non avviabili, 9,6 s contro 4,6 s); omarchycentral.com/news/omarchy-gives-local-ai-models-their-own-panel-with-a-memory-bar/ (28/11/2026: barra della memoria, «32 GB short», misure dei modelli, «Omarchy runs every model with no network access»); omarchycentral.com/news/omarchy-4-6-rc1-is-out-with-local-models-for-your-agents-chrome-by-default-and-a-live-try-mode/ (27/11/2026: quadro della RC, Chrome al posto di Chromium, nessuna data per la finale); aicrier.com/post/x4b590djl4k08s3gpgk4 (27/11/2026: isolamento letto come difesa da prompt injection, interpretazione); X, timeline di @dhh (28/11/2026: tetto di 4 GB, Neon come driver predefinito per il lavoro di sistema) e ricerca «Omarchy» (28/11/2026: i venti raccoglitori che saturano dieci thread su dodici).*
