#!/usr/bin/env bash
# Stadio 1 - rete fonti X: 3 keyword + 9 nucleo fisso + 1 rotazione = 13 chiamate
cd "$(dirname "$0")" || exit 1
D="$(cd "$(dirname "$0")" && pwd)"

run() {
  local name="$1"; shift
  local q="$1"; shift
  xurl search "$q" -n 10 > "$D/$name.json" 2> "$D/$name.err"
  echo "$name rc=$? bytes=$(wc -c < "$D/$name.json")"
}

# --- 3 keyword ---
run kw-hermes "(Hermes AI OR Hermes Agent OR Nous Research) lang:en -is:retweet"
run kw-venice "(Venice.ai OR VVV token OR DIEM token OR Erik Voorhees) lang:en -is:retweet"
run kw-crypto "(Bitcoin OR stablecoin OR blockchain) lang:en -is:retweet"

# --- 9 nucleo fisso ---
run from-HermesWatcher "from:HermesWatcher lang:en -is:retweet"
run from-NousResearch "from:NousResearch lang:en -is:retweet"
run from-Teknium "from:Teknium lang:en -is:retweet"
run from-venicestats "from:venicestats lang:en -is:retweet"
run from-AskVenice "from:AskVenice lang:en -is:retweet"
run from-JonShapeShift "from:JonShapeShift lang:en -is:retweet"
run from-CoinDesk "from:CoinDesk lang:en -is:retweet"
run from-BitcoinMagazine "from:BitcoinMagazine lang:en -is:retweet"
run from-VitalikButerin "from:VitalikButerin lang:en -is:retweet"

# --- 1 rotazione: giorno 10 -> (10 mod 8)+1 = 3 -> SECGov ---
run from-SECGov "from:SECGov lang:en -is:retweet"
