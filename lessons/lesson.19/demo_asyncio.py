# IO bound operation session.query(User).all()
# CPU bound operation 100 ** 100

import asyncio
from time import sleep

from loguru import logger


def sync_foo():
    logger.info("Starting sync foo")
    sleep(1)  # ex: session.query(User).all()
    logger.info("Finishing sync foo")


def sync_bar():
    logger.info("Starting sync bar")
    sleep(1)  # ex: session.query(User).all()
    logger.info("Finishing sync bar")


#


async def foo():
    logger.info("Starting async foo")
    await asyncio.sleep(1.001)
    logger.info("Finishing async foo")


async def bar():
    logger.info("Starting async bar")
    await asyncio.sleep(1)
    logger.info("Finishing async bar")


def run_sync():
    sync_foo()
    sync_bar()


async def run_async():
    await foo()
    await bar()


async def run_main():
    logger.info("Run main async")
    await asyncio.gather(foo(), bar())
    # weather_moscow, weather_riga = await asyncio.gather(
    #     fetch_weather("Moscow"), #  returns result
    #     fetch_weather("Riga"), #  returns result
    # )
    logger.info("Finish main async")


async def some_async_func(number: int):
    logger.info("Start func {}", number)
    await asyncio.sleep(1)
    if number % 3 == 0:
        await asyncio.sleep(number / 10)
    logger.info("Finishing func {}", number)


async def run_many_async_funcs(count: int):
    # coros = {
    #     some_async_func(i)
    #     for i in range(1, count + 1)
    # }
    coros = [
        some_async_func(i)
        for i in range(1, count + 1)
    ]
    logger.info("Created coros ({}), awating", count)
    # await asyncio.wait({asyncio.create_task(coro) for coro in coros})
    await asyncio.wait([asyncio.create_task(coro) for coro in coros])
    logger.info("Finished running many ({}) funcs", count)


def main():
    logger.info("Starting main")
    # run_sync()
    # main_coro = run_async()
    # main_coro = run_main()
    main_coro = run_many_async_funcs(13)
    asyncio.run(main_coro)
    logger.info("Finishing main")


if __name__ == '__main__':
    main()
