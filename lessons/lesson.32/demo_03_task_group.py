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
    await asyncio.sleep(1.0001)
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


async def get_user_preferences(name: str) -> dict[str, Any]:
    log.info("get user %s preferences", name)
    await asyncio.sleep(0.5)
    log.info("fetched user %s preferences", name)
    return {"tickers": ["foo", "bar"]}


async def get_market_rate(ticker: str) -> dict[str, Any]:
    log.info("getting market rate for %r", ticker)
    await asyncio.sleep(0.5)
    log.info("fetched market rate for %r", ticker)
    return {
        "value": 42,
        "ticker": ticker,
    }


async def main() -> None:
    configure_logging()

    log.warning("starting")

    currencies_coro = get_currencies()
    log.info("currencies coro: %s", currencies_coro)

    async with asyncio.TaskGroup() as tg:
        weather_task = tg.create_task(get_weather())
        log.info("weather_task: %s", weather_task)
        currencies_task = tg.create_task(currencies_coro)
        log.info("currencies_task: %s", currencies_task)
        preferences = await get_user_preferences("bob")
        log.info("preferences: %s", preferences)
        # res = await weather_task
        # log.info("weather_task res: %s", res)
        ticker_tasks = []
        for ticker in preferences["tickers"]:
            task = tg.create_task(get_market_rate(ticker))
            log.info("created task for ticker %r: %s", ticker, task)
            ticker_tasks.append(task)
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
