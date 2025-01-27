import asyncio

import logging

from common import configure_logging

log = logging.getLogger(__name__)


async def get_weather():
    log.info("Start getting weather")
    await asyncio.sleep(1)
    log.info("Got weather")
    return {"weather": {"rain-chance": 50}}


async def get_currencies():
    log.info("Start getting currencies")
    await asyncio.sleep(1)
    log.info("Got currencies")
    return {"currencies": {"exchange-rate": 42}}


async def main() -> None:
    configure_logging()
    log.info("Starting main 02")
    weather_coro = get_weather()
    log.info("created weather coro: %s", weather_coro)
    currencies = await get_currencies()
    log.info("currencies result: %s", currencies)
    weather = await weather_coro
    log.info("weather result: %s", weather)
    log.info("Finished main 02")


if __name__ == "__main__":
    asyncio.run(main())
