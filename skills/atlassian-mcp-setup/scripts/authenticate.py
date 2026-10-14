"""Atlassian Remote MCP OAuth 2.1 Authenticator.

Performs Dynamic Client Registration (DCR), PKCE + PAR authorization flow,
starts a local callback listener on localhost:8080, and generates / writes the
resulting MCP configuration with the ?tools=all URL.
"""

from pathlib import Path
import argparse
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
DEFAULT_CONFIG_PATH = Path.home() / ".gemini" / "config" / "mcp_config.json"
REDIRECT_URI = "http://localhost:8080/callback"


def get_oauth_metadata() -> dict:
    meta_url = "https://mcp.atlassian.com/.well-known/oauth-protected-resource/v2/mcp"
    req = urllib.request.Request(meta_url)
    return json.loads(urllib.request.urlopen(req).read().decode())


def register_client(auth_server_url: str, client_name: str) -> str:
    reg_url = f"{auth_server_url}/dcr/register"
    body = json.dumps(
        {
            "client_name": client_name,
            "redirect_uris": [REDIRECT_URI],
        }
    ).encode()
    req = urllib.request.Request(
        reg_url, data=body, headers={"Content-Type": "application/json"}
    )
    client_data = json.loads(urllib.request.urlopen(req).read().decode())
    return client_data["client_id"]


def update_mcp_config(config_path: Path, access_token: str) -> dict:
    config = {}
    if config_path.exists():
        try:
            with open(config_path, "r") as f_in:
                config = json.load(f_in)
        except Exception:
            config = {}

    mcp_servers = config.setdefault("mcpServers", {})
    mcp_servers["atlassian"] = {
        "url": MCP_URL,
        "headers": {
            "Authorization": f"Bearer {access_token}",
            "Accept": "application/json, text/event-stream",
        },
    }

    config_path.parent.mkdir(parents=True, exist_ok=True)
    with open(config_path, "w") as f_conf:
        json.dump(config, f_conf, indent=2)
    return config


def authenticate(
    config_path: Path | None = DEFAULT_CONFIG_PATH,
    client_name: str = "MCP Client",
    no_save: bool = False,
) -> None:
    meta = get_oauth_metadata()
    auth_server = meta["authorization_servers"][0]
    client_id = register_client(auth_server, client_name)

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

    auth_completed = False

    class CallbackHandler(http.server.BaseHTTPRequestHandler):
        def do_GET(self):
            nonlocal auth_completed
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

                config_snippet = {
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

                if not no_save and config_path:
                    update_mcp_config(config_path, access_token)
                    print(
                        f"Authentication successful! Token saved to {config_path}",
                        flush=True,
                    )
                else:
                    print("Authentication successful! Configuration snippet:")
                    print(json.dumps(config_snippet, indent=2), flush=True)

                self.send_response(200)
                self.send_header("Content-Type", "text/html")
                self.end_headers()
                self.wfile.write(
                    b"<h1>Authentication successful!</h1>"
                    b"<p>You can close this tab and return to your application.</p>"
                )
                auth_completed = True
            except Exception as e:
                self.send_response(500)
                self.end_headers()
                self.wfile.write(f"Token exchange error: {e}".encode())
                print(f"Token exchange error: {e}", flush=True)

    server = http.server.HTTPServer(("localhost", 8080), CallbackHandler)
    print(f"Opening browser for sign-in: {auth_url}", flush=True)
    webbrowser.open(auth_url)
    print("Listening on http://localhost:8080/callback ...", flush=True)
    while not auth_completed:
        server.handle_request()


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Authenticate with Atlassian Remote MCP server."
    )
    parser.add_argument(
        "--config",
        type=Path,
        default=DEFAULT_CONFIG_PATH,
        help=f"Path to MCP config file (defaults to e.g. Gemini/Antigravity path: {DEFAULT_CONFIG_PATH})",
    )
    parser.add_argument(
        "--client-name",
        type=str,
        default="MCP Client",
        help="Client display name to use during Dynamic Client Registration (default: 'MCP Client')",
    )
    parser.add_argument(
        "--no-save",
        action="store_true",
        help="Do not write to file; print configuration snippet to stdout instead.",
    )
    args = parser.parse_args()
    authenticate(
        config_path=args.config, client_name=args.client_name, no_save=args.no_save
    )


if __name__ == "__main__":
    main()
