from uuid import UUID

from fastapi import APIRouter
from starlette import status

from bookshelf.books import service
from bookshelf.books.schemas import BookCreate
from bookshelf.books.schemas import BookOut
from bookshelf.core.deps import SessionDep
from bookshelf.core.deps import SettingsDep


router = APIRouter(prefix="/books", tags=["books"])


@router.get("", name="books:list")
def list_books(session: SessionDep) -> list[BookOut]:
    return [BookOut.model_validate(book) for book in service.list_books(session)]


@router.post("", status_code=status.HTTP_201_CREATED, name="books:create")
def create_book(data: BookCreate, session: SessionDep, settings: SettingsDep) -> BookOut:
    book = service.create_book(session, data, settings.books)
    session.commit()
    return BookOut.model_validate(book)


@router.patch("/{book_id}/read", name="books:read")
def mark_read(book_id: UUID, session: SessionDep) -> BookOut:
    book = service.mark_read(session, book_id)
    session.commit()
    return BookOut.model_validate(book)
    # result = BookOut.model_validate(book)
    # result.is_read = True
    # return result
