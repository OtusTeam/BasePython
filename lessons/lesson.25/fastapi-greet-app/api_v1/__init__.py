from fastapi import APIRouter

from api_v1.views.items import router as items_router
from api_v1.views.users.views import router as users_router

api_v1_router = APIRouter(tags=["V1"])


api_v1_router.include_router(
    items_router,
    prefix="/items",
    tags=["Items"],
)

api_v1_router.include_router(
    users_router,
    prefix="/users",
    tags=["Users"],
)
