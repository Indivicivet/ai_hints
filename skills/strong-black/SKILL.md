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
3. Inspect `git diff` for awkward layout artifacts produced by line-length overflows or trailing comments.
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

1. Move comments above statements: The primary cause of awkward black wrapping is inline comments pushing lines past 88 characters. Move them above the code.
2. Shorten comments: Condense wording if a comment still wraps awkwardly.
3. Inline temporary variables: Avoid single-use variables where direct inlining clarifies structure without line overflow.
4. Avoid `# fmt: off`: Reserve for rare tabular data or matrices where vertical columns matter.
5. Keep logic intact: Change layout, comment position, and spacing only. Leave logic and variables unchanged.
6. Re-run black: Always re-run black after editing to verify it leaves the file untouched.
