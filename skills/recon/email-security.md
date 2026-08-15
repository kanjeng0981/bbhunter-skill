---
name: email-security
description: DMARC/SPF/DKIM check, email spoofing, SMTP test, and security header analysis
scope: web2
---
DMARC/SPF/DKIM check, email spoofing, SMTP test, and security header analysis

# Email Security -- DMARC, SPF, DKIM

## When to Use

- During passive reconnaissance (Phase 1)
- After initial DNS enumeration
- DMARC p=none means the domain can be totally spoofed
- Critical for identifying phishing/business email compromise risks

## DMARC/SPF/DKIM Check Commands



## Interpreting Results


## Email Spoofing via SMTP



## Headers That Indicate Security Level


## AWS SES Spoofing (When SPF includes amazonses.com)

With v=spf1 include:amazonses.com ~all:
1. Create AWS account
2. Configure SES with your own domain (verified)
3. Send email with From: admin@target.com
4. SPF PASSES (because of include:amazonses.com)
5. DMARC p=none -- provider delivers normally

## Real-World Cases

**Real-world case (CRITICAL)**: Political party -- DMARC p=none on both domains (DOMAIN_PLACEHOLDER_A, DOMAIN_PLACEHOLDER_B). SPF with include:amazonses.com (any SES account can send as the domain). Total email spoofing.

## Pitfalls


## Verification

## References
- Source: https://github.com/uphiago/recon-skills/blob/main/recon/email-security/SKILL.md
- License: MIT — Copyright (c) 2025 Hiago Felipe
- Distilled for bbhunter by scripts/import_recon_skills.py
