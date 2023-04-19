"""
items
"""
from flask import Blueprint

items_app = Blueprint(
    "items_app",
    __name__,
    url_prefix="/items",
)


@items_app.get("/")
def get_items_list():
    """
    get items list
    :return:
    """
    return {
        "data": [
            {
                "id": 1,
                "name": "I1",
            },
            {
                "id": 2,
                "name": "I2",
            },
        ],
    }


# @items_app.get("/<int:item_id>/")
# def get_item_by_id_int(item_id: int):
#     return {
#         "data": {
#             "id": item_id,
#             "name": f"I{item_id}",
#             "comment": "integer id",
#         },
#     }


@items_app.get("/<int:item_id>/")
@items_app.get("/<string:item_id>/")
def get_item_by_id_str(item_id: str):
    """
    get item by id str
    :param item_id:
    :return:
    """
    return {
        "data": {
            # "id": item_id.upper(),
            "id": item_id,
            "name": f"I{item_id}",
            "comment": "some id",
            "type": str(type(item_id)),
        },
    }
