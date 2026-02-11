from pydantic import BaseModel, SecretStr
from sqlalchemy import URL


class SQLAlchemyConfig(BaseModel):
    pool_size: int = 20
    max_overflow: int = 5
    echo: bool = False


class DatabaseConfig(BaseModel):
    name: str
    host: str
    port: int = 5432
    user: str
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
