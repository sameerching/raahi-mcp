"""Pure station lookup business logic for Raahi."""

from raahi_mcp.config import settings
from raahi_mcp.domain import LookupMetadata, LookupResponse, Station
from raahi_mcp.mock_data import STATIONS


def _matches(station: Station, query: str) -> bool:
    normalized = query.strip().lower()
    fields = [
        station.stationCode,
        station.stationName,
        station.city,
        station.state,
        *station.aliases,
    ]
    return any(normalized in field.lower() for field in fields)


def lookup_station_data(query: str) -> dict:
    """Read-only lookup for Indian railway station data backed by mock records."""
    matches = [station for station in STATIONS if _matches(station, query)]
    response = LookupResponse(
        query=query,
        stations=matches,
        metadata=LookupMetadata(provider=settings.provider, mock=True, app="Raahi"),
    )
    return response.model_dump()
