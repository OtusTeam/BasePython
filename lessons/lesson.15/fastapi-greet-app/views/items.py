from typing import Annotated

from fastapi import Path, APIRouter


router = APIRouter()


@router.get("/")
def get_items_list():
    return {
        "data": [
            {
                "id": 1,
                "name": "item one",
            },
            {
                "id": 2,
                "name": "item two",
            },
        ]
    }


@router.get("/{item_id}/")
def get_item_by_id(item_id: Annotated[int, Path(gt=0, le=999_999)]):
    return {
        "data": {
            "numerator": item_id.numerator,
            "id": item_id,
            "name": f"item {repr(item_id)}"
        }
    }
