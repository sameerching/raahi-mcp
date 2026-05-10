"""Pure station lookup logic (no MCP imports)."""

from __future__ import annotations

from raahi_mcp.mock_data import MOCK_STATIONS


def _normalize(value: str) -> str:
    return value.strip().casefold()


def lookup_station_data(query: str) -> dict[str, object]:
    """Look up station matches from mock data.

    Returns a dictionary with the original query and list of matched stations.
    """
    normalized_query = _normalize(query)

    if not normalized_query:
        return {"query": query, "matches": []}

    matches: list[dict[str, object]] = []
    for station in MOCK_STATIONS:
        search_fields = [
            station.code,
            station.name,
            station.city,
            station.state,
            *station.aliases,
        ]
        if any(_normalize(field) == normalized_query for field in search_fields):
            matches.append(station.to_dict())

    return {"query": query, "matches": matches}
