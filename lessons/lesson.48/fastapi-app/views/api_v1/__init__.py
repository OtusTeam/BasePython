from fastapi import APIRouter

from views.api_v1.hello import router as hello_router
from views.api_v1.items import router as items_router
from views.api_v1.secret_views import router as secret_router
from views.api_v1.users import router as users_router
from views.api_v1.authors import router as authors_router

api_v1 = APIRouter(prefix="/v1", tags=["API V1"])

api_v1.include_router(authors_router)
api_v1.include_router(users_router)
api_v1.include_router(hello_router)
api_v1.include_router(items_router)
api_v1.include_router(secret_router)
