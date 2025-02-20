from typing import Annotated

import uvicorn

from fastapi import FastAPI, Header, Request
from starlette.templating import Jinja2Templates

from api import router as api_router

app = FastAPI()
app.include_router(api_router)


templates = Jinja2Templates(directory="templates")


@app.get("/")
def get_root(
    request: Request,
):
    """
    Получение корня сайта.
    """
    todos = [
        "Do dishes",
        "Do the bed",
        "Vacuum",
    ]
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={"items": todos}
    )


@app.get("/me")
def get_me(
    # username: str = Header(),
    username: Annotated[str, Header()],
):
    return {"username": username}


if __name__ == "__main__":
    # uvicorn.run(app)
    uvicorn.run("main:app", reload=True)
