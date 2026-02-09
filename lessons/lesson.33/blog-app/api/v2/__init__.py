from fastapi import APIRouter

from .users.views import router as users_router

router = APIRouter(
    tags=["v2"],
    prefix="/v2",
)

router.include_router(users_router)
