---
title: "Il plugin che non c'era: Hermes 0.23.1 e il tetto di due megabyte"
date: 2026-11-10
draft: false
categories: ["Hermes", "AI"]
tags: ["hermes-agent", "plugin", "release", "nous-research"]
summary: "Il catalogo plugin di Hermes ha superato il limite di 2 MiB e le installazioni sono ricadute in silenzio sulla copia locale: la patch alza il tetto a 16."
---

Per poco più di un giorno, chi ha provato a installare un plugin appena pubblicato in Hermes Agent ha visto la stessa scena: il comando gira, restituisce un esito, e il plugin non c'è. Nessun errore, nessun avviso. Solo il catalogo vecchio, quello incluso nella release.

## Due megabyte di silenzio

La causa è piccola e istruttiva. Il catalogo dei plugin pubblicato sul sito il 9 novembre ha superato il tetto di 2 MiB che i client accettano: oltre quella soglia la risposta viene trattata come corrotta, il client scrive una riga nel log di debug e ricade sulla copia locale. Tre conseguenze, l'ultima delle quali è la più fastidiosa: i plugin nuovi non esistono su quella macchina, quelli ripinnati a commit più recenti si installano alla versione vecchia, e le voci di rimozione più recenti diventano invisibili, così un plugin formalmente ritirato continua a sembrare installabile. La patch v0.23.1, taggata alle 01:42 UTC del 10 novembre, alza il tetto a 16 MiB, circa novemila voci secondo il changelog. Chi resta su v0.23.0 o precedenti continua a usare il catalogo locale finché non aggiorna.

## Un patch release come censimento

La versione è dichiaratamente di stabilità, non di funzionalità, e serve anche a fotografare la finestra: circa 618 PR unite, 2.578 commit non-merge, 2.781 file cambiati, 409 issue chiuse. Le note curate arriveranno con la v0.24.0, e la scelta di non duplicarle qui dice qualcosa sul ritmo del progetto. In mezzo, quasi di sfuggita, alcune modifiche che cambiano l'uso quotidiano: il backtrack con Esc nella TUI, le group chat che girano su un gateway senza Desktop, il browser interno che si firma con il profilo del browser reale e riempie i login salvati dalla barra degli indirizzi, i nuovi hook del plugin API.

## La nuvola e i modelli

Sullo sfondo, due tasselli dello stesso disegno. Il 9 novembre Nous Research ha annunciato che gli agenti di Hermes Cloud si aprono in una scheda del browser con la stessa interfaccia di Desktop: si sceglie nome e modello su Nous Portal e l'agente gira in un container, raggiungibile dal telefono anche a computer spento; i piani Plus, Super e Ultra ne includono uno. Lo stesso giorno Claude Fable 5.2 è arrivato in Hermes via Nous Portal, OpenRouter e gli abbonamenti Claude, e su Venice a 8 e 40 dollari per milione di token, cioè al listino Anthropic del modello, con un milione di token di contesto.

La lezione di v0.23.1 non è tecnica, è di percezione: un sistema che degrada in silenzio sembra funzionare. Il fallback resta la scelta giusta, il silenzio no. Un aggiornamento e un'installazione di prova bastano a distinguere le due cose.

---
*Fonti verificate: release GitHub NousResearch/hermes-agent v0.23.1 (10 novembre 2026); Hermes Agent Changelog, hermes-agent-lab.com/releases/v0-23-1 (10 novembre 2026); Announcements di nousresearch.com su Hermes Cloud (9 novembre 2026); release notes Anthropic per Claude Fable 5.2 (9 novembre 2026); CNBC sul lancio di Fable 5.2 e Mythos 5.2 (9 novembre 2026).*
