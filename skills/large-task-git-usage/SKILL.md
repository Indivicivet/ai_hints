---
name: large-task-git-usage
description: Manage git branches and make frequent step-by-step checkpoint commits during large-scope tasks with changes. Use when the user specifies this skill for large refactors, multi-file redesigns, or long-running tasks.
---

# Large task git usage

Manage git state safely during complex tasks, by frequently committing working code.

## Core rules

1. Work only on an agent branch. Never modify `main` or human feature branches directly during an autonomous run.
2. Commit after each completed step. Small checkpoint commits make rollbacks painless.
3. Stage only explicit files. Never run `git add .` or `git add -A`.
4. Review every diff before committing.
5. Aim to not overly complicate the codebase. If you add a lot of lines in your commit to make something work, after committing, consider doing a light "pruning pass" over your changes so far. If you add complexity to a section of code, see if a minor refactor of the surrounding code can reduce this complexity.
6. No auto-merging. Merging back to human branches requires manual review by the user.

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

2. Continuously as you work on the code, after each update or logical step that improves the code:
   - Stage exact files:
     ```bash
     git add <path/to/file>
     ```
   - Inspect the staged diff:
     ```bash
     git diff --staged
     ```
   - Commit with what changed, and why. Consider adding tags like "- feature", "- fix", "- tidyup" etc to your "[AI commit]"
     ```bash
     git commit -m "[AI commit <optional tag>]: <what> - <why>"
     ```

3. If an approach fails:
   - Never use a --hard git reset if there are dirty or uncommitted files in the workspace.
   - If work is already committed on your agent branch, use the previous good commit by creating a new "second attempt" branch:
     ```bash
     # Identify the last known good commit:
     git log --oneline -n 10

     # Create a variant branch pointing at this commit.
     git checkout -b user/gemini/refactor-retry-1 <last-good-commit-hash>
     ```
     Leave all branches intact for inspection.
   - If there are uncommitted exploratory edits you need to discard without touching unrelated files, discard only the specific files you modified:
     ```bash
     git checkout HEAD -- <path/to/failed_file>
     ```

4. Leave the final changes committed on the agent branch. Report the branch name and commit list to the user so they can review and merge.
