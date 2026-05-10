from raahi_mcp.station_service import lookup_station_data


def test_lookup_by_station_code() -> None:
    response = lookup_station_data("SBC")
    assert response["stations"]
    assert response["stations"][0]["stationCode"] == "SBC"


def test_lookup_by_city_alias_bangalore() -> None:
    response = lookup_station_data("Bangalore")
    assert response["stations"]
    assert response["stations"][0]["stationCode"] == "SBC"


def test_lookup_by_kanpur() -> None:
    response = lookup_station_data("Kanpur")
    assert response["stations"]
    assert response["stations"][0]["stationCode"] == "CNB"


def test_lookup_unknown_returns_empty_list() -> None:
    response = lookup_station_data("NoSuchStation")
    assert response["stations"] == []
