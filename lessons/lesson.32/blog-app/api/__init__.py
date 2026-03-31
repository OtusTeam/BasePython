from fastapi import APIRouter
from api.v1.users.views import router as users_router

router = APIRouter(
    prefix="/api",
    tags=["API"],
)
router.include_router(users_router)
