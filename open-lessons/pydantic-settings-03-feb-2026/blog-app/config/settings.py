from pathlib import Path

from pydantic_settings import (
    BaseSettings,
    SettingsConfigDict,
    PydanticBaseSettingsSource,
    YamlConfigSettingsSource,
)

from config.app import AppConfig
from config.db import DatabaseConfig

CURRENT_DIR = Path(__file__).resolve().parent
ENVS_DIR = CURRENT_DIR / "envs"
YAML_DIR = CURRENT_DIR / "yaml"

# хост и порт, где запускается приложение
# уровень логирования
# окружение: прод или дев
# токен для OpenAI / GigaChat / etc..
# модель LLM - gpt-5 / gpt-5-mini / gpt-5-nano / etc..
# настройки для подключения к БД: хост, порт, юзер, пароль, база, опции (опционально)
# конфиг почты: smtp host, port, user, pass, ssl ..., sender


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_prefix="BLOG_APP__",
        env_nested_delimiter="__",
        env_file=(
            ENVS_DIR / ".env.template",
            ENVS_DIR / ".env",
        ),
        case_sensitive=False,
        # extra="ignore",
        yaml_config_section="blog-app",
        yaml_file=(
            YAML_DIR / "default.yaml",
            YAML_DIR / "local.yaml",
        ),
    )

    app: AppConfig = AppConfig()
    db: DatabaseConfig = DatabaseConfig()

    # настройки приложения:
    # _ где запускается приложение:
    # хост
    # порт
    # уровень логирования
    # окружение: прод или дев

    # подключение к LLM:
    # base api url
    # Proxy для подключения к openAI
    # токен для OpenAI
    # модель LLM - gpt-5 / gpt-5-mini / gpt-5-nano / etc..

    # настройки для подключения к БД:
    # хост,
    # порт,
    # юзер,
    # пароль,
    # база,
    # опции (опционально)

    # конфиг почты smtp:
    # host
    # , port
    # , user
    # , pass
    # , ssl
    # , ...
    # , sender

    @classmethod
    def settings_customise_sources(
        cls,
        settings_cls: type[BaseSettings],
        init_settings: PydanticBaseSettingsSource,
        env_settings: PydanticBaseSettingsSource,
        dotenv_settings: PydanticBaseSettingsSource,
        file_secret_settings: PydanticBaseSettingsSource,
    ) -> tuple[PydanticBaseSettingsSource, ...]:
        """
        Define the sources and their order for loading the settings values.

        Args:
            settings_cls: The Settings class.
            init_settings: The `InitSettingsSource` instance.
            env_settings: The `EnvSettingsSource` instance.
            dotenv_settings: The `DotEnvSettingsSource` instance.
            file_secret_settings: The `SecretsSettingsSource` instance.

        Returns:
            A tuple containing the sources and their order for loading the settings values.
        """
        return (
            init_settings,
            env_settings,
            dotenv_settings,
            file_secret_settings,
            YamlConfigSettingsSource(settings_cls),
        )


settings = Settings()
