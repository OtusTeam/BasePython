from fastapi import APIRouter

from api.api_v1.views.hello import router as hello_router
from api.api_v1.views.items import router as items_router
from api.api_v1.views.secret_views import router as secret_router
from api.api_v1.views.users import router as users_router


router = APIRouter()
router.include_router(hello_router)
router.include_router(items_router)
router.include_router(secret_router)
router.include_router(users_router)
