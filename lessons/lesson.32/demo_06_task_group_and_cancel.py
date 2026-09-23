import asyncio
import logging
from typing import Any

from common import configure_logging

log = logging.getLogger(__name__)


async def get_weather() -> dict:
    log.info("Getting weather data")
    # url = "https://openweathermap.org/?city=Moscow"
    # response = await httpx.get(url)
    # data = response.json()
    # return data
    # await asyncio.sleep(1.0001)
    await asyncio.sleep(0.5)
    1 / 0
    log.info("fetched weather data")
    return {"weather": {"temperature": 23}}


async def get_currencies() -> dict:
    log.info("Getting currencies data")
    # url = "https://exchange-rate.org/?from=FOO&to=BAR"
    # response = await httpx.get(url)
    # data = response.json()
    # return data
    await asyncio.sleep(1)
    log.info("fetched currencies data")
    return {"currencies": {"rate": 42}}


async def main() -> None:
    configure_logging()

    log.warning("starting")

    currencies_coro = get_currencies()
    log.info("currencies coro: %s", currencies_coro)

    try:
        async with asyncio.TaskGroup() as tg:
            weather_task = tg.create_task(get_weather())
            log.info("weather_task: %s", weather_task)
            currencies_task = tg.create_task(currencies_coro)
            log.info("currencies_task: %s", currencies_task)
    except ExceptionGroup as group:
        for exc in group.exceptions:
            log.error("failed", exc_info=exc)
        log.info(
            "weather_task: cancelled: %s %s", weather_task.cancelled(), weather_task
        )
        log.info(
            "currencies_task: cancelled: %s %s",
            currencies_task.cancelled(),
            currencies_task,
        )
        return

    log.info("exited tg")

    weather = weather_task.result()
    currencies = currencies_task.result()
    log.info("weather result %s", weather)
    log.info("currencies result %s", currencies)

    ticker_results = [t.result() for t in ticker_tasks]
    log.info("ticker results: %s", ticker_results)

    log.warning("finishing")


if __name__ == "__main__":
    asyncio.run(main())
