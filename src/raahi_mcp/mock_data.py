from raahi_mcp.domain import Station

STATIONS: list[Station] = [
    Station(
        stationCode="SBC",
        stationName="KSR Bengaluru",
        city="Bengaluru",
        state="Karnataka",
        aliases=["Bangalore", "Bengaluru City", "KSR"],
    ),
    Station(
        stationCode="NDLS",
        stationName="New Delhi",
        city="Delhi",
        state="Delhi",
        aliases=["Delhi", "New Delhi Railway Station"],
    ),
    Station(
        stationCode="CNB",
        stationName="Kanpur Central",
        city="Kanpur",
        state="Uttar Pradesh",
        aliases=["Kanpur"],
    ),
    Station(
        stationCode="LKO",
        stationName="Lucknow Charbagh",
        city="Lucknow",
        state="Uttar Pradesh",
        aliases=["Lucknow"],
    ),
    Station(
        stationCode="BCT",
        stationName="Mumbai Central",
        city="Mumbai",
        state="Maharashtra",
        aliases=["Bombay Central", "Mumbai"],
    ),
    Station(
        stationCode="HWH",
        stationName="Howrah Junction",
        city="Kolkata",
        state="West Bengal",
        aliases=["Howrah", "Kolkata"],
    ),
]
