"""Agent orchestrator: recon -> scan -> validate -> report."""
from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path

from .config import Settings
from .llm import LLM
from .models import ContractInfo, Finding, WebHost
from .pipeline import recon as recon_stage
from .pipeline import report as report_stage
from .pipeline import scan as scan_stage
from .pipeline import validate as validate_stage
from .skills import Skill, load_skills


@dataclass
class ReconResult:
    hosts: list[WebHost] = field(default_factory=list)
    contracts: list[ContractInfo] = field(default_factory=list)


class Agent:
    def __init__(self, settings: Settings):
        self.settings = settings
        self.llm = LLM(settings)
        self.skills: list[Skill] = load_skills(settings.skills_dir)

    def recon(self, web2_targets: list[str], contracts: list[str], chain: str) -> ReconResult:
        result = ReconResult()
        if web2_targets:
            result.hosts = recon_stage.recon_web2(web2_targets, self.settings)
        if contracts:
            result.contracts = recon_stage.recon_web3(contracts, chain, self.settings)
        return result

    def scan(self, recon: ReconResult) -> list[Finding]:
        findings: list[Finding] = []
        if recon.hosts:
            findings += scan_stage.scan_web2(recon.hosts, self.settings)
        if recon.contracts:
            findings += scan_stage.scan_web3(recon.contracts, self.llm, self.skills)
        return findings

    def validate(self, findings: list[Finding]) -> list[Finding]:
        return validate_stage.validate(findings, self.llm, self.skills)

    def report(self, recon: ReconResult, findings: list[Finding]) -> Path:
        return report_stage.write_report(
            self.settings.output_dir, recon.hosts, recon.contracts, findings
        )

    def run(
        self,
        web2_targets: list[str],
        contracts: list[str],
        chain: str,
        *,
        validate: bool = True,
    ) -> Path:
        recon = self.recon(web2_targets, contracts, chain)
        findings = self.scan(recon)
        if validate:
            findings = self.validate(findings)
        return self.report(recon, findings)
