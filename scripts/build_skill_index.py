#!/usr/bin/env python3
"""Generate a categorized skill index (SKILLS.md) from skills/.

Reads every skill via bbhunter.skills.load_skills and buckets each skill by
keyword rules matched against its name. Writes ``SKILLS.md`` at the project
root (outside ``skills/`` so the loader ignores it). Re-run any time skills
are added/removed:

    .venv/bin/python scripts/build_skill_index.py
"""
from __future__ import annotations

import re
from collections import Counter, OrderedDict
from datetime import date
from pathlib import Path

from bbhunter.skills import Skill, load_skills

ROOT = Path(__file__).resolve().parents[1]
SKILLS_DIR = ROOT / "skills"
OUT = ROOT / "SKILLS.md"

# Ordered keyword rules: first match wins. ``scope == "web3"`` is handled
# separately (a skill is web3 iff its frontmatter says so).
RULES: list[tuple[str, str]] = [
    # --- Injection ---
    ("Injection", "ssti"),
    ("Injection", "template"),
    ("Injection", "nosql"),
    ("Injection", "nosqli"),
    ("Injection", "sqli"),
    ("Injection", "xss"),
    ("Injection", "xxe"),
    ("Injection", "ldap"),
    ("Injection", "deserialization"),
    ("Injection", "prototype-pollution"),
    ("Injection", "smuggling"),
    ("Injection", "ssrf"),
    ("Injection", "traversal"),
    ("Injection", "lfi"),
    ("Injection", "file-upload"),
    ("Injection", "mass-assignment"),
    ("Injection", "rce"),
    ("Injection", "phpinfo"),
    # --- Client-side & web config (before framework so cors-credential-wordpress -> cors) ---
    ("Client-side & Web Config", "cors"),
    ("Client-side & Web Config", "csrf"),
    ("Client-side & Web Config", "host-header"),
    ("Client-side & Web Config", "open-redirect"),
    ("Client-side & Web Config", "cache"),
    ("Client-side & Web Config", "race"),
    ("Client-side & Web Config", "takeover"),
    ("Client-side & Web Config", "xssi"),
    ("Client-side & Web Config", "money-stealing"),
    ("Client-side & Web Config", "business-logic"),
    ("Client-side & Web Config", "dom"),
    # --- Framework & CMS (before auth so wp-*auth-bypass -> framework) ---
    ("Framework & CMS", "wordpress"),
    ("Framework & CMS", "wp"),
    ("Framework & CMS", "xmlrpc"),
    ("Framework & CMS", "aspnet"),
    ("Framework & CMS", "django"),
    ("Framework & CMS", "fastapi"),
    ("Framework & CMS", "flask"),
    ("Framework & CMS", "werkzeug"),
    ("Framework & CMS", "laravel"),
    ("Framework & CMS", "nestjs"),
    ("Framework & CMS", "nextjs"),
    ("Framework & CMS", "nodejs"),
    ("Framework & CMS", "springboot"),
    ("Framework & CMS", "sharepoint"),
    ("Framework & CMS", "exchange"),
    ("Framework & CMS", "owa"),
    ("Framework & CMS", "zimbra"),
    ("Framework & CMS", "deep-invade"),
    # --- Auth & access control ---
    ("Auth & Access Control", "idor"),
    ("Auth & Access Control", "object-authorization"),
    ("Auth & Access Control", "oauth"),
    ("Auth & Access Control", "jwt"),
    ("Auth & Access Control", "saml"),
    ("Auth & Access Control", "session"),
    ("Auth & Access Control", "mfa"),
    ("Auth & Access Control", "brute"),
    ("Auth & Access Control", "ato"),
    ("Auth & Access Control", "broken-function"),
    ("Auth & Access Control", "write-gap"),
    ("Auth & Access Control", "credential"),
    ("Auth & Access Control", "noauth"),
    ("Auth & Access Control", "unauth"),
    ("Auth & Access Control", "403-bypass"),
    ("Auth & Access Control", "auth"),
    # --- Recon & enumeration ---
    ("Recon & Enumeration", "subdomain"),
    ("Recon & Enumeration", "vhost"),
    ("Recon & Enumeration", "origin-ip"),
    ("Recon & Enumeration", "staging"),
    ("Recon & Enumeration", "cms-detection"),
    ("Recon & Enumeration", "asn"),
    ("Recon & Enumeration", "port"),
    ("Recon & Enumeration", "visual"),
    ("Recon & Enumeration", "source-leak"),
    ("Recon & Enumeration", "js-secrets"),
    ("Recon & Enumeration", "github"),
    ("Recon & Enumeration", "gitlab"),
    ("Recon & Enumeration", "error-log"),
    ("Recon & Enumeration", "schema"),
    ("Recon & Enumeration", "information-disclosure"),
    ("Recon & Enumeration", "metrics"),
    ("Recon & Enumeration", "enumeration"),
    # --- Cloud, API & infra ---
    ("Cloud, API & Infra", "k8s"),
    ("Cloud, API & Infra", "cloud"),
    ("Cloud, API & Infra", "firebase"),
    ("Cloud, API & Infra", "supabase"),
    ("Cloud, API & Infra", "s3"),
    ("Cloud, API & Infra", "minio"),
    ("Cloud, API & Infra", "cicd"),
    ("Cloud, API & Infra", "graphql"),
    ("Cloud, API & Infra", "grpc"),
    ("Cloud, API & Infra", "websocket"),
    ("Cloud, API & Infra", "mcp"),
    ("Cloud, API & Infra", "api"),
    ("Cloud, API & Infra", "iot"),
    ("Cloud, API & Infra", "scada"),
    ("Cloud, API & Infra", "hikvision"),
    ("Cloud, API & Infra", "camera"),
    # --- Network, TLS & stealth ---
    ("Network, TLS & Stealth", "tls"),
    ("Network, TLS & Stealth", "fingerprint"),
    ("Network, TLS & Stealth", "impersonation"),
    ("Network, TLS & Stealth", "http2"),
    ("Network, TLS & Stealth", "ntlm"),
    ("Network, TLS & Stealth", "stealth"),
    ("Network, TLS & Stealth", "humanize"),
    # --- Other / misc ---
    ("Other / Misc", "dispatch"),
    ("Other / Misc", "llm"),
    ("Other / Misc", "email"),
    ("Other / Misc", "waf"),
    ("Other / Misc", "misc"),
]

