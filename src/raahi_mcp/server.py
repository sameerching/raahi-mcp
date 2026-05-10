from mcp.server.fastmcp import FastMCP

from raahi_mcp.config import settings
from raahi_mcp.station_service import lookup_station_data

LOOKUP_DESCRIPTION = (
    "Look up Indian railway station codes by station code, station name, city, state, "
    "or alias. This is read-only and does not book tickets."
)

mcp = FastMCP(name="Raahi")


@mcp.tool(description=LOOKUP_DESCRIPTION)
def lookup_station(query: str) -> dict:
    """Read-only MCP tool that delegates to pure station lookup logic."""
    return lookup_station_data(query)


if __name__ == "__main__":
    mcp.run(
        transport="streamable-http",
        host="127.0.0.1",
        port=settings.port,
        path="/mcp",
    )
