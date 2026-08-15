"""Validation stage: LLM triage to prune false positives and calibrate severity."""
from __future__ import annotations

import json

from ..llm import LLM
from ..models import Finding
from ..skills import Skill, filter_skills, select_skills

VALIDATOR_SYSTEM = (
    "You are a bug bounty triage expert. Review automated findings and decide "
    "whether each is a real issue. Remove false positives, fix severity and "
    "confidence, and provide CVSS/CWE where appropriate. Be conservative: a "
    "finding should be downgraded or dropped when evidence is weak."
)


def validate(findings: list[Finding], llm: LLM, skills: list[Skill]) -> list[Finding]:
    if not findings:
        return findings
    if not llm.settings.llm_enabled:
        # Deterministic-only mode: no API key, so nothing to triage.
        return findings

    scopes: set[str] = set()
    for f in findings:
        scopes.add("web3" if f.module.startswith("web3") else "web2")
    relevant = select_skills(filter_skills(skills, scopes), findings)
    skill_prompts = "\n\n".join(s.as_prompt() for s in relevant)
    items = [
        {
            "id": f.id,
            "module": f.module,
            "target": f.target,
            "title": f.title,
            "description": f.description,
            "severity": f.severity,
            "evidence": f.evidence[:800],
        }
        for f in findings
    ]

    user = (
        "For each finding below, return a JSON object with a 'results' array "
        "(one entry per finding id). Each entry must have keys: id, verdict "
        "(one of confirmed/false_positive/needs_review), severity (one of "
        "info/low/medium/high/critical), confidence (low/medium/high), cvss "
        "(base vector string, or empty), cwe (string), reasoning (short).\n\n"
    )
    if skill_prompts:
        user += f"Apply these skills when judging:\n\n{skill_prompts}\n\n"
    user += "Findings:\n" + json.dumps({"findings": items}, ensure_ascii=False)

    try:
        data = llm.chat_json(
            [{"role": "system", "content": VALIDATOR_SYSTEM},
             {"role": "user", "content": user}],
            temperature=0.0,
        )
    except Exception:  # noqa: BLE001 — keep original findings on LLM failure
        return findings

    by_id = {r.get("id"): r for r in data.get("results", [])}
    kept: list[Finding] = []
    for f in findings:
        r = by_id.get(f.id)
        if not r:
            kept.append(f)
            continue
        if r.get("verdict") == "false_positive":
            continue
        f.severity = r.get("severity") or f.severity
        f.confidence = r.get("confidence") or f.confidence
        f.cvss = r.get("cvss") or f.cvss
        f.cwe = r.get("cwe") or f.cwe
        f.reasoning = r.get("reasoning") or f.reasoning
        kept.append(f)
    return kept
