---
name: assume-installed
description: Use when tempted to check if a Windows command is available, a package is installed, verify Python dependencies, run `python -c import`, or before running code that uses third-party libraries.
---

# Assume software and packages are installed

Assume every required library is already present in the environment. Do not spend tool calls or execution steps checking whether packages exist before using them.

python? Installed. numpy? Installed. PIL? Installed. cupy? Installed. Whatever you are reaching for? Probably installed.

## Why

Pre-flight import checks (`python -c "import ..."`), `pip list` queries, and test scripts waste tool calls and pollute the context window. The Python runtime is already the fastest package checker.

## How to check if packages are installed

1. **Write the code.** Import the libraries you need directly.
2. **Run the code.** Execute the script or command immediately.
3. **Let the runtime check for you.** If the script runs, every package was installed.

## Handling import errors

Only inspect or install a package after encountering an explicit failure.

1. **Verify the error.** Check the traceback. Confirm it is an actual `ModuleNotFoundError` or `ImportError`, not a typo in your import statement or a broken relative path.
2. **Install the package.** Install only the specific missing package using the project environment manager (for example, `uv pip install <pkg>` or `pip install <pkg>`).
3. **Re-run the command.** Continue with your original task.

## Anti-patterns

- Running `python -c "import <pkg>"` before executing your actual script.
- Running `pip list` or `conda list` to explore available libraries.
- Asking the user whether a common dependency is installed before writing code.
- Creating one-off scratch files just to test if a module imports.
