from typing import Annotated

from fastapi import (
    APIRouter,
    HTTPException,
    status,
    Depends,
    Query,
)
from pydantic import PositiveInt

from schemas.author import (
    AuthorCreate,
    AuthorRead,
)

from .crud import AuthorsStorage
from .dependencies import authors_crud_dependency

router = APIRouter(
    prefix="/authors",
    tags=["Author"],
)


@router.get(
    "/",
    response_model=list[AuthorRead],
)
async def get_authors_list(
    storage: Annotated[
        AuthorsStorage,
        Depends(authors_crud_dependency),
    ],
):
    return await storage.get()


@router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
    response_model=AuthorRead,
)
async def create_author(
    author_in: AuthorCreate,
    storage: Annotated[
        AuthorsStorage,
        Depends(authors_crud_dependency),
    ],
):
    return await storage.create(author_in=author_in)


@router.post(
    "/create-many",
    status_code=status.HTTP_201_CREATED,
    response_model=list[AuthorRead],
)
async def create_many_authors(
    count: Annotated[int, Query],
    storage: Annotated[
        AuthorsStorage,
        Depends(authors_crud_dependency),
    ],
):
    return await storage.create_many(n_authors=count)


@router.get(
    "/{author_id}/",
    response_model=AuthorRead,
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
    storage: Annotated[
        AuthorsStorage,
        Depends(authors_crud_dependency),
    ],
):
    author = await storage.get_by_id(author_id=author_id)
    if author:
        return author

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Author #{author_id} not found",
    )
