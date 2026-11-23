#!/bin/bash
cd /root/.hermes/profiles/raziel-news/workspace/raziel-news/reports/x-2026-11-22
for s in chainflip-12m-crypto-hack-10-percent-bounty wrapped-monero-token-crashes-998-amid-suspected-135m-exploit ecb-tokenized-deposits-securities-experiments-appia hong-kong-crypto-custody-advisory-licensing-bill us-prediction-market-whistleblower-rewards-30-percent sky-protocol-sees-2b-in-stablecoin-withdrawals-disputes-illicit-fund-claims binance-hacker-600m-eth-routes-thorchain-chainflip what-happened-in-crypto-today; do
  f="ct-$s.htm"
  curl -s -A "Mozilla/5.0" "https://cointelegraph.com/news/$s" -o "$f"
  echo "=== $s  size=$(wc -c < "$f")"
  grep -oE '"datePublished":"[^"]{10,25}' "$f" | head -1
  grep -oE '<title>[^<]*' "$f" | head -1
  grep -oE 'href="https?://[^"]*"' "$f" | grep -viE 'cointelegraph|twitter|facebook|linkedin|telegram|youtube|instagram|t\.me|google|apple|spotify|cloudflare|schema\.org|w3\.org|formulaagency|ct-api\.org|adbutler' | sort -u | head -6
done
