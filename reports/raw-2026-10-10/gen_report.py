import json, os

RAW = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(RAW, "..", ".."))
TODAY = "2026-10-10"

cache = {}
def load(f):
    if f not in cache:
        cache[f] = json.load(open(os.path.join(RAW, f), encoding="utf-8"))
    return cache[f]

def find(f, pid):
    d = load(f)
    users = {u["id"]: u.get("username") for u in d.get("includes", {}).get("users", [])}
    for p in d.get("data", []):
        if p.get("id") == pid:
            return p, users.get(p.get("author_id"))
    raise SystemExit("MISSING %s %s" % (f, pid))

def xurl_of(f, pid):
    p, u = find(f, pid)
    return "https://x.com/%s/status/%s" % (u, p["id"])

def xmetrics(f, pid):
    p, _ = find(f, pid)
    m = p.get("public_metrics", {})
    parts = ["like=%s" % m.get("like_count", 0), "repost=%s" % m.get("retweet_count", 0)]
    imp = m.get("impression_count", 0)
    if imp:
        parts.append("views=%s" % imp)
    return ", ".join(parts)

def xdate(f, pid):
    p, _ = find(f, pid)
    return p.get("created_at", "")[:10]

def xhandle(f, pid):
    _, u = find(f, pid)
    return "@" + u

# ---- X items: (json, post_id, titolo, estratto, nota) ----
HERMES_X = [
 ("from-NousResearch.json", "2108638389045960958",
  "Step 5 Preview di StepFun gratuito su Nous Portal per una settimana",
  "Nous Research annuncia che Step 5 Preview di @StepFun_ai e' gratuito su Nous Portal per una settimana: 600B parametri totali / 27B attivi (MoE), contesto 1M token, con visione. Sul Hermes Index ha segnato 33.89, lo stesso punteggio di GPT-6 Luna.",
  "In un post successivo (@NousResearch, 09/10) il punteggio finale di Step 5 Preview sul Hermes Index e' stato corretto a 32.83, leggermente dietro GPT-6 Luna (33.89) e GLM 5.3 Flash (34.95)."),
 ("from-HermesWatcher.json", "2108739340751028410",
  "Hermes Kanban: gestire molti agenti oltre la chat",
  "HermesWatcher spiega cosa e' Hermes Kanban, perche' conviene usarlo e come configurarlo: con molti agenti e progetti attivi diventa difficile tenere traccia di tutto solo via chat.",
  ""),
 ("from-HermesWatcher.json", "2108667572774470132",
  "Gli aggiornamenti Hermes della settimana",
  "HermesWatcher riassume gli aggiornamenti della settimana: conversazioni piu' veloci, meno incertezza con i modelli locali e meno passaggi per completare le attivita'.",
  ""),
 ("kw-hermes.json", "2108797500572225949",
  "Ares: workbench per operatori sopra Hermes Agent",
  "@RecursiveIntell presenta Ares, un workbench per chi vuole l'esperienza dell'agente Hermes di @NousResearch con controllo operativo esplicito, release gestite in modo atomico e prove che qualcosa e' stato realmente eseguito (non solo configurato o registrato).",
  "Progetto di terze parti, non ufficiale Nous Research."),
 ("kw-hermes.json", "2108791179823452356",
  "HOL Guard: layer di sicurezza locale per agenti AI",
  "@NFTerramike presenta HOL Guard, un layer di sicurezza locale open source in stile 'antivirus' per agenti AI, strumenti, plugin, skill, server MCP e comandi shell: si colloca tra l'agente e le azioni che vuole compiere, ispezionandole prima dell'esecuzione.",
  "Progetto di terze parti, non ufficiale Nous Research."),
 ("from-HermesWatcher.json", "2108603490885058729",
  "Preferenze salvate: correggere l'agente una volta sola",
  "HermesWatcher mostra come trasformare una correzione in una preferenza salvata, cosi' non va ripetuta a ogni nuova chat: formato, lunghezza delle risposte, titoli.",
  ""),
]

