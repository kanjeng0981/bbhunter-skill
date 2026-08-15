"""Markdown-based skill loader.

A skill is a Markdown file with an optional YAML-ish frontmatter:

    ---
    name: my-skill
    description: what this skill does
    scope: web2 | web3 | both
    ---
    ...instructions / checklist...   <-- injected into LLM prompts

    ## References
    ...links / write-ups...          <-- human reference, NOT injected

Skills live in the ``skills/`` directory (configurable via
``BBHUNTER_SKILLS_DIR``). The checklist part (before ``## References``) is
injected into LLM prompts; the references section is kept out to avoid
blowing up the token budget.
"""
from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path

FRONTMATTER_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL)
REFERENCE_HEADING = "## References"

VALID_SCOPES = {"web2", "web3", "both"}

_STOPWORDS = {
    "a", "an", "and", "any", "are", "as", "at", "be", "by", "can", "for",
    "from", "if", "in", "into", "is", "it", "no", "not", "of", "on", "or",
    "that", "the", "this", "to", "use", "via", "when", "with", "your",
}


def _tokens(text: str) -> set[str]:
    return {
        t for t in re.findall(r"[a-z0-9]+", text.lower()) if t not in _STOPWORDS
    }


@dataclass
class Skill:
    name: str
    description: str
    instructions: str
    path: Path
    scope: str = "both"

    def as_prompt(self) -> str:
        checklist = self.instructions.split(REFERENCE_HEADING, 1)[0].strip()
        return (
            f"## Skill: {self.name}\n"
            f"Description: {self.description or '(none)'}\n\n"
            f"{checklist}"
        )

    def references(self) -> str:
        parts = self.instructions.split(REFERENCE_HEADING, 1)
        return parts[1].strip() if len(parts) == 2 else ""


def load_skills(skills_dir: Path) -> list[Skill]:
    skills: list[Skill] = []
    if not skills_dir.is_dir():
        return skills
    for path in sorted(skills_dir.rglob("*.md")):
        if path.stem.lower() == "readme":
            continue
        try:
            text = path.read_text(encoding="utf-8", errors="replace")
        except OSError:
            continue
        name = path.stem
        description = ""
        scope = "both"
        instructions = text
        m = FRONTMATTER_RE.match(text)
        if m:
            for line in m.group(1).splitlines():
                line = line.strip()
                if line.lower().startswith("name:"):
                    name = line.split(":", 1)[1].strip()
                elif line.lower().startswith("description:"):
                    description = line.split(":", 1)[1].strip()
                elif line.lower().startswith("scope:"):
                    value = line.split(":", 1)[1].strip().lower()
                    scope = value if value in VALID_SCOPES else "both"
            instructions = text[m.end():].strip()
        skills.append(
            Skill(
                name=name,
                description=description,
                instructions=instructions,
                path=path,
                scope=scope,
            )
        )
    return skills


def filter_skills(skills: list[Skill], scopes: set[str]) -> list[Skill]:
    """Keep skills whose scope matches any of ``scopes`` (or is 'both')."""
    return [s for s in skills if s.scope == "both" or s.scope in scopes]


def select_skills(skills: list[Skill], findings: list, top_k: int = 6) -> list[Skill]:
    """Select the ``top_k`` skills most relevant to a set of findings.

    Scores each skill by keyword overlap between its name/description and the
    findings' module/title/description text. Keeps LLM prompts bounded when the
    skills directory contains a large catalog.
    """
    if not skills:
        return []
    if not findings:
        return skills[:top_k]

    text = " ".join(
        f"{getattr(f, 'module', '')} {getattr(f, 'title', '')} "
        f"{getattr(f, 'description', '')}"
        for f in findings
    ).lower()
    finding_tokens = _tokens(text)

    scored: list[tuple[int, int, str, Skill]] = []
    for s in skills:
        name_tokens = _tokens(s.name)
        desc_tokens = _tokens(s.description)
        body_tokens = _tokens(s.instructions.split(REFERENCE_HEADING, 1)[0])
        name_overlap = len(name_tokens & finding_tokens)
        desc_overlap = len(desc_tokens & finding_tokens)
        body_overlap = len(body_tokens & finding_tokens)
        # Name > description > body weighting.
        score = name_overlap * 10 + desc_overlap * 2 + body_overlap
        if score:
            scored.append((score, len(name_tokens) + len(desc_tokens), s.name, s))

    # Higher score first; tie-break on smaller vocabulary (more specific),
    # then alphabetical for determinism.
    scored.sort(key=lambda x: (-x[0], x[1], x[2]))
    selected = [s for _, _, _, s in scored[:top_k]]
    if not selected:
        selected = skills[:top_k]
    return selected
