import asyncio
import logging

import aiohttp

from common import configure_logging

log = logging.getLogger(__name__)


DEMO_URL = "https://pie.dev/get"


async def fetch_api(url: str) -> dict:
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if log.isEnabledFor(logging.INFO):
                log.info(
                    "Response status: %s, text: %s",
                    response.status,
                    await response.text(),
                )
            return await response.json()
            # return await response.text()
            # data = await response.json()
            # return data


async def main():
    configure_logging()
    log.info("Starting step 9 - async io http")

    result = await fetch_api(DEMO_URL)
    log.info("API response: %s", result)
    log.info("Finished main")


if __name__ == "__main__":
    asyncio.run(main())