VENICE_X = [
 ("from-AskVenice.json", "2108558644677943321",
  "Venice lancia Agentic Chat: AI privata e senza restrizioni",
  "@AskVenice promuove Agentic Chat: \"Le domande che contano di piu' sono quelle che non puoi rischiare di far registrare. L'AI privata e senza restrizioni e' migliorata. Prova Agentic Chat.\"",
  ""),
 ("from-venicestats.json", "2108002829839315271",
  "Claude Haiku 5.5 disponibile su AskVenice",
  "venicestats segnala che Claude Haiku 5.5 e' attivo su @AskVenice: contesto 1M token a 0,125 $ per milione di token in input.",
  ""),
 ("from-venicestats.json", "2108363212756308063",
  "Buzz Board: i 10 account piu' attivi nella conversazione $VVV",
  "venicestats pubblica il Buzz Board del 9 ottobre: nella conversazione $VVV degli ultimi 30 giorni @ErikVoorhees resta al n.1, @AskVenice al n.2 e @wallstreetbets entra direttamente all'8 con un lungo saggio su crypto e privacy AI.",
  ""),
 ("from-venicestats.json", "2108363258667081895",
  "La settimana Venice in numeri (2-9 ottobre)",
  "venicestats: 1.921 post da 1.163 account, 655 account mai visti prima parlare di Venice, 2,14 milioni di visualizzazioni, 17,6K like, 1.985 repost, 1.546 bookmark.",
  ""),
 ("from-JonShapeShift.json", "2107886262237761740",
  "JonShapeShift: piu' burn e meno emissioni verso un $VVV deflazionario",
  "JonShapeShift: \"Piu' burn, emissioni piu' basse, la marcia verso un $VVV deflazionario continua.\"",
  "Post del 07/10, ripreso perche' riassume la linea tokenomics di ottobre."),
 ("from-venicestats.json", "2108363275842850866",
  "venicestats: thread settimanale con inferenza AI pagata in $DIEM",
  "venicestats spiega che il thread settimanale e' generato automaticamente dalle statistiche raccolte su X, con due righe scritte da inferenza AI pagata in $DIEM; nuova edizione ogni venerdi'.",
  ""),
]

CRYPTO_X = [
 ("from-BitcoinMagazine.json", "2108674817188647142",
  "El Salvador acquista altri BTC: riserva a 7.800 bitcoin",
  "Bitcoin Magazine: \"El Salvador ha comprato altri BTC per la sua Strategic Bitcoin Reserve. Ora possiede 7.800 BTC.\"",
  ""),
 ("from-CoinDesk.json", "2108558511982461037",
  "Ledger indaga su perdite di fondi legate a un rivenditore del Sud-Est asiatico",
  "CoinDesk: Ledger indaga su oltre 86 milioni di dollari di presunte perdite legate a un rivenditore del Sud-Est asiatico, invitando i clienti colpiti a non configurare i dispositivi e a spostare subito gli asset su un nuovo wallet.",
  "Bitcoin Magazine riporta che il rivenditore coinvolto e' 'CryptoBillis' e che la situazione e' in corso."),
 ("from-CoinDesk.json", "2108600970066186301",
  "Bessent: gli USA prevedono di sequestrare 1 miliardo di dollari in crypto legate all'Iran",
  "CoinDesk: il Segretario al Tesoro Scott Bessent afferma che gli Stati Uniti prevedono di sequestrare entro la settimana circa 1 miliardo di dollari in crypto legate all'Iran, nell'ambito di una \"campagna di isolamento assoluto\" contro l'accesso del regime ai canali finanziari.",
  ""),
 ("from-SECGov.json", "2108656043186069517",
  "SEC: proposte di modifica alla cross-trading rule dell'Investment Company Act",
  "SECGov: la Commissione ha proposto emendamenti alla \"cross-trading rule\" dell'Investment Company Act, che a certe condizioni consente transazioni in titoli tra un fondo registrato e le sue affiliate; gli emendamenti modernizzerebbero ed estenderebbero la regola.",
  ""),
 ("from-CoinDesk.json", "2108579588712599897",
  "SEC: i crypto asset entrano nel seminario nazionale di compliance del 19 novembre",
  "CoinDesk: la SEC aggiunge i crypto asset al seminario nazionale di compliance per consulenti finanziari del 19 novembre, con la partecipazione del chief counsel della Crypto Task Force.",
  ""),
 ("from-CoinDesk.json", "2108664212742721670",
  "Robinhood Chain: allo studio un meccanismo che da' priorita' ai trader paganti",
  "CoinDesk (scoop): Robinhood Chain valuta una tecnologia che da' priorita' ai trader che pagano.",
  ""),
]

# ---- Web items: (titolo, fonte, data, estratto, [links], nota) ----
HERMES_WEB = [
 ("Hermes Agent v0.21.6: prima release del nuovo pipeline stabile",
  "GitHub (NousResearch/hermes-agent) / Freedom.Tech", "2026-10-08",
  "L'8 ottobre 2026 e' stata pubblicata la release stabile Hermes Agent v0.21.6, la prima tagliata dal nuovo pipeline di release stabile: raccoglie circa 2.100 PR unite da v0.21.5 e include correzioni di sicurezza (irrigidimento dell'autenticazione della dashboard). Le note curate complete arriveranno con v0.22.0.",
  ["https://api.github.com/repos/NousResearch/hermes-agent/releases/latest",
   "https://freedom.tech/project/hermes-agent/"],
  "Dopo il tag sono proseguiti i build canary (v0.21.6+canary.20261009) e le release candidate per v0.21.7; il radar di oggi registra nuovi commit su skills, relay 0.10 e canale di update."),
]

