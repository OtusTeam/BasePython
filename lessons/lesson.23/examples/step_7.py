import asyncio
import logging

from aiohttp import ClientSession

import common

log = logging.getLogger(__name__)


async def fetch_api(url: str) -> dict:
    async with ClientSession() as session:
        async with session.get(url) as response:
            data: dict = await response.json()
            return data


async def main():
    common.configure_logging()
    log.info("Starting step 7")
    # api_url = "https://pie.dev/get"
    api_url = "https://httpbin.org/get"
    result = await fetch_api(api_url)
    log.info("API response: %s", result)


if __name__ == "__main__":
    asyncio.run(main())
