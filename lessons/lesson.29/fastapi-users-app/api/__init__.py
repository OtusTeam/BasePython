from fastapi import APIRouter
from api.api_v1 import router as api_v1_router
from api.api_v2 import router as api_v2_router

router = APIRouter(prefix="/api")
router.include_router(api_v1_router, prefix="/v1", tags=["V1"])
router.include_router(api_v2_router, prefix="/v2", tags=["V2"])
