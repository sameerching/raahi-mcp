from raahi_mcp.station_service import lookup_station_data


def test_import_station_service_without_mcp() -> None:
    result = lookup_station_data("SBC")
    assert isinstance(result, dict)


def test_lookup_by_station_code() -> None:
    response = lookup_station_data("SBC")
    assert response["stations"]
    assert response["stations"][0]["stationCode"] == "SBC"


def test_lookup_by_city_bangalore() -> None:
    response = lookup_station_data("Bangalore")
    assert response["stations"]
    assert response["stations"][0]["stationCode"] == "SBC"


def test_lookup_by_kanpur() -> None:
    response = lookup_station_data("Kanpur")
    assert response["stations"]
    assert response["stations"][0]["stationCode"] == "CNB"


def test_lookup_unknown_returns_empty() -> None:
    response = lookup_station_data("NoSuchStation")
    assert response["stations"] == []
