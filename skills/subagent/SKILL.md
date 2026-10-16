---
name: subagent
description: Invoke a subagent using "flash" or "flash-lite". Use this ALWAYS when spawning a subagent in Antigravity.
---

# Subagent

When you invoke a subagent in Antigravity, you must pass "Model": "flash" or "Model": "flash_lite" to the invoke_subagent tool. Only make exceptions if specifically requested by the user.

## Rules

1. If the user EXPLICITLY specified a model to use, such as "spawn subagents using pro model", you may use this.
2. Otherwise, decide whether this is an "easier" or "harder" task, and pass "Model": "flash_lite" or "Model": "flash" to the invoke_subagent tool as appropriate.
3. If you believe a task requires a pro model, check with the user for explicit confirmation.
4. NEVER pass "Model": "inherit" or leave the model field blank.
