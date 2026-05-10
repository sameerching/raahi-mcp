"""Configuration helpers for Raahi MCP server."""

from __future__ import annotations

import os
from dataclasses import dataclass


@dataclass(frozen=True)
class ServerConfig:
    """Runtime configuration for the MCP server."""

    host: str = "0.0.0.0"
    port: int = 8000
    mcp_path: str = "/mcp"
    log_level: str = "INFO"



def load_config() -> ServerConfig:
    """Load configuration from environment variables."""
    return ServerConfig(
        host=os.getenv("HOST", "0.0.0.0"),
        port=int(os.getenv("PORT", "8000")),
        mcp_path=os.getenv("MCP_PATH", "/mcp"),
        log_level=os.getenv("LOG_LEVEL", "INFO"),
    )
