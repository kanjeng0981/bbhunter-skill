"""Report generation (Markdown)."""
from __future__ import annotations

import time
from pathlib import Path

from ..models import ContractInfo, Finding, SEVERITIES, WebHost


def _severity_sort(f: Finding) -> int:
    return -({"info": 0, "low": 1, "medium": 2, "high": 3, "critical": 4}[f.severity])


def write_report(
    report_dir: Path,
    hosts: list[WebHost],
    contracts: list[ContractInfo],
    findings: list[Finding],
) -> Path:
    report_dir.mkdir(parents=True, exist_ok=True)
    ts = time.strftime("%Y%m%d-%H%M%S")
    path = report_dir / f"bbhunter-{ts}.md"

    counts = {s: 0 for s in SEVERITIES}
    for f in findings:
        counts[f.severity] = counts.get(f.severity, 0) + 1

    lines: list[str] = []
    lines.append("# bbhunter report")
    lines.append(f"Generated: {time.strftime('%Y-%m-%d %H:%M:%S')}")
    lines.append("")
    lines.append("> ⚠️ Run only against targets you are authorized to test.")
    lines.append("")
    lines.append("## Summary")
    lines.append("")
    lines.append(f"- Web hosts probed: {len(hosts)}")
    lines.append(f"- Contracts analyzed: {len(contracts)}")
    lines.append(f"- Findings (after triage): {len(findings)}")
    for s in SEVERITIES:
        if counts[s]:
            lines.append(f"  - {s}: {counts[s]}")
    lines.append("")

    if findings:
        lines.append("## Findings")
        lines.append("")
        for f in sorted(findings, key=_severity_sort):
            lines.append(f"### [{f.severity.upper()}] {f.title}")
            lines.append("")
            lines.append(f"- **ID**: `{f.id}`")
            lines.append(f"- **Module**: `{f.module}`")
            lines.append(f"- **Target**: `{f.target}`")
            if f.confidence:
                lines.append(f"- **Confidence**: {f.confidence}")
            if f.cwe:
                lines.append(f"- **CWE**: {f.cwe}")
            if f.cvss:
                lines.append(f"- **CVSS**: `{f.cvss}`")
            lines.append("")
            lines.append(f.description)
            if f.reasoning:
                lines.append("")
                lines.append(f"**Triager reasoning**: {f.reasoning}")
            if f.evidence:
                lines.append("")
                lines.append("**Evidence**:")
                lines.append("")
                lines.append("```")
                lines.append(f.evidence[:1500])
                lines.append("```")
            lines.append("")

    if hosts:
        lines.append("## Web hosts")
        lines.append("")
        lines.append("| URL | Status | Title | Tech |")
        lines.append("| --- | --- | --- | --- |")
        for h in hosts:
            tech = ", ".join(h.technologies) or "-"
            lines.append(f"| {h.url} | {h.status} | {h.title or '-'} | {tech} |")
        lines.append("")

    if contracts:
        lines.append("## Contracts")
        lines.append("")
        lines.append("| Address | Chain | Code | Verified |")
        lines.append("| --- | --- | --- | --- |")
        for c in contracts:
            lines.append(
                f"| {c.address} | {c.chain or c.chain_id or '-'} | "
                f"{'yes' if c.has_code else 'no'} | {'yes' if c.verified else 'no'} |"
            )
        lines.append("")

    path.write_text("\n".join(lines), encoding="utf-8")
    return path
