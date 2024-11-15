from fastapi import APIRouter

from views.api_v1 import api_v1

api_router = APIRouter(
    prefix="/api",
)
api_router.include_router(api_v1)
