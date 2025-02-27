from fastapi import FastAPI

from views import router as api_router

app = FastAPI()
app.include_router(api_router)


@app.get(
    "/",
    summary="Hello World",
)
def read_root_hello_world():
    """
    Greets the World!

    # Header 1
    ## Header 2
    ### Header 3

    ToDo List:
    - learn FastAPI
    - learn Django
    - learn SQLAlchemy

    Example:
    ```json
    {"message": "Hello World!"}
    ```
    """
    return {"message": "Hello World"}


@app.get("/hello/")
def greet_by_name(name: str):
    return {"message": f"Hello, {name}!"}