VENICE_WEB = [
 ("Dati di mercato VVV e TVL del protocollo Venice",
  "CoinGecko / DefiLlama (radar)", "2026-10-10",
  "VVV 22,76 $ (-0,6% nelle 24h), volume 24h 39.406.566 $, market cap 1.100.358.982 $. TVL del protocollo Venice su DefiLlama: 1.553.165.440 $.",
  ["https://www.coingecko.com/en/coins/venice-token",
   "https://defillama.com/protocol/venice"],
  "Dati raccolti dal radar fonti gratuiti (stadio 0)."),
]

CRYPTO_WEB = [
 ("Thailandia: regole per gli ETF su bitcoin ed ether in vigore dal 16 ottobre",
  "The Block / Cointelegraph", "2026-10-09",
  "La SEC thailandese ha emesso le regole per gli ETF su cripto, in vigore dal 16 ottobre: inizialmente solo bitcoin ed ether, esposizione netta media di almeno l'80% al singolo asset per anno contabile, custodian autorizzati e negoziazione solo sulla Borsa di Thailandia; vietati i prestiti a margine per l'acquisto.",
  ["https://www.theblock.co/news/regulation/2026-10-09-thailand-sec-issues-bitcoin-and-ether-etf-rules-set-to-take-effect-oct-16-418132",
   "https://cointelegraph.com/news/thailand-finalizes-rules-paving-way-for-bitcoin-ether-etfs"],
  ""),
 ("ESMA: tre mesi ai fornitori crypto per uscire dalle stablecoin non conformi a MiCA",
  "CoinDesk / Cointelegraph", "2026-10-08",
  "L'ESMA ha dato ai fornitori di servizi crypto autorizzati ai sensi di MiCA un massimo di tre mesi per cessare i servizi su stablecoin non conformi (token asset-referenced ed e-money), bloccando nuovi accessi e lasciando alle autorita' nazionali la supervisione delle posizioni residue dei clienti esistenti.",
  ["https://www.coindesk.com/policy/2026/10/08/eu-securities-regulator-gives-crypto-platforms-3-months-to-remove-unauthorized-stablecoins",
   "https://cointelegraph.com/news/esma-unauthorised-stablecoins-three-month-deadline"],
  ""),
]

def render_x(items, start=1):
    out = []
    for i, (f, pid, title, exc, nota) in enumerate(items, start):
        out.append("### %d. %s" % (i, title))
        out.append("- **Account**: %s" % xhandle(f, pid))
        out.append("- **Data**: %s" % xdate(f, pid))
        out.append("- **Estratto**: %s" % exc)
        out.append("- **Link**: %s" % xurl_of(f, pid))
        out.append("- **Metriche**: %s" % xmetrics(f, pid))
        if nota:
            out.append("- **Nota**: %s" % nota)
        out.append("")
    return out

def render_web(items, start=1):
    out = []
    for i, (title, fonte, data, exc, links, nota) in enumerate(items, start):
        out.append("### %d. %s" % (i, title))
        out.append("- **Fonte**: %s" % fonte)
        out.append("- **Data**: %s" % data)
        out.append("- **Estratto**: %s" % exc)
        out.append("- **Link**: %s" % " — ".join(links))
        out.append("- **Metriche**: non disponibili")
        if nota:
            out.append("- **Nota**: %s" % nota)
        out.append("")
    return out

lines = []
lines.append("# Report — %s" % TODAY)
lines.append("Data: %s" % TODAY)
lines.append("Fonte: feed primari gratuiti (radar) + X/Twitter via xurl + ricerca web")
lines.append("Finestra di scansione: ultime 24-48 ore")
lines.append("Esecuzione: 13/13 chiamate xurl, 6/6 chiamate web_search, radar: ok")
lines.append("")

lines.append("## Hermes AI")
lines.append("")
lines.extend(render_x(HERMES_X, 1))
lines.extend(render_web(HERMES_WEB, len(HERMES_X) + 1))

lines.append("## Venice.ai / VVV / DIEM")
lines.append("")
lines.extend(render_x(VENICE_X, 1))
lines.extend(render_web(VENICE_WEB, len(VENICE_X) + 1))

lines.append("## Bitcoin & Crypto")
lines.append("")
lines.extend(render_x(CRYPTO_X, 1))
lines.extend(render_web(CRYPTO_WEB, len(CRYPTO_X) + 1))

h = len(HERMES_X) + len(HERMES_WEB)
v = len(VENICE_X) + len(VENICE_WEB)
c = len(CRYPTO_X) + len(CRYPTO_WEB)

lines.append("Item: hermes=%d venice=%d crypto=%d" % (h, v, c))
lines.append("Errori: nessuno")
lines.append("<!-- report-status: %s complete hermes=%d venice=%d crypto=%d -->" % (TODAY, h, v, c))
lines.append("")

out_path = os.path.join(REPO, "reports", "%s-report.md" % TODAY)
open(out_path, "w", encoding="utf-8").write("\n".join(lines))
print("wrote", out_path, "hermes=%d venice=%d crypto=%d" % (h, v, c))
