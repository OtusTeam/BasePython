"""
Asyncio =
asynchronous input / output

input / output examples:
- Network calls: API, RPC, Database
- Files, Filesystem
"""

import asyncio
import logging

from common import configure_logging

log = logging.getLogger(__name__)


async def get_weather() -> dict:
    log.info("Start getting weather")
    await asyncio.sleep(1)
    log.info("Got weather")
    return {"weather": {"rain-chance": 50}}


async def get_currencies() -> dict:
    log.info("Start getting currencies")
    await asyncio.sleep(1)
    log.info("Got currencies")
    return {"currencies": {"exchange-rate": 42}}


async def async_main() -> None:
    log.info("Start main 01")
    weather = await get_weather()
    log.info("Weather result: %s", weather)
    currencies = await get_currencies()
    log.info("Currencies result: %s", currencies)
    log.info("Finished main 01")


def main() -> None:
    configure_logging()
    asyncio.run(async_main())


if __name__ == "__main__":
    main()
