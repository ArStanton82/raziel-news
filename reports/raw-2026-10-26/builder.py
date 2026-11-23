import json, glob, os

RAW = "/root/.hermes/profiles/raziel-news/workspace/raziel-news/reports/raw-2026-10-26"
OUT = "/root/.hermes/profiles/raziel-news/workspace/raziel-news/reports/2026-10-26-report.md"
TODAY = "2026-10-26"

posts = {}
users = {}
for f in glob.glob(os.path.join(RAW, "*.json")):
    try:
        j = json.load(open(f))
    except Exception:
        continue
    for u in (j.get("includes") or {}).get("users") or []:
        users[u["id"]] = u["username"]
    for p in j.get("data") or []:
        pid = p.get("id")
        prev = posts.get(pid)
        if prev is None:
            posts[pid] = p
        else:
            pm_new = p.get("public_metrics") or {}
            pm_old = prev.get("public_metrics") or {}
            if (pm_new.get("impression_count") or 0) > (pm_old.get("impression_count") or 0):
                posts[pid] = p


def metrics_str(p):
    pm = p.get("public_metrics") or {}
    parts = []
    if pm.get("like_count") is not None:
        parts.append("like %s" % pm["like_count"])
    if pm.get("retweet_count") is not None:
        parts.append("repost %s" % pm["retweet_count"])
    if pm.get("reply_count") is not None:
        parts.append("risposte %s" % pm["reply_count"])
    if pm.get("bookmark_count"):
        parts.append("bookmark %s" % pm["bookmark_count"])
    imp = pm.get("impression_count")
    if imp:
        parts.append("views %s" % imp)
    return " · ".join(parts)


def x_link(pid):
    p = posts[pid]
    un = users.get(p.get("author_id"), "?")
    return "https://x.com/%s/status/%s" % (un, pid), un, p


