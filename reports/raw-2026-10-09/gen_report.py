import json, glob, os

BASE = os.path.dirname(os.path.abspath(__file__))            # reports/raw-2026-10-09
REPO = os.path.dirname(os.path.dirname(BASE))                 # repo root
TODAY = "2026-10-09"

X = {}
for path in glob.glob(os.path.join(BASE, "*.json")):
    try:
        d = json.load(open(path, encoding="utf-8"))
    except Exception:
        continue
    users = {u["id"]: u.get("username") for u in d.get("includes", {}).get("users", [])}
    for p in d.get("data", []):
        X[p["id"]] = {
            "user": users.get(p.get("author_id"), "?"),
            "date": (p.get("created_at") or "")[:10],
            "metrics": p.get("public_metrics", {}),
        }

def link(tid):
    it = X[tid]
    return f"https://x.com/{it['user']}/status/{tid}"

def met(tid):
    m = X[tid]["metrics"]
    parts = [f"like {m.get('like_count', 0)}", f"repost {m.get('retweet_count', 0)}"]
    imp = m.get("impression_count", 0)
    if imp:
        parts.append(f"views {imp}")
    return " \u00b7 ".join(parts)

def dat(tid):
    return X[tid]["date"]

out = []
A = out.append

A(f"# Report \u2014 {TODAY}")
A(f"Data: {TODAY}")
A("Fonte: feed primari gratuiti (radar) + X/Twitter via xurl + ricerca web")
A("Finestra di scansione: ultime 24-48 ore")
A("Esecuzione: 13 chiamate xurl su 13 (3 keyword + 9 nucleo fisso + 1 rotazione @circle) \u00b7 6 chiamate web_search su 6 \u00b7 radar: ok (reports/2026-10-09-feeds.md) \u00b7 esito: report completo, nessun blocco API X")
A("")

# ---------------- HERMES AI ----------------
A("## Hermes AI")
A("")
A("### 1. Nous Research chiude un Series B da 90 milioni di dollari a 1,5 miliardi di valutazione")
A("- **Fonte**: Nous Research (nota ufficiale) / TechCrunch / The Next Web")
A("- **Data**: 2026-10-07")
A("- **Estratto**: Nous Research ha raccolto 90 milioni di dollari in un round Series B che valuta la societ\u00e0 1,5 miliardi di dollari (cifra riportata dal WSJ). Investitori: Robot Ventures (lead), NVIDIA, M12 (Microsoft), Samsung, Union Square Ventures, Y Combinator, Menlo Ventures, 1789 Capital. Il finanziamento totale sale a 158 milioni. Hermes Agent \u00e8 stato clonato oltre 24 milioni di volte e, per stima interna, genera circa il 2,5% dell'uso globale di token; ricavi annualizzati ~36 milioni a met\u00e0 settembre 2026, attesi oltre 100 milioni entro fine anno. I fondi andranno a \"Hermes for Businesses\".")
A("- **Link**: https://nousresearch.com/a-note-on-our-fundraise ; https://techcrunch.com/2026/10/07/nous-research-confirms-it-hit-1-5b-valuation-launches-ai-agents-for-business-users/ ; https://thenextweb.com/news/nous-research-90m-1-5bn-hermes-agent-wsj")
A("- **Metriche**: non disponibili")
A("- **Nota**: Nous non ha confermato ufficialmente la cifra di 1,5 mld; la valutazione \u00e8 attribuita al WSJ e ripresa da TechCrunch.")
A("")

A("### 2. Hermes Agent v0.21.6 (release GitHub)")
A("- **Fonte**: GitHub \u00b7 NousResearch/hermes-agent (releases)")
A("- **Data**: 2026-10-08")
A("- **Estratto**: Il radar registra la release **v0.21.6** di Hermes Agent (08/10 11:51 UTC). Nei giorni precedenti il ramo canary aveva gi\u00e0 ricevuto build (06-07 ottobre). La release precedente stabile era v0.21.5 (v2026.9.24).")
A("- **Link**: https://github.com/NousResearch/hermes-agent/releases ; https://releasebot.io/updates/nousresearch/hermes-agent")
A("- **Metriche**: non disponibili")
A("")

