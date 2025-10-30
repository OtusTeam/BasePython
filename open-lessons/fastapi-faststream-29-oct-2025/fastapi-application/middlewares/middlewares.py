import logging
import time
from typing import Callable, Awaitable

from fastapi import FastAPI, Request, Response
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.base import BaseHTTPMiddleware

from middlewares.requests_count_middleware import requests_count_middleware_dispatch

log = logging.getLogger(__name__)


ALLOW_ORIGINS = [
    "http://localhost",
    "http://localhost:8000",
]


type CallNext = Callable[[Request], Awaitable[Response]]


async def add_process_time_to_requests(
    request: Request,
    call_next: CallNext,
) -> Response:
    start_time = time.perf_counter()
    response = await call_next(request)
    process_time = time.perf_counter() - start_time
    response.headers["X-Process-Time"] = f"{process_time:.5f}"
    return response


class ProcessTimeHeaderMiddleware(BaseHTTPMiddleware):
    def __init__(self, *args, process_time_header_name: str, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.header_name = process_time_header_name

    async def dispatch(
        self,
        request: Request,
        call_next: CallNext,
    ) -> Response:
        start_time = time.perf_counter()
        response = await call_next(request)
        process_time = time.perf_counter() - start_time
        response.headers[self.header_name] = f"{process_time:.5f}"
        return response


def register_middlewares(app: FastAPI) -> None:
    @app.middleware("http")
    async def log_new_requests(
        request: Request,
        call_next: CallNext,
    ) -> Response:
        log.info(
            "Request %s to %s",
            request.method,
            # request.url,
            request.url.path,
        )
        return await call_next(request)

    app.middleware("http")(add_process_time_to_requests)

    app.add_middleware(
        CORSMiddleware,
        allow_origins=ALLOW_ORIGINS,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.add_middleware(
        ProcessTimeHeaderMiddleware,
        process_time_header_name="X-Process-Time-New-Again",
    )

    app.add_middleware(
        BaseHTTPMiddleware,
        dispatch=requests_count_middleware_dispatch,
    )
