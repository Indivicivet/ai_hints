---
name: atlassian-mcp-usage
description: Guide for querying and mutating Jira, Confluence, and Bitbucket using the Atlassian MCP tools. Use when fetching pull requests, PR diffs, comments, Jira issues, or Confluence pages.
---

# Atlassian MCP Usage

Guide for querying and interacting with Jira, Confluence, and Bitbucket using the Atlassian Remote MCP server.

## Tool Architecture (Two Modes)

The available tools depend on your server URL in `mcp_config.json`:

1. **Flat Tools (`?tools=all`, Recommended)**:
   Disables dispatchers and exposes individual tools directly:
   - **Bitbucket**: `getBitbucketRepoPullRequest`, `getBitbucketRepoPullRequestDiff`, `listBitbucketRepoPullRequests`, `listBitbucketRepoPullRequestComments`, `listBitbucketRepositories`, `getBitbucketRepoFileContent`, etc.
   - **Jira / Confluence**: `jiraSearch`, `getJiraIssue`, `getConfluencePage`, etc.
   - *Note*: `discover` and `executeRead` do NOT exist in this mode.

2. **Dispatcher Mode (Default URL without `?tools=all`)**:
   Exposes only 6 meta-tools (`discover`, `executeRead`, `executeWrite`, `executeDestructive`, `getAccessibleAtlassianResources`, `atlassianUserInfo`).
   - Use `discover` to find operations.
   - Call operations via `executeRead` or `executeWrite`.
   - *Gotcha*: `discover` often returns empty results for Bitbucket; use `?tools=all` instead.

## Bitbucket Tool Calling Rules & Parameter Gotchas

1. **Parameter Names (`repoId`, `prId`, `workspaceId`)**:
   Bitbucket tools strictly enforce specific parameter names. Do NOT use standard REST names:
   - Use `repoId` (e.g. `"research_repo"` or UUID) — **NOT** `repoSlug` or `repository`.
   - Use `prId` (e.g. `78`) — **NOT** `pullRequestId` or `pull_request_id`.
   - Use `workspaceId` (e.g. `"idhteam"`) — **NOT** `workspace`.

2. **Workspace Slugs vs. UUIDs**:
   Always pass the human-readable workspace slug (e.g. `workspaceId: "idhteam"`). Passing raw workspace UUIDs (`{1234-...}`) often results in `404 Not Found`.

3. **Fetching Large Diffs / Details**:
   - For pull request metadata: call `getBitbucketRepoPullRequest`.
   - For pull request diffs: call `getBitbucketRepoPullRequestDiff` (returns the full unified git diff).
   - For review discussions: call `listBitbucketRepoPullRequestComments`.

## Direct HTTP / SSE Protocol Requirements

When calling the Atlassian MCP endpoint directly via HTTP/Python (e.g. in environments without eager native tool registration):
1. **Initialize First**: The server requires a JSON-RPC `initialize` handshake before any tool calls:
   ```json
   {"jsonrpc": "2.0", "id": 1, "method": "initialize", "params": {"protocolVersion": "2024-11-05", "capabilities": {}, "clientInfo": {"name": "client", "version": "1.0"}}}
   ```
2. **Session Header**: Capture the `Mcp-Session-Id` header from the `initialize` response, and attach `'Mcp-Session-Id': '<session_id>'` to all subsequent `tools/call` requests. Without this header, requests fail with error code `-32600`.

## Handling Expired Tokens (401 Unauthorized)

If an MCP call returns `401 {"error": "invalid_token"}`:
1. Run the authenticator from `atlassian-mcp-setup`:
   ```powershell
   python -u c:\personal_repos\ai_hints\skills\atlassian-mcp-setup\scripts\authenticate.py
   ```
2. **Immediately share the authorization URL in chat** as a clickable link so the user can authorize the request.
3. Once the task finishes and writes the refreshed token to `mcp_config.json`, resume the original query.
