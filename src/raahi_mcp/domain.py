"""Domain models for station lookup."""

from pydantic import BaseModel, Field


class Station(BaseModel):
    stationCode: str = Field(..., description="Indian Railways station code")
    stationName: str
    city: str
    state: str
    aliases: list[str]


class LookupMetadata(BaseModel):
    provider: str
    mock: bool = True
    app: str = "Raahi"


class LookupResponse(BaseModel):
    query: str
    stations: list[Station]
    metadata: LookupMetadata
