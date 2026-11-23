import json, glob, os

T = "2026-10-24"
RAW = "reports/raw-2026-10-24"

posts = {}
users = {}
for f in glob.glob(os.path.join(RAW, "*.json")):
    d = json.load(open(f))
    for u in (d.get("includes") or {}).get("users", []) or []:
        users[u["id"]] = u.get("username")
    for p in d.get("data", []) or []:
        posts.setdefault(p["id"], p)


def fmt(n):
    if n is None:
        return "n/d"
    return f"{n:,}".replace(",", ".")


def post(pid):
    p = posts[pid]
    return p, users.get(p["author_id"])


def metrics(p):
    m = p.get("public_metrics") or {}
    out = [f"like={fmt(m.get('like_count'))}", f"repost={fmt(m.get('retweet_count'))}",
           f"risposte={fmt(m.get('reply_count'))}"]
    if m.get("impression_count"):
        out.append(f"view={fmt(m.get('impression_count'))}")
    return " · ".join(out)


def xlink(pid):
    p, u = post(pid)
    return f"https://x.com/{u}/status/{pid}"


def xitem(title, pid, extra_ids, excerpt, note=None, acct=None):
    p, u = post(pid)
    links = [xlink(pid)] + [xlink(i) for i in extra_ids]
    return {
        "title": title,
        "kind": "x",
        "account": f"@{acct or u}",
        "date": p["created_at"][:10],
        "excerpt": excerpt,
        "links": links,
        "metrics": metrics(p),
        "note": note,
    }


def witem(title, source, date, excerpt, links, note=None):
    return {
        "title": title, "kind": "web", "source": source, "date": date,
        "excerpt": excerpt, "links": links, "metrics": "non disponibili", "note": note,
    }


CC = "https://cointelegraph.com"
BLOCK = "https://www.theblock.co"

