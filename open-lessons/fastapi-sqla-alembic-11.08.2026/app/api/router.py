from fastapi import APIRouter

from app.api.routes import authors
from app.api.routes import books
from app.api.routes import health
from app.config import get_settings

router = APIRouter()
api_router = APIRouter(prefix=get_settings().app.api_v1_prefix)
router.include_router(health.router)
router.include_router(api_router)

api_router.include_router(authors.router)
api_router.include_router(books.router)
