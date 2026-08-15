---
name: hunt-graphql
description: Hunting skill for graphql vulnerabilities. Built from 12 public bug bounty reports across IDOR via node() / GID, mutation IDOR including AI/LLM features, cross-tenant IDOR, SSRF via argument, batching-DoS, query-cost-bypass, SQLi via argument, broken-object-level-authz, auth-bypass via unscoped mutations, and PII exposure from missing field-level authz. Use when hunting graphql on any target.
scope: web2
---
Hunting skill for graphql vulnerabilities. Built from 12 public bug bounty reports across IDOR via node() / GID, mutation IDOR including AI/LLM features, cross-tenant IDOR, SSRF via argument, batching-DoS, query-cost-bypass, SQLi via argument, broken-object-level-authz, auth-bypass via unscoped mutations, and PII exposure from missing field-level authz. Use when hunting graphql on any target.

1. **Dual-write without atomic locking** — developers implement the same resource modification in both REST and GraphQL independently. Neither system is aware the other exists for that resource. State updates aren't serialized or compared.

2. **Inconsistent authorization middleware** — REST endpoints go through one auth layer (e.g., middleware chain), GraphQL resolvers go through a different resolver-level check. The same action, different enforcement.

3. **GraphQL as "new REST" migration** — teams add GraphQL mutations that mirror REST functionality without auditing the permission model. The GraphQL version is less mature and skips checks the REST version accumulated over time.

4. **Introspection left on in production** — default framework settings (Apollo, Graphene) enable introspection in all environments. Developers forget to disable it, treating it as "just documentation."

5. **Node ID trust without re-authorization** — GraphQL global IDs (base64("ObjectType:123")) are decoded and trusted without verifying the requesting user has access to that specific object.

6. **Mutation s
...

## References
- Source: https://github.com/uphiago/recon-skills/blob/main/redteam/hunt-graphql/SKILL.md
- License: MIT — Copyright (c) 2025 Hiago Felipe
- Distilled for bbhunter by scripts/import_recon_skills.py
