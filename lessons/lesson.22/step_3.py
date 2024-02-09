"""
asyncio gather example
"""

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
    await asyncio.sleep(1.2)
    log.info("Done, got currencies")
    return {"currencies": [1, 2, 3]}


async def main():
    common.configure_logging()
    log.info("Starting step 3")

    coro = get_weather()
    res = await asyncio.gather(
        coro,
        get_currencies(),
    )
    # weather_result = res[0]
    # currencies_result = res[1]
    weather_result, currencies_result = res
    log.info("Result: %s", res)
    log.info("Weather result: %s", weather_result)
    log.info("Currencies result: %s", currencies_result)
    log.info("Done")


if __name__ == "__main__":
    asyncio.run(main())
