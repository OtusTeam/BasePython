import asyncio
import logging

import common

log = logging.getLogger(__name__)


async def get_weather():
    log.info("Start getting weather")
    await asyncio.sleep(1)
    log.info("Done, got weather")
    return {"weather": {}}


async def get_currencies():
    log.info("Start getting currencies")
    await asyncio.sleep(1)
    log.info("Done, got currencies")
    return {"currencies": [1, 2, 3]}


async def main():
    common.configure_logging()
    log.info("Starting step 2")

    coro = get_weather()
    log.info("get weather coro: %s", coro)
    log.info("currencies result: %s", await get_currencies())
    weather_result = await coro
    log.info("weather result: %s", weather_result)


if __name__ == "__main__":
    asyncio.run(main())
