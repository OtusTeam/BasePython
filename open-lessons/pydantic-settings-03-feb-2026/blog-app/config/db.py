from pydantic import BaseModel, SecretStr, computed_field
from sqlalchemy import URL


class PostgresConfig(BaseModel):
    host: str = "localhost"
    port: int = 5432
    user: str = "app"
    password: SecretStr = SecretStr("password")
    database: str = "blog"


class SqlaConfig(BaseModel):
    echo: bool = False
    driver: str = "postgresql+psycopg"
    pool_size: int = 100
    max_overflow: int = 10


class DatabaseConfig(BaseModel):
    postgres: PostgresConfig = PostgresConfig()
    sqla: SqlaConfig = SqlaConfig()

    @property
    def url(self) -> URL:
        return URL.create(
            drivername=self.sqla.driver,
            host=self.postgres.host,
            port=self.postgres.port,
            username=self.postgres.user,
            password=self.postgres.password.get_secret_value(),
            database=self.postgres.database,
        )

    # помечать как computed_field в настройках обычно не требуется
    @computed_field
    @property
    def url_string_with_password(self) -> str:
        """
        поле только для демонстрации
        """
        return self.url.render_as_string(hide_password=False)