A("### 3. Hermes Agent arriva sul Microsoft Store (installazione one-click)")
A("- **Fonte**: Nous Research (sito ufficiale) / @HermesWatcher")
A(f"- **Data**: {dat('2108373130066657302')}")
A("- **Estratto**: Nous Research (8 ott): \"Hermes Agent \u00e8 ora live (e in evidenza) nel @Microsoft Store per un'installazione one-click. Altri aggiornamenti per l'ecosistema Windows in arrivo.\" @HermesWatcher: \"HERMES IS FREE! STEP 5 PREVIEW IS FREE! \u2026 puoi scaricare Hermes direttamente dal Microsoft [Store]\", con un sito generato usando Step 5 come modello principale.")
A(f"- **Link**: https://nousresearch.com/ ; {link('2108373130066657302')}")
A(f"- **Metriche**: {met('2108373130066657302')}")
A("")

A("### 4. Il plugin Spotify esce dal core di Hermes e diventa plugin di catalogo")
A(f"- **Account**: @{X['2108387691134058537']['user']}")
A(f"- **Data**: {dat('2108387691134058537')}")
A("- **Estratto**: \"@AustinReed930 Non viene distribuito con Hermes. \u00c8 un plugin del catalogo plugin.\" I commit sul repo (09/10 00:57) confermano lo spostamento: \"refactor: move Spotify out of core into the spotify catalog plugin\" e \"Plugin catalog: spotify (official, NousResearch)\".")
A(f"- **Link**: {link('2108387691134058537')} ; https://github.com/NousResearch/hermes-agent")
A(f"- **Metriche**: {met('2108387691134058537')}")
A("")

A("### 5. Caso d'uso \"estremamente produttivo\": Hermes crea un team di bot specializzati")
A(f"- **Account**: @{X['2108414654431342951']['user']}")
A(f"- **Data**: {dat('2108414654431342951')}")
A("- **Estratto**: \"Questo \u00e8 un caso d'uso di Hermes INCREDIBILMENTE PRODUTTIVO! \u2026 dare a Hermes i requisiti del progetto e fargli creare un intero team di bot specializzati, ognuno con il proprio ruolo e un modello scelto appositamente per il compito. \u00c8 esattamente ci\u00f2 che @tonbistudio dimostra.\"")
A(f"- **Link**: {link('2108414654431342951')}")
A(f"- **Metriche**: {met('2108414654431342951')}")
A("")

A("### 6. Reazione della community: loop di auto-miglioramento e oltre 200 skill")
A(f"- **Account**: @{X['2108433387497107625']['user']}")
A(f"- **Data**: {dat('2108433387497107625')}")
A("- **Estratto**: \"la cosa migliore di Hermes agent \u00e8 l'auto-evoluzione \u2026 ti accorgi che accumula 200+ skill in due settimane. Questo va sistemato: il mio harness Pi non carica alcun prompt di skill fuori dall'orchestratore, uso un indice per recuperarle.\"")
A(f"- **Link**: {link('2108433387497107625')}")
A(f"- **Metriche**: {met('2108433387497107625')}")
A("- **Nota**: opinione di un utente, non fonte ufficiale.")
A("")

# ---------------- VENICE ----------------
A("## Venice.ai / VVV / DIEM")
A("")
A("### 1. Burn discrezionale record: circa 414.000 dollari di $VVV")
A(f"- **Account**: @{X['2107885709768159724']['user']} (+ @{X['2107973621683749188']['user']})")
A(f"- **Data**: {dat('2107885709768159724')}")
A("- **Estratto**: @AskVenice: \"L'ultimo burn discrezionale di $VVV \u00e8 stato eseguito. Per un totale di 414.000 dollari in VVV al momento del burn, \u00e8 il pi\u00f9 grande finora.\" @venicestats: \"il buy-and-burn di ottobre di @AskVenice ha bruciato ~415.000 $VVV, il pi\u00f9 grande finora in USD e l'ottavo aumento mensile consecutivo; con Pro Sub e burn da crediti a soli 7 giorni dall'inizio, ottobre totalizza gi\u00e0 551.000 dollari.\"")
A(f"- **Link**: {link('2107885709768159724')} ; {link('2107973621683749188')}")
A(f"- **Metriche**: {met('2107885709768159724')} (@AskVenice)")
A("")

