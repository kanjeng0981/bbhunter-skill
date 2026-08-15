---
name: web3-fuzz-invariants
description: Invariant and fuzzing harness design (adapted from Pashov's fizz)
scope: web3
---
Stateful invariant / fuzzing harness design (Echidna/Medusa) checklist:

1. **Invariant categories to target**: accounting/conservation (sum of
   balances == totalSupply), authorization, token conservation, oracle
   assumptions, deposit/withdraw symmetry, liquidation health, upgrade
   state, and fee bounds.
2. **Entry-point selection**: prioritize core user flows (deposit, withdraw,
   mint, redeem, borrow, repay, swap, stake, claim, liquidate) as primary;
   demote admin setters/parameter changes to secondary.
3. **Handler design**: clamp inputs to valid ranges, vary caller roles, and
   add boundary-value stress variants.
4. **Setup fidelity**: reuse the project's existing deployment and mock setup
   rather than inventing a new one.
5. **Coverage**: drive core protocol contracts to high coverage before
   trusting "no bug found".
6. **Use fuzzing to validate hypotheses**: a fuzz run falsifies or confirms a
   concrete invariant; it is not a replacement for exploit reasoning.

## References

- Source: https://github.com/pashov/skills/blob/main/fizz/SKILL.md
- License: MIT (per upstream metadata). This file is a distilled summary of the
  upstream skill's methodology, adapted for bbhunter.
