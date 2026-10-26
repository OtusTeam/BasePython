from typing import TYPE_CHECKING

from fastapi.responses import JSONResponse

from bookshelf.core.errors import DomainError


if TYPE_CHECKING:
    from fastapi import FastAPI
    from fastapi import Request


def install_error_handlers(app: FastAPI) -> None:
    @app.exception_handler(DomainError)
    async def domain_error(_request: Request, exc: DomainError) -> JSONResponse:
        return JSONResponse({"detail": exc.detail}, status_code=exc.status)