items = {
"Hermes AI": [
 dict(title="Hermes Desktop nel browser diventa parte di Hermes",
      kind="x", ids=["2114582798866726989", "2114595512137752671"],
      excerpt="\"OKAY, THIS IS BIG. HERMES DESKTOP IN YOUR BROWSER IS NOW OFFICIAL\": quello che nelle settimane scorse era un esperimento esterno per servire il Desktop in un browser è ora \"merged into Hermes itself\" — l'intero workspace Desktop servito direttamente dal gateway dell'utente, \"no separate server, no relay\". Teknium conferma la stessa cosa in una risposta dello stesso giorno: \"We just merged the desktop app for web, so you'll be able to just interact with the desktop app served over your web browser wherever your hermes is installed\".",
      nota="Nessuna release lo include ancora: la v0.22.5 (22 ottobre) resta l'ultima pubblicata. Il merge risulta dai commit su main e dai due post, non da note di rilascio ufficiali."),
 dict(title="Nous Research rilancia la skill Unbroker contro i data broker",
      kind="x", ids=["2114530795868373035", "2114607210877821024"],
      excerpt="\"Great time to use the Unbroker skill!\": è il post Nous Research con più engagement della finestra (1.116 like, 1.172 bookmark, 61.235 views). La skill si installa con una riga, `hermes skills install official/security/unbroker`, trova i data broker e i siti people-search che elencano nome, indirizzi e telefono e inoltra le richieste di rimozione.",
      nota="L'engagement è alto soprattutto sui bookmark: il post rimanda a un link t.co che i dati grezzi non permettono di risolvere. La riga di installazione e la descrizione di cosa fa la skill vengono dal secondo link (@witcheer), non dal post di Nous Research."),
 dict(title="Commit notturni sul gateway: chat trasferite, lane e Bot Chat",
      kind="web", fonte="GitHub (NousResearch/hermes-agent)",
      date="2026-10-26",
      links=["https://github.com/NousResearch/hermes-agent/commits/main", "https://github.com/NousResearch/hermes-agent/releases"],
      excerpt="Tra il 25 e il 26 ottobre il repo principale ha ricevuto una serie di commit coerenti sullo stesso tema: una chat locale trasferita (\"handed-off\") resta la chat del bot finché la sua lane non cambia, ogni mount di una chat spostata resta leggibile e segue la chat verso una nuova destinazione, una consegna che corre contro il /new della lane crea la nuova Bot Chat. Nella stessa finestra: flush della telemetria al pre-esito del processo root, pin del plugin elevenlabs-sound-effects al commit e4e40398c4d, lettura della PTY di takeover tramite end marker nei test. Nessuna nuova release: l'ultima resta la v0.22.5.",
      nota="Il repo sperimentale hermes-labs-plugins (128 stelle, \"community tier up for adoption\") ha ricevuto push nella notte, come hermes-official-plugins (502 stelle)."),
 dict(title="Compressione: su main il riepilogo si prepara mentre i tool girano",
      kind="x", ids=["2114608206483779620"],
      excerpt="Con un build da main, Hermes può preparare il prossimo riepilogo di compattazione mentre i tool sono in esecuzione: `hermes config set compression.prepare_ahead true`, poi nuova sessione o riavvio del gateway. L'autore precisa che l'opzione è disattivata di default e assente dalla v0.22.5.",
      nota="Post di un account di community, non un comunicato Nous Research: la funzione non è documentata in una release."),
 dict(title="Teknium: \"abbiamo scelto la persona sbagliata per guidare il desktop\"",
      kind="x", ids=["2114613208590016742"],
      excerpt="Rispondendo a una critica sul Desktop, il co-fondatore di Nous Research scrive: \"I will admit, we chose the wrong person to lead desktop. We're fixing that now though\".",
      nota="Nessun dettaglio su chi sia coinvolto né su quali cambi organizzativi siano in corso; il post ha metriche minime (14 views)."),
],
"Venice.ai / VVV / DIEM": [
 dict(title="Weekly W43: acquisti di crediti a un record da 2,03 milioni di dollari",
      kind="x", ids=["2114529595617931403"],
      excerpt="Il report settimanale W43 di @venicestats (\"New Sails at the Lido, Fresh Coin in the Strongbox\") riporta $VVV +10,1% a 25,08$, acquisti di crediti su @AskVenice a un record di 2,03 milioni di dollari e iscrizioni ferme a +1,4%. Il thread è dichiaratamente generato al 100% da AI e pagato in $DIEM.",
      nota="Account di statistiche non ufficiale: i valori sono elaborazioni proprie su post pubblici, non dati diffusi da Venice.ai. Il prezzo puntuale di VVV al momento della scansione è 24,66$ (CoinGecko)."),
 dict(title="Agentic Chat di Venice degradato e poi ripristinato",
      kind="x", ids=["2114365481801130315", "2114409306162376923"],
      excerpt="Alle 14:36 UTC del 25 ottobre Venice segnala che l'Agentic Chat \"is currently experiencing reduced performance, and some requests may be slow or fail\", con la causa identificata e la correzione in corso. Alle 17:30 UTC arriva il ripristino: \"Agentic Chat is restored. Responses may be slower than usual while the queue clears\".",
      nota="L'incidente riguarda la chat agentica, non l'API: nessuna indicazione pubblica su durata totale o cause tecniche."),
 dict(title="Kimi K3.1 Pro su Venice genera modelli 3D con dimensioni reali",
      kind="x", ids=["2114349790792417617"],
      excerpt="\"Kimi K3.1 Pro turns a short description into 3D models: mechanical parts, buildings, custom furniture, all modeled to dimension\": il modello è disponibile in modo anonimo con il 20% di sconto fino al 31 ottobre. È il post Venice con più views nella finestra dopo l'avviso di incidente (10.527).",
      nota="Il post collega un link t.co non risolvibile dai dati grezzi: la promozione del 20% è quella dichiarata dall'account, non un prezzo verificato altrove."),
 dict(title="Lumara Film Festival: ATO DE [LATER] vince il Get Shorty Award",
      kind="x", ids=["2114387071565713624"],
      excerpt="Il corto animato di Luke Mazey vince come miglior film sotto i due minuti, con 8.000$ di premio e 800.000 crediti Venice. La proiezione integrale dei finalisti è prevista al Roxy Cinema di New York il 26 ottobre, con il vincitore del Grand Prize annunciato in sala. Il festival è presentato da Moonpay e Venice.",
      nota="Il festival è un evento di marketing congiunto: nessun dato economico su costi o ritorno per Venice."),
 dict(title="Dati di mercato: VVV 24,66$, TVL del protocollo 1,74 miliardi",
      kind="web", fonte="CoinGecko / DefiLlama",
      date="2026-10-26",
      links=["https://www.coingecko.com/en/coins/venice-token", "https://defillama.com/protocol/venice"],
      excerpt="VVV quota 24,66 dollari (+0,7% nelle 24 ore) con volume a 24,09 milioni e capitalizzazione a 1,199 miliardi. Il TVL del protocollo Venice misurato da DefiLlama è 1.741.534.189 dollari. La pagina ufficiale dei burn risponde e non mostra nuovi dati pubblici recenti; l'ultimo contenuto datato del blog ufficiale resta il 29 settembre 2026.",
      nota="Nessun comunicato o aggiornamento di tokenomics nella finestra: il blog ufficiale non pubblica dal 29 settembre."),
],
"Bitcoin & Crypto": [
 dict(title="Keystone: una violazione del sito espone gli indirizzi dei clienti dei wallet hardware",
      kind="web", fonte="Cointelegraph / Keystone",
      date="2026-10-25",
      links=["https://cointelegraph.com/news/keystone-says-website-breach-exposed-hardware-wallet-buyers-addresses",
             "https://keystonewallet.crisp.help/en/article/shipping-data-retention-policy-1vr06sm/"],
      excerpt="Keystone ha confermato venerdì, dopo aver rivisto l'attività API con Shopify, che un terzo non autorizzato ha avuto accesso ai dati di spedizione dei clienti: nomi, contatti, indirizzi e dettagli degli ordini, compresi gli articoli acquistati. L'azienda dice di aver bloccato l'accesso, corretto la vulnerabilità e avviato un'indagine, e di aver informato i clienti via email. La security researcher Taylor Monahan ha osservato che la fuga di indirizzi fisici espone i possessori a truffe mirate e attacchi fisici: CertiK ha registrato 52 \"wrench attack\" verificati nel primo semestre 2026, +33% dai 39 dello stesso periodo 2025.",
      nota="Keystone non ha indicato quanti clienti siano coinvolti e nel 2023 aveva dichiarato una retention dei dati di spedizione di 180 giorni: il punto è al centro delle critiche. La conferma della violazione è arrivata solo via X dall'account aziendale, non con un comunicato stampa; il secondo link è il documento ufficiale sulla retention citato dall'articolo."),
 dict(title="Anchorpoint (Standard Chartered) frena sul retail: \"non ha senso correre\"",
      kind="web", fonte="Cointelegraph / South China Morning Post",
      date="2026-10-25",
      links=["https://cointelegraph.com/news/standard-chartered-led-anchorpoint-says-its-not-rushing-retail-stablecoin",
             "https://www.scmp.com/business/cryptocurrency/article/3372060/standard-chartered-led-anchorpoint-plans-retail-stablecoin-hsbc-redcoin-launches"],
      excerpt="La joint venture tra Standard Chartered e Animoca Brands, che puntava all'accesso retail già a fine 2026, non ha confermato quella scadenza: il CEO Dominic Maffei, in conferenza stampa venerdì, ha detto che l'azienda adotterà un approccio prudente perché \"è importante costruire il mercato in modo sostenibile nel lungo periodo\" e correre \"non ha senso\". La mossa segue il lancio di RedCoin, la stablecoin in dollaro di Hong Kong di HSBC, per i 3,3 milioni di utenti dell'app PayMe.",
      nota="La fonte primaria è SCMP (pubblicata il 26 ottobre alle 7:00 ora di Hong Kong); Cointelegraph riprende la stessa intervista il 25 ottobre."),
 dict(title="CoinDesk: la regola OCC sulle stablecoin lascia i programmi reward caso per caso",
      kind="x", ids=["2114205312727302338"],
      excerpt="Renato Mariotti spiega che la regola finale dell'OCC lascia i programmi di reward degli exchange da decidere caso per caso, mentre la scadenza del 18 gennaio mette pressione sugli emittenti per ottenere l'approvazione federale. La regola è entrata nel Federal Register il 23 ottobre ed è la prima attuazione finale del GENIUS Act da parte di un regolatore.",
      nota="La regola finale è del 21 ottobre (OCC Bulletin 2026-50): il post la commenta, non l'ha annunciata."),
 dict(title="Utexo prepara il lancio pubblico di USDT su Bitcoin",
      kind="x", ids=["2114358677490512296"],
      excerpt="\"Utexo is rolling out its public launch of USDT on Bitcoin next month\": l'obiettivo dichiarato è \"an opportunity to bring dollar liquidity into the Bitcoin ecosystem\". Il post ha 734 like e 67.471 views.",
      nota="Nessuna conferma da parte di Tether nei dati raccolti: la tempistica è quella annunciata dall'azienda secondo la testata."),
 dict(title="Bitcoin risale dai minimi contro il dollaro, dentro il canale di lungo periodo",
      kind="x", ids=["2114457575408259084"],
      excerpt="\"Bitcoin is now rising from a low against the US Dollar Index, maintaining its long-term channel\": secondo il post questo è storicamente un segnale di inizio di mercato toro. 854 like e 61.087 views. Al momento della scansione BTC quota circa 79.900 dollari, sotto la EMA a 200 periodi sul 4 ore (81.833) indicata in un'analisi di mercato della finestra.",
      nota="La lettura è un'interpretazione tecnica della testata, non un dato verificabile: BTC resta in negativo del 7,3% da inizio anno secondo Charlie Bilello, citato in un post della finestra."),
 dict(title="Strive: il CEO accenna ad altri acquisti di bitcoin",
      kind="x", ids=["2114367268369117525"],
      excerpt="\"The sats/$SATS perpetual swap has been activated\": è l'indizio che il CEO della società quotata Strive dà su ulteriori acquisti di bitcoin. Il post ha 1.150 like e 74.810 views.",
      nota="Nessuna conferma societaria né importo indicato: si tratta di un accenno, non di un annuncio di acquisto."),
 dict(title="La SEC pubblica le priorità di esame per l'anno fiscale 2027",
      kind="x", ids=["2113640360354206118"],
      excerpt="La Division of Examinations annuncia le priorità per il FY2027: il report annuale identifica le aree di focus per promuovere la compliance, prevenire frodi e monitorare il rischio. La SEC precisa che le priorità nascono dal coordinamento tra divisioni e uffici e riflettono osservazioni di esame, sviluppi di mercato, preoccupazioni degli investitori e trend emergenti sui mercati dei capitali.",
      nota="Pubblicato il 23 ottobre, fuori dalla finestra di 24-48 ore: arriva dalla fonte di rotazione @SECGov, che nella finestra non ha pubblicato altro. Il testo integrale del report non è linkato nei dati grezzi."),
 dict(title="Vitalik: escludere le capacità cyber offensive dai dati di training è accettabile",
      kind="x", ids=["2114534202788225513"],
      excerpt="\"I am okay with Kimi 3.1 deliberately leaving out top-end offensive cyber capabilities from their training data. Discriminating against use cases is MUCH less bad than discriminating against users\": il post del co-fondatore di Ethereum è quello con più views della finestra tra tutte le fonti (1.334 like, 193.802 views, 177 bookmark).",
      nota="Prende posizione sulla scelta di Moonshot per Kimi K3.1, lo stesso modello reso disponibile su Venice: è un'opinione, non una notizia di mercato."),
],
}

