# Raahi MCP

Raahi is a read-only Indian travel MCP server prototype.

This project is not an official IRCTC or Indian Railways app.

## Phase 1 scope

This phase supports only one read-only tool:

- `lookup_station`: Look up station codes by station code, station name, city, state, or alias.

## Safety boundary

Raahi does not:

- book train tickets
- cancel tickets
- perform payments
- automate IRCTC login
- scrape IRCTC pages
- bypass captchas or OTPs
- provide Tatkal automation
- store IRCTC credentials

## Setup for tests

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
pytest
ruff check .
