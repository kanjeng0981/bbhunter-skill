#!/usr/bin/env python3
"""Import selected yaklang/hack-skills (MIT) into bbhunter.

Usage:
    python3 scripts/import_hack_skills.py /path/to/hack-skills [out_dir]

Imports the deep web/web3 skills that fill gaps beyond the recon-skills
catalog (deserialization, request smuggling, prototype pollution, JWT, SSTI,
SSRF, LFI, business logic, WAF bypass, 401/403 bypass, IDOR, NoSQL, smart
contracts, DeFi patterns). Each is distilled (frontmatter + digest above
``## References``; source URL + MIT attribution below).
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

UPSTREAM = "https://github.com/yaklang/hack-skills"
MAX_DIGEST_CHARS = 2500

# skill dir name -> bbhunter scope
SKILLS: dict[str, str] = {
    "deserialization-insecure": "web2",
    "request-smuggling": "web2",
    "prototype-pollution": "web2",
    "jwt-oauth-token-attacks": "web2",
    "ssti-server-side-template-injection": "web2",
    "ssrf-server-side-request-forgery": "web2",
    "path-traversal-lfi": "web2",
    "business-logic-vulnerabilities": "web2",
    "waf-bypass-techniques": "web2",
    "401-403-bypass-techniques": "web2",
    "idor-broken-object-authorization": "web2",
    "nosql-injection": "web2",
    "smart-contract-vulnerabilities": "web3",
    "defi-attack-patterns": "web3",
}


def parse_frontmatter(text: str) -> dict[str, str]:
    """Parse frontmatter, handling YAML folded-scalar descriptions (``>-``)."""
    m = re.match(r"^---\s*\n(.*?)\n---\s*\n", text, re.DOTALL)
    meta: dict[str, str] = {}
    if not m:
        return meta
    lines = m.group(1).splitlines()
    i = 0
    while i < len(lines):
        line = lines[i]
        if ":" in line and not line[:1].isspace():
            key, _, val = line.partition(":")
            key, val = key.strip(), val.strip()
            if val in (">", ">-", "|", "|-"):
                buf: list[str] = []
                i += 1
                while i < len(lines) and lines[i][:1].isspace():
                    buf.append(lines[i].strip())
                    i += 1
                meta[key] = " ".join(buf)
                continue
            meta[key] = val
        i += 1
    return meta


def strip_code(text: str) -> str:
    # Keep fenced-block content (these are payloads/signatures, not bash noise);
    # drop the fence markers and language tags to read cleanly in a prompt.
    text = re.sub(r"```[a-zA-Z0-9_+-]*\n?", "", text)
    text = re.sub(r"`([^`]*)`", r"\1", text)
    return text


def strip_routing(body: str) -> str:
    """Remove the '## 0. RELATED ROUTING' cross-load section (not applicable)."""
    return re.sub(r"## 0\. RELATED ROUTING.*?(?=\n## )", "", body, count=1, flags=re.DOTALL)


def build_digest(description: str, body: str) -> str:
    # Indicator/payload tables are the value here, so keep them.
    cleaned = strip_code(strip_routing(body))
    digest = (description + "\n\n" + cleaned).strip()
    if len(digest) > MAX_DIGEST_CHARS:
        digest = digest[:MAX_DIGEST_CHARS].rstrip() + "\n..."
    return digest


def main() -> int:
    if len(sys.argv) < 2:
        print("usage: import_hack_skills.py /path/to/hack-skills [out_dir]", file=sys.stderr)
        return 2
    src = Path(sys.argv[1])
    out_dir = Path(sys.argv[2]) if len(sys.argv) > 2 else Path("skills") / "hack"
    out_dir.mkdir(parents=True, exist_ok=True)

    imported = 0
    for name, scope in SKILLS.items():
        md = src / "skills" / name / "SKILL.md"
        if not md.is_file():
            print(f"skip (missing): {name}", file=sys.stderr)
            continue
        text = md.read_text(encoding="utf-8", errors="replace")
        meta = parse_frontmatter(text)
        description = meta.get("description", name)
        body = re.sub(r"^---\s*\n.*?\n---\s*\n", "", text, count=1, flags=re.DOTALL)
        digest = build_digest(description, body)

        out = (
            "---\n"
            f"name: {name}\n"
            f"description: {description}\n"
            f"scope: {scope}\n"
            "---\n"
            f"{digest}\n\n"
            "## References\n"
            f"- Source: {UPSTREAM}/blob/main/skills/{name}/SKILL.md\n"
            "- License: MIT — Copyright (c) 2026 VillanCh\n"
            "- Distilled for bbhunter by scripts/import_hack_skills.py\n"
        )
        (out_dir / f"{name}.md").write_text(out, encoding="utf-8")
        imported += 1

    print(f"imported {imported} skills -> {out_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
