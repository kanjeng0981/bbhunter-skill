---
name: hunt-idor
description: Hunting skill for idor vulnerabilities. Built from 26 public bug bounty reports. Use when hunting idor on any target.
scope: web2
---
Hunting skill for idor vulnerabilities. Built from 26 public bug bounty reports. Use when hunting idor on any target.

Use when the target has any endpoint that references user-owned resources by ID — API paths with user/order/invoice/message IDs, GraphQL queries with id arguments, file download endpoints, or any multi-tenant SaaS feature. IDOR is one of the most common and highest-paying vulnerabilities because it directly exposes other users' data without authentication bypass. Every feature that displays or acts on a resource by identifier is a candidate. Highest-value targets: financial documents/billing APIs, private repositories, user messages, account management endpoints, and cross-tenant business/org administration features.

1. **Missing ownership check in ORM queries**
   

2. **Authorization at the route level, not object level**
   - Developer checks "is user logged in?" but not "does this user own this object?"
   - Middleware confirms authentication; individual handlers skip ownership validation

3. **Trusting client-supplied IDs in request bodies**
   - Mobile apps or SPAs send org_id in POST body; server uses it directly without verifying caller belongs to that org

4. **GraphQL resolvers without field-level authorization**
   - Query resolvers fetch by ID from database without checking if the requesting user has permission
   - Especially common when resolvers are auto-generated from schema

5. **Inconsistent authorization across HTTP verbs**
   - GET endpoi
...

## References
- Source: https://github.com/uphiago/recon-skills/blob/main/redteam/hunt-idor/SKILL.md
- License: MIT — Copyright (c) 2025 Hiago Felipe
- Distilled for bbhunter by scripts/import_recon_skills.py
