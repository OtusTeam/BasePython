import asyncio
import logging
from typing import Any

import aiohttp

from logging_config import configure_logging

log = logging.getLogger(__name__)


PIE_DEV_GET = "https://pie.dev/get"
PIE_DEV_UUID = "https://pie.dev/uuid"


async def fetch_api(
    url: str,
) -> dict[str, Any]:
    # return requests.get(url).json()
    # return await requests.get(url).json()

    log.info("Fetching %s", url)
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            result = await response.json()
    log.info(
        "Fetched data from %s, result: %s",
        url,
        result,
    )
    return result


# number = 123
#
# version = str(number)  # slower
# version = f"{number}"  # faster
#
# response: str | None = None
#
# response_not_none = bool(response)
# response_not_none = not not response


async def sequential_fetch():
    response_pie_dev_get = await fetch_api(PIE_DEV_GET)
    response_pie_dev_uuid = await fetch_api(PIE_DEV_UUID)

    log.info("PieDev get: %s", response_pie_dev_get)
    log.info("PieDev uuid: %s", response_pie_dev_uuid)


async def concurrent_fetch():
    async with asyncio.TaskGroup() as tg:
        task_pie_dev_get = tg.create_task(fetch_api(PIE_DEV_GET))
        task_pie_dev_uuid = tg.create_task(fetch_api(PIE_DEV_UUID))

    response_pie_dev_get = task_pie_dev_get.result()
    response_pie_dev_uuid = task_pie_dev_uuid.result()
    log.info("PieDev get: %s", response_pie_dev_get)
    log.info("PieDev uuid: %s", response_pie_dev_uuid)


async def main():
    configure_logging(level=logging.DEBUG)
    log.info("Starting")
    # await sequential_fetch()
    await concurrent_fetch()

    log.info("Finished")


if __name__ == "__main__":
    asyncio.run(main())
