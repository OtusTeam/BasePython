from fastapi import APIRouter

from .books import router as books_router

router = APIRouter(
    tags=["v1"],
    prefix="/v1",
)
router.include_router(books_router)
