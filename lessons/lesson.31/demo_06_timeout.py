import asyncio
import logging

# from time import sleep

from common import configure_logging

log = logging.getLogger(__name__)


async def get_weather():
    log.info("Getting weather...")
    # await asyncio.sleep(1.05)
    await asyncio.sleep(0.05)
    # sleep(2)
    d = {}
    for num in range(7000):
        d[num] = num**num
        await asyncio.sleep(0)

    # await asyncio.sleep(1.001)
    log.info("Got weather")
    return {"weather": {"rain-chance": 42}}


async def get_currencies():
    log.info("Getting currencies...")
    await asyncio.sleep(1)
    # await asyncio.sleep(1)
    log.info("Got currencies")
    return {"currencies": {"exchange-rates": [42, 13]}}


async def get_weather_and_currencies():
    coro = get_currencies()
    log.info("created coro for currencies %s", coro)

    log.info("Get values")
    async with asyncio.timeout(1.1):
        weather_result, currencies_result, _ = await asyncio.gather(
            get_weather(),
            coro,
            get_currencies(),
        )
    log.info("weather result: %s", weather_result)
    log.info("currencies result: %s", currencies_result)


async def main():
    configure_logging()

    log.warning("Starting 06 thread")
    try:
        await get_weather_and_currencies()
    except TimeoutError:
        log.error("Could not fetch weather and currencies data in time")
    log.warning("Finished 06")


if __name__ == "__main__":
    asyncio.run(main())
