import asyncio
import logging

from common import configure_logging

log = logging.getLogger(__name__)


async def get_weather():
    log.info("Start getting weather")
    await asyncio.sleep(1)
    log.info("Got weather")
    return {"weather": {"rain_chance": 20}}


async def get_currencies():
    log.info("Start getting currencies")
    await asyncio.sleep(1)
    log.info("Got currencies")
    return {"currencies": {"exchange-rate": 42}}


async def main() -> None:
    configure_logging()
    log.info("Starting 01")

    weather = await get_weather()
    log.info("weather result: %s", weather)
    currencies = await get_currencies()
    log.info("currencies result: %s", currencies)

    log.info("Finished 01")


if __name__ == "__main__":
    asyncio.run(main())
