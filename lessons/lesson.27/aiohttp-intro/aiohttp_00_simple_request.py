import asyncio
import logging

import aiohttp

from common import configure_logging

log = logging.getLogger(__name__)

HTTPBIN_URL = "https://httpbin.org/get"


async def fetch_api(url: str, params: dict | None = None) -> dict:
    async with aiohttp.ClientSession() as session:
        async with session.get(url, params=params) as response:
            return await response.json()


async def main():
    configure_logging()
    log.warning("Starting all")

    log.warning("Starting main")
    async with asyncio.TaskGroup() as tg:
        task1 = tg.create_task(fetch_api(HTTPBIN_URL))
        task2 = tg.create_task(
            fetch_api(
                HTTPBIN_URL,
                params={
                    "foo": ["bar", "baz"],
                    "spam": "eggs",
                },
            )
        )
    log.info("Fetched data (1): %s", task1.result())
    log.info("Fetched data (2): %s", task2.result())
    log.warning("Finished main")


if __name__ == "__main__":
    asyncio.run(main())
