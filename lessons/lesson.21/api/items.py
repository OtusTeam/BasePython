from typing import Annotated

from fastapi import APIRouter, Form, status

from pydantic import PositiveInt


router = APIRouter(
    prefix="/items",
    tags=["Items"],
)


@router.get("")
def get_items():
    return {
        "data": [
            {"item_id": 1, "name": "item-1"},
            {"item_id": 2, "name": "item-2"},
            {"item_id": 3, "name": "item-3"},
        ],
    }


@router.post(
    "",
    status_code=status.HTTP_201_CREATED,
)
def create_item(
    name: Annotated[str, Form()],
):
    return {
        "data": {"item_id": 0, "name": name},
    }


@router.get("/{item_id}")
def get_item(item_id: PositiveInt):
    return {
        "data": {
            "item_id": item_id,
            "name": f"item-{item_id}",
        },
    }
