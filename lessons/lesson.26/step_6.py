import asyncio
import logging

from common import configure_logging

log = logging.getLogger(__name__)


async def get_weather():
    log.info("Start getting weather data")
    await asyncio.sleep(1)
    log.info("Done, got weather")
    return {"weather": {}}


async def get_currencies():
    log.info("Start getting currencies data")
    await asyncio.sleep(1)
    log.info("Done, got currencies")
    return {"currencies": [1, 2, 3]}


async def main():
    configure_logging()
    log.info("Starting step 6 - Task Group")

    coro_currencies = get_currencies()
    log.info(
        "%r coro: %s",
        coro_currencies.__name__,
        coro_currencies,
    )
    async with asyncio.TaskGroup() as tg:
        task_weather = tg.create_task(get_weather(), name="get-weather")
        task_currencies = tg.create_task(coro_currencies, name="get-currencies")

    weather_result = task_weather.result()
    currencies_result = task_currencies.result()
    log.info(
        "Weather result (task: %r): %s",
        task_weather.get_name(),
        weather_result,
    )
    log.info(
        "Currencies result (task: %r): %s",
        task_currencies.get_name(),
        currencies_result,
    )

    log.info("Finished main")


if __name__ == "__main__":
    asyncio.run(main())
