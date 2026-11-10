#!/usr/bin/env python3
"""Build the service levels comment for a deliverables pull request.

A deliverables report includes a `#### Service levels` table for the quarter,
reporting each SLO in the project's SLO file and the continuity obligations.
This script gives the maintainer that table pre-filled with their own SLOs, and
lists anything missing from the report. It is advisory: it never fails the PR.

Reads env vars:
  PAGE_PATH   — the project page changed in the PR, e.g. docs/projects/x.md
  HEAD_REF    — the PR branch, e.g. deliverables/x-2027q1
  SLO_PATH    — where the project's SLO file from main was saved, if it exists

Writes:
  slo-comment.md, when there is something to say

Outputs (to $GITHUB_OUTPUT):
  post — "true" when a comment should be posted or updated
"""

import os
import re

from render_proposal import write_github_output

MARKER = "<!-- pg-award-slo-report -->"
FIRST_SLO_QUARTER = (2027, 1)
INSTRUCTIONS = "https://scf-public-goods-maintenance.github.io/pg-award/proposer-instructions"
REPO_URL = "https://github.com/SCF-Public-Goods-Maintenance/scf-public-goods-maintenance.github.io"
FORM = f"{REPO_URL}/issues/new?template=pg-award-slo-form.yml"


def front_matter(text: str) -> str:
    match = re.match(r"---\n(.*?)\n---", text, re.DOTALL)
    return match.group(1) if match else ""


def read_slos(text: str) -> tuple[list[dict], str | None]:
    """
    Read the SLO list and `since` from an SLO file's front matter. The file is
    written by render_slo.py in a fixed shape, so a line reader is enough and
    keeps this free of a YAML dependency.
    """

    slos, current, since = [], None, None
    for line in front_matter(text).splitlines():
        if line.startswith("since:"):
            since = line.split(":", 1)[1].strip()
        m = re.match(r"  - id: (.+)", line)
        if m:
            current = {"id": m.group(1).strip()}
            slos.append(current)
            continue
        m = re.match(r"    (obligation|target|evidence_source): (.*)", line)
        if m and current is not None:
            current[m.group(1)] = m.group(2).strip().strip('"').replace('\\"', '"')
    return slos, since


def quarter_of(text: str | None) -> tuple[int, int] | None:
    m = re.search(r"(\d{4})\s*-?\s*q([1-4])", text or "", re.IGNORECASE)
    return (int(m.group(1)), int(m.group(2))) if m else None


def quarter_section(page: str, quarter: tuple[int, int]) -> str | None:
    """The `### {Year} Q{N}` section of the page for the reported quarter."""

    year, q = quarter
    m = re.search(rf"^### {year} Q{q}\b.*?(?=^#{{1,3}} |\Z)", page, re.MULTILINE | re.DOTALL)
    return m.group(0) if m else None


def main():
    page_path = os.environ["PAGE_PATH"]
    slo_path = os.environ.get("SLO_PATH", "")
    quarter = quarter_of(os.environ.get("HEAD_REF"))
    slug = os.path.basename(page_path)[:-3]

    with open(page_path) as f:
        page = f.read()
    if quarter is None:
        # Fall back to the newest quarter heading under Past Deliverables.
        quarter = quarter_of(next(iter(re.findall(r"^### (\d{4} Q[1-4])", page, re.MULTILINE)), None))
    if quarter is None or quarter < FIRST_SLO_QUARTER:
        write_github_output({"post": "false"})
        return

    label = f"{quarter[0]} Q{quarter[1]}"
    lines = [MARKER, "### Service levels", ""]

    if not slo_path or not os.path.exists(slo_path):
        lines += [
            f"There are no service levels on file for `{slug}`. Every project reports against its "
            f"SLOs from 2027 Q1, so please [submit the Service Levels Form]({FORM}) first. "
            f"See [Service Levels]({INSTRUCTIONS}/#service-levels).",
        ]
    else:
        with open(slo_path) as f:
            slos, since = read_slos(f.read())
        if quarter_of(since) and quarter < quarter_of(since):
            write_github_output({"post": "false"})
            return

        rows = [(s.get("obligation", s["id"]), s.get("target", "")) for s in slos]
        rows += [
            ("Deploy and publish runbook", "Present and current"),
            ("Code and configuration in the repository", "Complete"),
        ]
        width = max(len(r[0]) for r in rows)
        target_width = max(len("Target"), *(len(r[1]) for r in rows))
        table = [
            "#### Service levels",
            "",
            f"| {'SLO'.ljust(width)} | {'Target'.ljust(target_width)} | Result | Evidence | Met |",
            f"| {'-' * width} | {'-' * target_width} | ------ | -------- | --- |",
            *[f"| {o.ljust(width)} | {t.ljust(target_width)} |        |          |     |" for o, t in rows],
        ]

        section = quarter_section(page, quarter)
        missing = []
        if section is None:
            missing.append(f"a `### {label}` section under `## Past Deliverables`")
        elif not re.search(r"^#### Service levels", section, re.MULTILINE | re.IGNORECASE):
            missing.append(f"a `#### Service levels` table in the `### {label}` section")
        else:
            lowered = section.lower()
            missing += [f"a row for **{o}**" for o, _ in rows if o.lower() not in lowered]

        lines += [
            f"Your {label} report includes a `#### Service levels` table after the budget table, "
            f"reporting each of your SLOs from [`docs/slos/{slug}.md`]({REPO_URL}/blob/main/docs/slos/{slug}.md) "
            "and the continuity obligations. Copy this in and fill in **Result**, **Evidence** "
            "(links) and **Met** (Yes / No):",
            "",
            "```markdown",
            *table,
            "```",
            "",
        ]
        if missing:
            lines += ["Still missing from your report:", "", *[f"- [ ] {m}" for m in missing], ""]
        else:
            lines += [":white_check_mark: Every SLO has a row in your report.", ""]
        if quarter == FIRST_SLO_QUARTER:
            lines += ["_In 2027 Q1 a missed SLO is reported but does not affect Tranche 2._"]

    with open("slo-comment.md", "w") as f:
        f.write("\n".join(lines) + "\n")
    write_github_output({"post": "true"})


if __name__ == "__main__":
    main()
