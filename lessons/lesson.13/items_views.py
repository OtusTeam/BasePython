from fastapi import APIRouter

router = APIRouter(tags=["Items"], prefix="/items")


@router.get("")
def get_items():
    return [{"item_id": 1}, {"item_id": 2}]


@router.post("")
def create_item(data: dict):
    return {"data": data}


@router.get("/{item_id}")
def get_item(item_id: int):
    return {"item_id": item_id}
