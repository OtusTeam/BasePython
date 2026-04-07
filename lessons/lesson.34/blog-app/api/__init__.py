from fastapi import APIRouter
from api.v1 import router as api_v1_router
from api.v2 import router as api_v2_router

router = APIRouter(
    prefix="/api",
    tags=["API"],
)
router.include_router(api_v1_router)
router.include_router(api_v2_router)
