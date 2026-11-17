"""Compose resource routers under one API prefix."""

from fastapi import APIRouter

from app.routers import catalog, profile

router = APIRouter(prefix="/api")
router.include_router(catalog.router)
router.include_router(profile.router)
