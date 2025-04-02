import asyncio
import logging

from common import configure_logging

log = logging.getLogger(__name__)


async def get_weather():
    log.info("Getting weather...")
    await asyncio.sleep(1)
    log.info("Got weather")
    return {"weather": {"rain-chance": 42}}


async def get_currencies():
    log.info("Getting currencies...")
    await asyncio.sleep(1)
    log.info("Got currencies")
    return {"currencies": {"exchange-rates": [42, 13]}}


async def main():
    configure_logging()

    log.warning("Starting 02")

    coro = get_currencies()
    log.info("created coro for currencies %s", coro)

    log.info("Wait for get weather")
    weather_result = await get_weather()
    log.info("weather result: %s", weather_result)

    log.info("Wait for currencies coro %s", coro)
    currencies_result = await coro
    log.info("currencies result: %s", currencies_result)

    log.warning("Finished 02")


if __name__ == "__main__":
    asyncio.run(main())
