"""Scanning stage: run web2 and web3 checks against recon output."""
from __future__ import annotations

from ..config import Settings
from ..llm import LLM
from ..models import ContractInfo, Finding, WebHost
from ..modules.web2 import checks as web2_checks
from ..modules.web3 import checks as web3_checks
from ..skills import Skill, filter_skills


def scan_web2(hosts: list[WebHost], settings: Settings) -> list[Finding]:
    findings: list[Finding] = []
    for host in hosts:
        findings.extend(
            web2_checks.run_checks(host, settings.http_timeout, settings.user_agent)
        )
    return findings


def scan_web3(
    contracts: list[ContractInfo], llm: LLM, skills: list[Skill]
) -> list[Finding]:
    findings: list[Finding] = []
    relevant = filter_skills(skills, {"web3"})
    for contract in contracts:
        findings.extend(web3_checks.analyze_contract(contract, llm, relevant))
    return findings
