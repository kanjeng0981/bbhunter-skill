---
name: meme-coin-audit
description: Meme coin and token security audit — rug pull detection (honeypot, hidden mint, fee manipulation, LP lock bypass), Solana SPL token analysis (freeze authority, mint authority, metadata mutability), Token-2022 extension risks (transfer hooks, permanent delegate), DEX liquidity pool attacks (sandwich amplification, LP drain, bonding curve exploits), pump.fun/Raydium/Jupiter integration risks, and real exploit examples from 2024-2025. Use for any token audit, rug pull assessment, meme coin security review, or pre-investment due diligence.
scope: web3
---
Meme coin and token security audit — rug pull detection (honeypot, hidden mint, fee manipulation, LP lock bypass), Solana SPL token analysis (freeze authority, mint authority, metadata mutability), Token-2022 extension risks (transfer hooks, permanent delegate), DEX liquidity pool attacks (sandwich amplification, LP drain, bonding curve exploits), pump.fun/Raydium/Jupiter integration risks, and real exploit examples from 2024-2025. Use for any token audit, rug pull assessment, meme coin security review, or pre-investment due diligence.

- **Auditing without Solidity knowledge** — Web3 auditing requires understanding of reentrancy, delegatecall, tx.origin, and access control patterns specific to smart contracts.
- **Unverified contract without source** — you can't audit what you can't read. Use decompilers (Dedaub, Panoramix) but acknowledge limitations.
- **Front-running without practical exploit** — MEV is a known design consideration, not always a vulnerability. Demonstrate actual fund extraction.
- **Tokenomics flaws as security bugs** — inflation bugs, minting flaws, and fee manipulation are finance issues unless they enable unauthorized token creation.
- **Ignoring proxy patterns** — UUPS, Transparent, and Beacon proxies have different upgrade risks. Audit the proxy implementation separately from the logic contract.


---

## References
- Source: https://github.com/uphiago/recon-skills/blob/main/redteam/meme-coin-audit/SKILL.md
- License: MIT — Copyright (c) 2025 Hiago Felipe
- Distilled for bbhunter by scripts/import_recon_skills.py
