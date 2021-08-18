from pydantic import BaseSettings
from pydantic import PostgresDsn as GenericPostgresDsn


class PostgresDsn(GenericPostgresDsn):
    allowed_schemes = {"postgresql+asyncpg"}


class Settings(BaseSettings):
    PG_ECHO: bool = False
    PG_DSN: PostgresDsn = "postgresql+asyncpg://user:password@localhost:5432/blog_project"


settings = Settings()
