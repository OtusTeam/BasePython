import pytest
from sqlalchemy.orm import Session
from starlette import status
from starlette.testclient import TestClient

from bookshelf.books import service
from bookshelf.books.models import Book
from bookshelf.books.schemas import BookCreate, BookOut
from bookshelf.config.settings import Settings



@pytest.fixture
def book(db_session: Session, settings: Settings):
    book_create = BookCreate(
        title="Python Basics",
        pages=100,
    )
    book = service.create_book(db_session, book_create, settings.books)
    db_session.commit()
    # db_session.refresh(book)
    yield book
    db_session.delete(book)
    db_session.commit()


@pytest.mark.parametrize(
    "data_create",
    [
        pytest.param(
            BookCreate(
                title="Python Basics",
                pages=100,
            ),
            id="python-basics",
        ),
        pytest.param(
            BookCreate(
                title="JS Basics",
                pages=200,
            ),
            id="js-basics",
        ),
        pytest.param(
            BookCreate(
                title="   Strip Basics   ",
                pages=10,
            ),
            id="strip-basics",
        ),
        pytest.param(
            BookCreate(
                title="a",
                pages=1,
            ),
            id="single-char-title",
        ),
        pytest.param(
            BookCreate(
                title="a" * 100,
                pages=10_000,
            ),
            id="max-values",
        ),
    ],
)
def test_create_book(data_create: BookCreate, client: TestClient):
    url = client.app.url_path_for("books:create")
    response = client.post(
        url,
        json=data_create.model_dump(mode="json"),
    )
    assert response.status_code == status.HTTP_201_CREATED, response.text
    response_book = BookOut.model_validate(response.json())
    assert response_book.title == data_create.title
    assert response_book.pages == data_create.pages


def test_mark_book_read(client: TestClient, book: Book, db_session: Session):
    assert book.is_read is False, "expected to be read"
    url = client.app.url_path_for("books:read", book_id=book.id)
    response = client.patch(url)
    assert response.status_code == status.HTTP_200_OK, response.text
    assert BookOut.model_validate(response.json()).is_read is True
    db_session.refresh(book)
    assert book.is_read is True, "expected to be set in DB"
