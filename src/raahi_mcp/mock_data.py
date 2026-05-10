"""Mock station dataset used by Phase 1 station lookup."""

from __future__ import annotations

from raahi_mcp.domain import Station


MOCK_STATIONS: tuple[Station, ...] = (
    Station(
        code="SBC",
        name="KSR Bengaluru",
        city="Bengaluru",
        state="Karnataka",
        aliases=("Bangalore", "Bengaluru City", "KSR"),
    ),
    Station(
        code="NDLS",
        name="New Delhi",
        city="Delhi",
        state="Delhi",
        aliases=("Delhi", "New Delhi Railway Station"),
    ),
    Station(
        code="CNB",
        name="Kanpur Central",
        city="Kanpur",
        state="Uttar Pradesh",
        aliases=("Kanpur",),
    ),
    Station(
        code="LKO",
        name="Lucknow Charbagh",
        city="Lucknow",
        state="Uttar Pradesh",
        aliases=("Lucknow",),
    ),
    Station(
        code="BCT",
        name="Mumbai Central",
        city="Mumbai",
        state="Maharashtra",
        aliases=("Bombay Central", "Mumbai"),
    ),
    Station(
        code="HWH",
        name="Howrah Junction",
        city="Howrah",
        state="West Bengal",
        aliases=("Howrah", "Kolkata"),
    ),
)
