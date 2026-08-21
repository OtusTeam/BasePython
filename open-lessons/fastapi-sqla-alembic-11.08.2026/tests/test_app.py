from pathlib import Path

import pytest
from fastapi.testclient import TestClient
from pydantic import ValidationError
from sqlalchemy import CheckConstraint
from sqlalchemy import Text
from sqlalchemy import create_engine
from sqlalchemy import inspect
from sqlalchemy.pool import StaticPool

import app.main as main_module
from app.config.settings import Settings
from app.main import app
from app.models import Author
from app.models import Base
from app.models import Book


def test_yaml_defaults_can_be_overridden_by_dotenv(tmp_path: Path) -> None:
    env_file = tmp_path / ".env"
    env_file.write_text(
        "FASTAPI_DEMO__DATABASE__SQLALCHEMY__POOL_SIZE=7\n",
        encoding="utf-8",
    )

    settings = Settings(_env_file=env_file)

    assert settings.app.name == "FastAPI SQLAlchemy Alembic Demo"
    assert settings.database.sqlalchemy.pool_size == 7

    with pytest.raises(ValidationError):
        Settings(app={"api_v1_prefix": "/api/v1/"})


def test_table_names_are_derived_from_model_names() -> None:
    assert "__tablename__" not in Author.__dict__
    assert "__tablename__" not in Book.__dict__
    assert Author.__tablename__ == "author"
    assert Book.__tablename__ == "book"


def test_text_columns_have_length_constraints() -> None:
    assert isinstance(Author.__table__.c.name.type, Text)
    assert isinstance(Book.__table__.c.title.type, Text)

    author_check = Author.__table_args__[0]
    book_check = Book.__table_args__[0]

    assert isinstance(author_check, CheckConstraint)
    assert isinstance(book_check, CheckConstraint)
    assert author_check.name == "ck_author_name_length"
    assert str(author_check.sqltext) == "length(name) <= 120"
    assert book_check.name == "ck_book_title_length"
    assert str(book_check.sqltext) == "length(title) <= 200"


def test_create_all_builds_the_model_schema() -> None:
    engine = create_engine("sqlite://")

    Base.metadata.create_all(bind=engine)

    database = inspect(engine)
    assert set(database.get_table_names()) == {"author", "book"}
    assert database.get_foreign_keys("book")[0]["referred_table"] == "author"


def test_lifespan_creates_tables_without_postgres(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    test_engine = create_engine(
        "sqlite://",
        connect_args={"check_same_thread": False},
        poolclass=StaticPool,
    )
    monkeypatch.setattr(main_module, "engine", test_engine)

    with TestClient(app) as client:
        response = client.get("/health")

    assert response.json() == {"status": "ok", "database": "not_checked"}
    assert set(inspect(test_engine).get_table_names()) == {"author", "book"}
