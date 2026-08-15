---
name: idor-broken-object-authorization
description: IDOR and broken object authorization testing playbook. Use when requests expose object identifiers, tenant boundaries, writable fields, or missing object-level authorization checks.
scope: web2
---
IDOR and broken object authorization testing playbook. Use when requests expose object identifiers, tenant boundaries, writable fields, or missing object-level authorization checks.

# SKILL: IDOR / Broken Object Level Authorization — Expert Attack Playbook

> **AI LOAD INSTRUCTION**: IDOR is the #1 bug bounty finding. This skill covers non-obvious IDOR surfaces, all attack vectors (not just URL params), A-B testing methodology, BOLA vs BFLA distinction, chaining IDOR to higher impact, and what testers repeatedly miss.

---

## 1. IDOR vs BOLA vs BFLA

| Term | Meaning | Impact |
|---|---|---|
| IDOR | Insecure Direct Object Reference | Read/modify other users' data |
| BOLA | Broken Object Level Authorization (OWASP API Top 10 A1) | Same as IDOR, API terminology |
| BFLA | Broken Function Level Authorization | Low-priv user accesses HIGH-PRIV functions (e.g., admin endpoints) |

**Key distinction**: 
- BOLA = accessing **object** you shouldn't own (data belonging to other users)
- BFLA = accessing **function** you shouldn't be authorized for (admin CRUD operations, bulk actions, user management)

---

## 2. WHERE TO FIND OBJECT IDs (ALL LOCATIONS)

Don't stop at URL path parameters — IDs appear in:

URL path:        GET /api/v1/users/1234/profile
URL query:       GET /orders?order_id=982
Request body:    {"userId": 1234, "action": "view"}
JSON fields:     {"resource": {"id": 5678, "type": "invoice"}}
Headers:         X-User-ID: 1234
                 X-Account-ID: 9999
Cookies:         user_id=1234; account=org_5678
GraphQL args:    query { user(id: "1234") { ... } }
Form fields:     <input name="documentId" value="5678">
WebSocket msgs:  {"event":"subscribe","channel_id":9999}

---

## 3. A-B TESTING METHODOLOGY

The most systematic IDOR test approach:

Step 1: Create two test accounts: UserA and UserB
Step 2: Perform all actions as UserA, capture all requests
        (profile edit, order view, password change, file access, etc.)
Step 3: Note every object ID created or accessed by UserA
Step 4: Authenticate as UserB
Step 5: Replay UserA's requests using UserB's session token
Step 6: If UserB can read/modify UserA's data → BOLA confirmed

Victim matters: for real bugs, target existing users, not test accounts.
Report evidence: show UserA owns the resource, UserB accessed it.

---

## 4. ID TYPE ITS IMPLICATIONS

| ID Pattern | Example | Notes |
|---|---|---|
| Sequential int | id=1001 → id=1002 | Easy prediction, high hit rate |
| UUID v4 | 550e8400-... |
...

## References
- Source: https://github.com/yaklang/hack-skills/blob/main/skills/idor-broken-object-authorization/SKILL.md
- License: MIT — Copyright (c) 2026 VillanCh
- Distilled for bbhunter by scripts/import_hack_skills.py
