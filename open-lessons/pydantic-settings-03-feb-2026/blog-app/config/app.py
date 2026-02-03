import logging
from typing import Literal
from pydantic import BaseModel, computed_field

LOGGING_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"


class LoggingConfig(BaseModel):
    level_name: Literal[
        "DEBUG",
        "INFO",
        "WARNING",
        "ERROR",
        "CRITICAL",
    ] = "INFO"
    format: str = LOGGING_FORMAT

    # помечать как computed_field в настройках обычно не требуется
    @computed_field
    @property
    def level(self) -> int:
        return logging.getLevelNamesMapping()[self.level_name]


class AppConfig(BaseModel):
    host: str = "localhost"
    port: int = 8000

    environment: Literal[
        "development",
        "testing",
        "production",
    ] = "development"

    logging: LoggingConfig = LoggingConfig()
