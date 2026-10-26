from fastapi import FastAPI

from bookshelf.books.router import router
from bookshelf.config.settings import Settings
from bookshelf.config.settings import settings as default_settings
from bookshelf.core.http_errors import install_error_handlers
from bookshelf.lifespan import lifespan


def create_app(settings: Settings | None = None) -> FastAPI:
    settings = settings or default_settings
    application = FastAPI(title=settings.app.title, lifespan=lifespan)
    application.state.settings = settings
    install_error_handlers(application)
    application.include_router(router)

    @application.get(
        "/health",
        tags=["operations"],
        name="health",
    )
    def health() -> dict[str, str]:
        return {"status": "ok"}

    return application


app = create_app()
