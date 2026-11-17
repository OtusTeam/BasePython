"""Catalog views with explicit request preparation for the lesson baseline."""

import logging

from fastapi import APIRouter, Depends
from fastapi.responses import StreamingResponse

from app.catalog import Book
from app.dependencies import Page, Books, Authors, trace_scope

router = APIRouter(
    tags=["catalog"],
    # prefix="/foo/bar",
    # dependencies=[Depends(trace_scope)],
)
logger = logging.getLogger(__name__)


@router.get(
    "/books",
    dependencies=[Depends(trace_scope, scope="function")],
)
def list_books(
    page: Page,
    service: Books,
) -> tuple[Book, ...]:
    """List books after manually preparing pagination and the catalog."""
    return service.list_books(offset=page.offset, limit=page.limit)


@router.get(
    "/authors",
    dependencies=[Depends(trace_scope, scope="request")],
)
def list_authors(
    page: Page,
    service: Authors,
) -> tuple[str, ...]:
    """Repeat request preparation for another resource."""
    return service.list_authors(offset=page.offset, limit=page.limit)


@router.get(
    "/export",
    response_class=StreamingResponse,
    dependencies=[Depends(trace_scope)],
)
def export_books(
    service: Books,
) -> StreamingResponse:
    """Return a response whose body is produced after this handler ends."""
    logger.info("handler: RETURN")
    return StreamingResponse(service.stream_titles(), media_type="text/plain")
