---
name: hunt-race-condition
description: Hunting skill for race condition vulnerabilities. Built from 12 public bug bounty reports including modern HTTP/2 single-packet attack cases (James Kettle DEF CON 2023 "Smashing the State Machine"; RyotaK / Flatt Security 10,000-request first-sequence-sync expansion 2024). Covers coupon double-redemption, gift-card double-spend, MFA-OTP-validate race, account-create race, faucet/crypto token double-mint, email-activation race, vote/upvote inflation, password-reset token race, rate-limit bypass via concurrent requests. Use when hunting race conditions, TOCTOU bugs, MFA-bypass-via-timing.
scope: web2
---
Hunting skill for race condition vulnerabilities. Built from 12 public bug bounty reports including modern HTTP/2 single-packet attack cases (James Kettle DEF CON 2023 "Smashing the State Machine"; RyotaK / Flatt Security 10,000-request first-sequence-sync expansion 2024). Covers coupon double-redemption, gift-card double-spend, MFA-OTP-validate race, account-create race, faucet/crypto token double-mint, email-activation race, vote/upvote inflation, password-reset token race, rate-limit bypass via concurrent requests. Use when hunting race conditions, TOCTOU bugs, MFA-bypass-via-timing.

1. **Check-Then-Act without atomic operations** — Developer reads state (if voucher.used == false), then writes state (voucher.update(used: true)) in two separate database operations. Any thread can read the same "unused" state before either writes.

2. **Missing database-level locking** — Using ORM methods like find or filter instead of SELECT ... FOR UPDATE. The fix is one line but developers don't think about concurrency.

3. **Optimistic concurrency without version checking** — Systems increment counters or mark records without checking if the record changed since it was read.

4. **Microservice TOCTOU** — Service A validates eligibility, Service B executes the action. No shared atomic transaction spans both services.

5. **Client-side "protection"** — Developers disable the button in JavaScript after first click, assuming that prevents duplicate submissions. Server-side logic is never ha
...

## References
- Source: https://github.com/uphiago/recon-skills/blob/main/redteam/hunt-race-condition/SKILL.md
- License: MIT — Copyright (c) 2025 Hiago Felipe
- Distilled for bbhunter by scripts/import_recon_skills.py
