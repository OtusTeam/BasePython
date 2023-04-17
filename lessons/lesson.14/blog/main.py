import uvicorn
from fastapi import FastAPI

from items_views import router as items_router
from users.views import router as users_router

app = FastAPI(
    redoc_url=None,
)
app.include_router(
    items_router,
    prefix="/items",
    # tags=
)
app.include_router(
    users_router,
    prefix="/users",
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


if __name__ == '__main__':
    uvicorn.run(
        "main:app",
        reload=True,
    )