A("### 2. Claude Haiku 5.5 disponibile su Venice")
A(f"- **Account**: @{X['2108033849494298765']['user']} (+ @{X['2108002829839315271']['user']})")
A(f"- **Data**: {dat('2108033849494298765')}")
A("- **Estratto**: @AskVenice: \"Claude Haiku 5.5 \u00e8 ora live su Venice. Il modello piccolo pi\u00f9 capace di @AnthropicAI finora, e il primo Haiku con effort regolabile. Disponibile in forma anonima.\" @venicestats: \"1M di contesto a $0,125 per milione di token di input.\"")
A(f"- **Link**: {link('2108033849494298765')} ; {link('2108002829839315271')}")
A(f"- **Metriche**: {met('2108033849494298765')} (@AskVenice)")
A("")

A("### 3. Prestiti contro $VVV a tasso fisso, peer-to-peer")
A(f"- **Account**: @{X['2107849052108783863']['user']}")
A(f"- **Data**: {dat('2107849052108783863')}")
A("- **Estratto**: \"Prendi in prestito contro i tuoi $VVV. Tasso fisso, peer to peer.\"")
A(f"- **Link**: {link('2107849052108783863')}")
A(f"- **Metriche**: {met('2107849052108783863')}")
A("")

A("### 4. La corsa deflazionistica di $VVV")
A(f"- **Account**: @{X['2107886262237761740']['user']}")
A(f"- **Data**: {dat('2107886262237761740')}")
A("- **Estratto**: \"Pi\u00f9 burn, emissioni pi\u00f9 basse: la marcia verso un $VVV deflazionistico continua.\"")
A(f"- **Link**: {link('2107886262237761740')}")
A(f"- **Metriche**: {met('2107886262237761740')}")
A("")

A("### 5. Lumara World Premiere al Roxy Cinema di NYC il 26 ottobre")
A(f"- **Account**: @{X['2108243699465617908']['user']}")
A(f"- **Data**: {dat('2108243699465617908')}")
A("- **Estratto**: \"Unitevi per una serata di magia cinematografica. I giudici stanno selezionando i candidati per la Lumara World Premiere il 26 ottobre al Roxy Cinema di NYC. Sette premi, fino a 100.000 dollari in contanti e 10M di crediti Venice in palio.\"")
A(f"- **Link**: {link('2108243699465617908')}")
A(f"- **Metriche**: {met('2108243699465617908')}")
A("")

A("### 6. Un wallet nuovo compra il dip: 703.667 $VVV (~15,97 milioni di dollari)")
A(f"- **Account**: @{X['2108393681388724628']['user']}")
A(f"- **Data**: {dat('2108393681388724628')}")
A("- **Estratto**: \"Un wallet nuovo \u00e8 entrato circa 15 ore fa, proprio mentre il mercato vendeva. Ha prelevato 703.667 $VVV (~15,97 milioni di dollari) da Coinbase.\"")
A(f"- **Link**: {link('2108393681388724628')}")
A(f"- **Metriche**: {met('2108393681388724628')}")
A("- **Nota**: dato on-chain riportato da un account di analisi, non confermato da fonti ufficiali.")
A("")

A("### 7. Tokenomics: emissioni a 2M VVV/anno, burn dai crediti API, target DIEM a 40.000")
A("- **Fonte**: Venice (blog ufficiale) / CryptoNews")
A("- **Data**: 2026-10-01")
A("- **Estratto**: Le emissioni annuali di $VVV scendono da 3M a 2M (taglio a settembre e ottobre). Introdotto un burn programmatico: 5$ di ogni 100$ di crediti API acquistati vengono usati per comprare e bruciare $VVV, in aggiunta ai burn gi\u00e0 finanziati dagli abbonamenti Pro/Pro+/Max. Il target di offerta di $DIEM sale da 38.000 a 40.000 in quattro step (agosto-settembre). ~42% della supply iniziale (100M) risulta bruciata cumulativamente.")
A("- **Link**: https://venice.ai/blog/tokenomics-update-credit-burns-and-diem-supply-expansion ; https://cryptonews.net/news/altcoins/33474191/")
A("- **Metriche**: non disponibili")
A("")

A("### 8. Dati di mercato $VVV e TVL di Venice")
A("- **Fonte**: CoinGecko / DefiLlama")
A(f"- **Data**: {TODAY}")
A("- **Estratto**: $VVV a 22,96$ (-7,2% nelle 24h), volume 124.427.909$, market cap 1.109.924.175$. TVL del protocollo Venice: 1.582.226.356$.")
A("- **Link**: https://www.coingecko.com/en/coins/venice-token ; https://defillama.com/protocol/venice")
A("- **Metriche**: non disponibili")
A("")

