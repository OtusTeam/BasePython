import asyncio
import logging

import common

log = logging.getLogger(__name__)


async def get_weather():
    log.info("Start getting weather")
    await asyncio.sleep(1)
    log.info("Done, got weather")


async def get_currencies():
    log.info("Start getting currencies")
    await asyncio.sleep(1)
    log.info("Done, got currencies")


async def main():
    common.configure_logging()
    log.info("Starting step 1")

    coro = get_weather()
    log.info("get weather coro: %s", coro)
    await get_currencies()
    await coro
    # get_currencies()


if __name__ == "__main__":
    asyncio.run(main())
