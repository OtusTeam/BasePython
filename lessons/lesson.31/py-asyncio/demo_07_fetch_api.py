import asyncio
import logging
from typing import Any

import aiohttp

from common import configure_logging

log = logging.getLogger(__name__)

HTTPBIN_GET = "https://httpbin.org/get"
HTTPBIN_UUID = "https://httpbin.org/uuid"


async def fetch_api(url: str) -> Any:
    log.info("Fetching %s", url)
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            result = await response.json()
    log.info("got result from %s: %s", url, result)
    return result


async def sequential_fetch():
    result_api = await fetch_api(HTTPBIN_GET)
    result_uuid = await fetch_api(HTTPBIN_UUID)
    return result_api, result_uuid


async def async_fetch():

    async with asyncio.TaskGroup() as tg:
        fetch_api_task = tg.create_task(fetch_api(HTTPBIN_GET))
        fetch_uuid_task = tg.create_task(fetch_api(HTTPBIN_UUID))
    return fetch_api_task.result(), fetch_uuid_task.result()


async def main() -> None:
    configure_logging()
    log.info("Starting 07")

    # api_result, get_result = await sequential_fetch()
    api_result, get_result = await async_fetch()
    log.info("Response API %s", api_result)
    log.info("Response UUID %s", get_result)

    log.info("Finished 07")


if __name__ == "__main__":
    asyncio.run(main())
