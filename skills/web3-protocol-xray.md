---
name: web3-protocol-xray
description: Pre-audit protocol reconnaissance (adapted from Pashov's x-ray)
scope: web3
---
Pre-audit protocol reconnaissance checklist (before deep vulnerability hunting):

1. **Entry points**: enumerate every external/public function and classify it
   as permissionless, role-gated, or admin-only. Record caller, parameters
   (and their trust level), state modified, value flow (in/out/none), and
   reentrancy guard.
2. **Actors & trust boundaries**: list every privileged role (owner, admin,
   keeper, operator) and what each can do instantly vs timelocked.
3. **Value-holding state**: map balances, collateral, shares; for each
   state-changing function record the delta writes (Δ(var) = +expr).
4. **Invariants**: synthesize properties across categories — conservation
   (A + B = const), bounds, ratios, state-machine transitions, temporal
   (timestamps/deadlines), cross-contract assumptions, and economic
   derivations. Mark each as verified on-chain vs unguarded.
5. **Centralization & pause coverage**: which critical functions are pausable,
   which roles can extract/redirect funds.
6. **Protocol classification**: identify the protocol type (lending, DEX, CDP,
   staking, bridge, etc.) to focus on its typical failure modes.
7. **Backwards-compat remnants**: flag dead/legacy code that is no longer
   called but still in storage layout.

## References

- Source: https://github.com/pashov/skills/blob/main/x-ray/SKILL.md
- License: MIT (per upstream metadata). This file is a distilled summary of the
  upstream skill's methodology, adapted for bbhunter.
