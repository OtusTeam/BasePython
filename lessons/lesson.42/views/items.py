from flask import Blueprint

items_app = Blueprint(
    "items_app",
    __name__,
    url_prefix="/foobar/items",
)


@items_app.get("/")
def items_list():
    return {
        "data": [
            {
                "id": 1,
                "name": "abc",
            },
            {
                "id": 2,
                "name": "qwe",
            },
        ]
    }


@items_app.get("/<int:item_id>/")
def item_details(item_id: int):
    return {
        "data": {
            "id": item_id,
            "name": "single",
        }
    }


@items_app.post("/")
def create_item():
    return {

    }
