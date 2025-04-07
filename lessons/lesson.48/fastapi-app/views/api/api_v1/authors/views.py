from typing import Annotated

from fastapi import (
    APIRouter,
    HTTPException,
    status,
    Depends,
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
def get_authors_list(
    storage: Annotated[
        AuthorsStorage,
        Depends(authors_crud_dependency),
    ],
):
    return storage.get()


@router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
    response_model=AuthorRead,
)
def create_author(
    author_in: AuthorCreate,
    storage: Annotated[
        AuthorsStorage,
        Depends(authors_crud_dependency),
    ],
):
    return storage.create(author_in=author_in)


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
def get_author(
    author_id: PositiveInt,
    storage: Annotated[
        AuthorsStorage,
        Depends(authors_crud_dependency),
    ],
):
    author = storage.get_by_id(author_id=author_id)
    if author:
        return author

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Author #{author_id} not found",
    )
