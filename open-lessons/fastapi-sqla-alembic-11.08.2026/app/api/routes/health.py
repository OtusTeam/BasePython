from fastapi import APIRouter

from app.config import get_settings

router = APIRouter(tags=["service"])
settings = get_settings()


@router.get("/")
def root() -> dict[str, str]:
    return {"message": settings.app.name, "docs": "/docs", "health": "/health"}


@router.get("/health")
def health() -> dict[str, str]:
    # TODO: После реализации запросов добавить проверку БД через SELECT 1.
    return {"status": "ok", "database": "not_checked"}
