---
name: defi-attack-patterns
description: DeFi attack pattern playbook. Use when analyzing flash loan attacks, price oracle manipulation, MEV sandwich attacks, governance exploits, bridge vulnerabilities, and token standard edge cases in decentralized finance protocols.
scope: web3
---
DeFi attack pattern playbook. Use when analyzing flash loan attacks, price oracle manipulation, MEV sandwich attacks, governance exploits, bridge vulnerabilities, and token standard edge cases in decentralized finance protocols.

# SKILL: DeFi Attack Patterns — Expert Attack Playbook

> **AI LOAD INSTRUCTION**: Expert DeFi exploitation techniques. Covers flash loan mechanics, oracle manipulation (spot vs TWAP), MEV extraction (sandwich, JIT, liquidation), precision loss attacks, governance exploits, bridge vulnerabilities, and token standard pitfalls. Base models often miss the single-transaction atomicity constraint of flash loans and the distinction between spot price and TWAP manipulation.


## 1. FLASH LOAN ATTACKS

### 1.1 Mechanism

Flash loans provide uncollateralized borrowing within a single transaction. The entire borrow → use → repay cycle must complete atomically; if repayment fails, the transaction reverts as if nothing happened.

| Provider | Max Amount | Fee |
|---|---|---|
| Aave V3 | Pool liquidity per asset | 0.05% (can be 0 for approved borrowers) |
| dYdX | Pool liquidity | 0 (uses internal balance manipulation) |
| Uniswap V3 | Pool liquidity per pair | 0.3% (swap fee tier) |
| Balancer | Pool liquidity | Protocol-configurable |

### 1.2 Price Oracle Manipulation

1. Flash borrow 100,000 WETH
2. Swap 100,000 WETH → TOKEN on AMM_A
   → TOKEN spot price on AMM_A skyrockets
3. On Lending_Protocol (reads AMM_A spot price as oracle):
   → Deposit small TOKEN collateral (valued at inflated price)
   → Borrow large amount of WETH against it
4. Swap TOKEN back → WETH on AMM_A (restore price)
5. Repay flash loan (100,000 WETH + fee)
6. Keep borrowed WETH from Lending_Protocol minus collateral cost

**Key insight**: protocols using AMM spot reserves (getReserves()) as price oracles are vulnerable. Must use TWAP or external oracle (Chainlink).

### 1.3 Liquidity Pool Drain via Reentrancy

Flash borrow → deposit into pool → trigger reentrancy during callback → withdraw more than deposited → repay loan.

Exploits the combination of flash loan capital with reentrancy in pool accounting logic.

### 1.4 Governance Flash Borrow

1. Flash borrow governance tokens
2. Create/vote on malicious proposal (if no snapshot or timelock)
3. Proposal passes instantly
4. Execute proposal (drain treasury, change admin, etc.)
5. Return governance tokens

Defense: snapshot-based voting (Compound Governor Bravo), timelocks, minimum proposal period.

---

## 2. PRICE OR
...

## References
- Source: https://github.com/yaklang/hack-skills/blob/main/skills/defi-attack-patterns/SKILL.md
- License: MIT — Copyright (c) 2026 VillanCh
- Distilled for bbhunter by scripts/import_hack_skills.py
