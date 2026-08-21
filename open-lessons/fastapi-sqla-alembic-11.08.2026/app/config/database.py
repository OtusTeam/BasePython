from typing import Literal

from pydantic import BaseModel
from pydantic import Field
from pydantic import SecretStr
from sqlalchemy import URL


class PostgresConfig(BaseModel):
    host: str = "localhost"
    port: int = Field(default=5432, ge=1, le=65535)
    user: str = "app"
    password: SecretStr = SecretStr("app")
    database: str = "app"
    max_connections: int = Field(default=100, ge=10)


class SQLAlchemyConfig(BaseModel):
    driver: Literal["postgresql+psycopg"] = "postgresql+psycopg"
    echo: bool = False
    pool_size: int = Field(default=5, ge=1)
    max_overflow: int = Field(default=0, ge=0)
    pool_timeout_seconds: float = Field(default=2.0, gt=0)
    pool_recycle_seconds: int = Field(default=1800, ge=1)
    connect_timeout_seconds: int = Field(default=3, ge=1)


class DatabaseConfig(BaseModel):
    postgres: PostgresConfig = PostgresConfig()
    sqlalchemy: SQLAlchemyConfig = SQLAlchemyConfig()

    @property
    def url(self) -> URL:
        return URL.create(
            drivername=self.sqlalchemy.driver,
            username=self.postgres.user,
            password=self.postgres.password.get_secret_value(),
            host=self.postgres.host,
            port=self.postgres.port,
            database=self.postgres.database,
        )
