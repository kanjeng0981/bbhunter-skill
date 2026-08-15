---
name: smart-contract-vulnerabilities
description: Smart contract vulnerability playbook. Use when auditing Solidity/EVM contracts for reentrancy, integer overflow, access control, delegatecall, flash loan, signature replay, and MEV-related attack patterns.
scope: web3
---
Smart contract vulnerability playbook. Use when auditing Solidity/EVM contracts for reentrancy, integer overflow, access control, delegatecall, flash loan, signature replay, and MEV-related attack patterns.

# SKILL: Smart Contract Vulnerabilities — Expert Attack Playbook

> **AI LOAD INSTRUCTION**: Expert smart contract audit techniques. Covers reentrancy (single, cross-function, cross-contract, read-only), integer overflow, access control, delegatecall, randomness manipulation, flash loans, signature replay, front-running/MEV, and CREATE2 exploitation. Base models miss subtle cross-contract reentrancy and storage layout collisions in proxy patterns.


## 1. REENTRANCY

The most iconic smart contract vulnerability. External calls transfer execution control; if state is not updated before the call, the callee can re-enter.

### 1.1 Classic Reentrancy (Single-Function)

Victim.withdraw()
  ├── checks balance[msg.sender] > 0          ✓
  ├── msg.sender.call{value: balance}("")     ← external call
  │   └── Attacker.receive()
  │       └── Victim.withdraw()               ← re-enters before state update
  │           ├── checks balance[msg.sender]   ← still > 0!
  │           └── sends ETH again
  └── balance[msg.sender] = 0                 ← too late

### 1.2 Cross-Function Reentrancy

Two functions share state; attacker re-enters a different function during callback:

| Step | Execution | State |
|---|---|---|
| 1 | Call withdraw() → external call | balance still positive |
| 2 | Attacker fallback calls transfer(attacker2) | balance used before reset |
| 3 | transfer reads stale balance → moves funds | attacker2 receives tokens |
| 4 | Original withdraw completes, zeroes balance | damage done |

### 1.3 Cross-Contract Reentrancy

Contract A calls Contract B, which calls back into Contract A (or Contract C that reads A's stale state). Especially dangerous in DeFi protocols where multiple contracts share state.

### 1.4 Read-Only Reentrancy

The re-entered function is a view function used by a third-party contract for price calculation. No state modification in the victim, but the stale intermediate state misleads the reader.

**Real-world**: Curve pool get_virtual_price() read during remove_liquidity() callback → inflated price → profit on dependent lending protocol.

### Mitigations

| Pattern | Protection Level |
|---|---|
| Checks-Effects-Interactions (CEI) | Core defense; update state before external call |
| ReentrancyGuard (OpenZeppelin) | Mutex lock; p
...

## References
- Source: https://github.com/yaklang/hack-skills/blob/main/skills/smart-contract-vulnerabilities/SKILL.md
- License: MIT — Copyright (c) 2026 VillanCh
- Distilled for bbhunter by scripts/import_hack_skills.py
