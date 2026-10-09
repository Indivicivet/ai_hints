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

If the user has a checked-out branch that seems relevant to your work, you can create a new branch using the same user/project/ticket/ tags and just interjecting `/gemini/`.

Example:
- `bob/ai_hints/gemini/parser_task`

If project or ticket do not apply, omit those segments:
`bob/gemini/parser_task`

## Workflow

1. Check current status and create the task branch:
   ```bash
   git status -s
   git checkout -b <branch-name>
   ```

  When checking status you should flag to the user if they have uncommitted changes that could get overriden by later git usage, especially if you don't recognise them. If you KNOW they are your changes you can bring them with you and commit them on your branch.

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
   - Never use a hard git reset if there are dirty or uncommitted files in the workspace.
   - If work is already committed in a checkpoint commit on your agent branch, revert to the previous good commit by creating a new "second attempt" branch:
     ```bash
     # Inspect history to identify the last known good commit:
     git log --oneline -n 10

     # Create a variant branch pointing at this commit.
     git checkout -b user/gemini/refactor-retry-1 <last-good-commit-hash>
     ```
     Leave your other branch intact for inspection, and retrospective on what went wrong.
   - If there are uncommitted exploratory edits you need to discard without touching unrelated dirty files, discard only the specific files you modified:
     ```bash
     git checkout HEAD -- <path/to/failed_file>
     ```

4. Completion:
   - Leave the final changes committed on the agent branch.
   - Report the branch name and commit summary to the user so they can review and merge.