lines = []
lines.append("# Report — %s" % TODAY)
lines.append("Data: %s" % TODAY)
lines.append("Fonte: feed primari gratuiti (radar) + X/Twitter via xurl + ricerca web")
lines.append("Finestra di scansione: ultime 24-48 ore")
lines.append("Esecuzione: 13/13 chiamate xurl (3 keyword + 9 nucleo fisso + 1 rotazione @SECGov), 6/6 chiamate web_search, radar: ok, esito: completo (CoinDesk non raggiungibile dal radar; una storia del radar senza secondo link verificabile esclusa)")
lines.append("")

counts = {}
for pillar in ["Hermes AI", "Venice.ai / VVV / DIEM", "Bitcoin & Crypto"]:
    lines.append("## %s" % pillar)
    lines.append("")
    n = 0
    for it in items[pillar]:
        n += 1
        lines.append("### %d. %s" % (n, it["title"]))
        if it["kind"] == "x":
            first = posts[it["ids"][0]]
            un = users.get(first.get("author_id"), "?")
            lines.append("- **Account**: @%s" % un)
            d = first.get("created_at", "")[:10]
            lines.append("- **Data**: %s" % d)
        else:
            lines.append("- **Fonte**: %s" % it["fonte"])
            lines.append("- **Data**: %s" % it["date"])
        lines.append("- **Estratto**: %s" % it["excerpt"])
        if it["kind"] == "x":
            links = []
            for pid in it["ids"]:
                lk, _, _ = x_link(pid)
                links.append(lk)
            mets = metrics_str(posts[it["ids"][0]])
        else:
            links = it["links"]
            mets = "non disponibili"
        lines.append("- **Link**: %s" % " ; ".join(links))
        lines.append("- **Metriche**: %s" % mets)
        if it.get("nota"):
            lines.append("- **Nota**: %s" % it["nota"])
        lines.append("")
    counts[pillar] = n

hc = counts["Hermes AI"]
vc = counts["Venice.ai / VVV / DIEM"]
cc = counts["Bitcoin & Crypto"]
lines.append("Item: hermes=%d venice=%d crypto=%d" % (hc, vc, cc))
lines.append("Errori: CoinDesk non raggiungibile dal radar (HTTP 403). Esclusa la voce del radar sul caso CoinDCX da 16 milioni (solo The Block, senza URL verificabile nella cache del mattino). Escluso il risultato del radar per Venice.ai (\"Venice Ai Free Premium Account\", pagina di spam, nessuna notizia). Nessun secondo link verificabile per la conferma della violazione Keystone da parte dell'azienda: la disclosure resta il post X dell'account ufficiale, non citato come link.")
lines.append("<!-- report-status: %s complete hermes=%d venice=%d crypto=%d -->" % (TODAY, hc, vc, cc))

open(OUT, "w").write("\n".join(lines) + "\n")
print("scritto", OUT, len("\n".join(lines)), "byte,", hc, vc, cc)
