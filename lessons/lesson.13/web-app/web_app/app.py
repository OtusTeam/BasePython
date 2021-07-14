from fastapi import FastAPI


app = FastAPI()


@app.get("/", summary="Get a hello world json")
def hello(
    name: str = "World",
):
    """
    Hello world!
    1. processes `request`
    1. returns greeting
    """

    return {"Hello": name}
