---
name: large-task-git-usage
description: Manage git branches and step-by-step checkpoint commits during multi-step, large-scope tasks with major changes. Use when planning or executing large refactors, multi-file redesigns, or long-running tasks.
---

# Large task git usage

Manage git state safely during complex, multi-phase tasks.

## Core rules

1. Work only on an agent branch. Never modify `main` or human feature branches directly during an autonomous run.
2. Commit after each completed step. Small checkpoint commits make rollbacks painless.
3. Stage only explicit files. Never run `git add .` or `git add -A`.
4. Review every diff before committing.
5. No auto-merging. Merging back to human branches requires manual review by the user.

## Branch naming

Follow this hierarchy:

`<user>/<project if applicable>/<ticket if applicable>/<agent-name>/<desc>`

Examples:
- `indi/ai_hints/gemini/task-parser-split`
- `indi/proj/PROJ-104/gemini/refactor-step-1`

If project or ticket do not apply, omit those segments:
`indi/gemini/refactor-step-1`

## Workflow

1. Check current status and create the task branch:
   ```bash
   git status -s
   git checkout -b <branch-name>
   ```

2. After each milestone or logical step:
   - Format modified files (e.g. `python -m black .` for Python).
   - Stage exact files:
     ```bash
     git add <path/to/file>
     ```
   - Inspect the staged diff:
     ```bash
     git diff --staged
     ```
   - Commit with the step number, what changed, and why:
     ```bash
     git commit -m "[AI commit] step <N>: <what> - <why>"
     ```

3. If an approach fails:
   - Roll back to the previous step cleanly:
     ```bash
     git reset --hard HEAD~1
     ```

4. Completion:
   - Leave the final changes committed on the agent branch.
   - Report the branch name and commit summary to the user so they can review and merge.
