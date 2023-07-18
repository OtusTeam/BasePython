from fastapi import APIRouter

# assert "/hello" != "/hello/"

router = APIRouter(tags=["Items"])


@router.get("/")
def items_list():
    return {
        "data": [
            {"id": 1, "name": "foobar"},
            {"id": 2, "name": "spam-and-eggs"},
        ]
    }


@router.post("/")
def create_item(name: str, data: dict):
    return {"data": data, "name": name}


@router.get("/{item_id}/")
def get_item(item_id: int):
    return {
        "data": {
            "id": item_id,
            "name": f"item-{item_id}",
        },
    }
