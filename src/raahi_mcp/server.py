"""MCP server entrypoint for Raahi."""

from __future__ import annotations

from raahi_mcp.config import load_config
from raahi_mcp.station_service import lookup_station_data


TOOL_DESCRIPTION = (
    "Look up Indian railway station codes by station code, station name, city, "
    "state, or alias. This is read-only and does not book tickets."
)


def build_server():
    """Create and configure the MCP server.

    This function imports MCP lazily so tests can run without MCP installed.
    """
    from mcp.server.fastmcp import FastMCP

    server = FastMCP(name="Raahi")

    @server.tool(name="lookup_station", description=TOOL_DESCRIPTION)
    def lookup_station(query: str) -> dict[str, object]:
        return lookup_station_data(query)

    return server


def main() -> None:
    config = load_config()
    server = build_server()

    # Prefer streamable HTTP transport on /mcp.
    server.run(
        transport="streamable-http",
        host=config.host,
        port=config.port,
        path=config.mcp_path,
    )


if __name__ == "__main__":
    main()
