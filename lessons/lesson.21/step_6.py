import random
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
    log.info("start main")
    result_httpbin = await fetch_api("https://httpbin.org/get")
    log.info("httpbin response: %s", result_httpbin)
    log.info("finish main")


def run_main():
    configure_logging()
    asyncio.run(main())


if __name__ == '__main__':
    run_main()
