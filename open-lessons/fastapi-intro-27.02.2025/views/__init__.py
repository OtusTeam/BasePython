from fastapi import APIRouter

from .movies.views import router as movies_router

router = APIRouter(
    prefix="/api",
    tags=["API"],
)

router.include_router(movies_router)
