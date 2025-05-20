import asyncio
import logging

import httpx

from api.api_v1.users.schemas import UserBase
from api.api_v1.users.utils.email_senders import send_email
from config import LOG_DEFAULT_FORMAT

log = logging.getLogger(__name__)


body_template = """\
Hello, {name}!

Welcome to our site!
You can do here some things.

Feel free to ask me any questions!

Best regards,
Site Admin.
"""


async def send_welcome_email(
    user: UserBase,
):
    log.info("Sending welcome email to %s", user)
    # # НИКОГДА не делаем синхронных вызовов в асинк коде!!
    # response = httpx.get(
    #     "https://httpbin.org/get",
    #     params={"foo": "bar", "spam": "eggs"},
    # )
    async with httpx.AsyncClient() as client:
        response = await client.get(
            "https://httpbin.org/get",
            params={
                "foo": "bar",
                "spam": "eggs",
                "fizz": "buzz",
            },
        )
    log.info("fetched data from api %s", response.json())
    await asyncio.sleep(5)
    subject = "Welcome to our Shop!"
    body = body_template.format(
        name=user.full_name or user.username,
    )
    await send_email(
        recipient=str(user.email),
        subject=subject,
        body=body,
    )
    log.info("Successfully sent welcome email to %s", user)


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        format=LOG_DEFAULT_FORMAT,
    )
    # noinspection PyTypeChecker
    asyncio.run(
        send_welcome_email(
            UserBase(
                username="john",
                full_name="John Smith",
                email="john.smith@email.com",
            )
        )
    )
