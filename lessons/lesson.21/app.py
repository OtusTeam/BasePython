from fastapi import FastAPI, HTTPException
from fastapi.exception_handlers import http_exception_handler
from starlette import status
from starlette.responses import JSONResponse, HTMLResponse
from starlette.exceptions import HTTPException as StarletteHTTPException

from api.items import router as items_router
from api.users.views import router as users_router_sync
from api.users_async.views import router as users_router_async

app = FastAPI()
app.include_router(items_router)
app.include_router(users_router_sync, prefix="/sync")
app.include_router(users_router_async, tags=["async"])


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/hello")
def hello(name: str = "OTUS"):
    return {
        "message": f"Hello {name}!",
    }


# @app.get("{url_path:path}")
# def all_others(
#     url_path: str,
# ):
#     return {"request to": url_path}


@app.exception_handler(StarletteHTTPException)
@app.exception_handler(HTTPException)
async def custom_http_exception_handler(request, exc):
    return await http_exception_handler(request, exc)


@app.exception_handler(status.HTTP_404_NOT_FOUND)
async def custom_404_handler(request, exception):
    if (isinstance(exception, StarletteHTTPException)
            and exception.detail != "Not Found"):
        return await http_exception_handler(request, exception)

    return JSONResponse(
        {
            "request url": request.url.path,
            "exception": str(exception),
        },
        status_code=status.HTTP_404_NOT_FOUND,
    )
