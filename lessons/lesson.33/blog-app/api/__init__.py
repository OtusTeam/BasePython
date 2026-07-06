from fastapi import APIRouter

from api.v1 import router as v1_router
from api.v2 import router as v2_router

router = APIRouter(
    prefix="/api",
)
router.include_router(v1_router)
router.include_router(v2_router)
