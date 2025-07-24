import asyncio

import logging
from pathlib import Path

from common import configure_logging

NAME = Path(__file__).stem

log = logging.getLogger(__name__)


async def get_weather():
    log.info("Start getting weather")
    # имитация получения погоды
    # response = requests.get("https://openwerathermap.org/api?key=")
    # просто имитируем. точное ожидание: примерно 1с
    await asyncio.sleep(1)
    log.info("Got weather")
    return {"weather": {"rain-chance": 42}}


async def get_currencies():
    log.info("Start getting currencies")
    # просто имитируем. точное ожидание: примерно 1с
    await asyncio.sleep(1)
    log.info("Got currencies")
    return {"currencies": {"exchange-rate": 1.7}}


async def main():
    configure_logging()
    log.info("Starting %s", NAME)

    currencies_coro = get_currencies()
    log.info("currencies coro: %s", currencies_coro)
    async with asyncio.TaskGroup() as tg:
        log.info("Start task group (tg)")
        get_weather_task = tg.create_task(get_weather())
        log.info("added get weather to tg: task %s", get_weather_task)

        # log.info("start another async task")
        # await asyncio.sleep(0.5)

        get_currencies_task = tg.create_task(currencies_coro)
        log.info("added get currencies to tg: task %s", get_currencies_task)

        log.info("start another async task")
        await asyncio.sleep(0.5)

        log.info("finishing tg")

    log.info("left tg context")

    weather = get_weather_task.result()
    currencies = get_currencies_task.result()
    log.info("Weather result: %s", weather)
    log.info("Currencies result: %s", currencies)

    log.info("Finishing %s", NAME)


if __name__ == "__main__":
    asyncio.run(main())
