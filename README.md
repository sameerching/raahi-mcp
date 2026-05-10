# Raahi MCP (Phase 1)

Raahi is a **read-only** Indian travel MCP server prototype.

> This project is not an official IRCTC or Indian Railways app.

## Phase 1 scope

- A single read-only MCP tool: `lookup_station`
- Mock station data provider only
- No booking, cancellation, payments, login automation, scraping, or captcha/OTP bypass

## Install for tests and lint

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
```

## Run tests

```bash
pytest
```

## Run lint

```bash
ruff check .
```

## Install for MCP server runtime

```bash
pip install -e ".[dev,server]"
```

## Run the MCP server

```bash
python -m raahi_mcp.server
```

Default endpoint:

- `http://localhost:8000/mcp`

## Test with MCP Inspector

```bash
npx @modelcontextprotocol/inspector
```

Use:

- Transport: Streamable HTTP
- URL: `http://localhost:8000/mcp`

## Expose with ngrok

```bash
ngrok http 8000
```

Append `/mcp` to the ngrok HTTPS URL when configuring MCP clients.

## Later connection to ChatGPT Developer Mode

Use your HTTPS MCP URL (ending in `/mcp`) in ChatGPT Developer Mode.
