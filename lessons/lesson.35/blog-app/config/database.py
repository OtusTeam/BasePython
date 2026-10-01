from pydantic import BaseModel, SecretStr
from sqlalchemy import URL


class SQLAlchemyConfig(BaseModel):
    pool_size: int = 50
    max_overflow: int = 0
    echo: bool = False


class DatabaseConfig(BaseModel):
    name: str = "blog"
    host: str = "localhost"
    port: int = 5432
    user: str = "app"
    password: SecretStr

    sqla: SQLAlchemyConfig = SQLAlchemyConfig()

    @property
    def url(self) -> URL:
        return URL.create(
            drivername="postgresql+psycopg",
            database=self.name,
            host=self.host,
            port=self.port,
            username=self.user,
            password=self.password.get_secret_value(),
        )

    @property
    def async_url(self) -> URL:
        return URL.create(
            drivername="postgresql+asyncpg",
            database=self.name,
            host=self.host,
            port=self.port,
            username=self.user,
            password=self.password.get_secret_value(),
        )
