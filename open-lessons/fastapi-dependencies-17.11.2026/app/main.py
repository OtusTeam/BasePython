"""Create the application and mount the API routers."""
import logging
from logging import basicConfig

from fastapi import FastAPI

from app.routers import router

basicConfig(level=logging.INFO)

app = FastAPI(title="Book catalog · Depends", version="1.0.0")
app.include_router(router)

