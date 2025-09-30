from fastapi import APIRouter
from api.api_v1.users.views import router as users_router

router = APIRouter(
    prefix="/v1",
    tags=["v1"],
)
router.include_router(users_router)
