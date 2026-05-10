# Raahi MCP (Phase 1)

Raahi is a minimal, read-only Python MCP server that provides one tool: `lookup_station`.

## Scope (Phase 1)

This project is intentionally limited to station lookup only.

### Included
- Read-only station lookup by code, station name, city, state, or alias.
- Mock in-memory data source.
- MCP server tool: `lookup_station`.

### Explicitly excluded
- Booking
- Cancellation
- Payment
- IRCTC login automation
- Scraping
- Captcha/OTP bypass
- Tatkal automation

This project is **not** an official IRCTC or Indian Railways product.

## Package

- Product name: **Raahi**
- Python package: **`raahi_mcp`**

## Install

### Development (without MCP runtime)
```bash
pip install -e ".[dev]"
```

### With MCP server runtime
```bash
pip install -e ".[dev,server]"
```

## Run server

```bash
python -m raahi_mcp.server
```

Default MCP endpoint:
- `http://localhost:8000/mcp`

The server uses streamable HTTP transport when available in the installed MCP package.

## Tool

### `lookup_station`
Look up Indian railway station codes by station code, station name, city, state, or alias. This is read-only and does not book tickets.

Input:
- `query: str`

Output shape:
- `{"query": "...", "matches": [ ... ]}`
