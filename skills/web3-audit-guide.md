---
name: web3-audit-guide
description: Master EVM/Solidity audit checklist — attack lenses, DeFi bug classes, and reentrancy
scope: web3
---
EVM/Solidity audit guide. Combine the lenses below with the real-world bug
frequencies in `web3-real-world-bugs`.

## Attack lenses (apply to every function)
1. **Math / precision** — rounding direction, precision loss, overflow/underflow,
   share-price math, division-before-multiplication.
2. **Access control** — missing/incorrect modifiers, role confusion, ownership
   transfer, unprotected `initialize()`.
3. **Economic security** — tokenomics, fees, incentives, value extraction,
   redeem/claim manipulation.
4. **Execution trace** — follow the full call path from entry point to sink.
5. **Invariants** — state properties that must hold across all call sequences.
6. **Periphery** — external protocol interactions, composability, oracles.
7. **First principles** — re-derive behavior from scratch, don't trust names.
8. **Asymmetry** — attacker cost vs defender loss.
9. **Boundary** — edge cases, limits, empty sets, zero amounts, min/max.
10. **Numerical gap** — stored number vs what the code uses (scaling, decimals).
11. **Trust gap** — assumptions about trusted actors (admin, keeper, oracle).
12. **Flow gap** — missing or reorderable steps between related functions.

## DeFi bug classes (highest-impact patterns)
- **Accounting state desync** — two vars meant to stay in sync; one path updates
  A but not B. Watch for phantom yield, fast-path early `return` skipping state
  updates, and updates in the wrong order (shares computed before assets move).
- **Access control** — missing modifier on a *sibling* function (read ALL
  siblings: `vote` guarded but `poke` not), existence-vs-ownership checks
  (`_requireOwned` vs `ownerOf`), silent `if`-modifiers that don't revert,
  uninitialized proxy (`initialize()` callable by anyone).
- **Incomplete code path** — paired flows (`place/update`, `deposit/withdraw`,
  `mint/burn`): does the reverse do the reverse of every state change? Missing
  refunds, `mint()` bypassing `deposit()` validation.
- **Off-by-one / boundary** — `>` vs `>=` at period/epoch ends, `i <= length`,
  loop breaks, rounding-to-zero at exact balances.
- **Oracle / price** — stale price (no `updatedAt` / `price > 0` check), Pyth
  confidence interval ignored, TWAP too short, single-source spot price.
- **ERC4626** — first-depositor exchange-rate manipulation (use virtual
  shares), `transfer` moving shares without moving lock/stake records.
- **Flash loan** — spot-price reads manipulable within one block.
- **Signature replay** — signed hash missing nonce / chainId / contract address.
- **Proxy / upgrade** — storage collision, uninitialized implementation.

## Reentrancy
- Enumerate external calls (`.call`/`.transfer`/`.send`, transfers to untrusted
  contracts).
- Verify CEI (checks-effects-interactions) ordering.
- Check missing `nonReentrant` on fund-moving functions.
- Cross-function reentrancy (sibling relying on stale state) and read-only
  reentrancy (views returning stale data used by other protocols).

## General checks
- Unchecked return values of low-level calls.
- `tx.origin` vs `msg.sender` confusion.
- Front-running / MEV: uncommitted ordering, slippage, oracle manipulation.
- DoS: gas griefing, unbounded loops, external-call reverts.
- Upgradeability: storage collision, uninitialized implementation.

## Finding discipline
Every finding: one-sentence root cause + minimal fix + concrete proof (numbers,
a trace, or quoted code). Without proof it is a LEAD, not a finding.

## References

- Pashov solidity-auditor (MIT): https://github.com/pashov/skills/blob/main/solidity-auditor/SKILL.md
- uphiago/recon-skills web3-audit (MIT): https://github.com/uphiago/recon-skills/blob/main/redteam/web3-audit/SKILL.md
- DASP: http://www.dasp.co/
