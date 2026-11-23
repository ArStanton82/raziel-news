import json, os

BASE = '/root/.hermes/profiles/raziel-news/workspace/raziel-news'
items = json.load(open(f'{BASE}/reports/raw-2026-11-15/all.json'))
by_id = {}
for it in items:
    by_id.setdefault(it['id'], it)

def fmt(n):
    return f"{n:,}".replace(",", ".")

def metrics(it):
    m = it.get('metrics') or {}
    parts = []
    if m.get('like_count') is not None:
        parts.append(f"{fmt(m['like_count'])} like")
    if m.get('retweet_count') is not None:
        parts.append(f"{fmt(m['retweet_count'])} repost")
    v = m.get('impression_count') or 0
    if v:
        parts.append(f"{fmt(v)} visualizzazioni")
    return " · ".join(parts)

def snippet(txt, n=230):
    t = txt.strip()
    return t if len(t) <= n else t[:n].rsplit(' ', 1)[0] + '…'

SPEC = [
 ('hermes', dict(
   title="Workbench: plugin comunitario che porta Word, Excel e PowerPoint dentro Hermes Desktop",
   x=['2121845672911704314', '2121845686031515901'],
   extra_links=['https://hermes-agent.nousresearch.com/marketplace'],
   synth="Nuovo plugin comunitario «Workbench» (Atlas Omnia) nel catalogo Hermes: Word, Excel, PowerPoint, OneNote e Outlook si aprono in una scheda di Hermes Desktop accanto alla chat; il post di rilascio riporta anche il comando di installazione (`hermes plugins install <url> --enable`).",
   nota="Plugin comunitario, non ufficiale: richiede Hermes Desktop su macOS o Windows e un account Microsoft. La pagina del marketplace (hermes-agent.nousresearch.com/marketplace) risponde 200 ma il catalogo JSON su raw.githubusercontent è vuoto (14 byte), quindi il contenuto del plugin non è verificabile da fonte primaria.")),
 ('hermes', dict(
   title="GitHub: canary v0.23.1+canary.20261114T064334Z e repo a 263.458 stelle",
   web_source="GitHub — NousResearch/hermes-agent",
   date="2026-11-14",
   links=['https://github.com/NousResearch/hermes-agent/releases',
          'https://api.github.com/repos/NousResearch/hermes-agent/releases/latest'],
   synth="Il radar registra alle 07:46 UTC del 14/11 la canary `v0.23.1+canary.20261114T064334Z`; il repo hermes-agent ha un push alle 06:44 del 15/11 e 263.458 stelle. Ultima release stabile resta v0.23.1 (pubblicata su GitHub il 10/11 01:42 UTC), che rolla ~618 PR e rimanda le note curate a v0.24.0.",
   nota="La canary è un build giornaliero: non ha note di rilascio proprie, quindi il contenuto delle modifiche va letto nei commit. Le stelle arrivano dallo snapshot del radar.")),
 ('hermes', dict(
   title="Commit del fine settimana: allegati del gateway, docstring dei plugin, limiti dei provider",
   web_source="GitHub — commit su main",
   date="2026-11-15",
   links=['https://github.com/NousResearch/hermes-agent/commits/main',
          'https://github.com/NousResearch/hermes-agent'],
   synth="Tra il 14 e il 15/11: `fix(gateway): a reply's attachments follow its text onto the reconnected adapter` (03:31 UTC), `fix(plugins): a docstring critical stops at caution` (01:44), `fix(usage): provider limits first, Nous balance apart` (01:30), più il ripristino del confronto dell'endpoint di fallback con la query codificata (`fix(fallback)…`, 14/11 18:15) dopo un revert delle 17:30.",
   nota="Sono commit su main, non una release: nessun impatto dichiarato per gli utenti finali oltre alla correzione degli allegati e dei limiti di utilizzo.")),
 ('hermes', dict(
   title="Plugin hackathon: quasi 1.000 candidature, vincitori attesi «entro circa una settimana»",
   web_source="Nous Research (annuncio) / Hermes-ai.net",
   date="2026-11-12",
   links=['https://nousresearch.com/', 'https://hermes-ai.net/news/hermes-agent/'],
   synth="«Submissions for the Hermes Agent Plugin Hackathon closed at 5PM EST, and we received nearly 1,000 entries… Winners will be emailed directly, and we will announce them here in about a week.» Il montepremi annunciato all'avvio era di 20.000 $ in contanti più merch e crediti.",
   nota="Voce di contesto per l'ondata di plugin comunitari entrati in catalogo nelle ultime 24 ore; l'annuncio è del 12/11, fuori dalla finestra stretta di 24 ore.")),
 ('hermes', dict(
   title="Plugin comunitario permission-tiers: ogni comando shell passa da un consenso esplicito",
   x=['2121853432772399573'],
   synth="Plugin comunitario del catalogo Hermes che, in assenza di un file `tiers.json`, imposta ogni chiamata al terminale e ogni tool MCP su «ask»; i pattern dei nomi dei tool si assegnano a tre livelli (allow/ask/…).",
   nota="Post promozionale dell'autore del plugin (@GodsBoy7777): nessuna verifica indipendente del funzionamento.")),
 ('venice', dict(
   title="Seedance 2.5 Flash in early access su Venice: circa due volte più veloce e un terzo più economico",
   x=['2121658220083322986', '2121658232070631814'],
   synth="«Seedance 2.5 Flash is live on Venice in early access. Nearly twice as fast as Seedance 2.5 and a third cheaper at the same specs… Available anonymously.» Il modello video si usa senza account identificato.",
   nota="Il post gemello («Access Seedance 2.5 Flash on Venice») conferma la disponibilità, ma Venice non ha pubblicato una pagina prezzi dedicata nel blog (ultimo articolo del blog: 09/11).")),
 ('venice', dict(
   title="Gemini 4 Hydrogen disponibile su Venice: contesto da 1M token per coding e lavoro agentico",
   x=['2121636768403583425', '2121636780269310346'],
   synth="«Gemini 4 Hydrogen is live on Venice. For the quick jobs that don't need Gemini 4 Carbon. Google's fast, efficient model for coding and agentic work, with a 1M-token context window. Available anonymously.»",
   nota="Il nome «Gemini 4 Hydrogen» non risulta da un annuncio Google letto in questa esecuzione: il dato è quello dichiarato da Venice.")),
 ('venice', dict(
   title="Venice Studio punta sui filmmaker: modelli video ai prezzi più bassi «per tempo limitato»",
   x=['2121705789522129174', '2121705801182273946'],
   synth="«Venice Studio is for filmmakers. The best video models, now at the lowest prices for a limited time.» Il secondo post della serie invita a iniziare un progetto in Venice Studio.",
   nota="Non è indicata la durata della promozione né il listino; nessun comunicato ufficiale nel blog Venice nelle ultime 24 ore.")),
 ('venice', dict(
   title="VVV a 19,35 $ (+7,2%) mentre BTC ed ETH perdono il 4-6%",
   web_source="CoinGecko (snapshot radar 07:00 UTC) / DefiLlama",
   date="2026-11-15",
   links=['https://www.coingecko.com/en/coins/venice-token', 'https://defillama.com/protocol/venice'],
   extra_x=['2121859088090833247'],
   synth="Snapshot CoinGecko delle 07:00 UTC: VVV 19,35 $ (+7,2% in 24 ore), volume 61,0 mln $, market cap 947,7 mln $. DefiLlama nello stesso intervallo dà 19,25 $, market cap 942,8 mln $, volume 24h 63,43 mln $ e 617,98 mln $ di VVV in staking (65,55% della capitalizzazione). Su X un post rileva VVV in rialzo del ~7% da un minimo a 30 giorni di ~16,8 $ con BTC a -4% ed ETH a -6%.",
   nota="Il campo «TVL» del radar (1.235.965.679 $) non è verificabile: la pagina DefiLlama mostra TVL 0 $ e tratta lo staking come serie separata; il valore del radar sembra sommare staking e altre voci. Prezzo e market cap sono snapshot a orari diversi e vanno attribuiti alla fonte.")),
 ('venice', dict(
   title="Burn discrezionale record: 21.657 VVV (~458.000 $) il 9 novembre",
   web_source="TokenPost / CoinMarketCap Top Stories / VeniceStats",
   date="2026-11-09",
   links=['https://www.tokenpost.com/news/investing/53362',
          'https://coinmarketcap.com/th/top-stories/6af308506dcd1d4966205a2b/',
          'https://venicestats.com/report/2026-W45'],
   synth="Venice ha bruciato 21.657 VVV su Base il 9/11 per circa 458.000 $, il burn discrezionale più grande finora: +10% rispetto ai 414.000 $ di ottobre, ~0,04% della supply circolante (~48,9 mln) e circa un ottavo delle emissioni mensili (2 mln VVV/anno dal 1° ottobre). Il ciclo di buyback in corso aveva accumulato 533.464 USDC (23.439 VVV), circa il doppio della spesa del ciclo di ottobre, con utilizzo di DIEM al 49,5% (+4,3 punti).",
   nota="Il valore in dollari dipende dal prezzo al momento del burn; le fonti lo pubblicano tra il 10 e il 14/11. Il burn copre solo una parte delle nuove emissioni: la supply netta dipende dal saldo tra i due flussi.")),
 ('venice', dict(
   title="VeniceStats: «Revenue ATH and burn ATH on the same day»",
   x=['2121394983945056479'],
   synth="«Revenue ATH and burn ATH on the same day, in the worst week for $VVV in a while. Noted 📊 @AskVenice»",
   nota="L'account non pubblica i valori dei due record: il burn ATH del 9/11 (~458.000 $) è confermato da altre fonti, il record di ricavi no. Da trattare come indizio, non come dato.")),
 ('venice', dict(
   title="KR1 mette in staking 275.000 VVV al 5,74% annuo e usa DIEM per i crediti di inference",
   web_source="KR1 plc (RNS) / 6ix",
   date="2026-11-12",
   links=['https://www.investegate.co.uk/index.php/announcement/rns/kr1-plc--kr1/update-venice-infrastructure-operations/9871193',
          'https://6ix.com/news/update-venice-infrastructure-operations'],
   synth="La società quotata a Londra ha messo in staking l'intero holding di 275.000 VVV, con un rendimento indicativo del 5,74% annuo all'11/11; il DIEM, acquistato separatamente, è stakato per ottenere crediti giornalieri di inference rivenduti tramite marketplace terzi. L'annuncio ricorda che il 5% degli acquisti di crediti API alimenta il buy-and-burn di VVV e che al 28/10 il valore bruciato a ottobre aveva superato 1 mln $.",
   nota="Dato di società quotata, non un comunicato di Venice: il rendimento del 5,74% è indicativo e varia.")),
 ('crypto', dict(
   title="Bitcoin sotto i 65.000 $: -14% in una settimana, il mercato perde i minimi di venerdì",
   x=['2121646733650190650', '2121272939224109179'],
   synth="«BREAKING: Bitcoin falls below $65,000 HODL!» Il pezzo di Bitcoin Magazine registrato dal radar parla di un -14% in una settimana e della rottura dei minimi di venerdì; CoinDesk sottolinea che il 2026 è in calo di oltre il 21% dopo il -6,3% del 2025 e che servirebbe un recupero sopra 87.500 $ entro fine anno per evitare il primo doppio calo annuale della storia del Bitcoin.",
   nota="Prezzi da fonti diverse e a orari diversi: l'indice prezzi di Cointelegraph alle 07:00 UTC del 15/11 dava BTC 64.499 $ (-4,20% in 24 ore) ed ETH 1.797 $ (-5,69%).")),
 ('crypto', dict(
   title="ETF spot Bitcoin: -1,07 miliardi nella settimana, secondo consecutivo sopra il miliardo",
   web_source="The Block (dati SoSoValue)",
   date="2026-11-14",
   links=['https://www.theblock.co/news/markets/2026-11-14-bitcoin-etfs-lose-1-billion-for-the-second-week-in-a-row-as-crypto-funds-except-one-continue-bleeding-440337',
          'https://sosovalue.com/assets/etf/us-btc-spot'],
   synth="I 12 ETF spot USA sul bitcoin hanno registrato 1,07 mld $ di deflussi netti la settimana scorsa, seconda settimana consecutiva sopra il miliardo; la serie negativa dura sette sedute per 1,91 mld $ (la più lunga dal 17/6-1/7). Nelle ultime due settimane gli ETF bitcoin hanno perso 2,35 mld $. Venerdì BlackRock IBIT ha pesato per 143,5 mln $ (~77% del totale) e detiene bitcoin per 53,99 mld $; sull'intero comparto crypto ETF spot USA sono usciti ~1,55 mld $, con l'unico afflusso (227.000 $) sui fondi Avalanche.",
   nota="Elaborazione The Block su dati SoSoValue.")),
 ('crypto', dict(
   title="Kava Lend perde ~3,8 milioni in un exploit sul mercato BUSD: KAVA giù di quasi il 40%",
   web_source="The Block",
   date="2026-11-14",
   links=['https://www.theblock.co/news/defi/2026-11-14-kava-lend-loses-roughly-3-8-million-to-hack-sending-kava-token-down-nearly-40-440350',
          'https://bscscan.com/address/0x37D732914F86Cc6eb1E87419e3046A739F011042'],
   synth="L'attaccante ha gonfiato di circa 243.000 volte il valore dei depositi nel mercato dormiente BUSD di Kava Lend, poi ha preso in prestito KAVA 127 volte contro quel collaterale; circa 49,2 mln di KAVA sono stati trasferiti su BNB Chain via LayerZero e venduti per ~2,09 mln $ tra BNB e USDT. Perdita stimata ~3,8 mln $. Kava ha sospeso «per cautela» il bridge Axelar, precisando che il KAVA drenato è uscito via LayerZero.",
   nota="Importo e dinamica da dati onchain esaminati da The Block; Kava ha annunciato un incident report completo non ancora pubblicato.")),
 ('crypto', dict(
   title="Trump nomina quattro commissari per SEC e CFTC, ripristinando i quorum",
   web_source="The Block / Cointelegraph",
   date="2026-11-13",
   links=['https://www.theblock.co/newsletters/the-daily/2026-11-14-meta-prediction-market-app-doj-binance-hack-more-crypto-news-440304',
          'https://cointelegraph.com/news/trump-nominates-hester-peirce-successor-among-sec-cftc-picks'],
   synth="La Casa Bianca ha nominato Nathan Anonick e Matthew Rowland al CFTC e Kristin Johnson e Steven Levine alla SEC; Anonick e Rowland hanno lavorato al Clarity Act e Johnson è ex commissaria CFTC. Cointelegraph titola sulla «successora di Hester Peirce» alla SEC.",
   nota="Le nomine arrivano dopo lo stallo del Clarity Act in Senato a settembre e in vista della sessione lame-duck; le conferme non sono ancora avvenute.")),
 ('crypto', dict(
   title="Clarity Act: «l'85% va bene», lo scontro resta sul 15% delle norme DeFi",
   x=['2121706485642375449'],
   synth="Justin Slaughter (Paradigm): «Even they will admit that 85% of Clarity is fine. We're fighting over that remaining 15%.» Nel post si parla di margini per un accordo bipartisan, con le norme sulla DeFi come principale punto di rottura.",
   nota="È la lettura di un lobbista del settore, non un testo di legge né una dichiarazione del Congresso.")),
 ('crypto', dict(
   title="Il protocollo RWA stUSDT chiude dopo un picco di TVL di 2,3 miliardi",
   web_source="Cointelegraph / stUSDT",
   date="2026-11-15",
   links=['https://cointelegraph.com/news/rwa-protocol-stusdt-winds-down-three-years-after-23b-tvl-peak',
          'https://medium.com/@stusdt/important-notice-stusdt-protocol-orderly-unwinding-and-redemption-guide-87b6485b0a1d'],
   synth="stUSDT ha avviato la chiusura: gli interessi su stUSDT sono cessati sabato e i detentori di stUSDT e wstUSDT possono riscattare tramite il portale ufficiale fino al 14 maggio 2027; le richieste tardive saranno gestite in lotti mensili fino ad agosto 2027. Il team non ha indicato le ragioni e assicura che gli asset sottostanti restano interamente coperti.",
   nota="Il protocollo aveva raggiunto 2,3 mld $ di TVL; la chiusura segue altre uscite nel comparto RWA.")),
 ('crypto', dict(
   title="Thailandia: bozza di regole stablecoin con tetto di 5 milioni di baht al giorno per cliente",
   web_source="SEC Thailandia / Cointelegraph",
   date="2026-11-12",
   links=['https://www.sec.or.th/EN/Pages/News_Detail.aspx?SECID=13562',
          'https://cointelegraph.com/news/thailand-tighter-stablecoin-rules-crypto-exchange'],
   synth="La SEC thailandese ha posto in consultazione una bozza che limita a 5 mln di baht (~148.000 $) al giorno per cliente e per operatore i trasferimenti di stablecoin, ammettendo solo wallet verificati come appartenenti allo stesso cliente, con applicazione della Travel Rule e strumenti di analisi blockchain. Audizione pubblica aperta fino al 26 novembre.",
   nota="La bozza è in consultazione: non è una norma in vigore.")),
]

