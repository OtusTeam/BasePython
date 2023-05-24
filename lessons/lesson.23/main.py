import uvicorn
from fastapi import FastAPI

from items_views import router as items_router
from views.users_sync import router as users_sync_router
from views.users_async import router as users_async_router

app = FastAPI(
    redoc_url=None,
)
app.include_router(
    items_router,
    prefix="/items",
    # tags=
)

app.include_router(
    users_async_router,
    prefix="/async/users",
)

app.include_router(
    users_sync_router,
    prefix="/sync/users",
)


@app.get("/")
def index():
    return {
        "message": "Index",
    }


@app.get("/hello/")
def hello(name: str = "World"):
    return {
        "message": f"Hello, {name}!",
    }


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        reload=True,
    )
