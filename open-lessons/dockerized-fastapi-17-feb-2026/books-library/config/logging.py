from logging import getLevelNamesMapping
from typing import Literal

from pydantic import BaseModel


class LoggingConfig(BaseModel):
    format: str = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    level: Literal[
        "DEBUG",
        "INFO",
        "WARNING",
        "ERROR",
        "CRITICAL",
    ] = "INFO"

    @property
    def log_level(self) -> int:
        return getLevelNamesMapping()[self.level]
