from typing import Annotated
from fastapi import FastAPI, Path

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Hello World!!!"}


@app.get("/hello/")
def hello_user(name="Guest"):
    return {"message": f"Hello {name}!"}


@app.get(
    "/hello/{name}/",
    description="""\
## Greets user (pass name in path).

Actions:
- a
- b
- c

Code example: `foo.bar`
""",
)
def hello_user_path(name):
    return {"message": f"Hello {name}!!!"}


@app.get("/items/")
def get_items_list():
    return {
        "data": [
            {
                "id": 1,
                "name": "item one",
            },
            {
                "id": 2,
                "name": "item two",
            },
        ]
    }


@app.get("/items/{item_id}/")
def get_item_by_id(item_id: Annotated[int, Path(gt=0, le=999_999)]):
    return {
        "data": {
            "numerator": item_id.numerator,
            "id": item_id,
            "name": f"item {repr(item_id)}"
        }
    }
