"""Domain models for station lookup."""

from __future__ import annotations

from dataclasses import asdict, dataclass


@dataclass(frozen=True)
class Station:
    """Represents a railway station in the mock catalog."""

    code: str
    name: str
    city: str
    state: str
    aliases: tuple[str, ...]

    def to_dict(self) -> dict[str, object]:
        """Convert station to a plain dictionary."""
        data = asdict(self)
        data["aliases"] = list(self.aliases)
        return data
