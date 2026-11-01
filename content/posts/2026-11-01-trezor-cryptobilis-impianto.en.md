---
title: "The Box Was Right. The Circuit in the Middle Wasn't"
date: 2026-11-01
draft: false
categories: ["Crypto", "Blockchain"]
tags: ["Trezor", "Ledger", "hardware wallet", "supply chain", "CryptoBilis"]
summary: "A Safe 5 bought in Indonesia carried an extra board between the motherboard and the screen. After Ledger, Trezor drops the reseller and warns users."
url: "/en/2026/11/trezor-cryptobilis-impianto/"
---

The customer noticed from the weight. Inside a Trezor Safe 5 bought in August on Tokopedia, between the main board and the screen, there was an extra circuit, with a cellular module and an antenna. According to the person who reported it, the board reads what appears on the display — including the recovery phrase — and transmits it over the mobile network every time the device is connected.

Trezor received the report on 28 October, interviewed the customer over a video call, and does not yet have the device in the lab. It decided to warn everyone anyway.

## Why warn before you've seen it

"We preferred to warn now rather than wait for confirmation and find out in the meantime that someone had lost funds," said chief commercial officer Danny Sanders. The company also stressed that no buyer from CryptoBilis has reported losses to it, and that the customer who reported the implant had already moved his funds before noticing.

The warning covers every Trezor model bought from the reseller from March 2026 onward. Anyone who has already used the device must create a new wallet with a new phrase; restoring the old phrase on another device does not fix it.

## Ledger first, same reseller

CryptoBilis was an authorised reseller in Indonesia, Malaysia and the Philippines. Ledger opened an investigation on 9 October and later confirmed the presence of an unauthorised implant in one affected device. The loss estimates come from on-chain analysts, not from the company: between $72 million and $93 million according to Specter and tanuki42, about $87 million tracked by Arkham. On 28 October Singapore police issued a warning about tampered Ledger wallets bought in shops in the country.

Trezor removed CryptoBilis from its network on 9 October, the same day Ledger halted the reseller's sales.

## The defence was looking elsewhere

The checks a hardware wallet runs on first boot look for modified firmware and counterfeit devices. This implant does not touch the firmware: it reads pixels. A Trezor spokesperson admitted that seals and packaging alone are not enough. The device's cryptography stayed intact; it was bypassed by watching the screen.

## What's left to do

Anyone who bought from CryptoBilis since March 2026 and has not yet set up the device should not do so, and should not type an existing phrase into it. Anyone using one should move everything to a new wallet, checking the receiving address in full. Trezor is shipping a replacement device or a voucher to those who request one through support. And the immediate risk after news like this is not technical: it is the fake emails, letters and phone calls from people offering to recover your funds.

Self-custody is sold as giving up on trusting someone. In practice it moves trust onto a chain of hands — factory, courier, reseller, counter — that no user sees and no cryptographic signature covers.

---

*Verified sources: Trezor, "Implant reported in a Trezor sold by CryptoBilis" (official blog, 30 October 2026: report of 28 October, Safe 5 device bought in August on Tokopedia, technical details of the implant, instructions and replacements); Cointelegraph, "Trezor warns CryptoBilis buyers over suspected wallet implant", 30 October 2026 (Danny Sanders statement, Ledger background); The Block, "Trezor reports suspected hardware implant in Safe 5 sold by CryptoBilis", 30 October 2026; Decrypt, 30 October 2026; Crypto Briefing, "Ledger investigates wallet tampering tied to tens of millions in crypto thefts", 10 October 2026 (Specter, tanuki42, Arkham estimates); DeFiPrime, "Singapore police warn of tampered Ledger hardware wallets", 29 October 2026.*
