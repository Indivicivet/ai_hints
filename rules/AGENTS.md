# Project Rules & Guidelines

## Code & Formatting Standards
- Formatter: Follow 'Black' formatting rules (88 chars per line, double quotes, trailing commas). Run black to check.
- Comments: Add comments with detailed explanation or "gotcha" notes where necessary. You do not generally need to add "self-explanatory" comments. Comments MUST NOT be included if they simply declare what a variable is in a way that could be otherwise made clear by a better choice of variable name.
- Typing: Only use type hints when adding or modifying function signatures if this helps to clarify the types involved; don't bother with them if the types are highly variable (e.g. any arithmetic types). Don't bother with them if the code is already clear. Do not add types to existing code unless requested.
- Avoid single use variables - inline variables where possible, unless declaring them as a separate variable is used for debugging, or it makes it significantly clearer what something is for - typically including only at the use site is better.
- Imports: Use absolute imports. Do not reorganize existing imports unless a new one is required. Avoid "import X as Y" except for explicit cases that there is justification for IN THE CODEBASE you're working on (you are allowed `import numpy as np` and matplotlib pyplot as plt).
- Avoid mutating arguments except in rare cases where this is the only clear way to implement an algorithm.

## Development Workflow
- Zero Unsolicited Edits & Scope Boundaries: You are strictly forbidden from editing code or comments unrelated to the specific task. If you see "bad" code in a different function, ignore it unless it causes a breaking error for the current task. Do not simplify logic, rename variables, or change structure unless explicitly asked to "Refactor" or the code is being heavily modified for the current task. Do not add or remove comments from unrelated parts of code (removing a "TODO" comment when addressing that todo is allowed). You may make any edits to fully achieve the goal requested and no further.
- When doing scratch work to check functionality, such as inspect data manually in python, if your scratch work amounts to more than a couple of lines, you should work in a fixed scratch file for each task. This is so I can give you permission once and you can do variations on the script without added permission. If your scratch work could be useful in the final output, consider placing it in an appropriate place in the working directory; however if it's purely gaining an intermediate understanding, then it's ok to stay in brain/.
- You should check your outputs if you are in any doubt. If you produce image output you must look at the images visually.

## Completion Requirements
- Verify any modifications you made - check that ALL modifications in the diff relate DIRECTLY to the task you are currently working on. Check there are no random other changes to unrelated or unmodified code.
- After modifying any Python files, you should immediately run black using the integrated terminal; you can typically apply to the entire cwd with `python -m black .` . Silent Execution: You do not need to ask for permission to run the black formatter; consider it part of the "Save" process.

## Restricted Actions
- Never present estimates or assumptions as facts, even implicitly. Explicitly label any unverified or guessed figure as estimated.
