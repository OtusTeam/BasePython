from fastapi import APIRouter
from .authors.views import router as authors_router

router = APIRouter(
    prefix="/v2",
    tags=["API V2"],
)
router.include_router(authors_router)
