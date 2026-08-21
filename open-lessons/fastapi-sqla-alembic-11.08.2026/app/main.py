import asyncio
from collections.abc import AsyncIterator
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi import Request
from fastapi import status
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

from app.api.router import router
from app.config import get_settings
from app.db import engine
from app.exceptions import ApplicationError
from app.exceptions import ConflictError
from app.exceptions import NotFoundError
from app.exceptions import TemporaryUnavailableError
from app.models import Base

settings = get_settings()


@asynccontextmanager
async def lifespan(_: FastAPI) -> AsyncIterator[None]:
    yield


app = FastAPI(
    title=settings.app.name,
    debug=settings.app.debug,
    lifespan=lifespan,
)


@app.exception_handler(RequestValidationError)
async def request_validation_error_handler(
    request: Request,
    exc: RequestValidationError,
) -> JSONResponse:
    del request
    errors = [
        {key: error[key] for key in ("type", "loc", "msg")} for error in exc.errors()
    ]
    return JSONResponse(status_code=422, content={"detail": errors})


@app.exception_handler(ApplicationError)
async def application_error_handler(
    request: Request,
    exc: ApplicationError,
) -> JSONResponse:
    del request
    headers = None
    if isinstance(exc, NotFoundError):
        status_code = status.HTTP_404_NOT_FOUND
    elif isinstance(exc, ConflictError):
        status_code = status.HTTP_409_CONFLICT
    elif isinstance(exc, TemporaryUnavailableError):
        status_code = status.HTTP_503_SERVICE_UNAVAILABLE
        headers = {"Retry-After": "1"}
    else:
        status_code = status.HTTP_500_INTERNAL_SERVER_ERROR

    return JSONResponse(
        status_code=status_code,
        headers=headers,
        content={"error": {"code": exc.code, "message": exc.message}},
    )


app.include_router(router)
