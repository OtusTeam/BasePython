import logging
from uuid import uuid4

from fastapi import APIRouter, BackgroundTasks

from api.api_v1.users.schemas import UserRead, UserCreate
from api.api_v1.users.utils.welcome_email_sender import send_welcome_email

log = logging.getLogger(__name__)


router = APIRouter(
    prefix="/users",
    tags=["users"],
)


@router.post("/register")
async def register(
    user_create: UserCreate,
    background_tasks: BackgroundTasks,
) -> UserRead:
    log.info("Create new user %s", user_create)

    # мы будто бы сохранили юзера в базу
    user = UserRead(
        id=uuid4(),
        **user_create.model_dump(),
    )
    log.info("User %s created", user)
    # await send_welcome_email(user)
    background_tasks.add_task(send_welcome_email, user=user)
    return user
