from flask import Blueprint
from flask import render_template

items_app = Blueprint(
    "items_app",
    __name__,
    url_prefix="/foobar/items",
)


@items_app.get("/", endpoint="list")
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


@items_app.get("/<int:item_id>/", endpoint="details")
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


@items_app.get("/next-item/", endpoint="next-item")
def get_next_item_page():
    return render_template("items/next-item.html")
