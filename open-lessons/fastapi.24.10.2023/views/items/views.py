from typing import Annotated
from fastapi import APIRouter, Path

from .schemas import NewItemModel

router = APIRouter(prefix="/items", tags=["Items"])


@router.post("/")
def create_item(item: NewItemModel):
    return {"item": item.model_dump()}


@router.get("/{product_id}/")
def get_item(
    product_id: Annotated[int, Path(gt=0, lt=1_000_000)],
):
    return {
        "item":
            {
                "id": product_id,
                "name": f"product_{product_id}",
            },
    }
