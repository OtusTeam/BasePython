from fastapi import APIRouter

from .users import router as router_users

router = APIRouter(
    prefix="/v2",
    tags=["V2"],
)
router.include_router(router_users)
