from typing import Annotated

from fastapi import (
    Query,
    APIRouter,
)
from fastapi.responses import HTMLResponse


router = APIRouter()


@router.get("/hello/", tags=["Hello"])
def hello_name(
    name: Annotated[str, Query(min_length=3, max_length=50)],
):
    return {"message": f"Hello, {name}!"}


@router.get(
    "/hello-html/",
    response_class=HTMLResponse,
    tags=["Hello"],
)
def hello_page():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
      <meta charset="UTF-8">
      <title>Hello Page</title>
    </head>
    <body>
      <h1>Hello HTML World!</h1>
    </body>
    </html>
    """
