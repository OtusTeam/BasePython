import asyncio
from time import sleep

from loguru import logger


def foo_sync():
    logger.info("Starting foo sync")
    sleep(.1)
    logger.info("Finishing foo sync")


def bar_sync():
    logger.info("Starting bar sync")
    sleep(.1)
    logger.info("Finishing bar sync")


def run_sync():
    logger.info("Starting sync")
    foo_sync()
    bar_sync()


async def foo_async():
    logger.info("Starting foo async")
    await asyncio.sleep(.101)
    logger.info("Finishing foo async")


async def bar_async():
    logger.info("Starting bar async")
    await asyncio.sleep(.1)
    logger.info("Finishing bar async")


async def run_async():
    logger.info("Starting async")
    await foo_async()
    await bar_async()


async def run_main():
    logger.info("Starting main")
    coros = [
        foo_async(),
        bar_async(),
    ]
    logger.info("Created coros")
    coro = asyncio.wait({asyncio.create_task(coro) for coro in coros})
    await coro
    logger.info("Finishing main")


def main():
    # run_sync()
    # asyncio.run(run_async())
    asyncio.run(run_main())


if __name__ == '__main__':
    main()
