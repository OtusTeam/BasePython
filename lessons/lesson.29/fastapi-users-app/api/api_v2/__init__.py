from fastapi import APIRouter

from api.api_v2.views.users import router as users_router

router = APIRouter()
router.include_router(users_router)
