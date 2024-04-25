from fastapi import (
    FastAPI,
    APIRouter,
)
from fastapi.responses import HTMLResponse

import config
from views.hello import router as router_hello
from views.items import router as router_items
from api_v1 import router as router_api_v1
from api_v2 import router as router_api_v2


api_router = APIRouter(prefix=config.API_PREFIX, tags=["API"])
api_router.include_router(
    router_api_v1,
    prefix=config.API_V1_PREFIX,
    tags=["API v1"],
)
api_router.include_router(
    router_api_v2,
    prefix=config.API_V2_PREFIX,
    tags=["API v2"],
)


app = FastAPI()
app.include_router(router_hello)
app.include_router(router_items)
app.include_router(api_router)


@app.get("/")
def index_page():
    return {"message": "Hello World"}


@app.get("/demo-html", response_class=HTMLResponse)
def demo_html():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
      <meta charset="UTF-8">
      <title>Hi</title>
    </head>
    <body>
      <h1>Hello World</h1>
    </body>
    </html>
    """
