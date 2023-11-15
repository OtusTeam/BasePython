import asyncio
import logging

from common import configure_logging

log = logging.getLogger(__name__)


async def get_weather():
    log.info("Start get weather")
    await asyncio.sleep(1.0001)
    log.info("Done, got weather")
    return {"weather": {}}


async def get_currencies():
    log.info("Start get currencies")
    await asyncio.sleep(1)
    log.info("Done, got currencies")
    return {"currencies": [1, 2, 3]}


async def main():
    configure_logging()

    log.info("Start main")
    weather_coro = get_weather()

    async with asyncio.TaskGroup() as tg:
        task_weather = tg.create_task(weather_coro, name="get-weather")
        log.info("task_weather: %s", task_weather)
        task_currencies = tg.create_task(get_currencies(), name="get-currencies")

    log.info("result weather: %s", task_weather.result())
    log.info("result currencies: %s", task_currencies.result())
    log.info("Finish main")


if __name__ == "__main__":
    asyncio.run(main())
