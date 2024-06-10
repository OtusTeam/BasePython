from contextlib import asynccontextmanager
from pathlib import Path

import uvicorn
from fastapi import (
    FastAPI,
    APIRouter,
)

from models.database import sqlalchemy_init
from urls import register_routes

CURRENT_FILE = Path(__file__).resolve()
PROJECT_DIR = CURRENT_FILE.parent
DB_URL = f"sqlite+aiosqlite:///{PROJECT_DIR}/db.sqlite3"


@asynccontextmanager
async def lifespan(app: FastAPI):
    await sqlalchemy_init()
    yield


router = APIRouter(prefix="/api")
register_routes(router)

app = FastAPI(lifespan=lifespan)
app.include_router(router)

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
    )
