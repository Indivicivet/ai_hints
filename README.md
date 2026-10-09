# AI Hints

Developer rules, formatting standards, and pair-programming skills.

## Gemini Setup

~/.gemini/config/plugins.json:
```
{
  "entries": [
    {
      "path": "... repo folder ..."
    }
  ]
}
```

and add "... repo folder .../" to Antigravity settings -> General -> File Access Rules
(if using skills: just read. if you want to build on it, e.g. using `/create-global-skill`, then also give write access)

## Claude Code Setup

(untested)

~/.claude/CLAUDE.md:
```
@c:/path/to/repos/ai_hints/rules/AGENTS.md
```

## Custom Skills

Skills developed specifically for this environment and workflow:

- **[assume-installed](./skills/assume-installed/SKILL.md)**: Assume packages and libraries are installed without pre-flight check commands.
- **[clang-format-black](./skills/clang-format-black/SKILL.md)**: Format C/C++ (and supported languages) using clang-format with a black-esque style configuration.
- **[create-global-skill](./skills/create-global-skill/SKILL.md)**: Draft a cross-cutting, personal skill in ai_hints regardless of active workspace.
- **[create-project-skill](./skills/create-project-skill/SKILL.md)**: Draft a project-specific skill inside the current workspace repository.
- **[desktop-gui](./skills/desktop-gui/SKILL.md)**: Guidelines for building desktop GUIs (PySide6 default, slider-spinbox sync, theme safety).
- **[direct-web-cite](./skills/direct-web-cite/SKILL.md)**: Verify and extract verbatim quotes from live web pages as unmanipulated HTML citations.
- **[large-task-git-usage](./skills/large-task-git-usage/SKILL.md)**: Manage branches and step-by-step checkpoint commits during multi-step, large-scope tasks.
- **[mathematical-audience](./skills/mathematical-audience/SKILL.md)**: Frame technical concepts for a mathematically experienced reader without assuming niche domain vocabulary.
- **[pitch-higher](./skills/pitch-higher/SKILL.md)**: Nudge the last explanation a step higher in assumed competence and density.
- **[pitch-lower](./skills/pitch-lower/SKILL.md)**: Nudge the last explanation a step lower in assumed background, unpacking jargon and steps.
- **[safe-commit](./skills/safe-commit/SKILL.md)**: Stage specific files, review staged diffs, and write structured commit messages.
- **[skill-writing](./skills/skill-writing/SKILL.md)**: Draft, review, or refine an agent skill with anti-slop and opinionated constraints.
- **[sort-out-imports](./skills/sort-out-imports/SKILL.md)**: Tidy Python imports via isort and enforce explicit namespace imports.
- **[strong-black](./skills/strong-black/SKILL.md)**: Run black, inspect diffs for awkward wrapping or comment artifacts, manually fix layout, and re-run black.
- **[transcribe](./skills/transcribe/SKILL.md)**: Extract image text with optional kana reading/pronunciation (`ro`), translation (`tl`), and nuance explanation (`explain`).

## pstack Skills

Engineering principles and discipline adapted from [pstack](https://github.com/cursor/plugins/tree/main/pstack) (Lauren Tan / `@poteto`):

- **[bro](./skills/bro/SKILL.md)**: Restate the last message in plain language with no jargon. (essentially unmodified)
- **[principle-fix-root-causes](./skills/principle-fix-root-causes/SKILL.md)**: Trace bugs to root cause; no symptom-guard band-aids. (essentially unmodified)
- **[principle-guard-the-context-window](./skills/principle-guard-the-context-window/SKILL.md)**: Route bulk payloads to subagents; keep context window clean. (essentially unmodified)
- **[principle-laziness-protocol](./skills/principle-laziness-protocol/SKILL.md)**: Minimal diffs, flat call chains, and deletion over addition. (essentially unmodified)
- **[principle-minimize-reader-load](./skills/principle-minimize-reader-load/SKILL.md)**: Fewer layers of indirection and reduced mutable state. (essentially unmodified)
- **[unslop](./skills/unslop/SKILL.md)**: Cut AI tells, fluff, and puffery from writing. (Diverged: adapted rules around bolding, colons, em dashes, shorthand like e.g./i.e., and streamlined guidelines)

## Matt Pocock Skills

Workflows and feedback loops adapted from [mattpocock/skills](https://github.com/mattpocock/skills):

- **[grilling](./skills/grilling/SKILL.md)**: Stress-test plans and assumptions through structured design-tree interview rounds. (Diverged: cleaned formatting/unicode artefacts, consolidated standalone prompt)
- **[research](./skills/research/SKILL.md)**: Investigate questions against primary sources with direct citations. (essentially unmodified)
- **[wait-what](./skills/wait-what/SKILL.md)**: Re-pitch the last message in plain English with missing context. (essentially unmodified)
