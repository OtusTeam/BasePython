from fastapi import APIRouter

from api.hello import router as hello_router
from api.numbers import router as numbers_router
from api.items import router as items_router
from api.movies import router as movies_router
from api.users.views import router as users_router

router = APIRouter(
    prefix="/api",
    tags=["API"],
)
router.include_router(hello_router)
router.include_router(numbers_router)
router.include_router(items_router)
router.include_router(movies_router)
router.include_router(users_router)
