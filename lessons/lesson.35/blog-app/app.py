import logging

from fastapi import FastAPI

from config import settings

from api import router as api_router

logging.getLogger("uvicorn.access").disabled = True

app = FastAPI(
    title=settings.app.title,
)
app.include_router(api_router)
