"""Atlassian Remote MCP OAuth 2.1 Authenticator.

Performs Dynamic Client Registration (DCR), PKCE + PAR authorization flow,
starts a local callback listener on localhost:8080, and writes the resulting
access token to ~/.gemini/config/mcp_config.json with the ?tools=all URL.
"""

from pathlib import Path
import base64
import hashlib
import http.server
import json
import secrets
import sys
import urllib.parse
import urllib.request
import webbrowser

MCP_URL = "https://mcp.atlassian.com/v2/mcp?tools=all"
CONFIG_PATH = Path.home() / ".gemini" / "config" / "mcp_config.json"
REDIRECT_URI = "http://localhost:8080/callback"


def get_oauth_metadata() -> dict:
    meta_url = "https://mcp.atlassian.com/.well-known/oauth-protected-resource/v2/mcp"
    req = urllib.request.Request(meta_url)
    return json.loads(urllib.request.urlopen(req).read().decode())


def register_client(auth_server_url: str) -> str:
    reg_url = f"{auth_server_url}/dcr/register"
    body = json.dumps(
        {
            "client_name": "Antigravity MCP Client",
            "redirect_uris": [REDIRECT_URI],
        }
    ).encode()
    req = urllib.request.Request(
        reg_url, data=body, headers={"Content-Type": "application/json"}
    )
    client_data = json.loads(urllib.request.urlopen(req).read().decode())
    return client_data["client_id"]


def authenticate() -> None:
    meta = get_oauth_metadata()
    auth_server = meta["authorization_servers"][0]
    client_id = register_client(auth_server)

    code_verifier = secrets.token_urlsafe(64)
    code_challenge = (
        base64.urlsafe_b64encode(hashlib.sha256(code_verifier.encode("ascii")).digest())
        .decode("ascii")
        .rstrip("=")
    )
    state = secrets.token_urlsafe(16)
    scopes = " ".join(meta.get("scopes_supported", ["read:me", "offline_access"]))

    par_body = urllib.parse.urlencode(
        {
            "client_id": client_id,
            "response_type": "code",
            "redirect_uri": REDIRECT_URI,
            "scope": scopes,
            "code_challenge": code_challenge,
            "code_challenge_method": "S256",
            "state": state,
        }
    ).encode()

    par_req = urllib.request.Request(
        "https://auth.atlassian.com/oauth/par",
        data=par_body,
        headers={"Content-Type": "application/x-www-form-urlencoded"},
    )
    par_res = json.loads(urllib.request.urlopen(par_req).read().decode())
    request_uri = par_res["request_uri"]

    auth_url = (
        f"https://auth.atlassian.com/authorize"
        f"?client_id={client_id}&request_uri={urllib.parse.quote(request_uri)}"
    )

    class CallbackHandler(http.server.BaseHTTPRequestHandler):
        def do_GET(self):
            parsed = urllib.parse.urlparse(self.path)
            params = urllib.parse.parse_qs(parsed.query)

            if "code" not in params:
                self.send_response(400)
                self.end_headers()
                self.wfile.write(b"Error: Missing code parameter")
                return

            code = params["code"][0]
            returned_state = params.get("state", [""])[0]

            if returned_state != state:
                self.send_response(400)
                self.end_headers()
                self.wfile.write(b"Error: State mismatch")
                return

            token_data = urllib.parse.urlencode(
                {
                    "grant_type": "authorization_code",
                    "client_id": client_id,
                    "code": code,
                    "redirect_uri": REDIRECT_URI,
                    "code_verifier": code_verifier,
                }
            ).encode()

            token_req = urllib.request.Request(
                "https://auth.atlassian.com/oauth/token",
                data=token_data,
                headers={"Content-Type": "application/x-www-form-urlencoded"},
            )

            try:
                token_res = json.loads(
                    urllib.request.urlopen(token_req).read().decode()
                )
                access_token = token_res["access_token"]

                config = {
                    "mcpServers": {
                        "atlassian": {
                            "url": MCP_URL,
                            "headers": {
                                "Authorization": f"Bearer {access_token}",
                                "Accept": "application/json, text/event-stream",
                            },
                        }
                    }
                }
                CONFIG_PATH.parent.mkdir(parents=True, exist_ok=True)
                with open(CONFIG_PATH, "w") as f_conf:
                    json.dump(config, f_conf, indent=2)

                self.send_response(200)
                self.send_header("Content-Type", "text/html")
                self.end_headers()
                self.wfile.write(
                    b"<h1>Authentication successful!</h1>"
                    b"<p>You can close this tab and return to the chat.</p>"
                )
                print("Authentication successful! Token saved to config.", flush=True)
            except Exception as e:
                self.send_response(500)
                self.end_headers()
                self.wfile.write(f"Token exchange error: {e}".encode())
                print(f"Token exchange error: {e}", flush=True)

    server = http.server.HTTPServer(("localhost", 8080), CallbackHandler)
    print(f"Opening browser for sign-in: {auth_url}", flush=True)
    webbrowser.open(auth_url)
    print("Listening on http://localhost:8080/callback ...", flush=True)
    while True:
        server.handle_request()
        if CONFIG_PATH.exists() and "Bearer" in CONFIG_PATH.read_text():
            break


if __name__ == "__main__":
    authenticate()
    