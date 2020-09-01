import asyncio
from time import sleep

from loguru import logger

# async IO
# Asynchronous IO


def foo_sync():
    logger.info("foo_sync start")
    sleep(.1)
    logger.info("foo_sync finish")


def bar_sync():
    logger.info("bar_sync start")
    sleep(.1)
    logger.info("bar_sync finish")


def run_sync():
    logger.info("Start sync")
    foo_sync()
    bar_sync()


async def foo():
    logger.info("async foo starting")
    await asyncio.sleep(.1)
    logger.info("async foo finishing")
    return 3


async def bar():
    logger.info("async bar starting")
    await asyncio.sleep(.11)
    logger.info("async bar finishing")
    return 7


async def run_async():
    res_foo = await foo()
    logger.info("res foo {}", res_foo)
    res_bar = await bar()
    logger.info("res bar {}", res_bar)


def run_main():
    logger.info("Starting main")
    # asyncio.run(run_async())
    coros = [
        foo(),
        bar(),
    ]
    coro = asyncio.wait(coros)
    asyncio.run(coro)
    logger.info("Finishing main")


if __name__ == '__main__':
    # run_sync()
    # print(foo())
    run_main()
    asyncio.run(run_async())