hermes = [
    witem("Hermes Agent v0.22.5: patch release con ~81 PR e backend di delegation sostituibili",
          "GitHub · NousResearch/hermes-agent", "2026-10-22",
          "\u00abPatch release. This tag rolls up the ~81 PRs merged since v0.22.4 into a stable release for the GitHub release (CLI and installers), the Microsoft Store app, Docker and Hermes Cloud.\u00bb Nella finestra: 231 commit non-merge su 804 file (+35.212/\u221217.885), 81 PR unite e 30 issue chiuse. Tra le novit\u00e0 citate: delegation backend sostituibili (subagent instradati per model map o profilo, cambiabili per sessione), `hermes import-agent`, migrazione da OpenClaw, `hermes mcp serve` e backend Singularity spostati dal core ai plugin, sign-in Nous rifatto come device login. Le note curate complete arriveranno con v0.23.0.",
          [f"https://github.com/NousResearch/hermes-agent/releases/tag/v0.22.5",
           "https://github.com/NousResearch/hermes-agent/releases"],
          "Fonte primaria (repository ufficiale): il tag \u00e8 stato pubblicato il 23/10 alle 05:28 UTC con data di release 22/10. Nelle 24 ore successive il radar registra altri commit su MCP (masking degli argomenti a forma di segreto, trust prompt) e push su hermes-official-plugins (\u2605421) e hermes-labs-plugins (\u2605107); il repo hermes-agent risulta a \u2605256.582."),

    xitem("Il plugin trycua Spaces d\u00e0 a Hermes un computer che il team pu\u00f2 guardare e pilotare",
          "2113391397760041329", [],
          "\u00abYour team and your Hermes can now share a computer. The new @trycua Spaces plugin gives Hermes its own Linux, macOS, or Windows Space on hardware you already own. Anyone on your team can open it, watch live, step in, and hand it back while Hermes keeps working.\u00bb",
          "Lo stesso annuncio compare nella pagina Announcements di nousresearch.com, datata 22-23/10."),

    xitem("Plugin ufficiale Meshy: modelli 3D in chat e un mese di Pro a 1$",
          "2113375941431009526", [],
          "\u00abMeshy is offering Hermes users a month of Pro, which includes API access and 1,000 credits, for $1. After you subscribe and install the plugin, create a key at meshy.ai/developers/keys and paste it into Settings > Plugins > Meshy in Hermes Desktop.\u00bb",
          "Il plugin ufficiale per @MeshyAI (MCP server: text/image-to-3D, rigging, animazione, preparazione per la stampa) era stato annunciato lo stesso giorno; l'offerta a 1$ \u00e8 riservata agli utenti Hermes."),

    xitem("hermes-talk: voce bidirezionale in tempo reale come plugin open source (MIT)",
          "2113846794778284242", ["2113846807247888856"],
          "\u00abSTOP TYPING TO HERMES. JUST TALK TO IT. \u2026 hermes-talk is an open-source plugin that gives Hermes Agent a realtime voice, with all of Hermes's real tools behind it. What it does: \u25b8 Live two-way voice you can interrupt mid-sentence\u00bb",
          "Comandi di installazione nel secondo link: `hermes plugins install TheSmokeDev/hermes-talk --enable` e `pip install \"hermes-talk[audio]\"`. Autore @ItsSmokeDev; plugin della community, non ufficiale Nous. Il post \u00e8 il pi\u00f9 discusso del pilastro nelle 24 ore."),

    witem("Jensen Huang chiude il keynote GTC Berlin con una demo di Hermes Agent su RTX Spark",
          "Nous Research (announcements)", "2026-10-22",
          "\u00abJensen closed his GTC Berlin 2026 keynote with this Hermes Agent demo as the finale. \u2026 he installed and set up a customized Hermes in one prompt. Then he used Hermes, running on @nvidia RTX Spark, to create a simulated training environment for the @huggingface Microduck. Hermes planned an obstacle course with Nemotron and had GPT-6 Astra build it using FreeCAD, Omniverse libraries, Blender, Newton, and Isaac Lab. Hermes trained thousands of simulated ducks on that course until the validated policy was ready to run on the real robot in the physical world.\u00bb",
          ["https://nousresearch.com/",
           "https://alphasignal.ai/news/nous-research-s-hermes-agent-trained-a-real-robot-from-a-single-prompt"],
          "Il secondo link \u00e8 un'analisi di settore senza data visibile in pagina: la data indicata \u00e8 quella dell'annuncio sul sito ufficiale."),

    xitem("Kimi K3.1 Pro arriva su Nous Portal: un comando `hermes model` per usarlo in Hermes",
          "2113865988693508269", ["2113864233666638128"],
          "\u00abKimi K3.1 Pro is already on Nous Portal, so it's one `hermes model` away in your Hermes Agent :)\u00bb Il secondo post: \u00abKimi K3.1 Pro @Kimi_Moonshot is crazy. Just one-shotted RESULT. using oh-my-hermes + Kimi K3.1 Pro.\u00bb",
          "Segnalazioni della community, non un annuncio ufficiale di Nous Research. Lo stesso modello \u00e8 stato reso disponibile su Venice il giorno prima (vedi sezione Venice)."),
]

