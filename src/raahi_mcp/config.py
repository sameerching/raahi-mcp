"""Runtime configuration for Raahi."""

from __future__ import annotations

import os

from pydantic import BaseModel


class Settings(BaseModel):
    """Environment-driven settings."""

    port: int = int(os.getenv("PORT", "8000"))
    log_level: str = os.getenv("LOG_LEVEL", "INFO")
    provider: str = os.getenv("RAAHI_PROVIDER", "mock")


settings = Settings()
