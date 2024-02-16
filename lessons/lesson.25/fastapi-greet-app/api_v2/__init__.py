from fastapi import APIRouter

from api_v2.views.users.views import router as users_router

api_v2_router = APIRouter(tags=["V2"])

api_v2_router.include_router(
    users_router,
    prefix="/users",
    tags=["Users"],
)