venice = [
    xitem("Kimi K3.1 Pro sbarca su Venice: open weight, sconto del 20% fino al 31 ottobre",
          "2113758524916576312", ["2113759857966780800"],
          "\u00abKimi K3.1 Pro is live on Venice. @Kimi_Moonshot's strongest open-weight model: frontier-level intelligence for long-running coding and agent work, and it even designs 3D models, writing Blender and CAD scripts. Available anonymously. 20% off Pro and Highspeed (API) thru Oct 31.\u00bb",
          "@venicestats aggiunge i numeri del produttore: 65,7% su Terminal-Bench contro 66,4% di Opus 5.5, contesto 1M, pesi pubblicati il 4 novembre, $3/$15 per milione di token contro $4/$20 di Opus 5.5."),

    xitem("Abliterated Large Flash disponibile su Venice, in forma anonima",
          "2113720168023212097", [],
          "\u00abYou can\u2019t fight back with an AI that keeps apologizing. @abliteration_ai's Abliterated Large Flash doesn\u2019t flinch. Available anonymously on Venice.\u00bb"),

    xitem("Lumara Film Festival: il Terminal Award va a \u00abReviver\u00bb, 12.000$ e 1,2 milioni di crediti Venice",
          "2113662969712365920", ["2113662973369884946"],
          "\u00abPresenting the Terminal Award winner of Lumara Film Festival\u2026 REVIVER by Aleksey Dor. This 13-minute visual feast spanning thousands of years of human existence wins the award for best experimental film, and comes with a $12,000 prize along with 1.2 million Venice credits.\u00bb",
          "Festival presentato da @moonpay e Venice; proiezione integrale il 26 ottobre al Roxy Cinema insieme agli altri finalisti (secondo link)."),

    xitem("Settimana 16-23 ottobre: 2.158 post su VVV/DIEM da 1.103 account, 1,48 milioni di view",
          "2113437850217722104", ["2113437802591371317"],
          "\u00abThe week in numbers, Oct 16 to Oct 23: \U0001F4DD 2,158 posts from 1,103 accounts \U0001F331 548 accounts we had never seen post about Venice \U0001F440 1.48M views \u2764\ufe0f 15.9K likes \u00b7 \U0001F501 1,626 reposts \u00b7 \U0001F516 1,878 bookmarks\u00bb",
          "Board generato automaticamente dai dati che @venicestats raccoglie su X (Buzz Score = (like + bookmark) \u00d7 log\u2082(post + 1) + view/100): non sono numeri ufficiali Venice. Nel Buzz Board del 23/10 @ErikVoorhees resta #1, @TrustlessState #2, @moonpay risale al #9."),

    xitem("Come funziona DIEM: si spende prima dei crediti, non si accumula, si brucia per sbloccare il VVV",
          "2113345311154524501", ["2113345287947526151", "2113345386882674943"],
          "\u00abDIEM is always spent first, before account credits. If you go past your day's DIEM allowance, your regular USD credits keep you going. DIEM credits do not roll over.\u00bb Dal thread: per riavere il VVV messo in stake bisogna bruciare la stessa quantit\u00e0 di DIEM mintata, e vendere DIEM lascia il VVV bloccato finch\u00e9 non si brucia.",
          "@JonShapeShift (terzo link) descrive DIEM come \u00abtokenized inference\u00bb: trasforma l'inferenza da costo ricorrente in un asset posseduto."),

    witem("VVV a 24,79$ (\u22124,4% in 24 ore), volume 28,1 milioni di dollari",
          "CoinGecko · rilevazione radar", "2026-10-24",
          "VVV 24,79$ (\u22124,4% nelle 24 ore), volume 24h 28.062.489$, capitalizzazione 1.205.643.277$ (rilevazione del radar alle 06:01 UTC del 24/10).",
          ["https://www.coingecko.com/en/coins/venice-token",
           "https://www.21shares.com/en-eu/product/venc"],
          "Emissioni annuali scese da 14M VVV al lancio a 2M dal 1\u00b0 ottobre 2026 (\u221286%), secondo 21Shares; la stessa pagina segnala che il DIEM in circolazione non \u00e8 cresciuto insieme ai ricavi e che i burn ricorrenti restano sotto le emissioni. Un post della community (@Vx_nior, 24/10) indica ~25,71$ e ~1,25 mld$ di capitalizzazione: valori non riconciliati con la rilevazione CoinGecko."),
]

