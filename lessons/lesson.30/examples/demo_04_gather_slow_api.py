import asyncio
import logging
import aiohttp

from common import configure_logging

log = logging.getLogger(__name__)


async def fetch_slow_api() -> dict:
    # session = aiohttp.ClientSession()
    # ...
    # await session.close()

    async with aiohttp.ClientSession() as session:
        async with session.get("http://127.0.0.1:8080") as response:
            return await response.json()


async def get_weather() -> dict:
    log.info("Start getting weather")
    await fetch_slow_api()
    log.info("Got weather")
    return {"weather": {"rain-chance": 50}}


async def get_currencies() -> dict:
    log.info("Start getting currencies")
    await fetch_slow_api()
    log.info("Got currencies")
    return {"currencies": {"exchange-rate": 42}}


async def async_main() -> None:
    log.info("Start main 04 slow api")

    currencies_coro = get_currencies()
    log.info("get currencies coro: %s", currencies_coro)

    coro = asyncio.gather(
        get_weather(),
        currencies_coro,
    )
    log.info("coro gather: %s", coro)
    weather, currencies = await coro
    # await get_currencies()

    log.info("Weather result: %s", weather)
    log.info("Currencies result: %s", currencies)

    log.info("Finished main 04 slow api")


def main() -> None:
    configure_logging()
    asyncio.run(async_main())


if __name__ == "__main__":
    main()
