from fastapi import FastAPI, Query

app = FastAPI()


@app.get(
    "/items/{item_id}", summary="Read an item", description="Retrieve an item by its ID"
)
async def read_item(
    item_id: int,
    q: str = Query(
        'Nothing do not write',
        title="Query string",
        description="Query string for the items",
    ),
):
    return {"item_id": item_id, "q": q}
