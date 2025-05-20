import asyncio
from email.message import EmailMessage

import aiosmtplib

from config import ADMIN_EMAIL


async def send_email(
    recipient: str,
    subject: str,
    body: str,
):
    message = EmailMessage()
    message["Subject"] = subject
    message["From"] = ADMIN_EMAIL
    message["To"] = recipient
    message.set_content(body)

    await aiosmtplib.send(
        message,
        sender=ADMIN_EMAIL,
        recipients=[recipient],
        hostname="localhost",
        port=1025,
    )


if __name__ == "__main__":
    asyncio.run(
        send_email(
            "rec@a.b",
            "hello",
            "first line\n\nanother line",
        ),
    )
