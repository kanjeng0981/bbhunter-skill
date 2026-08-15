---
name: business-logic-vulnerabilities
description: Business logic vulnerability playbook. Use when reasoning about workflows, race conditions, price manipulation, coupon abuse, state machines, and multi-step authorization gaps.
scope: web2
---
Business logic vulnerability playbook. Use when reasoning about workflows, race conditions, price manipulation, coupon abuse, state machines, and multi-step authorization gaps.

# SKILL: Business Logic Vulnerabilities — Expert Attack Playbook

> **AI LOAD INSTRUCTION**: Business logic flaws are scanner-invisible and high-reward on bug bounty. This skill covers race conditions, price manipulation, workflow bypass, coupon/referral abuse, negative values, and state machine attacks. These require human reasoning, not automation. For specific exploitation techniques (payment precision/overflow, captcha bypass, password reset flaws, user enumeration), load the companion [SCENARIOS.md](./SCENARIOS.md). For the workflow approach itself (modeling → state machine → attack-surface matrix → human judgement) load [METHODOLOGY.md](./METHODOLOGY.md). For the per-module check items load [CHECKLIST.md](./CHECKLIST.md).

### Companion files

| File | When to load |
|---|---|
| [METHODOLOGY.md](./METHODOLOGY.md) | Need the 5-phase workflow, attack-surface 5×N matrix, human-judgement decision tree |
| [CHECKLIST.md](./CHECKLIST.md) | Going through a target module-by-module (login / register / payment / IDOR / privacy) and want every line item with why+verify |
| [SCENARIOS.md](./SCENARIOS.md) | Drilling deeper into payment precision/overflow, captcha bypass, password reset, enumeration, frontend bypass |

### Extended Scenarios

Also load [SCENARIOS.md](./SCENARIOS.md) when you need:
- Payment precision & integer overflow attacks — 32-bit overflow to negative, decimal rounding exploitation, negative shipping fees
- Payment parameter tampering checklist — price, discount, currency, gateway, return_url fields
- Condition race practical patterns — parallel coupon application, gift card double-spend with Burp group send
- Captcha bypass techniques — drop verification request, remove parameter, clear cookies to reset counter, OCR with tesseract
- Arbitrary password reset — predictable tokens (md5(username)), session replacement attack, registration overwrite
- User information enumeration — login error message difference, masked data reconstruction across endpoints, base64 uid cookie manipulation
- Frontend restriction bypass — array parameters for multiple coupons (couponid[0]/couponid[1]), remove disabled/readonly attributes
- Application-layer DoS patterns — regex backtracking, WebSocket abuse

---

## 1. PRICE AND VALUE MANIPULATION

### Negative Quantity / Price
Many applicat
...

## References
- Source: https://github.com/yaklang/hack-skills/blob/main/skills/business-logic-vulnerabilities/SKILL.md
- License: MIT — Copyright (c) 2026 VillanCh
- Distilled for bbhunter by scripts/import_hack_skills.py
