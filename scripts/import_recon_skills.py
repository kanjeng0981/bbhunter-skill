#!/usr/bin/env python3
"""Import uphiago/recon-skills (MIT) into bbhunter skills.

Usage:
    python3 scripts/import_recon_skills.py /path/to/recon-skills [out_dir]

For each SKILL.md in scope (redteam/hunt-*, recon/*, web3-audit, meme-coin-audit),
writes a distilled bbhunter skill under ``skills/recon/``:

    - frontmatter: name / description (from upstream) / scope
    - distilled digest: description + "When to Use" / root-causes / pitfalls
      sections, with code fences and tables stripped, capped in size
    - "## References" section with upstream source URL + MIT attribution

The digest (above "## References") is what bbhunter injects into LLM prompts;
the source link + license stay human-readable only.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

UPSTREAM_REPO = "https://github.com/uphiago/recon-skills"
MAX_DIGEST_CHARS = 1500

# Section headings worth keeping in the distilled digest (in priority order).
KEEP_SECTIONS = [
    "When to Use",
    "Common Root Causes",
    "Root Cause Patterns",
    "Pitfalls",
    "Quick Reference Checklist",
]

WEB3_KEYWORDS = ("web3", "blockchain", "solidity", "solana", "meme-coin", "meme coin", "defi")


def parse_frontmatter(text: str) -> dict[str, str]:
    """Parse a simple `key: value` YAML-ish frontmatter block."""
    m = re.match(r"^---\s*\n(.*?)\n---\s*\n", text, re.DOTALL)
    meta: dict[str, str] = {}
    if not m:
        return meta
    for line in m.group(1).splitlines():
        line = line.strip()
        if ":" not in line:
            continue
        key, _, value = line.partition(":")
        meta[key.strip()] = value.strip()
    return meta


def unquote(s: str) -> str:
    s = s.strip()
    if len(s) >= 2 and s[0] == s[-1] and s[0] in "\"'":
        return s[1:-1]
    return s


def strip_code(text: str) -> str:
    # Remove fenced code blocks entirely (mostly bash/commands).
    text = re.sub(r"```.*?```", "", text, flags=re.DOTALL)
    # Inline code: keep the content, drop only the backticks, so tokens like
    # `html_safe` or `<style>` survive the distillation.
    text = re.sub(r"`([^`]*)`", r"\1", text)
    return text


def strip_tables(text: str) -> str:
    return "\n".join(
        line for line in text.splitlines() if not line.strip().startswith("|")
    )


def extract_section(body: str, title: str) -> str:
    pattern = re.compile(r"^#{2,4}\s+" + re.escape(title) + r"\s*$", re.M | re.I)
    m = pattern.search(body)
    if not m:
        return ""
    start = m.end()
    next_m = re.search(r"^#{1,4}\s+", body[start:], re.M)
    end = start + next_m.start() if next_m else len(body)
    return body[start:end].strip()


def build_digest(description: str, body: str) -> str:
    parts: list[str] = []
    if description:
        parts.append(description)

    for heading in KEEP_SECTIONS:
        section = strip_tables(strip_code(extract_section(body, heading))).strip()
        if section:
            parts.append(f"{section}")

    digest = "\n\n".join(parts).strip()

    # Fallback: skills without those sections (mostly recon/procedure skills)
    # get a code-stripped prefix of their body.
    if len(digest) < 400:
        fallback = strip_tables(strip_code(body)).strip()
        digest = (description + "\n\n" + fallback) if description else fallback

    if len(digest) > MAX_DIGEST_CHARS:
        digest = digest[:MAX_DIGEST_CHARS].rstrip() + "\n..."

    return digest.strip()


def detect_scope(name: str, description: str, tags: str) -> str:
    haystack = f"{name} {description} {tags}".lower()
    return "web3" if any(k in haystack for k in WEB3_KEYWORDS) else "web2"


def in_scope(rel_path: Path) -> bool:
    """Only import hunt-* + recon/* + the web3 audit skills."""
    parts = rel_path.parts
    stem = rel_path.parent.name
    if "hunt-" in stem:
        return True
    if "recon" in parts:
        return True
    if stem in {"web3-audit", "meme-coin-audit"}:
        return True
    return False


def main() -> int:
    if len(sys.argv) < 2:
        print("usage: import_recon_skills.py /path/to/recon-skills [out_dir]", file=sys.stderr)
        return 2
    src = Path(sys.argv[1])
    out_dir = Path(sys.argv[2]) if len(sys.argv) > 2 else Path("skills") / "recon"
    out_dir.mkdir(parents=True, exist_ok=True)

    imported = 0
    skipped = 0
    for skill_md in sorted(src.rglob("SKILL.md")):
        rel = skill_md.relative_to(src)
        if not in_scope(rel):
            skipped += 1
            continue

        text = skill_md.read_text(encoding="utf-8", errors="replace")
        meta = parse_frontmatter(text)
        name = unquote(meta.get("name", skill_md.parent.name))
        description = unquote(meta.get("description", ""))
        tags = meta.get("tags", "")
        scope = detect_scope(name, description, tags)

        # strip frontmatter from body
        body = re.sub(r"^---\s*\n.*?\n---\s*\n", "", text, count=1, flags=re.DOTALL)
        digest = build_digest(description, body)

        out = (
            "---\n"
            f"name: {name}\n"
            f"description: {description or name}\n"
            f"scope: {scope}\n"
            "---\n"
            f"{digest}\n\n"
            "## References\n"
            f"- Source: {UPSTREAM_REPO}/blob/main/{rel.as_posix()}\n"
            "- License: MIT — Copyright (c) 2025 Hiago Felipe\n"
            "- Distilled for bbhunter by scripts/import_recon_skills.py\n"
        )
        (out_dir / f"{name}.md").write_text(out, encoding="utf-8")
        imported += 1

    print(f"imported {imported} skills -> {out_dir}")
    print(f"skipped {skipped} out-of-scope SKILL.md files")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
