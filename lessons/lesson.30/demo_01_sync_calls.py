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

    log.warning("Starting 01")

    await get_currencies()
    await get_weather()

    log.warning("Finished 01")


if __name__ == "__main__":
    asyncio.run(main())
