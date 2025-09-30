from pathlib import Path

from pydantic import BaseModel, SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict

from sqlalchemy import URL


BASE_DIR = Path(__file__).resolve().parent


class DbConfig(BaseModel):
    driver_sync: str = "postgresql+psycopg"
    driver_async: str = "postgresql+asyncpg"

    echo: bool = False
    host: str
    port: int = 5432
    database: str

    username: str
    password: SecretStr

    max_overflow: int = 0
    pool_size: int = 50

    def build_url(self, driver_name: str) -> URL:
        return URL.create(
            driver_name,
            host=self.host,
            port=self.port,
            database=self.database,
            username=self.username,
            password=self.password.get_secret_value(),
        )

    @property
    def url(self) -> URL:
        return self.build_url(self.driver_sync)

    @property
    def async_url(self) -> URL:
        return self.build_url(self.driver_async)


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_prefix="BLOG_APP__",
        env_nested_delimiter="__",
        env_file=(
            BASE_DIR / ".env.default",
            BASE_DIR / ".env",
        ),
    )
    db: DbConfig


# noinspection PyArgumentList
settings = Settings()
