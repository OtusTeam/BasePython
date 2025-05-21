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
    log.info("Starting 04")

    currencies_coro = get_currencies()
    log.info("created currencies coro: %s", currencies_coro)

    async with asyncio.TaskGroup() as tg:
        get_weather_task = tg.create_task(
            get_weather(),
        )
        log.info("get weather task: %s", get_weather_task)
        get_currencies_task = tg.create_task(
            currencies_coro,
        )
        log.info("get weather task (still insidde): %s", get_weather_task)
        await asyncio.sleep(0.5)
        # data = await get_data()
        # tg.create_task(process_data(data))

    log.info("get weather task (after): %s", get_weather_task)

    log.info("weather result: %s", get_weather_task.result())
    log.info("currencies result: %s", get_currencies_task.result())

    log.info("Finished 04")


if __name__ == "__main__":
    asyncio.run(main())
