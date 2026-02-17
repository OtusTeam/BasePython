from uuid import UUID

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from models import Book
from schemas import BookCreate


class Crud:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def list(self) -> list[Book]:
        stmt = select(Book).order_by(Book.id)
        books = await self.session.scalars(stmt)
        return list(books.all())

    async def get_by_id(self, book_id: UUID) -> Book | None:
        return await self.session.get(Book, book_id)

    async def create(
        self,
        book_create: BookCreate,
    ) -> Book:
        book = Book(
            **book_create.model_dump(),
        )
        self.session.add(book)
        await self.session.commit()
        return book
