from fastapi import APIRouter

from .authors import router as authors_router

api_v2 = APIRouter(prefix="/v2", tags=["API V2"])

api_v2.include_router(authors_router)
