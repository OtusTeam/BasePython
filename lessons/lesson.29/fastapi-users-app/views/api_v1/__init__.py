from fastapi import APIRouter

from .users import router as router_users

router = APIRouter(
    prefix="/v1",
    tags=["V1"],
)
router.include_router(router_users)
