import logging

from typing import Annotated

from faststream import Depends
from faststream.rabbit import RabbitRouter
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import (
    db_helper,
    User,
)

from core.config import settings
from events.schemas.user_events import UserRegistered
from mailing.send_email import send_email


router = RabbitRouter()

log = logging.getLogger(__name__)


@router.subscriber(
    queue=settings.rabbitmq.queues.queue_name,
    exchange=settings.rabbitmq.queues.exchange_name,
)
async def send_welcome_email_to_registered_user(
    user_info: UserRegistered,
    session: Annotated[
        "AsyncSession",
        Depends(db_helper.session_getter),
    ],
):
    log.info(
        "Process registered user %s",
        user_info,
    )
    await send_email(
        user_info.email,
        "Welcome to our site!",
        "Hello there!",
        "<b>Hello there!</b>",
    )
    user: User | None = await session.get(User, user_info.user_id)
    if user:
        log.info("User details: %s", user)
