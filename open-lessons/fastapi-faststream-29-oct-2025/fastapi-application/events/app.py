import logging

from faststream import FastStream

from core.config import settings
from core.fs_broker import broker
from events.subscribers.user_registered import router as user_registered_router
from events.subscribers.user_statistics import router as user_statistics_router

app = FastStream(broker)

broker.include_routers(
    user_registered_router,
    user_statistics_router,
)

log = logging.getLogger(__name__)


@app.on_startup
def configure_logging() -> None:
    logging.basicConfig(
        level=settings.logging.log_level_value,
        format=settings.logging.log_format,
        datefmt=settings.logging.log_date_format,
    )
    log.warning("Logging configured")
