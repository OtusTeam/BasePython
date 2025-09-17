import asyncio
import logging
from pathlib import Path
from typing import Any

import aiohttp

from common import configure_logging


NAME = Path(__file__).stem

log = logging.getLogger(__name__)


PIE_DEV_GET = "https://pie.dev/get"
# PIE_DEV_GET = "https://httpbin.org/get"
PIE_DEV_UUID = "https://pie.dev/uuid"
# PIE_DEV_UUID = "https://httpbin.org/uuid"


async def fetch_api(
    url: str,
) -> dict[str, Any]:
    log.info("fetching %s", url)
    async with (
        aiohttp.ClientSession() as session,
        session.get(url) as response,
    ):
        result = await response.json()

    log.info(
        "got result from url %s: %s",
        url,
        result,
    )
    return result


async def sequential_fetch():
    res_get = await fetch_api(PIE_DEV_GET)
    res_uuid = await fetch_api(PIE_DEV_UUID)
    log.info("res get: %s", res_get)
    log.info("res uuid: %s", res_uuid)

    return res_get, res_uuid


async def concurrent_fetch():
    async with asyncio.TaskGroup() as tg:
        task_get = tg.create_task(
            fetch_api(PIE_DEV_GET),
            name="pie-dev-get",
        )
        task_uuid = tg.create_task(
            fetch_api(PIE_DEV_UUID),
            name="pie-dev-uuid",
        )

    res_get = task_get.result()
    res_uuid = task_uuid.result()
    log.info("res get: %s", res_get)
    log.info("res uuid: %s", res_uuid)
    return res_get, res_uuid


async def main() -> None:
    configure_logging()
    log.info("Starting %s", NAME)

    # data_get, data_uuid = await sequential_fetch()
    data_get, data_uuid = await concurrent_fetch()
    log.info("got results: %s; %s", data_get, data_uuid)

    log.info("Finishing %s", NAME)


if __name__ == "__main__":
    asyncio.run(main())
