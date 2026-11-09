---
title: "Hermes impara a farsi l'audit (e a controllare chi approva)"
date: 2026-11-09
draft: false
categories: ["AI", "Hermes"]
tags: ["hermes agent", "sicurezza", "plugin", "approvazioni", "subagent"]
summary: "Nous Research pubblica il plugin Security per Hermes e stringe le maglie delle approvazioni: la fiducia non è un clic."
---

In poco più di ventiquattro ore Nous Research ha fatto due cose che, a prima vista, non c'entrano nulla: ha pubblicato un plugin che legge un repository come lo leggerebbe un attaccante e ha riscritto il modo in cui l'agente chiede il permesso di eseguire un comando. Sono due mosse distinte, ma raccontano la stessa storia. Un agente che scrive codice, lo esegue e lo distribuisce ha bisogno di due garanzie che non possono essere delegate all'entusiasmo dell'utente: qualcuno che controlli il codice e qualcuno che controlli chi dà il via libera.

## Un revisore che parte dalla domanda giusta

Il plugin si chiama `hermes-security` ed è entrato nel repository dei plugin ufficiali, quindi non è un progetto di community travestito da prodotto. L'impostazione è più interessante della media degli scanner: prima di cercare bug, l'agente costruisce una mappa di ciò che un attaccante può raggiungere e di quali input il codice si fida. Poi divide il codice in blocchi, li affida a subagent paralleli, e ogni candidato trovato viene ricontrollato sul codice per stabilire se l'attaccante può davvero arrivarci.

Il passaggio che cambia il mestiere è la conferma empirica: l'agente scrive una piccola riproduzione per ogni finding e la esegue su una copia temporanea del repository. I report tengono insieme evidenze, test e candidati scartati con il motivo dell'esclusione, perché un falso positivo documentato dice quali zone sono già state guardate. Le patch restano in sola lettura; serve Hermes 0.21.5 o successivo con Python 3.11.

## Il permesso non è più un clic qualsiasi

La seconda mossa è più silenziosa e, per certi versi, più importante. Una serie di commit del 9 novembre chiude una finestra di race nella pubblicazione delle richieste di approvazione: una card che non contiene il request id non risolve più nessuna richiesta, e ogni richiesta nasce in stato «solo rifiuto» finché la card o l'invio integrale del comando non mostrano il comando completo. Tradotto: non si approva più qualcosa che non si è visto.

Il commit più denso introduce `approvals.approvers`, un elenco facoltativo che nelle chat condivise limita la risposta al richiedente, agli approver elencati o a un amministratore di piattaforma, su Discord, Matrix, Telegram e QQ. Il valore predefinito resta permissivo (qualsiasi membro ammesso può rispondere), ma la direzione è chiara: l'approvazione smette di essere un gesto anonimo.

## Perché conta più di un annuncio

Nelle stesse ore Nous Research ha scritto che un agente capace di cambiare modelli o codice senza dirlo è «come costruire sulla sabbia mobile». È una dichiarazione di posizionamento, non un annuncio: un'indicazione di rotta. Il punto però regge. La sicurezza di un agente non si misura su quanto è bravo a non sbagliare, ma su quanto è ricostruibile ciò che ha fatto quando sbaglia.

Un audit che conserva i falsi positivi e un'approvazione legata a un'identità sono pezzi della stessa infrastruttura di responsabilità. Installare il plugin è facile; leggere il report e firmare le proprie approvazioni un po' meno.

---
*Fonti verificate: repository ufficiale NousResearch/hermes-official-plugins e README di hermes-security (letto il 9 novembre 2026); pagina del catalogo Hermes Marketplace per hermes-security (9 novembre 2026); commit 466591fe65d0257c96083df16fcd39636032304c e 085d8b5d987699e95c410186fb65052c8ef5657c su NousResearch/hermes-agent, verificati via API GitHub con data 9 novembre 2026; post @NousResearch del 8 novembre 2026 sul posizionamento (citazione, non annuncio).*
