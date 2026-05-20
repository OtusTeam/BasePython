from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi import Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

from config import BASE_DIR
from misc.shutdown import shutdown
from misc.templating import templates
from orders.views import router

STATIC_DIR = BASE_DIR / "static"


@asynccontextmanager
async def lifespan(_app: FastAPI) -> AsyncGenerator:
    shutdown.install_shutdown_handlers()
    yield
    shutdown.request_shutdown()


app = FastAPI(
    title="Orders API: SSE + HTMX Demo",
    lifespan=lifespan,
)
app.mount(
    "/static",
    StaticFiles(directory=STATIC_DIR),
    name="static",
)
app.include_router(router)


@app.get("/", include_in_schema=False)
def get_index(request: Request) -> HTMLResponse:
    return templates.TemplateResponse(
        request=request,
        name="index.html",
    )
