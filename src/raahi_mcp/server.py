from mcp.server.fastmcp import FastMCP

from raahi_mcp.config import settings
from raahi_mcp.domain import LookupMetadata, LookupResponse, Station
from raahi_mcp.mock_data import STATIONS

LOOKUP_DESCRIPTION = (
    "Look up Indian railway station codes by station code, station name, city, state, "
    "or alias. This is read-only and does not book tickets."
)

mcp = FastMCP(name="Raahi")


def _matches(station: Station, query: str) -> bool:
    q = query.strip().lower()
    fields = [
        station.stationCode,
        station.stationName,
        station.city,
        station.state,
        *station.aliases,
    ]
    return any(q in field.lower() for field in fields)


@mcp.tool(description=LOOKUP_DESCRIPTION)
def lookup_station(query: str) -> dict:
    matches = [station for station in STATIONS if _matches(station, query)]
    response = LookupResponse(
        query=query,
        stations=matches,
        metadata=LookupMetadata(provider=settings.provider, mock=True, app="Raahi"),
    )
    return response.model_dump()


if __name__ == "__main__":
    mcp.run(transport="streamable-http", host="127.0.0.1", port=settings.port, path="/mcp")
