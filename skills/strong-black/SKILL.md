---
name: strong-black
description: Run black across files or an entire project, inspect diffs for awkward formatting artifacts (such as trailing comment wraps or unnatural line breaks), and manually fix them cleanly before re-running black.
---

# Strong black

Run black across a project or targeted scope, inspect the resulting diff for unnatural formatting artifacts, fix the underlying code or comment layout manually, and re-run black until clean.

Default scope: the entire project workspace unless the user names specific files or directories.

## Workflow

1. Check git status to ensure working tree changes are understood or clean before formatting.
2. Run black on the target scope (`python -m black <scope>`).
3. Inspect `git diff` for awkward layout artifacts produced by line-length overflows, trailing comments, or weird code structure. If Black's layout for an expression is acceptable, keep it.
4. Manually edit those awkward sections so black formats them naturally.
5. Re-run black on the edited files.
6. Verify diffs are clean, readable, and fully compliant with black.

## Detecting awkward black formatting

Black strictly enforces line length (88 characters). When an inline comment, tuple wrap, or expression barely exceeds that limit, black often splits code into visually jarring shapes:

- Dangling trailing comments wrapped in parens:
  ```python
  # Awkward:
  result = (
      value
  )  # here is a long comment that forced the assignment into parentheses

  # Fix: move comment above the statement
  # Here is a long comment explaining the calculation
  result = value
  ```
- Unnecessary multi-line splits from trailing commas or comments.
- Short dicts or lists split over multiple lines due to inline comments.
- Single returns wrapped in parens to accommodate line-trailing annotations.

## Remediation rules

1. Formatting only, no structural refactors: Never convert expressions or ternaries into multi-line `if`/`elif`/`else` statements. Avoid introducing new variables unless there's no better way to solve the problem.
2. Move whole-statement comments above: When a comment annotates an entire assignment or return statement and forces dangling parens, move it above the statement.
3. Preserve clause-level and toggle comments: Do NOT move comments that belong to a specific sub-clause or contain toggleable code (e.g. `# * 4` or branch-specific explanations). Moving them destroys locality and ease of modification.
4. Shorten comments: Condense wording if a comment still wraps awkwardly.
5. You may occasionally inline temporary variables if this helps with awkwardly formatted code, but ONLY if this is helping black.
6. Avoid `# fmt: off`: Reserve for rare tabular data or matrices where vertical columns matter.
7. Keep logic intact: Change layout, comment position, and spacing only. Leave control flow, logic, and variables unchanged.
8. Re-run black: Always re-run black after editing to verify it leaves the file untouched.
