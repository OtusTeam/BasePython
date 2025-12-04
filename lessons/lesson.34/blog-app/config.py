from pydantic import BaseModel, SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict
from sqlalchemy import URL

sqla_naming_convention = {
    "ix": "ix_%(column_0_label)s",
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s",
}


class PostgresConfig(BaseModel):
    host: str = "localhost"
    port: int = 5432
    db: str = "blog"
    user: str = "postgres"
    password: SecretStr = SecretStr("password")


class SQLAlchemyConfig(BaseModel):
    pool_size: int = 50
    max_overflow: int = 0
    echo: bool = False


class DatabaseConfig(BaseModel):
    pg: PostgresConfig = PostgresConfig()
    sqla: SQLAlchemyConfig = SQLAlchemyConfig()

    def build_url(self, driver: str) -> URL:
        return URL.create(
            drivername=driver,
            username=self.pg.user,
            password=self.pg.password.get_secret_value(),
            host=self.pg.host,
            port=self.pg.port,
            database=self.pg.db,
        )

    @property
    def url(self) -> URL:
        return self.build_url("postgresql+psycopg")

    @property
    def async_url(self) -> URL:
        return self.build_url("postgresql+asyncpg")


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_prefix="BLOG_APP__",
        env_nested_delimiter="__",
        case_sensitive=False,
    )

    db: DatabaseConfig = DatabaseConfig()


settings = Settings()
