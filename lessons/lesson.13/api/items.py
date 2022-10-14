from fastapi import APIRouter

router = APIRouter(
    prefix="/items",
    tags=["Items"],
)


@router.get("")
def get_items():
    return {
        "data": [
            {
                "id": 1,
                "value": "qwerty",
            },
            {
                "id": 2,
                "value": "wasd",
            },
        ]
    }


@router.get("/{item_id}")
def get_item(item_id: int):
    # a: int = "2"
    # assert isinstance(a, str)
    return {
        "item": {"id": item_id},
    }


@router.post("")
def create_item(data: dict):
    return {
        "item": data,
    }
