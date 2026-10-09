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

- **Dangling trailing comments**:
  ```python
  # Awkward:
  result = (
      value
  )  # here is a long comment that forced the assignment into parentheses

  # Fix: move comment above the statement
  # Here is a long comment explaining the calculation
  result = value
  ```
- **Unnecessary multi-line splits from trailing commas or comments**: Single short arguments pushed onto new lines solely because of inline trailing comments.
- **Awkward dictionary or list wraps**: Short collections split over 4 lines when minor trimming or moving an inline comment above keeps it compact and readable.
- **Pointless parenthesis enclosures**: Single variable returns or assignments wrapped in parens just to accommodate line-trailing annotations.

## Remediation rules

1. **Move comments above statements**: The primary cause of awkward black wrapping is inline/trailing comments pushing lines past 88 characters. Move the comment to the line immediately preceding the code.
2. **Shorten or rephrase bloated comments**: If a comment wraps awkwardly, condense the wording while preserving technical detail.
3. **Inline temporary variables if appropriate**: Per project guidelines, avoid single-use variables where direct inlining clarifies structure without line overflow.
4. **Avoid `# fmt: off`**: Do not reach for `# fmt: off` / `# fmt: on` as a routine workaround. Only consider it for rare, highly structured tabular data or mathematical matrices where vertical column alignment is essential. If used, apply to the smallest possible block and document why.
5. **No semantic changes**: Keep edits strictly limited to formatting, comment placement/wording, and structural layout. Do not alter program logic, variable names, or behavior.
6. **Re-run black**: Always re-run `python -m black <target>` after editing to guarantee black leaves the file untouched.
