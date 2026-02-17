from fastapi import FastAPI

from models import async_engine
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(_: FastAPI):
    yield
    await async_engine.dispose()