crypto = [
    witem("L'OCC finalizza le regole GENIUS su riserve e rimborsi; l'ABA accusa: \u00abscavalca il Congresso\u00bb",
          "Cointelegraph", "2026-10-21",
          "\u00abThe OCC has finalized rules for stablecoin reserves and redemptions\u2026 The regulation bans direct yield payments to customers from stablecoin issuers, but the OCC said it would \u201cevaluate\u201d third-party yield arrangements on a case-by-case basis.\u00bb Il regolamento entra in vigore il 18 gennaio. L'American Bankers Association contesta le norme finali sullo yield, sostenendo che \u00abundermine\u00bb il Congresso.",
          [f"{CC}/news/occ-finalizes-genius-act-rules-stablecoin-issuers-custody",
           "https://www.bankingdive.com/news/occ-final-rule-genius-stablecoin-yield-gould-bessent-icba/833638/"],
          "Storia del 21/10, fuori dalla finestra di 48 ore, ripresa dal radar: resta la base regolatoria delle voci stablecoin della settimana. Banking Dive precisa che la norma non copre Bank Secrecy Act, antiriciclaggio e sanzioni, oggetto di un regolamento separato con il Tesoro."),

    witem("Singapore, Malaysia e Thailandia allargano il corridoio stablecoin transfrontaliero con Ripple, Visa e Mastercard",
          "Cointelegraph", "2026-10-23",
          "Le due testate titolano: \u00abMalaysia, Thailand join Singapore\u2019s cross-border stablecoin push\u00bb (Cointelegraph) e \u00abSingapore, Malaysia and Thailand central banks expand cross-border stablecoin initiative involving Ripple, Visa and Mastercard\u00bb (The Block). Il radar segnala la stessa storia su due testate.",
          [f"{CC}/news/malaysia-thailand-join-singapores-cross-border-stablecoin-push",
           f"{BLOCK}/news/regulation/2026-10-23-singapore-malaysia-and-thailand-central-banks-expand-cross-border-stablecoin-initiative-involving-ripple-visa-and-mastercard-426492"]),

    witem("Gli ETF spot Bitcoin tornano in deflusso: \u2212636 milioni e ottobre di nuovo in rosso",
          "The Block", "2026-10-23",
          "\u00abBitcoin ETFs swing back to net outflows as $636 million in withdrawals erase previous day\u2019s inflows\u00bb (The Block); \u00abBitcoin ETFs bleed $635M as October slides back into the red\u00bb (Cointelegraph).",
          [f"{BLOCK}/news/markets/2026-10-23-bitcoin-etfs-swing-back-to-net-outflows-erase-previous-day-inflows-426483",
           f"{CC}/markets/bitcoin-etfs-erase-october-gains-outflow"],
          "Le due testate riportano 636 e 635 milioni (arrotondamenti diversi). Il post di @CoinDesk del 23/10 indica 635M$ di deflussi gioved\u00ec dopo oltre 1 mld$ di afflussi a inizio settimana, con BTC intorno a 82.000$."),

    xitem("CME Group: trimestre record e 326,7 miliardi di dollari di nozionale sui derivati Bitcoin",
          "2113745243543871935", ["2113633800546873674"],
          "\u00abJUST IN: CME Group recorded $326.7 billion in total notional trading volume for its Bitcoin derivatives in Q3!\u00bb Il secondo post (CoinDesk): ricavi trimestrali record a 1,74 mld$ (+13% anno su anno) e volume medio giornaliero record di 29,4 milioni di contratti.",
          "Nello stesso giorno CME ha definito Bitcoin soprattutto \u00aba decentralized store of value\u00bb, \u00abmaturing along distinct economic, functional, and regulatory paths\u00bb (@BitcoinMagazine, 23/10)."),

    witem("JPMorgan: le mosse di SEC e CFTC compensano in parte il fallimento del CLARITY Act, ma resta il rischio norme a macchia di leopardo",
          "The Block", "2026-10-22",
          "\u00abJPMorgan says crypto regulatory moves partly offset Clarity Act failure, but risks remain\u00bb (The Block). CoinDesk: \u00abJPMorgan says recent SEC and CFTC actions have partially offset the CLARITY Act\u2019s failure, but warns crypto faces a patchwork of regulatory measures that could be reversed in two years if Democrats win the White House.\u00bb",
          [f"{BLOCK}/news/regulation/2026-10-22-jpmorgan-crypto-regulatory-moves-clarity-act-failure-risks-423473",
           xlink("2113708283873693779")],
          "Il secondo link \u00e8 il post di @CoinDesk del 23/10 (id verificato nei JSON xurl della giornata)."),

    witem("New York chiede 1,37 miliardi di dollari ai fondatori di NovaTech per la frode Ponzi",
          "The Block", "2026-10-23",
          "\u00abNew York seeks over $1.3 billion from NovaTech founders after couple fled the US\u00bb (The Block); \u00abNew York AG seeks $1.37B from NovaTech founders over Ponzi scheme\u00bb (Cointelegraph). Il procuratore generale Letitia James chiede un giudizio da 1,37 mld$ contro Cynthia ed Eddy Petion e le loro societ\u00e0.",
          [f"{BLOCK}/news/regulation/2026-10-23-new-york-seeks-over-1-3-billion-from-novatech-founders-after-couple-fled-the-us-424453",
           f"{CC}/news/new-york-ag-novatech-founders-companies-crypto-ponzi"],
          "Si tratta di una richiesta di giudizio, non di una condanna. La coppia ha lasciato gli Stati Uniti secondo The Block. Il radar contava la storia su tre testate."),

    witem("HSBC lancia RedCoin, la sua prima stablecoin in dollaro di Hong Kong, per i pagamenti retail",
          "The Block", "2026-10-23",
          "\u00abHSBC rolls out its first HKD stablecoin RedCoin to retail users\u00bb (The Block); \u00abHSBC launches Hong Kong dollar stablecoin for retail payments\u00bb (Cointelegraph).",
          [f"{BLOCK}/news/business/2026-10-23-hsbc-hkd-stablecoin-redcoin-424018",
           f"{CC}/news/hsbc-launches-redcoin-hong-kong-dollar-stablecoin-payme"]),

    witem("Blumenthal chiede conto a Tether dei pagamenti all'ex consulente crypto della Casa Bianca",
          "Cointelegraph", "2026-10-23",
          "\u00abUS senator probes Tether after reported deal with ex-Trump crypto adviser\u00bb (Cointelegraph). CoinDesk: \u00abSen. Richard Blumenthal questions payments tied to Tether\u2019s U.S. chief Bo Hines\u00bb.",
          [f"{CC}/news/us-senator-probe-bo-hines-trump-crypto-adviser-tether-deal",
           xlink("2113722131146031518")],
          "Il secondo link \u00e8 il post di @CoinDesk del 23/10. Indagine su pagamenti a una societ\u00e0 di consulenza legata a Bo Hines, responsabile US di Tether."),
]

