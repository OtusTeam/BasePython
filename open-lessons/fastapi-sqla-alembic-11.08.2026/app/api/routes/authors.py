from collections.abc import Sequence

from fastapi import APIRouter
from fastapi import status

from app.api.params import Limit
from app.api.params import Offset
from app.api.params import PrimaryKey
from app.dependencies import CatalogServiceDependency
from app.models.author import Author
from app.schemas.authors import AuthorCreate
from app.schemas.authors import AuthorRead
from app.schemas.authors import AuthorWithBooks

router = APIRouter(prefix="/authors", tags=["authors"])


@router.post(
    "",
    response_model=AuthorRead,
    status_code=status.HTTP_201_CREATED,
)
def create_author(
    payload: AuthorCreate,
    service: CatalogServiceDependency,
) -> Author:
    return service.create_author(payload)


@router.get("", response_model=list[AuthorWithBooks])
def list_authors(
    service: CatalogServiceDependency,
    offset: Offset = 0,
    limit: Limit = 20,
) -> Sequence[Author]:
    return service.list_authors(offset=offset, limit=limit)


@router.get("/{author_id}", response_model=AuthorWithBooks)
def get_author(
    author_id: PrimaryKey,
    service: CatalogServiceDependency,
) -> Author:
    return service.get_author(author_id)
