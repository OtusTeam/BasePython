from flask import Blueprint

items_app = Blueprint(
    "items_app",
    __name__,
    url_prefix="/items",
)


@items_app.route("/")
def get_items():
    return {
        "items": ["a", "b"],
    }


@items_app.route("/<int:item_id>/")
def get_item_by_id(item_id):
    val = 42
    res = val / item_id
    print("res:", res)
    return {
        "data": {
            "item_id": item_id,
            "res": res,
        }
    }
