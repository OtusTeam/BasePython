from fastapi import APIRouter

from .v1 import router as router_v1
from .v2 import router as router_v2

router = APIRouter(
    tags=["API"],
    prefix="/api",
)

router.include_router(router_v1)
router.include_router(router_v2)
