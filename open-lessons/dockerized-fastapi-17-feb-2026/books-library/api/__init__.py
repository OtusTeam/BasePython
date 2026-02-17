from fastapi import APIRouter

from .v1 import router as v1_router

router = APIRouter(
    tags=["api"],
    prefix="/api",
)
router.include_router(v1_router)