CATEGORY_ORDER = [
    "Web3 / Smart Contract",
    "Injection",
    "Auth & Access Control",
    "Client-side & Web Config",
    "Framework & CMS",
    "Recon & Enumeration",
    "Cloud, API & Infra",
    "Network, TLS & Stealth",
    "Other / Misc",
]

CATEGORY_BLURB = {
    "Web3 / Smart Contract": "Solidity/EVM audit guide, real-world exploit & finding data, protocol recon, fuzzing invariants, Solana, and rug-pull kill signals.",
    "Injection": "SQLi/NoSQLi, XSS, SSTI, XXE, SSRF, LFI/path traversal, RCE, LDAP, deserialization, request smuggling, prototype pollution, file upload, mass assignment.",
    "Auth & Access Control": "Auth bypass, IDOR/BOLA, OAuth/JWT/SAML, session flaws, MFA bypass, brute force, ATO, and 401/403 bypass.",
    "Client-side & Web Config": "CORS, CSRF, host header, open redirect, cache poisoning, race conditions, subdomain takeover, XSSI, and business-logic flaws.",
    "Framework & CMS": "WordPress, Django, Laravel, Flask, Node/Next/Nest, Spring Boot, ASP.NET, SharePoint, Exchange, and Zimbra.",
    "Recon & Enumeration": "Subdomain/vhost/ASN/port discovery, JS & GitHub secret mining, source leak, schema & info disclosure.",
    "Cloud, API & Infra": "Kubernetes, cloud misconfig, Firebase/Supabase, S3/MinIO, CI/CD, GraphQL/gRPC/WebSocket, MCP, and IoT/SCADA.",
    "Network, TLS & Stealth": "TLS fingerprinting, HTTP/2, NTLM, stealth browsing, and automation humanization.",
    "Other / Misc": "LLM/AI, email security, WAF bypass, orchestrator/loader meta-skills, and uncategorized.",
}


def _matches(name: str, kw: str) -> bool:
    """Match keyword as a whole token (boundaries on non-alphanumerics)."""
    return re.search(rf"(?<![a-z0-9]){re.escape(kw)}(?![a-z0-9])", name) is not None


def classify(name: str, scope: str) -> str:
    if scope == "web3":
        return "Web3 / Smart Contract"
    n = name.lower()
    for category, kw in RULES:
        if _matches(n, kw):
            return category
    return "Other / Misc"


def _desc(skill: Skill) -> str:
    d = (skill.description or "").replace("\n", " ").strip()
    # First sentence is usually the gist.
    for sep in (". ", ". ", " - "):
        pass
    if len(d) > 110:
        cut = d[:110].rsplit(" ", 1)[0]
        d = cut + "…"
    return d


def build() -> str:
    skills = load_skills(SKILLS_DIR)
    buckets: dict[str, list[Skill]] = OrderedDict(
        (c, []) for c in CATEGORY_ORDER
    )
    for s in skills:
        buckets[classify(s.name, s.scope)].append(s)
    for c in buckets:
        buckets[c].sort(key=lambda s: s.name)

    lines: list[str] = []
    lines.append("# Skill Catalog")
    lines.append("")
    lines.append(
        f"**{len(skills)} skills** "
        f"({sum(1 for s in skills if s.scope == 'web3')} web3 / "
        f"{sum(1 for s in skills if s.scope == 'web2')} web2). "
        f"Generated {date.today().isoformat()} by `scripts/build_skill_index.py`."
    )
    lines.append("")
    lines.append(
        "> Live in `skills/`. Web2 skills are keyword-checklists for LLM triage; "
        "web3 skills cover Solidity/EVM audit. Re-run the script after adding skills."
    )
    lines.append("")

    # TOC
    lines.append("## Categories")
    lines.append("")
    for c in CATEGORY_ORDER:
        n = len(buckets[c])
        if n:
            lines.append(f"- [{c}](#{_anchor(c)}) — {n}")
    lines.append("")

    for c in CATEGORY_ORDER:
        items = buckets[c]
        if not items:
            continue
        lines.append(f"## {c}")
        lines.append("")
        lines.append(CATEGORY_BLURB.get(c, ""))
        lines.append("")
        for s in items:
            rel = s.path.relative_to(SKILLS_DIR).as_posix()
            lines.append(f"- **`{s.name}`** — {_desc(s)} ·`{rel}`")
        lines.append("")
    return "\n".join(lines)


def _anchor(category: str) -> str:
    return category.lower().replace(" ", "-").replace("&", "").replace("/", "").replace(",", "")


def main() -> None:
    text = build()
    OUT.write_text(text, encoding="utf-8")
    skills = load_skills(SKILLS_DIR)
    counts = Counter(classify(s.name, s.scope) for s in skills)
    print(f"wrote {OUT.name} — {len(skills)} skills")
    for c in CATEGORY_ORDER:
        if counts.get(c):
            print(f"  {c:<28} {counts[c]}")
    # Sanity: nothing silently dropped.
    assert sum(counts.values()) == len(skills), "category count mismatch"


if __name__ == "__main__":
    main()
