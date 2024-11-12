import asyncio
import logging
import aiohttp

from common import configure_logging

log = logging.getLogger(__name__)


async def fetch_slow_api() -> dict:
    async with aiohttp.ClientSession() as session:
        async with session.get("http://127.0.0.1:8080") as response:
            return await response.json()


async def get_weather() -> dict:
    log.info("Start getting weather")
    # await fetch_slow_api()
    await asyncio.sleep(2)
    log.info("Got weather")
    return {"weather": {"rain-chance": 50}}


async def get_currencies() -> dict:
    log.info("Start getting currencies")
    await fetch_slow_api()
    log.info("Got currencies")
    return {"currencies": {"exchange-rate": 42}}


async def async_main() -> None:
    log.info("Start main 05 task group")

    currencies_coro = get_currencies()
    log.info("get currencies coro: %s", currencies_coro)

    async with asyncio.TaskGroup() as tg:
        task_weather = tg.create_task(get_weather())
        task_currencies = tg.create_task(currencies_coro)
        log.info("all tasks set")
        log.info("wait smth else")
        await asyncio.sleep(0.5)
        log.info("smth else done")
        tg.create_task(get_currencies())
    log.info("context left")

    weather = task_weather.result()
    currencies = task_currencies.result()
    log.info("Weather result: %s", weather)
    log.info("Currencies result: %s", currencies)

    log.info("Finished main 05 task group")


def main() -> None:
    configure_logging()
    asyncio.run(async_main())


if __name__ == "__main__":
    main()
