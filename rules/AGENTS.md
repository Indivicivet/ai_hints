# Agent Rules

## Restricted Actions
- Never present estimates or assumptions as facts, even implicitly. Explicitly label any unverified or guessed figure as estimated. If you expect a user wants you to search the internet or consult a direct source for a result but you can't find one, do NOT report your best guess as if it were a search result, instead label it CLEARLY as your imagination.

## Coding Standards
- Formatter: For python, follow 'Black' formatting rules (88 chars per line, double quotes, trailing commas). For C++ use a similar style.
- Add comments with detailed explanation or "gotcha" notes where necessary. You do not generally need to add "self-explanatory" comments. Comments MUST NOT be included if they simply declare what a variable is in a way that could be otherwise made clear by a better choice of variable name.
- Typing: Only use type hints when adding or modifying function signatures if this helps to clarify the types involved; don't bother with them if the types are highly variable (e.g. any arithmetic types). Don't bother with them if the code is already clear. Do not add types to existing code unless requested.
- Avoid single use variables. Inline variables where possible, unless declaring them as a separate variable is used for debugging, or it makes it significantly clearer what something is for.
- Never create redundant aliases for variables. If you are tempted to create aliases for "backwards compatibility", instead update all usages of the functionality to represent the new API; if it's a public interface, inform the user.
- Exception handling in Python: You must avoid overly general try-except with a bare Exception as much as possible. Only use when necessary, and scope a try-except block as narrowly as you can. You can use a high level try-except to catch errors from internal code in a GUI and report the error within the GUI. You may use try-except for control flow. You may use a high level try-finally to deal with closing hardware, connections, etc.
- Imports: Use absolute imports. Do not reorganize existing imports unless a new one is required. If modifying existing imports, use the `sort-out-imports` skill.
- Do not mutate function arguments.
-- There may be exceptions: perfomance, mutation being needed to implement an algorithm sensibly, writing C/CUDA etc.
-- Avoid non-constant variables for similar reasons; it is ok for a scope to have one or two non-constant variables, or those that are only modified in a local segment. Use of mutation must be justifiable.
-- Overriding input values that default to None with conditional alternative values is fine.

## Development Workflow
- Avoid unsolicited edits: You are forbidden from editing code unrelated to the specific task. If you see "bad" code in a different function, ignore it unless it causes a breaking error for the current task. Do not add or remove comments from unrelated parts of code (removing a "TODO" comment when addressing that todo is allowed). You may make any edits to fully achieve the goal requested and no further.
- When doing scratch work to check functionality, such as inspect data manually in python, if your scratch work amounts to more than a couple of lines, you should work in a sensible scratch file: if your scratch work could be useful in the final output, consider placing it in an appropriate place in the working directory. If it's purely gaining an intermediate understanding, then it's ok to stay in brain/.
- You should check your outputs if you are in any doubt. If you produce image output you must look at the images visually. Whenever you use your file view tool, you should be critical and meticulous in how you interpret it.

## Completion Requirements
- Verify any modifications you made - check that all modifications in the diff relate directly to the task you are currently working on. Check there are no random other changes to unrelated code.
- After modifying any Python files, you should immediately run black using the integrated terminal; you can typically apply to the entire cwd with `python -m black .` . You do not need to ask for permission to run the black formatter.
- After modifying C++ files, use the `clang-format-black` skill. You do not need to ask for permission to use this skill.
