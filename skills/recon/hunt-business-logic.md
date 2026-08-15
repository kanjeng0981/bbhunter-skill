---
name: hunt-business-logic
description: Hunting skill for business logic vulnerabilities. Built from 12 public bug bounty reports. Covers coupon-race-stacking (Instacart, Stripe, Reverb), negative-quantity-in-cart price tampering (Upserve, Eternal/Zomato), decimal/fraction price-field overflow (Shipt), client-side checkout amount trust on PayPal redirect (WordPress.org), price-per-unit mass-assignment (Krisp), and archived-price swap / cart-TOCTOU (Stripe). Use when hunting business logic — heavy emphasis on financial-impact-demonstrated cases.
scope: web2
---
Hunting skill for business logic vulnerabilities. Built from 12 public bug bounty reports. Covers coupon-race-stacking (Instacart, Stripe, Reverb), negative-quantity-in-cart price tampering (Upserve, Eternal/Zomato), decimal/fraction price-field overflow (Shipt), client-side checkout amount trust on PayPal redirect (WordPress.org), price-per-unit mass-assignment (Krisp), and archived-price swap / cart-TOCTOU (Stripe). Use when hunting business logic — heavy emphasis on financial-impact-demonstrated cases.

1. **Server trusts client-supplied data for financial decisions.** Developers offload price calculation to the frontend or pass amount fields through forms/URLs without re-validating on the server against a canonical source (the product database).

2. **Verification is enforced only in the UI, not the API.** Frontend hides features behind a verification gate, but the backend API endpoints are fully functional without a verified status — any authenticated request succeeds.

3. **IP-based rate limiting reads from spoofable headers.** Developers implement rate limits using request.headers['X-Forwarded-For'] instead of the actual connection IP, allowing trivial bypass by header manipulation.

4. **Payment webhooks lack signature validation.** Developers implement "success" webhooks without verifying the HMAC signature provided by the payment provider, allowing anyone to POST a fake success notification.

5. **Internal/employee pages aren't access-controlled.** Internaltools are
...

## References
- Source: https://github.com/uphiago/recon-skills/blob/main/redteam/hunt-business-logic/SKILL.md
- License: MIT — Copyright (c) 2025 Hiago Felipe
- Distilled for bbhunter by scripts/import_recon_skills.py
