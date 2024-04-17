import asyncio
import logging

from common import configure_logging

log = logging.getLogger(__name__)


async def get_weather():
    log.info("Start getting weather")
    await asyncio.sleep(1)
    log.info(f"Done, got weather")


async def get_currencies():
    log.info("Start getting currencies")
    await asyncio.sleep(1)
    log.info(f"Done, got currencies")


async def main():
    configure_logging()
    log.info("Start step 1")

    coro_currencies = get_currencies()
    log.info("Coro get currencies: %s", coro_currencies)
    await get_weather()
    await coro_currencies

    log.info("End step 1")


if __name__ == "__main__":
    asyncio.run(main())
