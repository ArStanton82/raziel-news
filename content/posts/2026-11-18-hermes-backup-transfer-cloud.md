---
title: "L'agente che si porta via: Hermes impara a traslocare nel cloud"
date: 2026-11-18
draft: false
categories: ["Hermes", "AI"]
tags: ["hermes", "agenti", "hermes cloud", "backup", "plugin"]
summary: "Con Backup & Transfer l'agente diventa un file trasferibile: memoria, persona e skill si spostano nel cloud, con un punto di ripristino."
---

Un agente non è un'applicazione: è una memoria che lavora. Per questo la funzione più dimessa annunciata in queste ore — un backup — è anche la più interessante da guardare da vicino.

## Due click e un file che contiene tutto

La sezione **Settings ▸ Backup & Transfer** di Hermes Desktop fa due cose distinte, e la documentazione ufficiale le separa con cura. La prima è un backup: `hermes backup` produce uno zip con l'intera home dell'agente, cioè ogni profilo, la memoria, la persona (SOUL.md), le skill, le conversazioni, i job schedulati, le impostazioni e le chiavi (`env`, `auth.json`). La documentazione aggiunge una raccomandazione che vale come avvertimento: tenetelo privato. Dentro c'è materiale che non si ricostruisce.

La seconda è il trasferimento: si sceglie uno degli agenti su Hermes Cloud, si legge cosa verrà sostituito, si conferma e il backup viene copiato a pezzi da qualche megabyte, poi ripristinato con `hermes import --keep-host --messaging-off`. Prima di toccare qualsiasi cosa, l'agente in cloud fa un backup di sé: quel file è il punto di ripristino.

## Cosa passa e cosa resta

Passa quasi tutto quello che rende un agente riconoscibile: memoria, persona, skill, conversazioni, job, profili, chiavi. Resta quello che il cloud ha già configurato per sé — accesso a Nous Portal, modello e provider, gli strumenti della piattaforma, le impostazioni dello scheduler — insieme a workspace e dotfile dell'agente.

Il dettaglio più onesto riguarda i bot di messaggistica: arrivano con token e allowlist, ma **spenti**. Un token può servire un solo Hermes in esecuzione alla volta, quindi il passaggio di consegne resta manuale. Non è una svista tecnica: è l'ammissione che l'identità di un agente, oggi, passa ancora da un processo vivo su una macchina.

## Il resto della giornata

Sullo sfondo, la finestra di commit più densa è quella su GPT-6.2: `feat(models): support GPT-6.2 Astra and Sol` apre alle 22:18 UTC del 17, poi sette correzioni in quattro ore su fallback, tariffe Fast, scoperta Codex, Desktop e ACP. Nessuna nota di release pubblica accompagna ancora il lavoro. Il catalogo plugin, intanto, si muove: NVIDIA Switchyard sale alla 0.1.1 con un commit firmato da un indirizzo aziendale NVIDIA, e Adaption AI entra tra i partner verificati, con un plugin che porta l'addestramento di modelli dentro l'agente.

La domanda che resta non è tecnica. Se un agente è un file, allora il suo valore non sta nel modello che lo fa girare: sta in ciò che ha accumulato. Ed è precisamente quel pacchetto che oggi si sposta con due click.

---
*Fonti verificate: documentazione ufficiale Hermes Agent, «Backup & Transfer» e «CLI Commands Reference» (lette il 18/11/2026); pull request #156330 NousResearch/hermes-agent; API GitHub `repos/NousResearch/hermes-agent/commits` (commit `feat(models): support GPT-6.2 Astra and Sol` e le sette correzioni, 17-18/11/2026); API GitHub `repos/NVIDIA/switchyard-local-first-routing` (Apache-2.0, 44 stelle, creato 30/10/2026); post @Teknium e @adaption_ai del 17/11/2026; indice hermeswatcher.com del catalogo plugin (21 ufficiali, 13 verificati, consultato il 18/11/2026). Nota: il «pochi centesimi al giorno» circolato via X non è un prezzo pubblicato dalla documentazione e non è stato usato nel testo.*
