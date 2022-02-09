import asyncio
from time import sleep
from loguru import logger

#

def sync_foo():
    logger.info("Starting sync foo")
    sleep(1)  # session.query(User).all()
    logger.info("Finishing sync foo")


def sync_bar():
    logger.info("Starting sync bar")
    sleep(1)  # session.query(User).all()
    logger.info("Finishing sync bar")

#


async def foo():
    logger.info("Starting async foo")
    await asyncio.sleep(1.001)
    logger.info("Finishing async foo")
    return "foo done"


async def bar():
    logger.info("Starting async bar")
    await asyncio.sleep(1)
    logger.info("Finishing async bar")
    return "bar done"


def run_sync():
    sync_foo()
    sync_bar()


async def run_async():
    foo_coro = foo()
    await foo_coro
    await bar()


async def main_async():
    logger.info("Starting main async")
    # await run_async()
    coro = asyncio.gather(foo(), bar())
    logger.info("await future {}", coro)
    result = await coro
    logger.info("result gather: {}", result)

    await run_many_async_funcs(10)

    logger.info("Finishing main async")


async def some_async_func(number: int):
    logger.info("Start some func #{}", number)
    await asyncio.sleep(1)
    if number % 3 == 0:
        await asyncio.sleep(number / 10)
    logger.info("Finish func #{}", number)


async def run_many_async_funcs(count: int):
    coros = [
        some_async_func(i)
        for i in range(count)
    ]
    logger.info("prepare {} coros", count)
    # await asyncio.gather(*coros)
    tasks = [asyncio.create_task(coro) for coro in coros]
    logger.info("start awaiting {} tasks", count)
    result = await asyncio.wait(tasks)
    logger.info("result wait: {}", result)

    logger.info("finished running {} coros", count)


def main():
    logger.info("Starting main")
    # run_sync()
    asyncio.run(main_async())


if __name__ == '__main__':
    main()