lines = []
lines.append(f"# Report \u2014 {T}")
lines.append(f"Data: {T}")
lines.append("Fonte: feed primari gratuiti (radar) + X/Twitter via xurl + ricerca web")
lines.append("Finestra di scansione: ultime 24-48 ore")
lines.append("Esecuzione: 13 chiamate xurl su 13 (3 keyword + 9 nucleo fisso + 1 rotazione @tether), 6 chiamate web_search su 6, radar: ok")
lines.append("")

counts = {}
for name, title, items in (("hermes", "## Hermes AI", hermes),
                           ("venice", "## Venice.ai / VVV / DIEM", venice),
                           ("crypto", "## Bitcoin & Crypto", crypto)):
    counts[name] = len(items)
    lines.append(title)
    lines.append("")
    for i, it in enumerate(items, 1):
        lines.append(f"### {i}. {it['title']}")
        if it["kind"] == "x":
            lines.append(f"- **Account**: {it['account']}")
        else:
            lines.append(f"- **Fonte**: {it['source']}")
        lines.append(f"- **Data**: {it['date']}")
        lines.append(f"- **Estratto**: {it['excerpt']}")
        lines.append(f"- **Link**: {' · '.join(it['links'])}")
        lines.append(f"- **Metriche**: {it['metrics']}")
        if it.get("note"):
            lines.append(f"- **Nota**: {it['note']}")
        lines.append("")

lines.append(f"Item: hermes={counts['hermes']} venice={counts['venice']} crypto={counts['crypto']}")
lines.append("Errori: radar con CoinDesk non raggiungibile (HTTP 403: Forbidden), coperto via @CoinDesk su X; rotazione @tether senza post nella finestra 24-48 ore (ultimi rilevati 21/10 e 20/10: investimento in Peso e in Tenstorrent), non sostituita come da contratto; @VitalikButerin fermo al 22/10 01:22, fuori finestra; nessun item per Franklin Templeton/ETF DRIP Nasdaq (solo post @BitcoinMagazine, nessun secondo link verificabile, escluso) e per la rete blockchain cinese al 2030 (solo @CoinDesk); TVL DefiLlama di Venice (1.706.386.403 USD) non pubblicato perch\u00e9 valore implausibile per un TVL; blog ufficiale Venice vivo ma senza articoli nuovi (ultima data 2026-09-29).")
lines.append(f"<!-- report-status: {T} complete hermes={counts['hermes']} venice={counts['venice']} crypto={counts['crypto']} -->")

out = "\n".join(lines) + "\n"
open("reports/%s-report.md" % T, "w", encoding="utf-8").write(out)
print("scritto reports/%s-report.md (%d byte)" % (T, len(out.encode())))
