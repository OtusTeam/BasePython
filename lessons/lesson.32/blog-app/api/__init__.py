from fastapi import APIRouter

from api.api_v1 import router as api_v1

router = APIRouter(prefix="/api", tags=["API"])

router.include_router(api_v1)
