from typing import Literal

from pydantic import Field

from bookshelf.config.base import Config


class AppConfig(Config):
    environment: Literal["dev", "test"]
    title: str = Field(min_length=1)
