from fastapi import APIRouter

from .views.users import router as users_router


router = APIRouter(prefix="/v2")
router.include_router(users_router)
