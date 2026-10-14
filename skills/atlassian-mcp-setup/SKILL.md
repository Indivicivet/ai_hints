---
name: atlassian-mcp-setup
description: Set up, authenticate, or troubleshoot the Atlassian Remote MCP server. Use when configuring mcp_config.json for Jira, Confluence, or Bitbucket via Atlassian MCP.
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

3. **Workspace Slugs vs. UUIDs**:
   Bitbucket tools (`getBitbucketRepoPullRequest`, `listBitbucketRepoPullRequests`) will fail with `404 Not Found` if passed the raw Bitbucket workspace UUID (e.g. `{12345678-...}`). Always pass the human-readable workspace slug (e.g. `workspaceId: "<workspace-slug>"`). If unknown, retrieve it via `listBitbucketWorkspaces`.

## Authentication

Do not generate bespoke authentication scripts from scratch. Run the bundled script:

```powershell
python -u <skill_directory>/scripts/authenticate.py
```

This performs Dynamic Client Registration (DCR), sets up PKCE + PAR, starts a local callback listener on `http://localhost:8080/callback`, opens the browser authorization prompt, and updates `~/.gemini/config/mcp_config.json` with the Bearer token.
