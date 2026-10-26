from pathlib import Path

from pydantic_settings import BaseSettings
from pydantic_settings import PydanticBaseSettingsSource
from pydantic_settings import SettingsConfigDict
from pydantic_settings import YamlConfigSettingsSource

from bookshelf.config.app import AppConfig
from bookshelf.config.books import BookConfig
from bookshelf.config.database import DatabaseConfig


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_prefix="BOOKSHELF__",
        env_nested_delimiter="__",
        extra="forbid",
        hide_input_in_errors=False,
    )

    app: AppConfig
    database: DatabaseConfig
    books: BookConfig

    @classmethod
    def settings_customise_sources(
        cls,
        settings_cls: type[BaseSettings],
        init_settings: PydanticBaseSettingsSource,
        env_settings: PydanticBaseSettingsSource,
        dotenv_settings: PydanticBaseSettingsSource,
        file_secret_settings: PydanticBaseSettingsSource,
    ) -> tuple[PydanticBaseSettingsSource, ...]:
        del dotenv_settings, file_secret_settings
        config_dir = Path(__file__).parent / "yaml"
        defaults_file = config_dir / "default.yaml"
        defaults = YamlConfigSettingsSource(settings_cls, yaml_file=defaults_file)
        init_app = init_settings().get("app", {})
        if isinstance(init_app, AppConfig):
            init_app = init_app.model_dump()
        environment = init_app.get(
            "environment",
            env_settings().get("app", {}).get("environment", defaults()["app"]["environment"]),
        )
        if environment not in {"dev", "test"}:
            msg = "BOOKSHELF__APP__ENVIRONMENT must be dev or test"
            raise ValueError(msg)
        yaml_source = YamlConfigSettingsSource(
            settings_cls,
            yaml_file=[defaults_file, config_dir / f"{environment}.yaml"],
            deep_merge=True,
        )
        return init_settings, env_settings, yaml_source


settings = Settings()
