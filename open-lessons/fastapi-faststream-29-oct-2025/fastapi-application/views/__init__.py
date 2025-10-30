from fastapi import APIRouter
from views.home import router as home_router
from views.verification import router as verification_router

router = APIRouter()
router.include_router(home_router)
router.include_router(verification_router)
