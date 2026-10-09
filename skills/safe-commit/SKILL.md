---
name: safe-commit
description: Stage specific files and commit changes with a reviewed diff and clean summary. Use when asked to commit, save git changes, or when the user invokes /safe-commit.
---

# Safe commit

Stage explicit files, inspect the exact diff, and record a commit.

## Core constraints

1. Never run `git add .`, `git add -A`, or wildcard adds. Add only explicit paths.
2. Only commit if currently on a dedicated agent branch or when the user explicitly approved the commit.
3. Never auto-merge or push to remote branches without explicit instruction.

## Procedure

1. Verify the current branch:
   ```bash
   git branch --show-current
   ```
   If on `main`, `master`, or a shared human branch and the user has not asked to commit there, stop and ask the user, or switch to an agent branch first.

2. Run repository formatters before staging (e.g. `python -m black .` for Python).

3. Stage only the relevant changed files:
   ```bash
   git add <path/to/file1> <path/to/file2>
   ```

4. Inspect the staged diff:
   ```bash
   git diff --staged
   ```
   Confirm no scratch files, secrets, build artifacts, or unrelated edits are included.

5. Formulate the commit message:
   - Format: `[AI commit] <what>: <why>`
   - State what changed and why it changed. Do not add decorative commentary or marketing adjectives.

6. Commit:
   ```bash
   git commit -m "[AI commit] <what>: <why>"
   ```
