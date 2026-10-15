---
name: atlassian-mcp-usage
description: Guide for querying and mutating Jira, Confluence, and Bitbucket using the Atlassian MCP tools (discover, executeRead, executeWrite). Use when fetching pull requests, PR comments, Jira issues, or Confluence pages.
---

# Atlassian MCP

Query and update Jira, Confluence, and Bitbucket using the Atlassian MCP tools.

## Architecture

The Atlassian MCP does not expose separate top-level tools per action. It routes through generic dispatchers:
- `discover`: Searches available API operations across products.
- `executeRead`: Runs read-only operations.
- `executeWrite` / `executeDestructive`: Runs mutations.

## Core Rules

1. **Bitbucket vs Jira/Confluence scoping**:
   - **Bitbucket**: Does NOT use `cloudId`. Pass all parameters in flat `inputs`:
     - `getPullRequest`: `{inputs: {workspace: "...", repo_slug: "...", pull_request_id: 123}}`
     - `getPullRequestComments`: `{inputs: {workspace: "...", repo_slug: "...", pull_request_id: 123}}`
   - **Jira / Confluence**: STRICTLY requires `cloudId`. Call `getAccessibleAtlassianResources` once to obtain the site UUID or pass site URL.

2. **Discover before guessing**:
   - Never invent operation names. If unsure of the exact operation or its parameter names, call `discover` with a query or product filter (e.g. `query="pull request comments"`).
2. **Workspace Slugs vs. UUIDs**:
   Always pass the human-readable workspace slug (e.g. `workspaceId: "idhteam"`). Passing raw workspace UUIDs (`{1234-...}`) often results in `404 Not Found`.


3. **Re-fetching vs transcript scraping**:
   - If you need verbatim PR comment text, re-call `executeRead` with `getPullRequestComments` rather than parsing internal `transcript.jsonl`.
   - If inspecting saved JSON/logs from disk, write a standalone scratch script in `brain/<conversation-id>/scratch/` with explicit `encoding="utf-8"`. Never run nested JSON parsing inside PowerShell `python -c` one-liners.
## Handling Expired Tokens (401 Unauthorized)

If an MCP call returns `401 {"error": "invalid_token"}`:
1. Run the authenticator from `atlassian-mcp-setup`:
   ```powershell
   python -u c:\personal_repos\ai_hints\skills\atlassian-mcp-setup\scripts\authenticate.py
   ```
2. **Immediately share the authorization URL in chat** as a clickable link so the user can authorize the request.
3. Once the task finishes and writes the refreshed token to `mcp_config.json`, resume the original query.
