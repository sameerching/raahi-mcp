from raahi_mcp.station_service import lookup_station_data


def test_lookup_by_code_sbc() -> None:
    result = lookup_station_data("SBC")
    assert result["matches"]
    assert result["matches"][0]["code"] == "SBC"


def test_lookup_by_alias_bangalore() -> None:
    result = lookup_station_data("Bangalore")
    assert result["matches"]
    assert result["matches"][0]["code"] == "SBC"


def test_lookup_by_city_kanpur() -> None:
    result = lookup_station_data("Kanpur")
    assert result["matches"]
    assert result["matches"][0]["code"] == "CNB"


def test_lookup_unknown_station_returns_empty_list() -> None:
    result = lookup_station_data("NoSuchStation")
    assert result["matches"] == []
