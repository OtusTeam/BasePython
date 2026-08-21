from functools import lru_cache
from pathlib import Path
from typing import override

from pydantic import Field
from pydantic_settings import BaseSettings
from pydantic_settings import PydanticBaseSettingsSource
from pydantic_settings import SettingsConfigDict
from pydantic_settings import YamlConfigSettingsSource

from app.config.app import AppConfig
from app.config.database import DatabaseConfig

CONFIG_DIR = Path(__file__).resolve().parent
PROJECT_DIR = CONFIG_DIR.parents[1]


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_prefix="FASTAPI_DEMO__",
        env_nested_delimiter="__",
        env_file=PROJECT_DIR / ".env",
        env_file_encoding="utf-8",
        yaml_config_section="fastapi-db-demo",
        yaml_file=(
            CONFIG_DIR / "yaml" / "default.yaml",
            CONFIG_DIR / "yaml" / "local.yaml",
        ),
        case_sensitive=False,
        extra="ignore",
    )

    app: AppConfig = AppConfig()
    database: DatabaseConfig = DatabaseConfig()

    @classmethod
    @override
    def settings_customise_sources(
        cls,
        settings_cls: type[BaseSettings],
        init_settings: PydanticBaseSettingsSource,
        env_settings: PydanticBaseSettingsSource,
        dotenv_settings: PydanticBaseSettingsSource,
        file_secret_settings: PydanticBaseSettingsSource,
    ) -> tuple[PydanticBaseSettingsSource, ...]:
        return (
            init_settings,
            env_settings,
            dotenv_settings,
            file_secret_settings,
            YamlConfigSettingsSource(settings_cls, deep_merge=True),
        )


@lru_cache(maxsize=1)
def get_settings() -> Settings:
    return Settings()


settings = get_settings()
