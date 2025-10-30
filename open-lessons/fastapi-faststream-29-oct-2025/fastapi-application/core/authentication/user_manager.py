import logging
from typing import Optional, TYPE_CHECKING

from fastapi_cache import FastAPICache
from fastapi_users import (
    BaseUserManager,
    IntegerIDMixin,
)
from fastapi_users.db import BaseUserDatabase

from core.config import settings
from core.fs_broker import user_registered
from core.types.user_id import UserIdType
from core.models import User
from events.schemas.user_events import UserRegistered
from mailing.send_email_confirmed import send_email_confirmed
from mailing.send_verification_email import send_verification_email
from utils.webhooks.user import send_new_user_notification

if TYPE_CHECKING:
    from fastapi import Request, BackgroundTasks
    from fastapi_users.password import PasswordHelperProtocol

log = logging.getLogger(__name__)


class UserManager(IntegerIDMixin, BaseUserManager[User, UserIdType]):
    reset_password_token_secret = settings.access_token.reset_password_token_secret
    verification_token_secret = settings.access_token.verification_token_secret

    def __init__(
        self,
        user_db: BaseUserDatabase[User, UserIdType],
        password_helper: Optional["PasswordHelperProtocol"] = None,
        background_tasks: Optional["BackgroundTasks"] = None,
    ):
        super().__init__(user_db, password_helper)
        self.background_tasks = background_tasks

    async def on_after_register(
        self,
        user: User,
        request: Optional["Request"] = None,
    ):
        if self.background_tasks:
            self.background_tasks.add_task(
                FastAPICache.clear,
                namespace=settings.cache.namespace.users_list,
            )
        else:
            await FastAPICache.clear(
                namespace=settings.cache.namespace.users_list,
            )
        log.warning(
            "User %r has registered.",
            user.id,
        )

        user_registered_event_model = UserRegistered(
            user_id=user.id,
            email=user.email,
        )
        await user_registered.publish(
            message=user_registered_event_model,
        )

        # await send_new_user_notification(user)

    async def on_after_forgot_password(
        self,
        user: User,
        token: str,
        request: Optional["Request"] = None,
    ):
        log.warning(
            "User %r has forgot their password. Reset token: %r",
            user.id,
            token,
        )

    async def on_after_request_verify(
        self,
        user: User,
        token: str,
        request: Optional["Request"] = None,
    ):
        log.warning(
            "Verification requested for user %r. Verification token: %r",
            user.id,
            token,
        )
        verification_link = request.url_for("verify_email").replace_query_params(
            token=token
        )
        self.background_tasks.add_task(
            send_verification_email,
            user=user,
            verification_link=str(verification_link),
        )

    async def on_after_verify(
        self,
        user: User,
        request: Optional["Request"] = None,
    ):
        log.warning(
            "User %r has been verified",
            user.id,
        )

        self.background_tasks.add_task(
            send_email_confirmed,
            user=user,
        )
