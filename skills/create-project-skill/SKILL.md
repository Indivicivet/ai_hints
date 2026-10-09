---
name: create-project-skill
description: Draft a project-specific skill inside the current workspace repository. Use when teaching the agent local build commands, runbooks, or repository conventions.
---

# Create project skill

Add a project-scoped skill to the active repository.

## Location

Write the file to `<project-root>/.agents/skills/<skill-name>/SKILL.md`.

Antigravity natively auto-discovers skills placed in `.agents/skills/` (and its variants `_agents/skills/` or `.agent/skills/`) by walking up from the current working directory to the project repository root.

If the repository does not use `.agents/skills/` but already has a top-level `skills/` registered in a workspace config, follow that existing pattern instead.

## Rules

1. Tie instructions to the codebase. Hardcode local paths, configuration files, test scripts, and build flags. General advice belongs in global skills.
2. Provide exact commands and expected results. Specify the exact CLI command to run, along with the expected exit code or success output.
3. No syntax primers. Do not explain standard language features or library basics.
4. Separate guidelines from workflows. If the skill describes a passive invariant rather than an executable sequence, add `disable-model-invocation: true` to the frontmatter.
