from typing import Annotated

from fastapi import Depends
from sqlalchemy.orm import Session

from app.db import get_session
from app.services import CatalogService

SessionDependency = Annotated[
    Session,
    Depends(get_session, scope="function"),
]


def get_catalog_service(session: SessionDependency) -> CatalogService:
    return CatalogService(session)


CatalogServiceDependency = Annotated[
    CatalogService,
    Depends(get_catalog_service),
]
