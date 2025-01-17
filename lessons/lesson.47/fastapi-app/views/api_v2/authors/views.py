from fastapi import (
    APIRouter,
    HTTPException,
    status,
    Depends,
)
from pydantic import PositiveInt

from models import Author

from schemas.author import (
    AuthorReadSchema,
    AuthorCreateSchema,
)
from .crud import AuthorStorage
from .dependencies import (
    authors_crud_dependency,
    get_author_by_email,
)

router = APIRouter(
    prefix="/authors",
    tags=["Authors"],
)


@router.get(
    "/",
    response_model=list[AuthorReadSchema],
)
async def get_authors_list(
    storage: AuthorStorage = Depends(authors_crud_dependency),
) -> list[Author]:
    return await storage.get()


@router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
    response_model=AuthorReadSchema,
)
async def create_author(
    author_in: AuthorCreateSchema,
    storage: AuthorStorage = Depends(authors_crud_dependency),
) -> Author:
    return await storage.create(author_in=author_in)


@router.post(
    "/create-many",
    status_code=status.HTTP_201_CREATED,
    response_model=list[AuthorReadSchema],
)
async def create_many_authors(
    n_authors: PositiveInt,
    storage: AuthorStorage = Depends(authors_crud_dependency),
) -> list[Author]:
    return await storage.create_many(n_authors=n_authors)


@router.get(
    "/find/",
    response_model=AuthorReadSchema,
)
def get_by_email(
    author: Author = Depends(get_author_by_email),
) -> Author:
    return author


@router.get(
    "/{author_id}/",
    response_model=AuthorReadSchema,
    responses={
        status.HTTP_404_NOT_FOUND: {
            "description": "Author not found",
            "content": {
                "application/json": {
                    "example": {
                        "detail": "Author #0 not found",
                    },
                },
            },
        },
    },
)
async def get_author(
    author_id: PositiveInt,
    storage: AuthorStorage = Depends(authors_crud_dependency),
) -> Author:
    author = await storage.get_by_id(author_id=author_id)
    if author:
        return author

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Author #{author_id} not found",
    )
