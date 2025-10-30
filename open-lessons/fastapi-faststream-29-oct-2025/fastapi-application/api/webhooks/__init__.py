from fastapi import APIRouter

from .user import router as user_router

webhooks_router = APIRouter()
webhooks_router.include_router(user_router)
