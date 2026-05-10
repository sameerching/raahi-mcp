from raahi_mcp.server import lookup_station


def test_lookup_by_station_code() -> None:
    response = lookup_station("SBC")
    assert response["stations"]
    assert response["stations"][0]["stationCode"] == "SBC"


def test_lookup_by_city_bangalore() -> None:
    response = lookup_station("Bangalore")
    assert response["stations"]
    assert response["stations"][0]["stationCode"] == "SBC"


def test_lookup_by_kanpur() -> None:
    response = lookup_station("Kanpur")
    assert response["stations"]
    assert response["stations"][0]["stationCode"] == "CNB"


def test_lookup_unknown_returns_empty() -> None:
    response = lookup_station("NoSuchStation")
    assert response["stations"] == []
