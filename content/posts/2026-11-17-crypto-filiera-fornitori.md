---
title: "Non hanno bucato Trezor né la BBC: hanno bucato i loro fornitori"
date: 2026-11-17
draft: false
categories: ["Crypto", "Blockchain"]
tags: ["sicurezza", "supply chain", "Ledger", "Trezor", "Optimizely", "malware"]
summary: "In 24 ore due attacchi passati da terze parti: script infetti su 178 siti e 27mila ordini Trezor esposti. Il perimetro è la filiera"
---

Due notizie di sicurezza in ventiquattro ore che sembrano separate e raccontano la stessa cosa: uno script compromesso ha veicolato un malware che ruba criptovalute e carte di credito su 178 organizzazioni, tra cui Ledger, BBC, CNN e Salesforce; Trezor ha comunicato che un corriere ha perso i dati di circa 27.000 ordini. In nessuno dei due casi l'attacco è partito dall'azienda che compare nel titolo.

## Centottantotto file, un solo vettore

L'analisi di Report URI è dettagliata: il 16 novembre, tramite la piattaforma di test Optimizely Web, è stato servito JavaScript malevolo ai visitatori di 178 organizzazioni. Ogni cliente carica da `cdn.optimizely.com` uno snippet con il proprio codice di esperimenti e un campo di JavaScript personalizzato; l'attaccante ha scritto il proprio codice lì dentro, lasciando intatto il resto del file, che continuava ad arrivare dal dominio fidato. Dei 1.611 snippet controllati, 188 risultano infetti, e il payload è stato ricostruito ventisei volte in un giorno.

Il malware sostituiva gli indirizzi dei wallet — Bitcoin, Ethereum, Tron, Solana, Ton, Litecoin, Bitcoin Cash, Dogecoin — validando i checksum, anche al momento della copia negli appunti; intercettava i dati delle carte inseriti nei form del sito, non quelli dentro gli iframe dei provider di pagamento; rubava cookie e screenshot. Su iPhone e iPad caricava una seconda fase legata ai kit di exploit Coruna e DarkSword.

Optimizely ha confermato lo sfruttamento di una vulnerabilità nella procedura di iscrizione agli account di Experimentation e di aver bloccato il percorso, revocato token e sessioni e fermato la consegna via Cloudflare. Come l'attaccante abbia ottenuto quell'accesso resta non chiarito.

## Quanto è stato rubato, con cautela

Qui i numeri divergono. Report URI contava 7.040 dollari arrivati ai wallet alle 19:25 UTC; StepSecurity stima 6.600 dollari; Alex Thorn di Galaxy Digital calcola che le vittime abbiano inviato 2.300 dollari, perché buona parte dei bitcoin in entrata erano fondi dell'attaccante. L'ordine di grandezza resta di poche migliaia di dollari: il danno vero, se c'è stato, è fatto di carte e cookie che non lasciano traccia on-chain.

## La terza volta per Trezor

Il secondo caso è più lento e più insidioso. Skladon, corriere che spedisce per Trezor, ha subito una violazione il 7 novembre e ha informato l'azienda il 15: circa 27.000 ordini coinvolti, tra il 9 agosto e il 7 novembre, con nomi, telefoni, indirizzi, email, prodotti e prezzi. Nessun backup di wallet, nessun PIN. Trezor ha attivato il ritiro anonimo in 18 paesi europei e riduce la conservazione dei dati d'ordine da 90 a 45 giorni. È la terza violazione di un fornitore in un anno, dopo ShipMonk ad agosto e Brevo a settembre.

## Il perimetro è la filiera

La lezione è scomoda: nessuna difesa perimetrale copre un marcatore di terze parti o un corriere. Per chi possiede cripto un registro di spedizione trapelato fa più danni di quanto sembri, perché collega una persona, un indirizzo e il fatto che possieda cripto. La sicurezza si è spostata dal proteggere i propri server al verificare ogni anello della catena, compresi quelli che non si controllano.

---
*Fonti verificate: blog.report-uri.com, «World's Largest Brands Infected With Malware Via Optimizely» (16/11/2026, cronologia e conteggi); stepsecurity.io, «OPTIMJACK» (17/11/2026, analisi indipendente e stima dei fondi); Cointelegraph, «Hackers inject credit card, crypto-stealing malware into 178 major websites» (17/11/2026, con la dichiarazione di Optimizely e la stima di Alex Thorn); trezor.io/blog, «Data breach at Trezor shipping partner, Skladon» (15/11/2026, fonte primaria con i dati esposti); Cointelegraph, «Trezor customer data exposed in 3rd partner breach this year» (17/11/2026). Le stime sull'ammontare sottratto sono riportate separatamente perché non coincidono. Non pubblicata la voce CFTC/Backpack-tZERO del report: resta a una sola fonte, senza comunicato corrispondente sul sito dell'agenzia.*
