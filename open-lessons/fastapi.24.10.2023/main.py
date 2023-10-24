import uvicorn
from fastapi import FastAPI

from views.calc import router as calc_router
from views.items import router as items_router

app = FastAPI()
app.include_router(calc_router)
app.include_router(items_router)


@app.get("/")
def hello_index():
    return {"message": "Hello Index!"}


@app.get("/hello/")
def hello_world(name: str = "World"):
    return {"message": f"Hello {name}!"}


@app.get("/hello/{name}/")
def hello_view(name: str):
    return {"message": f"Hello {name.title()}!"}


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        # app=app,
        reload=True,
    )
    # uvicorn.run(app)
