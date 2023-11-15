import asyncio
import logging
from aiohttp import ClientSession

from common import configure_logging

log = logging.getLogger(__name__)


async def fetch_api(url: str) -> dict:
    async with ClientSession() as session:
        async with session.get(url) as response:
            data: dict = await response.json()
            return data


async def main():
    configure_logging()

    log.info("Start main")

    result = await fetch_api("https://httpbin.org/get")
    log.info("got result %s", result)
    log.info("Finish main")


if __name__ == "__main__":
    asyncio.run(main())
