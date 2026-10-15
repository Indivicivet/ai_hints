---
name: atlassian-mcp-setup
description: Set up, authenticate, or troubleshoot the Atlassian Remote MCP server. Use when configuring mcp_config.json for Jira, Confluence, or Bitbucket.
---

# Atlassian MCP setup

Configuring and authenticating the Atlassian Remote MCP server (`https://mcp.atlassian.com/v2/mcp`).

## Required configuration

1. **Append `?tools=all` to the URL**:
   The default URL hides Bitbucket and uses a discovery catalog that returns empty results. You must configure the URL with `?tools=all`:
   ```text
   https://mcp.atlassian.com/v2/mcp?tools=all
   ```
   This exposes all 34 tools directly.

2. **Required headers**:
   The server returns `406 Not Acceptable` without SSE streaming headers. `mcp_config.json` must include:
   ```json
   "headers": {
     "Authorization": "Bearer <ACCESS_TOKEN>",
     "Accept": "application/json, text/event-stream"
   }
   ```

## Authentication

Run the bundled script to generate tokens via OAuth PKCE:

```powershell
python -u <skill_directory>/scripts/authenticate.py
```

Arguments:
- `--config <path>`: MCP config file to write (defaults to `~/.gemini/config/mcp_config.json`).
- `--client-name <name>`: Client display name for DCR (default: `MCP Client`).
- `--no-save`: Print configuration to stdout without editing files.

When running `authenticate.py`, check the output immediately and print the authorization URL (`https://auth.atlassian.com/authorize?...`) into chat as a clickable link. Do not rely on `webbrowser.open()` to focus a browser window.
