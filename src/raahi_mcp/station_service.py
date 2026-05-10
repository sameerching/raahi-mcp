from raahi_mcp.config import settings
from raahi_mcp.domain import LookupMetadata, LookupResponse, Station
from raahi_mcp.mock_data import STATIONS


def _matches(station: Station, query: str) -> bool:
    normalized_query = query.strip().lower()

    if not normalized_query:
        return False

    searchable_fields = [
        station.stationCode,
        station.stationName,
        station.city,
        station.state,
        *station.aliases,
    ]

    return any(normalized_query in field.lower() for field in searchable_fields)


def lookup_station_data(query: str) -> dict:
    """Read-only lookup for Indian railway stations from mock data."""
    matches = [station for station in STATIONS if _matches(station, query)]

    response = LookupResponse(
        query=query,
        stations=matches,
        metadata=LookupMetadata(provider=settings.provider, mock=True, app="Raahi"),
    )

    return response.model_dump()
