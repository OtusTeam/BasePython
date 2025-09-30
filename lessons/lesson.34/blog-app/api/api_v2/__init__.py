from fastapi import APIRouter
from api.api_v2.users.views import router as users_router

router = APIRouter(
    prefix="/v2",
    tags=["v2"],
)
router.include_router(users_router)
