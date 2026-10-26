from pathlib import Path

from sqlalchemy.engine import URL

from bookshelf.config.base import Config


class DatabaseConfig(Config):
    path: Path

    @property
    def url(self) -> URL:
        return URL.create("sqlite+pysqlite", database=str(self.path))
