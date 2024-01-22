from fastapi import FastAPI

from views.items import router as items_router
from views.users.views import router as users_router

app = FastAPI()
app.include_router(
    items_router,
    prefix="/items",
    tags=["Items"],
)
app.include_router(
    users_router,
    prefix="/users",
    tags=["Users"],
)


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