# ---------------- CRYPTO ----------------
A("## Bitcoin & Crypto")
A("")
A("### 1. Bitcoin rimbalza a 82.000$ dopo che Trump esclude attacchi all'Iran")
A("- **Fonte**: CoinDesk (+ @BitcoinMagazine)")
A("- **Data**: 2026-10-09")
A("- **Estratto**: CoinDesk: \"Bitcoin \u00e8 rimbalzato a 82.000$ dopo che Trump ha escluso un attacco all'Iran prima delle midterm, mentre il petrolio scende.\" @BitcoinMagazine: \"Bitcoin scende sotto 81.000$ mentre il Brent sale a un massimo mensile di 105$/barile.\"")
A(f"- **Link**: https://www.coindesk.com/markets/2026/10/09/bitcoin-rebounds-to-usd82-000-as-trump-rules-out-iran-strikes ; {link('2108260813031325984')}")
A(f"- **Metriche**: {met('2108260813031325984')} (@BitcoinMagazine)")
A("")

A("### 2. La CFTC apre una consultazione su un quadro federale per il crypto retail")
A("- **Fonte**: CoinDesk / Bitcoin.com News")
A("- **Data**: 2026-10-05")
A("- **Estratto**: La CFTC ha avviato il 5 ottobre una consultazione su un framework nazionale per le transazioni retail di commodity crypto, con una categoria di registrazione dedicata agli exchange che offrono leva, margine o finanziamenti; commenti entro 60 giorni dalla pubblicazione in Federal Register. Procede in parallelo alle misure della SEC su custodia e trading di azioni on-chain.")
A("- **Link**: https://www.coindesk.com/policy/2026/10/05/u-s-cftc-joins-sec-in-proposing-crypto-regulations-though-spot-market-gap-lingers ; https://news.bitcoin.com/regulation-and-legal/us-regulators-push-national-crypto-rules-as-america-chases-global-lead/")
A("- **Metriche**: non disponibili")
A("")

A("### 3. La Grecia prepara una tassa del 10% sulle plusvalenze crypto")
A("- **Fonte**: CoinDesk / Cointelegraph / Reuters")
A("- **Data**: 2026-10-08")
A("- **Estratto**: La Grecia si prepara a introdurre una capital gains tax del 10% sulle cripto con un disegno di legge atteso in Parlamento a novembre; i guadagni fino a 500 euro (560$) l'anno sarebbero esenti. Il testo \u00e8 in consultazione pubblica. L'aliquota \u00e8 pi\u00f9 bassa di quelle di diversi vicini europei.")
A("- **Link**: https://www.coindesk.com/policy/2026/10/08/greece-prepares-to-levy-10-capital-gains-tax-on-cryptocurrency ; https://cointelegraph.com/news/greece-capital-gains-tax-cryptocurrencies ; https://www.reuters.com/business/finance/greece-plans-10-cryptocurrency-capital-gains-tax-2026-10-08/")
A("- **Metriche**: non disponibili")
A("")

A("### 4. Standard Chartered lancia la custodia di asset digitali a Singapore")
A("- **Fonte**: Cointelegraph / Standard Chartered (comunicato ufficiale)")
A("- **Data**: 2026-10-08")
A("- **Estratto**: La banca annuncia servizi di custodia per criptovalute selezionate, stablecoin e asset reali tokenizzati destinati a clienti istituzionali e corporate qualificati come investitori accreditati a Singapore, soggetti ai requisiti regolatori applicabili.")
A("- **Link**: https://cointelegraph.com/news/standard-chartered-digital-asset-custody-services-singapore ; https://www.sc.com/en/press-release/standard-chartered-advances-into-digital-asset-custody-offering-in-singapore/")
A("- **Metriche**: non disponibili")
A("")

