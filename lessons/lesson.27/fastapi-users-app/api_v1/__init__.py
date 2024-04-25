from fastapi import APIRouter

from .views.users import router as users_router

router = APIRouter()
router.include_router(users_router)
