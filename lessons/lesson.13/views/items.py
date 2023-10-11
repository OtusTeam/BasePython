from fastapi import APIRouter, status
from pydantic import BaseModel, EmailStr

router = APIRouter(prefix="/items", tags=["Items"])


class CreateItem(BaseModel):
    name: str
    email: EmailStr


@router.get("/")
def items_list():
    return {
        "data": [
            {
                "id": 1,
                "name": "foobar",
            },
            {
                "id": 2,
                "name": "fizzbuzz",
            },
        ]
    }


@router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
    responses={
        # status.HTTP_201_CREATED: {"model": CreateItem},
    },
    # status_code=201,
)
def create_item(item: CreateItem):
    # item.name.title()
    return {
        "data": {
            "id": 0,
            **item.model_dump(),
        }
    }


@router.get("/{item_id}/")
def get_item(item_id: int):
    return {
        "data": {
            "id": item_id,
            "name": f"foobar_{item_id}"
        }
    }
