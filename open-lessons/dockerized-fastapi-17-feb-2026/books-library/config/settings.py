from pathlib import Path

from pydantic_settings import (
    BaseSettings,
    SettingsConfigDict,
    PydanticBaseSettingsSource,
    YamlConfigSettingsSource,
)

from config.app import AppConfig
from config.database import DatabaseConfig
from config.http import HttpConfig
from config.logging import LoggingConfig


CONFIG_DIR = Path(__file__).resolve().parent
ENVS_DIR = CONFIG_DIR / "envs"
YAML_DIR = CONFIG_DIR / "yaml"


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        case_sensitive=False,
        env_prefix="BOOKS_LIB__",  # suffix: two underscore chars
        env_nested_delimiter="__",  # two underscore chars
        env_file=(
            ENVS_DIR / ".env.template",
            ENVS_DIR / ".env",
        ),
        yaml_config_section="books-library",
        yaml_file=(
            YAML_DIR / "default.yaml",
            YAML_DIR / "local.yaml",
        ),
    )

    app: AppConfig = AppConfig()
    logging: LoggingConfig = LoggingConfig()
    db: DatabaseConfig
    http: HttpConfig = HttpConfig()

    @classmethod
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
            # file_secret_settings,
            #
            YamlConfigSettingsSource(
                settings_cls,
                # pydantic > 2.12.0 required
                # deep_merge=True,
            ),
        )


settings = Settings()


# just for demo
if __name__ == "__main__":
    print(settings)
    print(settings.model_dump_json(indent=2))
    print("db password:", settings.db.password.get_secret_value())
    print("db url", settings.db.async_url)
    print("db url", settings.db.async_url.render_as_string(hide_password=False))
