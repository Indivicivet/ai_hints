---
name: atlassian-mcp-usage
description: Query and mutate Jira, Confluence, and Bitbucket using the Atlassian MCP tools. Use when fetching pull requests, diffs, comments, Jira issues, or Confluence pages.
---

# Atlassian MCP usage

Guidelines for querying Jira, Confluence, and Bitbucket using the Atlassian Remote MCP server.

## Tool modes

The tools available depend on the server URL configured in `mcp_config.json`:

1. **Flat tools (`?tools=all`, expected)**:
   This is the standard setup. It bypasses dispatchers and exposes distinct tools directly:
   - Bitbucket: `getBitbucketRepoPullRequest`, `getBitbucketRepoPullRequestDiff`, `listBitbucketRepoPullRequests`, `listBitbucketRepoPullRequestComments`, `listBitbucketRepositories`, `getBitbucketRepoFileContent`, etc.
   - Jira / Confluence: `jiraSearch`, `getJiraIssue`, `getConfluencePage`, etc.
   - `discover` and `executeRead` do not exist in this mode.

2. **Dispatcher mode (bare URL without `?tools=all`)**:
   Exposes only six meta-tools (`discover`, `executeRead`, `executeWrite`, `executeDestructive`, `getAccessibleAtlassianResources`, `atlassianUserInfo`). `discover` often returns empty results for Bitbucket, making it unsuitable for Bitbucket work. Update the URL to `?tools=all` instead of fighting it.

## Bitbucket parameter rules

1. **Parameter names (`repoId`, `prId`, `workspaceId`)**:
   Bitbucket tools do not accept standard REST names:
   - Use `repoId` (e.g. `"research_repo"` or UUID), not `repoSlug` or `repository`.
   - Use `prId` (e.g. `78`), not `pullRequestId` or `pull_request_id`.
   - Use `workspaceId` (e.g. `"idhteam"`), not `workspace`.

2. **Workspace slug over UUID**:
   Pass the workspace slug (e.g. `workspaceId: "idhteam"`). Raw workspace UUIDs (`{1234-...}`) often return `404 Not Found`.

3. **Diffs and comments**:
   - `getBitbucketRepoPullRequest`: PR metadata, title, author, branch, and status.
   - `getBitbucketRepoPullRequestDiff`: Full unified git diff.
   - `listBitbucketRepoPullRequestComments`: Review threads and discussion.

## Direct HTTP calls

When making direct JSON-RPC calls over HTTP/SSE instead of client native tool dispatch:
1. **Initialize first**: Send an `initialize` JSON-RPC handshake before calling any tools:
   ```json
   {"jsonrpc": "2.0", "id": 1, "method": "initialize", "params": {"protocolVersion": "2024-11-05", "capabilities": {}, "clientInfo": {"name": "client", "version": "1.0"}}}
   ```
2. **Forward session ID**: Extract `Mcp-Session-Id` from the `initialize` response headers and pass `'Mcp-Session-Id': '<session_id>'` on every subsequent `tools/call`. Omitting this returns error `-32600`.

## Handling expired tokens (401 Unauthorized)

When an MCP call fails with `401 {"error": "invalid_token"}`:
1. Run `python -u c:\personal_repos\ai_hints\skills\atlassian-mcp-setup\scripts\authenticate.py`.
2. Print the output authorization URL in chat immediately as a clickable link.
3. Resume the query once the task finishes and writes the fresh token to `mcp_config.json`.
