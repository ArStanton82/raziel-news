---
title: "La firma, non il bottino: come Binance ha perso miliardi in quattro minuti"
date: 2026-10-29
draft: false
url: "/2026/10/la-firma-non-il-bottino-come-binance-ha-perso-miliardi-in-quattro-minuti/"
categories: ["Crypto", "Blockchain"]
tags: ["Binance", "EIP-7702", "hack", "Tether", "Circle"]
summary: "Un wallet caldo svuotato in una transazione da 0,93 dollari di commissioni. I miliardi sono il titolo, ma la domanda vera è una sola: chi ha firmato."
---

Ogni exchange, sotto la superficie, è un problema di firme. Giovedì 29 ottobre, alle 20:24 UTC, un wallet caldo di Binance — l'indirizzo che Etherscan etichetta «Binance 14» — ha trasferito 167.464 ETH e 63 token diversi, tra cui 1,615 miliardi di USDT, verso un indirizzo creato poche ore prima. Il costo per spostare quel patrimonio è stato di **0,93 dollari**.

Non è stato l'exploit di un contratto intelligente. Non c'è codice difettoso da correggere, non c'è una funzione da mettere in pausa. C'è una firma che qualcuno ha prodotto e non doveva poter produrre. Tutto il resto — i miliardi, i congelamenti, i comunicati — discende da lì.

## Quattro minuti, riga per riga

La ricostruzione viene dall'on-chain, ed è la parte su cui le fonti concordano anche quando i totali divergono.

- **28 e 29 ottobre.** Un wallet riceve tre depositi da circa 0,1 ETH ciascuno passando per Tornado Cash, un mixer. È il primo segnale: un exchange non paga le commissioni di transazione così.
- **15:59 UTC.** Quello stesso wallet pubblica un contratto delegato, preparato in mattinata.
- **20:20:59 UTC.** Invia un'autorizzazione **EIP-7702** sul wallet Binance 14, delegando il controllo del wallet al proprio contratto.
- **20:24 UTC.** Chiama quel contratto. Il wallet si svuota in una sola transazione: 167.464 ETH più i token, verso l'indirizzo `0x5227…2f8c`, che Etherscan ora marca come «Binance Hot Wallet Exploiter 2».
- **Pochi secondi dopo.** Il wallet Binance 16 manda altri 28.005,6 ETH allo stesso destinatario.
- **20:41 UTC.** Lo stesso delegate preleva 780 milioni di USDC da un altro wallet di Binance, poi altri 43 milioni.
- **21:01 UTC.** Tether blacklista l'indirizzo ricevente: 975,1 milioni di USDT diventano immobili.
- **21:04 UTC.** Circle congela 823 milioni di USDC. Allaire parla di oltre 800 milioni, «in coordinamento con le forze dell'ordine».
- **21:15 UTC.** CZ scrive che «sembra un hack» e ringrazia i due emittenti. Alle 22:23 aggiunge che la perdita «potrebbe essere un po' più alta» delle stime circolanti, ma che sarà coperta.
- **21:29 UTC.** Binance aggiorna il comunicato: «i fondi degli utenti sono completamente al sicuro». Non ha mai usato la parola hack.

## Perché EIP-7702 sposta la domanda

EIP-7702 è attivo su Ethereum dal 7 maggio 2025, con l'upgrade Pectra. Permette a un wallet normale di delegare il proprio controllo a un contratto: serve a raggruppare più trasferimenti in un'unica operazione, ed è per questo che gli exchange lo usano per distribuire fondi in modo efficiente.

La caratteristica che conta è un'altra, e l'ha spiegata Odysseas Lamtzidi di Phylax Systems: la delega **persiste**. Il codice installato può autorizzare trasferimenti successivi senza bisogno di un'altra firma del wallet. Non è una password rubata che si cambia: è un binario che resta aperto finché qualcuno non lo revoca.

E la delega, per esistere, richiede una firma con la chiave privata del wallet. L'attaccante ce l'aveva. Questo è il fatto, ed è l'unico che conti davvero: il perimetro dell'incidente non è il wallet, è chi firma per il wallet. Chiave in chiaro su una macchina connessa, infrastruttura di firma compromessa, accesso interno — nessuna delle ipotesi è confermata, e finché Binance non pubblica la catena di custodia delle proprie chiavi, la differenza tra queste ipotesi resta la differenza tra un errore di configurazione e un problema di insider.

## Il conto che ancora non torna

I totali pubblicati divergono, e non per imprecisione giornalistica: misurano cose diverse.

