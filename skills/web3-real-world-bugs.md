---
name: web3-real-world-bugs
description: Real-world bug frequency from 850+ on-chain exploits and 866 audit findings
scope: web3
---
Real-world bug patterns, weighted by frequency. Two independent datasets agree:
modern DeFi bugs cluster around oracle/price, business logic/accounting, and
math — NOT reentrancy. Use this to prioritize, paired with `web3-audit-guide`.

## On-chain exploits (850+ reproduced incidents)
1. **Price / oracle manipulation (~24%)** — spot reads from reserves
   (`getReserves`/`slot0`), short TWAP, stale oracle, skim/reserve mismatch
   after flash-swaps, reward recycling via flash-loaned liquidity.
2. **Business logic / accounting (~26%)** — late `syncRewards()`, double
   settlement/claim, reward deflation/recycling, payoff mispricing, interest
   boundaries.
3. **Access control / permission (~14%)** — unprotected `claim()`/forwarder,
   permissionless registration, missing auth on siblings, allowance sweep,
   `ecrecover` address(0) bypass.
4. **Rounding / precision / math (~14%)** — rounding direction, reserve
   mismatch, issue boundary, split-invariance violations.
5. **Signature (~6%)** — replay, broken verification, missing nonce/chainId.
6. **Arbitrary call / delegatecall** — call injection via unvalidated
   forwarding, callback price-spread, wrong approval.
7. **Flash loan** — levers other bugs, not a bug itself.
8. **Governance** — takeover of abandoned governors, timeout exploits.
9. **Newer vectors** — EIP-7702 self-delegation, TOCTOU via pre-issue hooks,
   uninitialized proxies, owner backdoors / insider rug pulls.
10. **Reentrancy** — rare recently (<1%); still verify CEI.

## Audit findings (866 findings / 87 audits; ~20% Crit/High, 29% Medium, 51% Low/Info)
1. **Oracle / price / frontrunning** — donation attacks on vault-rate oracles,
   stale/future-timestamp oracles, wrong price-feed units (USD vs EUR), missing
   `minShares`/slippage bounds, pool-init frontrunning (Uniswap v4).
2. **DoS / griefing / gas** — revert-on-edge bricks reads, flows broken when a
   dependency is paused/frozen/at-cap, cancel-before-batch, unbounded loops.
3. **Math / rounding / precision** — mulDiv guards firing before the real
   guard, decimal mismatch (WBTC 8 decimals), precision-loss reverts, rounding
   that drains accumulated yield.
4. **Input validation** — missing `address(0)`, unchecked return values,
   missing bounds, unsafe assembly.
5. **Proxy / upgrade / storage** — layout drift, initializer frontrunning,
   interface/implementation mismatch.
6. **Liquidation** — `maxLiquidatable` ignoring the bonus, leverage-vs-
   liquidation contradictions, repay on paused assets.
7. **Access control** — missing/wrong modifiers, approvals not reset, role read
   from wrong source.
8. **Signature / replay / nonce** — missing signed params, replay, unchecked
   permit timestamp.
9. **Reentrancy** — missing `nonReentrant` on token callbacks, execution-path
   reentrancy.
10. **Flash loan** — direct `onFlashLoan()` call, unchecked beneficiary.

## Target triage (DeFi)
Skip low-payoff targets: TVL < ~$500K, 2+ top-tier audits on a simple protocol,
< 500 lines single A→B→C flow. Rough ceiling: `min(10% × TVL, program cap)`.

## References

- DeFiHackLabs (850+ exploits + root causes): https://github.com/SunWeb3Sec/DeFiHackLabs
- DeFi Hack Incidents Explorer: https://defihacklabs.io/explorer/index.html
- 0xSimao findings (866 / 87 audits): https://0xsimao.com/findings
