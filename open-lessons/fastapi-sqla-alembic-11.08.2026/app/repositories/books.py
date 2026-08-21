from collections.abc import Sequence

from sqlalchemy.orm import Session

from app.models.book import Book


class BookRepository:
    def __init__(self, session: Session) -> None:
        self.session = session

    def add(self, book: Book) -> None:
        # TODO: Добавить книгу в Session, выполнить flush() и refresh().
        # Ошибку внешнего ключа преобразовать в AuthorNotFoundError.
        raise NotImplementedError

    def list(self, *, offset: int, limit: int) -> Sequence[Book]:
        # TODO: Выбрать книги через select(Book), отсортировать по id и
        # применить offset/limit.
        raise NotImplementedError

    def get(self, book_id: int) -> Book:
        # TODO: Получить книгу через Session.get() и выбросить
        # BookNotFoundError, если запись не найдена.
        raise NotImplementedError
