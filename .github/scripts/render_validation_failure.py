#!/usr/bin/env python3
"""Render .github/validator/failure.mustache with a list of validation errors.

Reads:
  COMMENT_ERRORS -- JSON array of error strings (from issue-ops/validator output)

Writes rendered Markdown to stdout, suitable for piping to:
  gh issue comment ... --body-file -
"""

import json
import os
import re
import sys

errors_json = os.environ.get("COMMENT_ERRORS", "[]")
errors = json.loads(errors_json)

template_path = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "..", "validator", "failure.mustache"
)
with open(template_path) as f:
    body = f.read()

# Render {{#each errors}}\n- {{this}}\n{{/each}}
error_lines = "\n".join(f"- {e}" for e in errors)
body = re.sub(
    r"\{\{#each errors\}\}\n.*?\n\{\{/each\}\}",
    error_lines,
    body,
    flags=re.DOTALL,
)

# Strip HTML comments (markdownlint/prettier directives)
body = re.sub(r"<!--.*?-->", "", body, flags=re.DOTALL)

# Collapse runs of blank lines left behind by comment removal
body = re.sub(r"\n{3,}", "\n\n", body)

sys.stdout.write(body.strip() + "\n")
