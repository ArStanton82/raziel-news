---
title: "Il plugin come interfaccia: l'ecosistema Hermes cresce ai margini del core"
date: 2026-10-14
draft: false
categories: ["Hermes", "AI"]
tags: ["hermes-agent", "plugin", "nous-research", "sprites", "release"]
summary: "Hermes Agent v0.21.7 consolida il core, mentre catalogo ufficiale e plugin comunitari diventano il vero terreno di crescita."
---

Mentre il core di Hermes Agent entra in una fase di consolidamento, la parte più interessante del progetto si sta spostando ai margini: nei plugin. È lì che si vede dove va un agente che vuole essere una piattaforma e non soltanto un programma.

## Un core che si ferma a rifinire

Il tag stabile v0.21.7, pubblicato l'11 ottobre e diffuso il 12, è un rilascio di manutenzione: raccoglie circa 204 pull request accumulate da v0.21.6 e non introduce funzionalità di rilievo. Le novità sono di carattere operativo, e vale la pena notarle perché raccontano un prodotto che inizia a pensare a chi lo installa: gli aggiornamenti da sorgente ora seguono le release etichettate invece di ogni commit su main, l'app desktop guadagna un interruttore per scegliere il canale di aggiornamento, il ragionamento firmato sopravvive alla ripresa di una sessione e gli aggiornamenti non falliscono più dietro alcuni firewall regionali. Sono dettagli. Sono anche il segno che il progetto ha smesso di dover dimostrare di esistere.

## Plugin ufficiali e sandbox remoti

Il movimento vero è nel catalogo. Il repository hermes-official-plugins raccoglie i plugin first-party — Home Assistant, Spotify, Claude Subscription DirectSDK, blender, langfuse, snyk e altri — installabili con una riga dal catalogo dei plugin, e ha superato le 270 stelle. Accanto a questo compare hermes-plugin-sprites, che registra un backend terminale basato su sandbox cloud stateful di Fly.io, con checkpoint e restore, costruito sull'estensione del backend terminale senza toccare il core. Il repository principale, intanto, risulta aggiornato al 14 ottobre con circa 254.000 stelle e 55.000 fork: numeri che dicono più sulla visibilità del progetto che sulla sua maturità.

## La coda lunga della community

Sotto i plugin ufficiali cresce una coda lunga di strumenti comunitari. Tra questi Hermes Activity, una dashboard di utilizzo in sola lettura con griglia di contribuzione in stile GitHub, scomposizione dei token per modello e riepilogo di strumenti e skill. È un plugin di terze parti, non un prodotto Nous Research, e va letto come tale: segnala un bisogno reale — capire quanto e come un agente consuma — che il core non copre ancora.

Restano invece non verificate le voci circolate su X in queste ore, come un presunto Hermes Agent ospitato da Tencent per Telegram, WhatsApp e Discord, o un plugin capace di pilotare le app del telefono. Nessuna fonte ufficiale Nous Research le conferma, e vanno trattate come rumore di fondo.

La domanda che resta aperta è se questa architettura a estensioni reggerà alla scala. Un core stabile e margini vivaci è un buon modello; un core stabile e margini frammentati è un problema di governance. Per ora Hermes sta scegliendo la prima strada.

---
*Fonti verificate: GitHub NousResearch/hermes-agent releases e org repositories (consultati il 2026-10-14); GitHub NousResearch/hermes-official-plugins (272 stelle, consultato il 2026-10-14); GitHub NousResearch/hermes-plugin-sprites (consultato il 2026-10-14); releasebot.io/updates/nousresearch/hermes-agent e releases.sh/nousresearch/hermes-agent (v0.21.7, consultati il 2026-10-14); GitHub topics token-usage, repo hassan-kamel/hermes-activity (plugin comunitario, consultato il 2026-10-14).*
