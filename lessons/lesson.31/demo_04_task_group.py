import asyncio
import logging
from pathlib import Path

from common import configure_logging


NAME = Path(__file__).stem

log = logging.getLogger(__name__)


async def get_weather():
    log.info("Start getting weather")
    # имитируем отправку настоящего запроса и ожидание ответа
    await asyncio.sleep(1)
    data = {"weather": {"rain-chance": 70}}
    log.info("Got weather")
    return data


async def get_currencies():
    log.info("Start getting currencies")
    # имитируем отправку настоящего запроса и ожидание ответа
    await asyncio.sleep(1)
    data = {"currencies": {"exchange-rate": 1.5}}
    log.info("Got currencies")
    return data


async def main() -> None:
    configure_logging()
    log.info("Starting %s", NAME)

    currencies_coro = get_currencies()
    log.info("currencies coro: %s", currencies_coro)

    async with asyncio.TaskGroup() as tg:
        log.info("Starting task group (tg)")
        get_weather_task = tg.create_task(get_weather())
        log.info("added get weather task to tg. task: %s", get_weather_task)

        log.info("start +0.5 async task")
        await asyncio.sleep(0.5)

        get_currencies_task = tg.create_task(currencies_coro)
        log.info("added get currencies task to tg. task: %s", get_currencies_task)

        # log.info("wait for something small")
        # await asyncio.sleep(0.5)
        # log.info("done waiting for something small")
    log.info("task group done.")

    weather = get_weather_task.result()
    currencies = get_currencies_task.result()

    log.info("Weather result: %s", weather)
    log.info("Currencies result: %s", currencies)

    log.info("Finishing %s", NAME)


if __name__ == "__main__":
    asyncio.run(main())
