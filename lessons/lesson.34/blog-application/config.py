__all__ = ("settings",)

from pathlib import Path

from pydantic import BaseModel, PostgresDsn
from pydantic_settings import BaseSettings, SettingsConfigDict


BASE_DIR = Path(__file__).resolve().parent


class DbConfig(BaseModel):
    url: PostgresDsn
    async_url: PostgresDsn
    echo: bool = False

    pool_size: int = 50
    max_overflow: int = 0


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        case_sensitive=False,
        env_file=(
            BASE_DIR / ".env.template",
            BASE_DIR / ".env",
        ),
        env_nested_delimiter="__",
        env_prefix="BLOG__",
    )

    db: DbConfig


# noinspection PyArgumentList
settings = Settings()