| Misura | Valore | Cosa significa |
|---|---|---|
| Ethereum, tre wallet | ~3,5 miliardi | conteggio di Unchained sui trasferimenti in uscita |
| Tre catene | ~5,57 miliardi | stima aggregata: 3,51 Ethereum, 18.270 BTC, 0,63 su Tron |
| Congelato | 1,8-2,4 miliardi | 975,1 mln USDT in un wallet, 823 mln USDC; Tether rivendica oltre 1,567 mld complessivi |
| Fuori dai congelamenti | ~3,8 miliardi | Bitcoin ed ETH non sono congelabili da nessun emittente |

Da qui nasce il numero che circola da ieri sera. Il fondatore di DefiLlama, 0xngmi, ha scritto che con USDT e USDC congelati la perdita si aggira intorno al miliardo, lo 0,69% dei 144 miliardi di asset in custodia di Binance, e che l'exchange la coprirà dal bilancio senza difficoltà. CZ ha risposto citandolo: «Loss might be a bit higher than that, but will cover». Potrebbe essere un po' più alta, ma la copriamo.

Il ragionamento sulla solvibilità è solido. Il numero però descrive una **perdita netta**, non il furto: se il conteggio a tre catene regge, il buco non coperto è nell'ordine dei 3-4 miliardi, non di uno. Confondere le due voci è l'errore che in questi casi costa più caro, perché la prima dice se l'exchange sta in piedi, la seconda dice quanto è stato perso.

C'è anche un dettaglio contabile che nessuno ha ancora chiarito: un token congelato non è un token recuperato. Resta dove sta, inutilizzabile dall'attaccante, finché Tether o Circle non decidono — di norma con l'autorità giudiziaria — se bruciarlo e riemetterlo a favore del danneggiato. Fino a quel momento, il congelamento protegge il mercato dai movimenti, non ricostituisce le riserve.

## Il mercato non ha aspettato la contabilità

Nell'ora successiva il Bitcoin è scivolato da 80.327 a 78.763 dollari, sotto quota 79 mila, con circa 628 milioni di posizioni a leva liquidate. BNB ha perso tra il 6 e il 7 per cento, scendendo intorno ai 699 dollari. Nessuno dei due movimenti racconta un default: raccontano che il mercato, davanti a un wallet caldo che si svuota, prezza la possibilità che il problema sia più grande di quello che si vede.

## Cosa resta da verificare

Cinque domande sono aperte, e vanno tenute separate dai fatti on-chain.

1. **Come è stata ottenuta la firma.** È la domanda che determina tutto il resto: compromissione di una chiave, di un firmatario, o di un processo.
2. **Se i deflussi su Bitcoin e su Tron appartengono allo stesso attaccante.** Il conteggio a 5,57 miliardi si basa su un'etichettatura di wallet che Binance non ha confermato.
3. **Se Binance pubblicherà una prova delle riserve** o una ricostruzione tecnica. Finora ha comunicato due volte, senza dettagli e senza la parola hack.
4. **Che fine faranno i fondi congelati**, e con quali tempi.
5. **Quali altri exchange usano la stessa architettura di firma.** EIP-7702 non è un difetto di Binance, è uno standard: chiunque deleghi un wallet caldo a un contratto ha lo stesso perimetro di attacco, e nessuno ha ancora pubblicato i propri controlli.

Un exchange non è un caveau. È una macchina che firma, esposta a internet, e il suo rischio non si misura in quanto custodisce ma in quante persone e quante macchine possono produrre una firma valida per conto suo. La commissione di 0,93 dollari per spostare due miliardi e mezzo è il prezzo di listino di quell'architettura: quasi zero, e questa è esattamente la parte del problema che nessun congelamento risolve.

---
*Fonti verificate: CryptoTicker, «Binance Hack: $2.8B Drained From Hot Wallet via EIP-7702», 29 ottobre 2026; Unchained, «Binance Says User Funds Are 'Completely Safe' After $3.5 Billion Drains From Its Hot Wallets», 29 ottobre 2026; Decrypt, «Binance Drained of $5.5 Billion in Suspected Hack, Tether and Circle Freeze $1.8 Billion», 29 ottobre 2026; post di @binance (21:29 UTC), @cz_binance (21:15 e 22:23 UTC), @0xngmi, @paoloardoino, @jerallaire, @spreekaway, @odysseas_eth e @WazzCrypto del 29 ottobre 2026, letti via API; EIP-7702, specifica su eips.ethereum.org. Tutte le fonti consultate il 29 ottobre 2026.*
