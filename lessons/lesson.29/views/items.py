from flask import Blueprint, request

items_app = Blueprint(
    "items_app",
    __name__,
    url_prefix="/items",
)


@items_app.get("/")
def get_items_by_ids():
    # items_ids = request.args.getlist("ids", type=int)
    items_ids = request.args.getlist("ids")
    # print(request.args)
    return {
        "items": items_ids,
        "one_id": request.args.get("ids"),
    }


@items_app.get("/<int:item_id>/")
def get_item(item_id: int):
    return {
        "data": {
            "item_id": item_id,
        }
    }


@items_app.get("/<item_id>/")
def get_item_str(item_id: str):
    return {
        "string item id": item_id,
    }
