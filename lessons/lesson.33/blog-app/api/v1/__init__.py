from fastapi import APIRouter

from .users.views import router as users_router

router = APIRouter(
    tags=["v1"],
    prefix="/v1",
)

router.include_router(users_router)