out = []
out.append("# Report — 2026-11-15")
out.append("Data: 2026-11-15")
out.append("Fonte: feed primari gratuiti (radar) + X/Twitter via xurl + ricerca web")
out.append("Finestra di scansione: ultime 24-48 ore")
out.append("Esecuzione: 13 chiamate xurl su 13 (3 keyword + 9 nucleo fisso + 1 rotazione: simonw), 6 chiamate web_search su 6, radar: ok")
out.append("")

heads = [('hermes', '## Hermes AI'), ('venice', '## Venice.ai / VVV / DIEM'), ('crypto', '## Bitcoin & Crypto')]
counts = {}
for key, head in heads:
    out.append(head)
    n = 0
    for pillar, spec in SPEC:
        if pillar != key:
            continue
        n += 1
        out.append(f"### {n}. {spec['title']}")
        links = []
        date = spec.get('date')
        metrics_line = "non disponibili"
        if spec.get('x'):
            primary = by_id[spec['x'][0]]
            handle = primary['user']
            out.append(f"- **Account**: @{handle}")
            date = (primary['created_at'] or '')[:10]
            for pid in spec['x']:
                it = by_id[pid]
                links.append(f"https://x.com/{it['user']}/status/{it['id']}")
            metrics_line = metrics(primary)
            excerpt = spec['synth']
            if not excerpt.startswith('«'):
                excerpt += f' (citazione: «{snippet(primary["text"])}»)'
        else:
            out.append(f"- **Fonte**: {spec['web_source']}")
            for l in spec['links']:
                links.append(l)
            for pid in spec.get('extra_x', []) or []:
                it = by_id[pid]
                links.append(f"https://x.com/{it['user']}/status/{it['id']}")
            excerpt = spec['synth']
        out.append(f"- **Data**: {date}")
        out.append(f"- **Estratto**: {excerpt}")
        out.append(f"- **Link**: {' ; '.join(links)}")
        out.append(f"- **Metriche**: {metrics_line}")
        if spec.get('nota'):
            out.append(f"- **Nota**: {spec['nota']}")
        out.append("")
    counts[key] = n

out.append(f"Item: hermes={counts['hermes']} venice={counts['venice']} crypto={counts['crypto']}")
out.append("Errori: CoinDesk non raggiungibile dal radar (HTTP 403) — copertura crypto affidata a Cointelegraph, The Block, Bitcoin Magazine; feed RSS di Bitcoin Magazine in Cloudflare (0 <pubDate>), quindi nessun secondo link dal feed; il campo TVL Venice del radar (1.235.965.679 USD) non corrisponde alla pagina DefiLlama (TVL 0 USD, staking 617,98 mln USD come serie separata); la rotazione simonw ha restituito 10 post ma nessuno pertinente ai tre pilastri; catalogo plugin su raw.githubusercontent vuoto (14 byte), plugin Workbench verificato solo via marketplace e post X; «Revenue ATH» di @venicestats non confermato da valori pubblicati.")
out.append("<!-- report-status: 2026-11-15 complete hermes=%d venice=%d crypto=%d -->" % (counts['hermes'], counts['venice'], counts['crypto']))

txt = "\n".join(out) + "\n"
path = f'{BASE}/reports/2026-11-15-report.md'
open(path, 'w').write(txt)
print("scritto", path, len(txt), "byte")
print("counts", counts)
