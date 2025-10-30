import logging
from typing import Annotated, Literal

from fastapi import APIRouter
from fastapi import Depends
from faststream.rabbit.message import RabbitMessage
from pydantic import PositiveInt

from core.authentication.fastapi_users import (
    current_active_user,
    current_active_superuser,
)
from core.config import settings
from core.fs_broker import user_statistics
from core.models import User
from core.schemas.user import UserRead
from events.schemas.user_events import UserStatisticsResponse, UserStatisticsRequest

log = logging.getLogger(__name__)
router = APIRouter(
    prefix=settings.api.v1.messages,
    tags=["Messages"],
)


@router.get("/error")
def view_may_raise_error(
    raise_error: bool = False,
):
    if raise_error:
        # 1 / 0
        UserRead.model_validate(None)
    return {"ok": True}


@router.get("")
def get_user_messages(
    user: Annotated[
        User,
        Depends(current_active_user),
    ],
):
    return {
        "messages": ["m1", "m2", "m3"],
        "user": UserRead.model_validate(user),
    }


@router.get("/secrets")
def get_superuser_messages(
    user: Annotated[
        User,
        Depends(current_active_superuser),
    ],
):
    return {
        "messages": ["secret-m1", "secret-m2", "secret-m3"],
        "user": UserRead.model_validate(user),
    }


@router.get("/stats")
async def get_users_stats(
    user_id: PositiveInt,
    kind: Literal["fizz", "buzz"] = "fizz",
):
    request = UserStatisticsRequest(
        user_id=user_id,
        kind=kind,
    )

    response: RabbitMessage = await user_statistics.request(
        request,
        timeout=10,
    )
    log.info("Got response from user statistics request: %s", response)
    body = UserStatisticsResponse.model_validate_json(response.body)
    log.info("Got response model: %s", body)
    # return body.model_dump(mode="json")
    return body
