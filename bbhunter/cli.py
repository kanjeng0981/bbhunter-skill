"""Command-line interface for bbhunter."""
from __future__ import annotations

from pathlib import Path

import click
from rich.console import Console
from rich.table import Table

from . import __version__
from .agent import Agent, ReconResult
from .config import Settings
from .models import Finding, SEVERITY_ORDER

console = Console()

BANNER = (
    "⚠️  bbhunter — only use against targets you are AUTHORIZED to test.\n"
    "   Unauthorized scanning is illegal and violates bug bounty program rules."
)


def _build_agent(output: str) -> Agent:
    settings = Settings()
    if output:
        settings.output_dir = Path(output)
    settings.resolve()
    return Agent(settings)


def _scope(
    web2_targets: tuple[str, ...],
    contracts: tuple[str, ...],
    web2_only: bool,
    web3_only: bool,
) -> tuple[list[str], list[str]]:
    if web2_only:
        return list(web2_targets), []
    if web3_only:
        return [], list(contracts)
    return list(web2_targets), list(contracts)


def _print_findings(findings: list[Finding]) -> None:
    if not findings:
        console.print("[dim]No findings.[/dim]")
        return
    table = Table(title=f"Findings ({len(findings)})")
    table.add_column("Severity")
    table.add_column("Title")
    table.add_column("Target")
    table.add_column("Confidence")
    for f in sorted(findings, key=lambda x: -SEVERITY_ORDER[x.severity]):
        color = {
            "critical": "bold red", "high": "red", "medium": "yellow",
            "low": "cyan", "info": "dim",
        }[f.severity]
        table.add_row(f"[{color}]{f.severity}[/{color}]", f.title, f.target, f.confidence)
    console.print(table)


@click.group()
@click.version_option(__version__, prog_name="bbhunter")
def main() -> None:
    """bbhunter — AI-powered bug bounty hunter agent (web2 + web3)."""


@main.command()
@click.option("-t", "--target", "web2_targets", multiple=True, help="Web2 domain or URL (repeatable).")
@click.option("-c", "--contract", "contracts", multiple=True, help="Web3 contract address (repeatable).")
@click.option("--chain", default="", help="Chain name for web3 (e.g. ethereum, polygon).")
@click.option("-o", "--output", default="", help="Output directory for reports.")
@click.option("--no-validate", is_flag=True, help="Skip LLM triage stage.")
@click.option("--web2-only", is_flag=True, help="Only run web2 stages.")
@click.option("--web3-only", is_flag=True, help="Only run web3 stages.")
def run(
    web2_targets: tuple[str, ...],
    contracts: tuple[str, ...],
    chain: str,
    output: str,
    no_validate: bool,
    web2_only: bool,
    web3_only: bool,
) -> None:
    """Run the full pipeline: recon -> scan -> validate -> report."""
    console.print(BANNER)
    web2, web3 = _scope(web2_targets, contracts, web2_only, web3_only)
    if not web2 and not web3:
        raise click.UsageError("Provide at least one --target or --contract.")

    agent = _build_agent(output)
    with console.status("[bold green]Running recon..."):
        recon = agent.recon(web2, web3, chain)
    console.print(
        f"Recon: {len(recon.hosts)} host(s), {len(recon.contracts)} contract(s)"
    )

    with console.status("[bold green]Scanning..."):
        findings = agent.scan(recon)

    if not no_validate:
        if agent.settings.llm_enabled:
            with console.status("[bold green]Validating with LLM..."):
                findings = agent.validate(findings)
        else:
            console.print(
                "[dim]LLM disabled (no BBHUNTER_LLM_API_KEY) — skipping triage.[/dim]"
            )

    path = agent.report(recon, findings)
    _print_findings(findings)
    console.print(f"\n[bold green]Report written to[/bold green] {path}")


@main.command()
@click.option("-t", "--target", "web2_targets", multiple=True, help="Web2 domain or URL (repeatable).")
@click.option("-c", "--contract", "contracts", multiple=True, help="Web3 contract address (repeatable).")
@click.option("--chain", default="", help="Chain name for web3.")
def recon(
    web2_targets: tuple[str, ...],
    contracts: tuple[str, ...],
    chain: str,
) -> None:
    """Run recon only and print a summary."""
    console.print(BANNER)
    agent = _build_agent("")
    with console.status("[bold green]Running recon..."):
        result: ReconResult = agent.recon(list(web2_targets), list(contracts), chain)

    if result.hosts:
        table = Table(title=f"Web hosts ({len(result.hosts)})")
        table.add_column("URL"); table.add_column("Status"); table.add_column("Title"); table.add_column("Tech")
        for h in result.hosts:
            table.add_row(h.url, str(h.status), h.title or "-", ", ".join(h.technologies) or "-")
        console.print(table)
    if result.contracts:
        table = Table(title=f"Contracts ({len(result.contracts)})")
        table.add_column("Address"); table.add_column("Chain"); table.add_column("Has code"); table.add_column("Verified")
        for c in result.contracts:
            table.add_row(c.address, c.chain or c.chain_id or "-", "yes" if c.has_code else "no", "yes" if c.verified else "no")
        console.print(table)
    if not result.hosts and not result.contracts:
        console.print("[dim]Nothing found.[/dim]")


@main.command()
@click.option("-t", "--target", "web2_targets", multiple=True, help="Web2 domain or URL (repeatable).")
@click.option("-c", "--contract", "contracts", multiple=True, help="Web3 contract address (repeatable).")
@click.option("--chain", default="", help="Chain name for web3.")
@click.option("--no-validate", is_flag=True, help="Skip LLM triage stage.")
def scan(
    web2_targets: tuple[str, ...],
    contracts: tuple[str, ...],
    chain: str,
    no_validate: bool,
) -> None:
    """Run recon + scan (+ validate) and print findings."""
    console.print(BANNER)
    web2, web3 = _scope(web2_targets, contracts, False, False)
    if not web2 and not web3:
        raise click.UsageError("Provide at least one --target or --contract.")

    agent = _build_agent("")
    with console.status("[bold green]Running recon..."):
        result = agent.recon(web2, web3, chain)
    with console.status("[bold green]Scanning..."):
        findings = agent.scan(result)
    if not no_validate:
        if agent.settings.llm_enabled:
            with console.status("[bold green]Validating with LLM..."):
                findings = agent.validate(findings)
        else:
            console.print(
                "[dim]LLM disabled (no BBHUNTER_LLM_API_KEY) — skipping triage.[/dim]"
            )
    _print_findings(findings)


@main.command()
def skills() -> None:
    """List loaded skills from the skills directory."""
    agent = _build_agent("")
    if not agent.skills:
        console.print("[dim]No skills found. Drop Markdown skill files into the skills/ directory.[/dim]")
        return
    console.print(f"[dim]{len(agent.skills)} skills loaded[/dim]\n")
    for s in agent.skills:
        console.print(f"[bold]{s.name}[/bold] [dim]({s.scope})[/dim] — {s.description or '(no description)'}")


if __name__ == "__main__":
    main()
