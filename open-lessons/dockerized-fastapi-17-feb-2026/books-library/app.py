from fastapi import FastAPI
from api import router as api_router
from app_lifespan import lifespan

from config.settings import settings

app = FastAPI(
    title=settings.app.title,
    lifespan=lifespan,
)
app.include_router(api_router)
