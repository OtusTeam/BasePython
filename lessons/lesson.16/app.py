from typing import Annotated
from fastapi import (
    FastAPI,
    Path,
    Depends,
    Query,
    Header,
    HTTPException,
    status,
)
from fastapi.responses import HTMLResponse

from pydantic import BaseModel, Field
from pydantic.functional_validators import AfterValidator

from annotated_types import (
    MinLen,
    MaxLen,
)
from annotated_types import (
    Ge,
    Lt,
)
from pydantic import (
    PositiveInt,
    ValidationError,
)

app = FastAPI()


class SecretInfo(BaseModel):
    answer: int = Field(example=33)
    token: str = Field(
        example="spam-and-eggs",
        description="The secret token provided by user",
    )


def name_constraints(min_len: int, max_len: int):
    def _validator(name: str) -> str:
        if min_len <= len(name) <= max_len:
            return name
        raise ValueError(f"name should be between {min_len} and {max_len}")

    return _validator


@app.get("/")
def hello_root():
    return {
        "message": "Hello World!",
        "secret": None,
    }


@app.get("/items/", tags=["items"])
def get_items():
    return {
        "data": [
            {"id": 1, "name": "qwerty"},
            {"id": 2, "name": "foobar"},
        ],
    }


@app.get("/items/{item_id}/", tags=["items"])
def get_item(
    # item_id: Annotated[int, Ge(1), Lt(100_000)],
    item_id: Annotated[int, Path(ge=1, lt=100_000)],
):
    # get_item_from_db(item_id)
    return {
        "data": {"id": item_id, "name": "abc"},
    }


@app.get("/hello/", tags=["Hello"])
def hello_name(
    # name: Annotated[str, MinLen(3), MaxLen(50)],
    # name: Annotated[str, AfterValidator(name_constraints(3, 50))],
    name: Annotated[str, Query(min_length=3, max_length=50)],
):
    return {"message": f"Hello, {name}!"}


@app.get("/hello-html/", response_class=HTMLResponse, tags=["Hello"])
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


VALID_TOKENS = {
    "qwertyabc",
    "aksdfhgasdhfgaf",
    "foobar",
}


def check_token(token: str = Header(alias="x-secret-token")) -> str:
    if token in VALID_TOKENS:
        return token
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid token",
    )


@app.get(
    "/secret/",
    response_model=SecretInfo,
    responses={
        status.HTTP_401_UNAUTHORIZED: {
            "description": "Invalid token provided",
            "content": {
                "application/json": {
                    "example": {
                        "detail": "Invalid token"
                    },
                },
            },
        },
    },
)
def get_secret(
    token: Annotated[str, Depends(check_token)],
):
    return {
        "answer": 42,
        "token": token,
    }
