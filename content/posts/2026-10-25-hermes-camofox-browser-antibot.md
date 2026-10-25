---
title: "Hermes impara a non sembrare un bot, e lascia la password nella snapshot"
date: 2026-10-25
draft: false
categories: ["Hermes", "AI"]
tags: ["hermes-agent", "camofox", "browser", "sicurezza", "plugin"]
summary: "Il plugin camofox dà a Hermes un Firefox con fingerprint falsificato, locale e senza cloud. Il conto si paga in trasparenza."
---

Camofox non è il browser di Nous Research: è un plugin ufficiale del catalogo Hermes che avvolge Camoufox, un fork di Firefox con spoofing del fingerprint scritto in C++, dietro un server Node che gira sulla macchina dell'utente. La distinzione conta, perché il post che ha diffuso la notizia parlava di un browser «proprio»: il fork non è di Nous. Quello che c'è è più interessante. Hermes, che finora si presentava ai siti come un client automatizzato, adesso può presentarsi come un Firefox qualunque — e il modo in cui lo fa dice dove si sta spostando il confine tra navigare e fingersi qualcun altro.

## Un Firefox che non dichiara di essere un agente

L'architettura è volutamente umile. Il plugin non scarica né avvia niente: il server va lanciato a mano su `localhost:9377`, con Node o con l'immagine Docker, e Hermes lo pilota via REST. Nessuna dipendenza dal cloud: il traffico resta sulla macchina di chi lo usa. Il plugin registra undici strumenti e aggiunge l'importazione dei cookie da un file `cookies.txt`, disponibile solo con una chiave API, con un tetto di cinque megabyte e cinquecento cookie.

Per impostazione predefinita ogni sessione riceve un'identità casuale, quindi login e cookie non sopravvivono a un riavvio; chi vuole persistenza la attiva, e allora Camofox scrive il profilo su disco solo a un checkpoint esplicito o a uno spegnimento pulito. Chiudere Node di forza butta via i login mai salvati.

## Il prezzo si paga in trasparenza

Un browser che nasconde la propria identità, per definizione, nasconde anche a chi lo possiede. La documentazione del plugin è insolitamente onesta: il deposito delle credenziali di Hermes non raggiunge la scheda Camofox, quindi le credenziali vanno digitate nel browser. E Camoufox stampa il valore di ogni campo compilato, password compresa, senza segnalare nella snapshot quale campo sia un campo password. La password finisce così nel testo della snapshot e nel risultato della navigazione, cioè nella cronologia della conversazione. Il resto del perimetro è più solido: le URL che contengono segreti, gli endpoint di metadati cloud e i domini della blocklist vengono rifiutati.

## Perché serve, e a chi conviene

I muri anti-bot hanno trasformato la navigazione automatica in un problema tecnico e politico insieme: un agente che legge un sito commerciale viene trattato come un intruso, e la risposta più semplice è sembrare un utente. È una corsa agli armamenti in cui nessuno dei due lati ha interesse a dichiarare quanto è avanti l'altro.

Il contesto è la release v0.22.5 del 23 ottobre: circa 81 pull request unite dal tag precedente, 231 commit non di merge su 804 file, trenta issue chiuse, con le note curate rinviate alla 0.23.0.

La domanda non è se un agente debba sembrare umano. È chi paga il conto quando ci riesce: il sito che riceve traffico indistinguibile da quello di una persona, o l'utente che credeva di aver messo la password in una cassaforte e l'ha ritrovata in una snapshot.

---
*Fonti verificate: pagina del plugin camofox nel catalogo ufficiale Hermes Agent, hermes-agent.nousresearch.com/docs/plugins/camofox, consultata il 25/10/2026 (server Node self-hosted, Camoufox come fork di Firefox con spoofing C++, undici strumenti, CAMOFOX_URL su porta 9377, import cookie con limiti 5 MB e 500 cookie, assenza di copertura del vault sulle schede Camofox, valori dei campi compilati — password inclusa — stampati nelle snapshot, blocco di URL con segreti e metadati cloud); codice `tools/browser_camofox.py` nel repository NousResearch/hermes-agent, commit eb75627f (backend REST, URL predefinito localhost:9377); GitHub, release v0.22.5, github.com/NousResearch/hermes-agent/releases, pubblicata il 23/10/2026 (81 PR unite, 231 commit non di merge, 804 file, +35.212/−17.885, 30 issue chiuse, note curate con la v0.23.0). Discrepanze annotate: il report di Echo descrive Camofox come «un proprio browser» rilasciato da Hermes e cita un «plugin ufficiale Nous Research»; le fonti primarie indicano un plugin ufficiale che avvolge il server camofox-browser di jo-inc e il fork Camoufox, non un browser sviluppato da Nous, e segnalano che il codice viveva prima nel core. La descrizione tecnica del post X di @HermesWatcher non è stata usata come fonte: il link t.co non è risolvibile dai dati grezzi. Escluso per assenza di seconda fonte l'avviso di @NousResearch del 25/10 sui progetti terzi che usano il marchio Hermes.*
