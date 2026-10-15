---
name: atlassian-mcp-setup
description: Set up, authenticate, or troubleshoot the Atlassian Remote MCP server. Use when configuring mcp_config.json (e.g. for Gemini, Claude, or other MCP clients) for Jira, Confluence, or Bitbucket.
---

# Atlassian MCP Setup

Instructions and constraints for configuring and authenticating the Atlassian Remote MCP server (`https://mcp.atlassian.com/v2/mcp`).

## Critical Gotchas & Overrides

1. **Always append `?tools=all` to the URL**:
   The default server URL (`https://mcp.atlassian.com/v2/mcp`) hides Bitbucket tools and relies on a dynamic discovery catalog that returns empty results for Bitbucket. You MUST configure the URL as:
   ```text
   https://mcp.atlassian.com/v2/mcp?tools=all
   ```
   This exposes all 50+ available tools (Jira, Confluence, and Bitbucket pull requests, branches, and diffs) as flat, callable tools.

2. **Required HTTP Headers**:
   The server rejects requests that do not accept SSE streaming with `406 Not Acceptable`. Headers in `mcp_config.json` must include:
   ```json
   "headers": {
     "Authorization": "Bearer <ACCESS_TOKEN>",
     "Accept": "application/json, text/event-stream"
   }
   ```

## Authentication

Do not generate bespoke authentication scripts from scratch. Run the bundled script:

```powershell
python -u <skill_directory>/scripts/authenticate.py
```

Optional arguments:
- `--config <path>`: Custom path to save the MCP configuration file (defaults to `~/.gemini/config/mcp_config.json`, e.g. for Gemini CLI / Antigravity).
- `--client-name <name>`: Custom client display name for OAuth registration (default: `MCP Client`).
- `--no-save`: Prints the configuration JSON to stdout without modifying any file.

The script performs Dynamic Client Registration (DCR), sets up PKCE + PAR, starts a local callback listener on `http://localhost:8080/callback`, opens the browser authorization prompt, and updates the target MCP configuration with the Bearer token.

> [!IMPORTANT]
> **Always link the Auth URL in chat**:
> When running `authenticate.py`, immediately check the task output / log and print the full authorization URL (`https://auth.atlassian.com/authorize?...`) in chat as a clickable markdown link. Never rely solely on automated browser opening (`webbrowser.open`), as it often fails to focus or run in background/remote environments.
