import asyncio

import logging
from typing import Any

import aiohttp

from common import configure_logging

log = logging.getLogger(__name__)


HTTPBIN_URL_GET = "https://httpbin.org/get"
HTTPBIN_URL_UUID = "https://httpbin.org/uuid"


async def fetch_api(url: str) -> dict[str, Any]:
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.json()


async def fetch_httpbin_get() -> None:
    data = await fetch_api(HTTPBIN_URL_GET)
    log.info("Fetched data: %s", data)


async def fetch_httpbin_uuid() -> str:
    data = await fetch_api(HTTPBIN_URL_UUID)
    log.info("Fetched data: %s", data)
    return data["uuid"]


async def main() -> None:
    configure_logging()
    log.info("Starting main 07")
    async with asyncio.TaskGroup() as tg:
        tg.create_task(fetch_httpbin_get())
        tg.create_task(fetch_httpbin_uuid())
    # await fetch_httpbin_get()
    # await fetch_httpbin_uuid()
    log.info("Finished main 07")


if __name__ == "__main__":
    asyncio.run(main())
