import asyncio
import logging
import random

from common import configure_logging


log = logging.getLogger(__name__)


async def get_weather() -> dict:
    log.info("Getting weather data")
    await asyncio.sleep(1.001)
    log.info("fetched weather data")
    return {"weather": {"temperature": 23}}


async def get_currencies() -> dict:
    log.info("Getting currencies data")
    await asyncio.sleep(1)
    log.info("fetched currencies data")
    return {"currencies": {"rate": 42}}


async def get_user_tickers() -> list[str]:
    log.info("Getting user tickers")
    await asyncio.sleep(0.5)
    log.info("fetched user tickers")
    return ["foo", "bar"]


async def get_market_rate(ticker: str) -> dict:
    log.info("Getting market rate for %r", ticker)
    await asyncio.sleep(0.5)
    log.info("fetched market rate for %r", ticker)
    return {
        "market_rate": random.randint(100, 900),
        "ticker": ticker,
    }


async def main() -> None:
    configure_logging()
    log.warning("starting")

    currencies_coro = get_currencies()
    log.info("currencies coro: %s", currencies_coro)

    async with asyncio.TaskGroup() as tg:
        weather_task = tg.create_task(get_weather())
        log.info("created weather_task %s", weather_task)
        user_tickers_task = tg.create_task(get_user_tickers())
        log.info("created user_tickers_task %s", user_tickers_task)
        currencies_task = tg.create_task(currencies_coro)
        log.info("created currencies_task %s", currencies_task)

        user_tickers = await user_tickers_task
        # user_tickers = await get_user_tickers()
        log.info("user's tickers: %s", user_tickers)
        tickers_tasks = []
        for ticker in user_tickers:
            task = tg.create_task(get_market_rate(ticker))
            log.info("created ticker task for %r: %s", ticker, task)
            tickers_tasks.append(task)

    log.info("finished tg")

    weather = weather_task.result()
    currencies = currencies_task.result()
    # weather = await weather_task
    # currencies = await currencies_task
    log.info("weather result %s", weather)
    log.info("currencies result %s", currencies)

    log.info("tickers info: %s", [t.result() for t in tickers_tasks])
    log.warning("finishing")


if __name__ == "__main__":
    asyncio.run(main())
