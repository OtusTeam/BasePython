from fastapi import FastAPI

from api_v1 import api_v1_router
from api_v2 import api_v2_router
from config import API_V1_PREFIX, API_V2_PREFIX


app = FastAPI()
app.include_router(
    api_v1_router,
    prefix=API_V1_PREFIX,
)
app.include_router(
    api_v2_router,
    prefix=API_V2_PREFIX,
)

# main_app.mount(app_v1)


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
