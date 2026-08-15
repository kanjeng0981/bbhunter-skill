---
name: hunt-sqli
description: Hunting skill for sqli vulnerabilities. Built from 12 public bug bounty reports including modern NoSQL injection (Rocket.Chat CVE-2021-22911 MongoDB $regex, Mongoose ORM CVE-2024-53900 $where bypass), modern ORM raw-fragment SQLi (Django CVE-2024-42005, Sequelize GHSA-wrh9-cjv3-2hpw), second-order SOQL injection (HackerOne Salesforce), time-based blind SQLi in GraphQL resolvers, and SQLi on OIDC-proxy backends. Use when hunting SQLi / NoSQLi on any target.
scope: web2
---
Hunting skill for sqli vulnerabilities. Built from 12 public bug bounty reports including modern NoSQL injection (Rocket.Chat CVE-2021-22911 MongoDB $regex, Mongoose ORM CVE-2024-53900 $where bypass), modern ORM raw-fragment SQLi (Django CVE-2024-42005, Sequelize GHSA-wrh9-cjv3-2hpw), second-order SOQL injection (HackerOne Salesforce), time-based blind SQLi in GraphQL resolvers, and SQLi on OIDC-proxy backends. Use when hunting SQLi / NoSQLi on any target.

Use when the target has any endpoint that interacts with a database — search, filter, sort, login, ID-based lookups, API parameters, or any user input that could be used in a query. SQL injection (including NoSQL injection) remains one of the highest-paying vulnerability classes because it directly threatens data confidentiality, integrity, and availability. Every parameter in GET/POST/JSON/headers/cookies that reaches a backend database is a candidate. Highest-value targets: multi-tenant SaaS platforms, e-commerce/payment systems, search endpoints, analytics subdomains, and third-party plugins.

1. **String concatenation instead of parameterized queries** — The #1 root cause. Developers build SQL strings with user input directly: "SELECT * FROM items WHERE id=" + userId.

2. **ORMs bypassed for "performance"** — Developer switches from safe ORM to raw query for complex joins or reports: db.query("SELECT " + userColumn + " FROM table").

3. **Search/filter functionality** — Sorting and filtering logic is notoriously hard t
...

## References
- Source: https://github.com/uphiago/recon-skills/blob/main/redteam/hunt-sqli/SKILL.md
- License: MIT — Copyright (c) 2025 Hiago Felipe
- Distilled for bbhunter by scripts/import_recon_skills.py
