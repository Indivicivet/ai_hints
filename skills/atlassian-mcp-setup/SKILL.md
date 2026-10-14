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

## Authentication Workflow (OAuth 2.1)

Atlassian MCP requires OAuth 2.1 via Dynamic Client Registration (DCR), PKCE, and Pushed Authorization Requests (PAR).

When running or generating an authentication script:
1. **Dynamic Client Registration (DCR)**:
   Discover the authorization server from `https://mcp.atlassian.com/.well-known/oauth-protected-resource/v2/mcp` and register a client at `<auth_server>/dcr/register` with redirect URI `http://localhost:8080/callback`.
2. **Pushed Authorization Request (PAR)**:
   Submit authorization parameters (including PKCE `code_challenge`, `S256`, and requested scopes) via `POST` as `application/x-www-form-urlencoded` to `https://auth.atlassian.com/oauth/par`.
3. **Execution & Flushing**:
   Always launch the callback receiver with unbuffered output (`python -u`) to ensure URLs print immediately to logs. Loop the server (`while True: server.handle_request()`) until the token is written to disk, rather than relying on a brittle single-call handler.
4. **Target config path**:
   Write the resulting access token directly to `~/.gemini/config/mcp_config.json`.
