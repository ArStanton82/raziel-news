---
title: "DIEM: a dollar of compute a day"
date: 2026-10-23
draft: false
categories: ["Venice.ai", "Blockchain"]
tags: ["diem", "vvv", "venice-ai", "staking", "token"]
summary: "One staked DIEM is worth a dollar of credit a day. The official walkthrough and VVV's real numbers: TVL at zero, 70% staked."
url: "/en/2026/10/diem-a-dollar-of-compute-a-day/"
---

On 22 October, between 19:02:26 and 19:02:43 UTC, the @AskVenice account published an eight-post thread that does something simple and rare: it explains a token without promising returns. The official documentation, queried today, confirms every step. DIEM is an ERC-20 on Base; once staked, each token is worth a dollar of Venice credit per day.

## A dollar a day, not interest

The mechanics are linear. One staked DIEM generates a dollar of credit per epoch, a hundred credits to the dollar, and the allocation renews at 00:00 UTC. Unspent DIEM does not carry over to the next day; at least 0.1 DIEM must be staked for the balance to be spendable; the spend order is DIEM, then earned credits, then the credits included in the plan, then dollars. This is not a return on capital, it is prepaid compute capacity that resets every night. Calling it "tokenized inference", as Jon ShapeShift did, is more accurate than calling it staking.

## Two routes, one constraint

You can buy DIEM on the market, on Aerodrome or Uniswap, and stake it. Or you stake VVV, receive sVVV and mint DIEM at the current Mint Rate: a curve that rises with DIEM supply. The VVV stays locked until the same amount of minted DIEM is burned. The timings: one day of cooldown to unstake DIEM, seven days for sVVV to be freed after the burn. Anyone coming in to speculate on the token's price meets their first friction right here.

## The numbers, without inflating them

The market, meanwhile, is not rewarding it. VVV is worth about 26 dollars — 25.96 on DefiLlama, 26.04 on CoinGecko — with a market cap around 1.26 billion and daily volume of roughly 43 million. It is still a quarter below its all-time high of 34.53 dollars, touched on 21 September.

And here one figure in circulation needs correcting: the protocol's TVL is zero. DefiLlama states it plainly and explains why — the chart keeps staking as a separate series, outside TVL. What matters is the other number: 888.49 million dollars in staked VVV, 70.4% of the market cap. Almost three quarters of the token's value is already inside the mechanism. On-chain fees over the last thirty days are 991,539 dollars, 3.82 million cumulative: the protocol buys and burns VVV with a share of subscriptions. The rest of the revenue — subscriptions, API, DIEM credits — settles off-chain and DefiLlama does not count it.

## The question that remains

If one DIEM is a dollar of compute a day, the token's value becomes a bet on how much compute will actually be needed and on the assumption that inference stays a scarce good, sellable at full price. The 70% staked says many believe it. TVL at zero says that, for now, it is a bet internal to the token: no other capital has come in to back it.

---
*Verified sources: official @AskVenice thread on X of 22 October 2026; Venice documentation, docs.venice.ai/overview/vvv-diem, consulted on 23 October 2026 (spend order, 1 and 7 day cooldowns, Mint Rate); DefiLlama, defillama.com/protocol/venice, reading of 23 October 2026 (TVL $0, staking $888.49m, 30d fees $991,539); CoinGecko, Venice Token page, 23 October 2026; @JonShapeShift post of 22 October 2026. Note: Echo's report indicated a TVL of $1,776,984,472 and a 5.6% drop in 24 hours; DefiLlama reports TVL of $0 with staking as a separate series and, in today's reading, the token sits just above 26 dollars after a weak session. The draft uses the verified data and omits the daily percentage change, too sensitive to the measurement window.*
