# NotebookLM MCP Server Setup

## Installation

Installed via `uv tool install notebooklm-mcp` (version 2.0.11).

Executables available at:
- `/root/.local/bin/notebooklm-mcp`
- `/root/.local/bin/notebooklm-server`

## MCP Configuration

The MCP server is configured in `.mcp.json`:

```json
{
  "mcpServers": {
    "notebooklm": {
      "command": "/root/.local/bin/notebooklm-mcp",
      "args": []
    }
  }
}
```

## Authentication (Required — Manual Step)

The NotebookLM MCP server uses Chrome browser automation to authenticate with Google.

### Prerequisites
- **Sign out of all Google accounts in your browser before starting**
- Chrome or Chromium must be installed on your system

### Steps

1. Open a terminal and run the init command with your NotebookLM notebook URL:
   ```bash
   notebooklm-mcp init https://notebooklm.google.com/notebook/<your-notebook-id>
   ```

2. A Chrome browser window will open — log in to your Google account when prompted.

3. Once authenticated, a `chrome_profile_notebooklm/` directory will be created to store your session.

4. Test the connection:
   ```bash
   notebooklm-mcp test
   ```

### Headless/Remote Server Authentication

If you're on a headless server, authenticate on a local machine first, then export and import the profile:

```bash
# On local machine (after authenticating):
notebooklm-mcp export-profile --output my_profile.zip

# On the server:
notebooklm-mcp import-profile --input my_profile.zip
```

## Verifying Installation

Once authenticated, verify by starting the server:
```bash
notebooklm-mcp server
```

Or test connectivity:
```bash
notebooklm-mcp test
```

## MCP Server Usage with Claude Code

With `.mcp.json` configured, Claude Code will automatically load the `notebooklm` MCP server. You may be prompted to approve it on first use.

To enable it for the project, run:
```bash
claude mcp list
```
