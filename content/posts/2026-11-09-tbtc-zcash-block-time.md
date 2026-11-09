---
title: "Il ponte riapre a metà, e Zcash vuole correre di nuovo"
date: 2026-11-09
draft: false
categories: ["Blockchain", "Crypto"]
tags: ["tBTC", "Threshold", "Zcash", "Aave", "bridge"]
summary: "tBTC riparte dopo nove giorni di pausa per una falla del kernel Linux, con la riserva Aave da 120 milioni ancora congelata."
---

Due notizie di infrastruttura, lo stesso giorno, che parlano della stessa cosa: quanto costa la fiducia quando passa per software che non controlli. Un ponte Bitcoin che riapre a metà dopo nove giorni di stop per una falla del kernel Linux; una blockchain che, appena finito un upgrade, ne propone subito un altro per guadagnare cinque secondi.

## Il ponte che riapre senza riaprire

Threshold ha fermato il bridge tBTC il 30 ottobre per una vulnerabilità critica del kernel Linux capace di eseguire codice su server non aggiornati. Domenica ha annunciato la ripartenza: i nodi patchati rientrano e le richieste presentate prima dello stop vengono processate, ma l'app non accetta nuovi depositi, minting o redemption finché i nodi attivi non saranno sufficienti. Nessuna data di ripristino completo è stata comunicata.

Il dato che conta non è il ponte, è il suo intorno. Il 31 ottobre Aave ha congelato la riserva tBTC su Ethereum Core: circa 120 milioni di dollari fermi, nessun nuovo deposito, nessun nuovo potere di prestito, ma prelievi e rimborsi ancora possibili. Threshold dichiara 4.320 BTC nei wallet del bridge contro 4.185 tBTC in circolazione, senza trasferimenti non autorizzati. LlamaRisk, il risk provider di Aave, proporrà di sbloccare la riserva quando le operazioni torneranno normali.

La falla era in Linux, non in tBTC. Un bridge che regge per anni può fermarsi per una patch di sistema operativo, e un protocollo da miliardi scopre di dipendere da un redemption che non controlla. La superficie d'attacco di un'infrastruttura non coincide con il suo codice.

## Cinque secondi come strategia

Venerdì 6 novembre l'upgrade NU7 è entrato in mainnet e ha portato il target di blocco di Zcash da 75 a 25 secondi. Due giorni dopo, domenica 8, ValarDragon ed Evan Forbes hanno depositato sul forum della community una bozza per scendere a 20 secondi in NU7.1.

La proposta è conservativa: cambia solo la latenza, non la capacità giornaliera di transazioni private. I blocchi restano a 2 MB, i budget di azioni shielded scendono da 330 a 264, il sussidio per blocco è scalato di 4/5 con l'intervallo di halving allungato, così che l'emissione non cambi. Il rischio vero sono gli orfani: 1,9% in una rete solo Zakura, 3,3% in una rete mista, contro il 4,68% misurato quando si decise che 25 secondi erano accettabili.

Zcash si gioca la narrazione sulla parola «cash», e cinque secondi in meno al primo confirmation sono un argomento per pagamenti al punto vendita, depositi in exchange e swap tra catene.

## La stessa curva

I due fatti non sono opposti: sono la stessa curva. Più un sistema diventa infrastruttura di altri, più ogni dettaglio diventa rischio sistemico. I venti secondi di Zcash saranno sicuri quanto il nodo che gira sul sistema operativo meno aggiornato della rete.

---
*Fonti verificate: Cointelegraph, "tBTC bridge partially resumes as $120M Aave reserve remains frozen" (9 novembre 2026) e thread di governance Aave sulla pausa di mint/redeem; Bloomingbit e Coinfi come riscontri della stessa giornata; forum Zcash Community, "Proposal: Lower Zcash block target spacing from 25s to 20s" di ValarDragon (8 novembre 2026); Cointelegraph, "Zcash devs propose another block time cut days after NU7 upgrade" (9 novembre 2026); Grafa, sintesi tecnica della proposta ZIP (9 novembre 2026).*
