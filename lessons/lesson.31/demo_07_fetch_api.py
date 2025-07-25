import asyncio

import logging
from pathlib import Path

import aiohttp

from common import configure_logging

NAME = Path(__file__).stem

log = logging.getLogger(__name__)

HTTPBIN_GET = "https://httpbin.org/get"
HTTPBIN_UUID = "https://httpbin.org/uuid"


async def fetch_api(
    url: str,
):
    log.info("Fetching %s", url)
    async with (
        aiohttp.ClientSession() as session,
        session.get(url) as response,
    ):
        result = await response.json()

    log.info(
        "got result from %s: %s",
        url,
        result,
    )
    return result


async def sequential_fetch():
    res_get = await fetch_api(HTTPBIN_GET)
    res_uuid = await fetch_api(HTTPBIN_UUID)
    log.info("res get: %s", res_get)
    log.info("res uuid: %s", res_uuid)

    return res_get, res_uuid


async def concurrent_fetch():

    async with asyncio.TaskGroup() as tg:
        task_get = tg.create_task(
            fetch_api(HTTPBIN_GET),
            name="httpbin-get",
        )
        task_uuid = tg.create_task(
            fetch_api(HTTPBIN_UUID),
            name="httpbin-uuid",
        )

    res_get = task_get.result()
    res_uuid = task_uuid.result()
    log.info("res get: %s", res_get)
    log.info("res uuid: %s", res_uuid)

    return res_get, res_uuid


async def main():
    configure_logging(
        level=logging.DEBUG,
    )
    log.info("Starting %s", NAME)
    # result_get, res_uuid = await sequential_fetch()
    await concurrent_fetch()

    log.info("Finishing %s", NAME)


if __name__ == "__main__":
    asyncio.run(main())
