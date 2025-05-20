import logging

from fastapi import FastAPI, Request

from api import router as api_router
from config import LOG_DEFAULT_FORMAT

logging.basicConfig(
    level=logging.INFO,
    format=LOG_DEFAULT_FORMAT,
)

app = FastAPI()
app.include_router(api_router)


@app.get("/")
def read_root(request: Request):
    url = request.url.replace(path="/docs")
    return {
        "docs": str(url),
    }
