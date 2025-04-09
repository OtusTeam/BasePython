from typing import Annotated
from fastapi import (
    APIRouter,
    Path,
)

router = APIRouter(
    prefix="/items",
    tags=["items"],
)


@router.get("/")
def get_items():
    return {
        "data": [
            {"id": 1, "name": "qwerty"},
            {"id": 2, "name": "foobar"},
        ],
    }


@router.get("/{item_id}/")
def get_item(
    # item_id: Annotated[int, Ge(1), Lt(100_000)],
    item_id: Annotated[int, Path(ge=1, lt=100_000)],
):
    # get_item_from_db(item_id)
    return {
        "data": {"id": item_id, "name": "abc"},
    }