A("### 5. L'ESMA d\u00e0 3 mesi alle piattaforme per rimuovere le stablecoin non autorizzate")
A("- **Fonte**: CoinDesk / Cointelegraph")
A("- **Data**: 2026-10-08")
A("- **Estratto**: L'autorit\u00e0 europea degli strumenti finanziari ha stabilito che le piattaforme autorizzate devono bloccare i nuovi accessi alle stablecoin non conformi a MiCA, mentre le autorit\u00e0 nazionali gestiscono le giacenze esistenti dei clienti.")
A("- **Link**: https://www.coindesk.com/policy/2026/10/08/eu-securities-regulator-gives-crypto-platforms-3-months-to-remove-unauthorized-stablecoins ; https://cointelegraph.com/news/esma-unauthorised-stablecoins-three-month-deadline")
A("- **Metriche**: non disponibili")
A("")

A("### 6. Un senatore democratico indaga sui legami Cantor Fitzgerald\u2013Tether")
A("- **Fonte**: CoinDesk / Cointelegraph")
A("- **Data**: 2026-10-08")
A("- **Estratto**: Il senatore Richard Blumenthal, tra gli investigatori del Senate Permanent Subcommittee on Investigations, sta esaminando il partenariato finanziario di Tether negli USA (Cantor Fitzgerald), mentre cresce la probabilit\u00e0 che i democratici riprendano la maggioranza al Senato.")
A("- **Link**: https://www.coindesk.com/policy/2026/10/08/top-democrat-among-senate-investigators-probes-ties-between-cantor-fitzgerald-tether ; https://cointelegraph.com/news/cantor-fitzgerald-faces-senate-democrats-probe-over-tether-ties")
A("- **Metriche**: non disponibili")
A("")

A("### 7. Il governo USA sposta 12.267 BTC (1,01 mld $) da wallet legati al caso Bitfinex")
A(f"- **Account**: @{X['2108227167339606047']['user']}")
A(f"- **Data**: {dat('2108227167339606047')}")
A("- **Estratto**: \"Wallet collegati al governo USA hanno spostato 12.267 BTC (1,01 mld di dollari) da un wallet di sequestro del caso Bitfinex a nuovi indirizzi non etichettati. Nessun deposito su exchange \u00e8 stato registrato, il che indica una riorganizzazione dei wallet piuttosto che una vendita.\"")
A(f"- **Link**: {link('2108227167339606047')}")
A(f"- **Metriche**: {met('2108227167339606047')}")
A("")

A("### 8. Vitalik: prendere sul serio i rischi per la crittografia dall'IA")
A(f"- **Account**: @{X['2107976296320106851']['user']}")
A(f"- **Data**: {dat('2107976296320106851')}")
A("- **Estratto**: \"Non consiglio a nessuno di correre a spostare i fondi su nuovi wallet oggi. Ma dovremmo prendere sul serio i rischi per la crittografia derivanti dalla matematica accelerata dall'IA, e minimizzare l'esposizione non solo alla crittografia vulnerabile ai quantum, ma anche a quella potenzialmente vulnerabile all'IA.\"")
A(f"- **Link**: {link('2107976296320106851')}")
A(f"- **Metriche**: {met('2107976296320106851')}")
A("- **Nota**: segue il panico del 7-8 ottobre su un presunto indebolimento di ECDSA; Vitalik ha poi pubblicato correzioni sulle regole per i multisig.")
A("")

A("Item: hermes=6 venice=8 crypto=8")
A("Errori: (1) la pagina TechCrunch del Series B \u00e8 protetta da Cloudflare: contenuto verificato via snippet di ricerca/cache, non dal render diretto. (2) Gli slug Cointelegraph derivati dal titolo per le storie Standard Chartered e Grecia hanno restituito 404: URL esatti recuperati dalle pagine di sezione (tags/banking, tags/taxes). (3) La pagina Cointelegraph 'bitcoin-regulation' e la tag 'regulation' non elencavano la storia della Grecia: URL trovato via tags/taxes. (4) Storia 'Hermes Agent su ASUS ProArt RTX Spark' presente sul radar (sito Nous Research) ma esclusa per assenza di un secondo link indipendente verificabile. (5) La notizia 'US government moves seized Bitcoin' non ha un URL articolo verificato: riportata come voce X (@CoinDesk).")
A(f"<!-- report-status: {TODAY} complete hermes=6 venice=8 crypto=8 -->")

text = "\n".join(out) + "\n"
dest = os.path.join(REPO, "reports", f"{TODAY}-report.md")
open(dest, "w", encoding="utf-8").write(text)
print("scritto", dest, len(text), "byte")
print("righe:", text.count(chr(10)))
