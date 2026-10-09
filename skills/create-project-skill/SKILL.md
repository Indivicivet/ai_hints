---
name: create-project-skill
description: Draft a project-specific skill inside the current workspace repository. Use when teaching the agent local build or testing commands, and repository conventions.
---

# Create project skill

Add a project-scoped skill to the active repository.

## Location

Write the file to `<project-root>/.agents/skills/<skill-name>/SKILL.md`. If the repository does not use `.agents/skills/` but already has a top-level `skills/` folder, follow that existing pattern instead.

## Rules

Follow general `skill-writing` guidelines.

Tie instructions to the codebase. Hardcode local paths, configuration files, test scripts, and build flags. General advice belongs in global skills and use of `create-global-skill`.

Provide exact commands and expected results. Specify the exact CLI command to run, along with the expected output.

Separate guidelines from workflows.
