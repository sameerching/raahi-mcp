# Raahi MCP (Phase 1)

Raahi is a **read-only** Indian travel MCP server prototype.

> This project is not an official IRCTC or Indian Railways app.

## Scope in this phase

- Read-only station lookup via MCP tool `lookup_station`
- Mock data provider only
- No booking, cancellation, payment, login automation, scraping, or captcha/OTP bypass

## Setup for development and tests (without MCP runtime)

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

## Setup for MCP server runtime

Install with server extras when you want to run the MCP transport:

```bash
pip install -e ".[dev,server]"
```

## Run the MCP server

```bash
python -m raahi_mcp.server
```

Default local endpoint (Streamable HTTP):

- `http://localhost:8000/mcp`

## Test with MCP Inspector

In another shell while server is running:

```bash
npx @modelcontextprotocol/inspector
```

Connect to:

- Transport: Streamable HTTP
- URL: `http://localhost:8000/mcp`

## Expose with ngrok

```bash
ngrok http 8000
```

Then use the generated HTTPS forwarding URL with `/mcp` appended.

## Later: connect to ChatGPT Developer Mode

When ready, configure your MCP connector in ChatGPT Developer Mode with your ngrok HTTPS URL ending in `/mcp`.

## Environment

Copy `.env.example` to `.env` and edit as needed.
