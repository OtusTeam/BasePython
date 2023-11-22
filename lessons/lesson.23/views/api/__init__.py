from fastapi import APIRouter
from .api_v1 import router as router_v1
from .api_v2 import router as router_v2

router = APIRouter(prefix="/api")
router.include_router(router_v1)
router.include_router(router_v2)
