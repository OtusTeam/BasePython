import asyncio
import logging
from pathlib import Path
from typing import Any

import aiohttp

from common import configure_logging

NAME = Path(__file__).stem
log = logging.getLogger(NAME)

# получить ответ от API по url

PIE_DEV_GET = "https://pie.dev/get"
PIE_DEV_UUID = "https://pie.dev/uuid"


async def fetch_api(url: str) -> dict[str, Any]:
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            return await resp.json()


# получить ответ от API по очереди
async def sequential_fetch():
    response_pie_dev_get = await fetch_api(PIE_DEV_GET)
    response_pie_dev_uuid = await fetch_api(PIE_DEV_UUID)

    log.info("res get: %s", response_pie_dev_get)
    log.info("res uuid: %s", response_pie_dev_uuid)


# получить ответ от API конкурентно
async def concurrent_fetch():

    # response_pie_dev_get, response_pie_dev_uuid = await asyncio.gather(
    #     fetch_api(PIE_DEV_GET),
    #     fetch_api(PIE_DEV_UUID),
    # )

    async with asyncio.TaskGroup() as tg:
        response_pie_dev_get_task = tg.create_task(fetch_api(PIE_DEV_GET))
        response_pie_dev_uuid_task = tg.create_task(fetch_api(PIE_DEV_UUID))

    response_pie_dev_get = response_pie_dev_get_task.result()
    response_pie_dev_uuid = response_pie_dev_uuid_task.result()

    log.info("res get: %s", response_pie_dev_get)
    log.info("res uuid: %s", response_pie_dev_uuid)


async def main() -> None:
    configure_logging()
    log.info("Starting")

    # await sequential_fetch()
    await concurrent_fetch()

    log.info("Finishing")


if __name__ == "__main__":
    asyncio.run(main())
