from fastapi import APIRouter

from views.api_v1 import api_v1
from views.api_v2 import api_v2

api_router = APIRouter(
    prefix="/api",
)
api_router.include_router(api_v1)
api_router.include_router(api_v2)
