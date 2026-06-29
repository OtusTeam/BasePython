from fastapi import APIRouter

from api.v1.users.views import router as users_router

router = APIRouter(
    prefix="/v1",
)
router.include_router(users_router)
