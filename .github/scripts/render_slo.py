#!/usr/bin/env python3
"""Render a parsed PG Award service levels issue form into an SLO file.

Reads env vars set by the workflow:
  PARSED_JSON  — JSON string from the issue-ops/parser step
  ISSUE_NUMBER — GitHub issue number
  ISSUE_AUTHOR — GitHub username of the issue author
  PROJECT_SLUG — slug of the project page, when the form linked one; otherwise
                 the slug is derived from the project name, exactly as the
                 proposal form does, so both files end up with the same name
  SUBMITTED_AT — ISO date the issue was opened (defaults to today)

Writes:
  docs/slos/{slug}.md

The SLOs are stored twice: as structured front matter, which later automated
checks read, and as a table for people. Every SLO starts as `check: manual`;
an individual SLO moves to `automated` once a check exists for it, without the
project resubmitting anything.

Outputs (to $GITHUB_OUTPUT):
  slug, file_path, project_title
"""

import datetime
import json
import os
import re
import sys

from render_proposal import MarkdownLinterFlag, slugify, wrap_with_md_lint, write_github_output

# SLOs bind from 2027 Q1. A project submitting earlier is committing for then.
FIRST_SLO_QUARTER = (2027, 1)


def table_rows(markdown: str) -> list[list[str]]:
    """
    Read the data rows of a markdown table, skipping the header, the separator
    and rows left empty from the form's pre-filled template.
    """

    rows = []
    for line in markdown.splitlines():
        line = line.strip()
        if not line.startswith("|"):
            continue
        cells = [c.strip() for c in line.strip("|").split("|")]
        if all(re.fullmatch(r":?-*:?", c) for c in cells):
            continue  # separator, or a row with every cell empty
        rows.append(cells)

    if rows and [c.lower() for c in rows[0][:3]] == ["obligation", "target", "evidence source"]:
        rows = rows[1:]

    return rows


def parse_repositories(text: str) -> list[dict]:
    repos = []
    for line in text.splitlines():
        line = line.strip().lstrip("-* ").strip()
        if not line:
            continue
        upstream = bool(re.search(r"\(upstream\)", line, re.IGNORECASE))
        url = re.sub(r"\(upstream\)", "", line, flags=re.IGNORECASE).strip().strip("<>")
        repos.append({"url": url, "upstream": upstream})
    return repos


def applies_from(submitted: datetime.date) -> tuple[int, int]:
    current = (submitted.year, (submitted.month - 1) // 3 + 1)
    return max(current, FIRST_SLO_QUARTER)


def front_matter_value(project_page: str, key: str) -> str | None:
    """Read one scalar from an existing project page's front matter."""

    try:
        with open(project_page) as f:
            text = f.read()
    except FileNotFoundError:
        return None
    match = re.match(r"---\n(.*?)\n---", text, re.DOTALL)
    if not match:
        return None
    for line in match.group(1).splitlines():
        if line.startswith(f"{key}:"):
            return line.split(":", 1)[1].strip().strip('"')
    return None


def q(value: str) -> str:
    """Quote a string for YAML front matter. JSON strings are valid YAML."""
    return json.dumps(value, ensure_ascii=False)


def md_url(url: str) -> str:
    url = url.strip()
    return f"<{url}>" if url and not url.startswith("<") else url


def main():
    raw = os.environ.get("PARSED_JSON")
    if not raw:
        sys.exit("Error: PARSED_JSON environment variable is not set")

    issue_number = os.environ.get("ISSUE_NUMBER", "0")
    issue_author = os.environ.get("ISSUE_AUTHOR", "unknown")
    submitted = datetime.date.fromisoformat(
        os.environ.get("SUBMITTED_AT", "")[:10] or datetime.date.today().isoformat()
    )

    parsed = json.loads(raw)
    project_name_raw = str(parsed.get("project-name", "Untitled Project"))
    project_title = project_name_raw.replace("\n", "⏎")
    repositories = parse_repositories(str(parsed.get("repositories", "")))
    slo_rows = table_rows(str(parsed.get("slos", "")))
    runbook = str(parsed.get("runbook", "")).strip()
    exceptions = str(parsed.get("continuity-exceptions", "")).strip()
    notes = str(parsed.get("notes", "")).strip()

    slug = os.environ.get("PROJECT_SLUG") or slugify(project_name_raw) or f"project-{issue_number}"
    project_page = os.path.join("docs", "projects", f"{slug}.md")
    canonical_id = front_matter_value(project_page, "canonical_id")
    year, quarter = applies_from(submitted)

    # --- Front matter ---------------------------------------------------------
    fm = [
        "---",
        f"title: {q('Service Levels: ' + project_title)}",
        "parent: Service Levels",
        f"project: {slug}",
    ]
    if canonical_id:
        fm.append(f"canonical_id: {canonical_id}")
    fm += [
        f"slo_issue: {issue_number}",
        f"submitted_by: {issue_author}",
        f"since: {year}Q{quarter}",
        "repositories:",
    ]
    for repo in repositories:
        fm.append(f"  - url: {q(repo['url'])}")
        if repo["upstream"]:
            fm.append("    upstream: true")
    fm.append("slos:")
    used_ids = set()
    for cells in slo_rows:
        obligation, target, source = (cells + ["", "", ""])[:3]
        slo_id = slugify(obligation, max_len=48) or "slo"
        base, n = slo_id, 2
        while slo_id in used_ids:
            slo_id, n = f"{base}-{n}", n + 1
        used_ids.add(slo_id)
        fm += [
            f"  - id: {slo_id}",
            f"    obligation: {q(obligation)}",
            f"    target: {q(target)}",
            f"    evidence_source: {q(source)}",
            "    check: manual",
        ]
    fm += [
        "continuity:",
        f"  runbook: {q(runbook)}",
        "  in_repository: true",
        f"  exceptions: {'true' if exceptions else 'false'}",
        "---",
    ]

    # --- Body -----------------------------------------------------------------
    body = [
        f"# Service Levels: {project_title}\n",
        "| | |",
        "| --- | --- |",
        f"| **Project page** | [{project_title}](/projects/{slug}/) |",
        f"| **Submitted in** | #{issue_number} |",
        f"| **Applies from** | {year} Q{quarter} |",
        "",
        "## Repositories Covered\n",
        *[f"- {md_url(r['url'])}{' (upstream)' if r['upstream'] else ''}" for r in repositories],
        "",
        "## Service Level Objectives\n",
        "| Obligation | Target | Evidence source |",
        "| --- | --- | --- |",
        *[f"| {' | '.join((c + ['', '', ''])[:3])} |" for c in slo_rows],
        "",
        "## Continuity\n",
        "| | |",
        "| --- | --- |",
        f"| **Deploy and publish runbook** | {md_url(runbook)} |",
        "| **Code and configuration in the repository** | Yes |",
        "",
    ]
    if exceptions:
        body += ["### Exceptions\n", wrap_with_md_lint(exceptions, MarkdownLinterFlag.MD034), ""]
    if notes:
        body += ["## Notes\n", wrap_with_md_lint(notes, MarkdownLinterFlag.MD034), ""]

    content = "\n".join(fm) + "\n\n" + "\n".join(body)

    out_dir = os.path.join("docs", "slos")
    os.makedirs(out_dir, exist_ok=True)
    file_path = os.path.join(out_dir, f"{slug}.md")
    with open(file_path, "w") as f:
        f.write(content)

    print(f"Rendered {file_path} ({len(content)} bytes, {len(slo_rows)} SLOs)")
    write_github_output({"slug": slug, "file_path": file_path, "project_title": project_title})


if __name__ == "__main__":
    main()
