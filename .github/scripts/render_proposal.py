#!/usr/bin/env python3
"""Render a parsed PG Award proposal issue form into a Jekyll project page.

Reads env vars set by issue-ops/parser in a GitHub Actions workflow:
  PARSED_JSON  — JSON string from the parser step
  ISSUE_NUMBER — GitHub issue number
  ISSUE_AUTHOR — GitHub username of the issue author

Writes:
  docs/projects/{slug}.md

Outputs (to $GITHUB_OUTPUT):
  slug, file_path, project_title
"""

import enum
import json
import os
import re
import sys
import textwrap


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

MD_ENABLE_MD036 = "<!-- markdownlint-enable MD036 -->"
MD_DISABLE_MD036 = "<!-- markdownlint-disable MD036 -->"
MD_ENABLE_MD034 = "<!-- markdownlint-enable MD034 -->"
MD_DISABLE_MD034 = "<!-- markdownlint-disable MD034 -->"


class MarkdownLinterFlag(enum.Enum):
    MD036 = "MD036/no-emphasis-as-header"  # allow # Header\n_Emphasis_ as title
    MD034 = "MD034/no-bare-urls"  # allow bare URLs in project description, etc.


def slugify(name: str, max_len: int = 64) -> str:
    """Lowercase, replace non-alnum with hyphens, collapse, strip, truncate."""
    s = name.lower()
    s = re.sub(r"[^a-z0-9]+", "-", s)
    s = s.strip("-")
    return s[:max_len].rstrip("-")


def unwrap_dropdown(value):
    """Parser returns dropdown values as '["Value"]'; extract the string."""
    if isinstance(value, list):
        return value[0] if value else ""
    return str(value)


def format_checkboxes(value) -> str:
    """Format checkboxes dict into readable markdown."""
    if isinstance(value, dict):
        lines = []
        for item in value.get("selected", []):
            lines.append(f"- [x] {item}")
        for item in value.get("unselected", []):
            lines.append(f"- [ ] {item}")
        return "\n".join(lines)
    return str(value)


def write_github_output(pairs: dict[str, str]):
    """Append key=value pairs to $GITHUB_OUTPUT."""
    output_file = os.environ.get("GITHUB_OUTPUT")
    if output_file:
        with open(output_file, "a") as f:
            for k, v in pairs.items():
                f.write(f"{k}={v}\n")
    else:
        # Local testing: print to stderr
        for k, v in pairs.items():
            print(f"  {k}={v}", file=sys.stderr)


def wrap_with_md_lint(content: str, lint_flag: MarkdownLinterFlag) -> str:
    match lint_flag:
        case MarkdownLinterFlag.MD036:
            return f"{MD_DISABLE_MD036}\n{content}\n{MD_ENABLE_MD036}"
        case MarkdownLinterFlag.MD034:
            return f"{MD_DISABLE_MD034}\n{content}\n{MD_ENABLE_MD034}"
        case _:
            return content


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------


def main():
    raw = os.environ.get("PARSED_JSON")
    if not raw:
        sys.exit("Error: PARSED_JSON environment variable is not set")

    issue_number = os.environ.get("ISSUE_NUMBER", "0")
    issue_author = os.environ.get("ISSUE_AUTHOR", "unknown")

    parsed = json.loads(raw)

    # --- Extract fields -------------------------------------------------------
    project_name = str(parsed.get("project-name", "Untitled Project"))
    one_sentence = str(parsed.get("one-sentence", ""))
    intake_link = str(parsed.get("pg-award-intake", ""))
    release_date = str(parsed.get("release-date", ""))
    category = unwrap_dropdown(parsed.get("category", "Other"))
    description = str(parsed.get("project-description", ""))
    website = str(parsed.get("website", ""))
    git_repo = str(parsed.get("git-repo", ""))
    team_experience = str(parsed.get("team-experience", ""))
    retro_impact = str(parsed.get("pg-retroactive-impact", ""))
    retro_deliverable = str(parsed.get("pg-retroactive-deliverable", ""))
    proposal_impact = str(parsed.get("pg-proposal-impact", ""))
    proposal_deliverable = str(parsed.get("pg-proposal-deliverable", ""))
    budget_ask = str(parsed.get("budget-ask", ""))
    legal = format_checkboxes(parsed.get("legal-acknowledgements", ""))

    slug = slugify(project_name)
    if not slug:
        slug = f"project-{issue_number}"

    # --- Build page -----------------------------------------------------------
    front_matter = textwrap.dedent(
        f"""\
        ---
        title: "{project_name.replace('"', '\\"')}"
        parent: Public Good Projects
        proposal_issue: {issue_number}
        proposer: {issue_author}
        category: "{category.replace('"', '\\"')}"
        budget: "{budget_ask.replace('"', '\\"')}"
        ---
    """
    )

    def md_url(url: str) -> str:
        """Wrap a URL in angle brackets to satisfy MD034/no-bare-urls."""
        url = url.strip()
        if url and not url.startswith("<"):
            return f"<{url}>"
        return url

    body_parts = [
        f"# {project_name}\n",
        wrap_with_md_lint(f"_{one_sentence}_", MarkdownLinterFlag.MD036),
        "| | |",
        "| --- | --- |",
        f"| **Category** | {category} |",
        f"| **Website** | {md_url(website)} |",
        f"| **Repository** | {md_url(git_repo)} |",
        f"| **First Released** | {release_date} |",
        f"| **Intake** | {md_url(intake_link)} |",
        f"| **Budget Requested** | {budget_ask} |",
        "",
        "## Project Description\n",
        wrap_with_md_lint(description, MarkdownLinterFlag.MD034),
        "",
        "## Team & Experience\n",
        wrap_with_md_lint(team_experience, MarkdownLinterFlag.MD034),
        "",
        "## Retroactive Impact\n",
        wrap_with_md_lint(retro_impact, MarkdownLinterFlag.MD034),
        "",
        "## Past Deliverables\n",
        wrap_with_md_lint(retro_deliverable, MarkdownLinterFlag.MD034),
        "",
        "## Proposed Impact\n",
        wrap_with_md_lint(proposal_impact, MarkdownLinterFlag.MD034),
        "",
        "## Proposed Deliverables\n",
        wrap_with_md_lint(proposal_deliverable, MarkdownLinterFlag.MD034),
        "",
        "## Legal Acknowledgements\n",
        legal,
        "",
    ]

    content = front_matter + "\n".join(body_parts) + "\n"

    # --- Write file -----------------------------------------------------------
    out_dir = os.path.join("docs", "projects")
    os.makedirs(out_dir, exist_ok=True)
    file_path = os.path.join(out_dir, f"{slug}.md")

    with open(file_path, "w") as f:
        f.write(content)

    print(f"Rendered {file_path} ({len(content)} bytes)")

    # --- Outputs --------------------------------------------------------------
    write_github_output(
        {
            "slug": slug,
            "file_path": file_path,
            "project_title": project_name,
        }
    )


if __name__ == "__main__":
    main()
