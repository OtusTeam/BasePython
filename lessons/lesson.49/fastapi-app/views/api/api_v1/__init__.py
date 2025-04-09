from fastapi import APIRouter
from .authors.views import router as authors_router

router = APIRouter(
    prefix="/v1",
    tags=["API V1"],
)
router.include_router(authors_router)
