import asyncio
from time import sleep

from loguru import logger


def sync_foo():
    logger.info("Starting sync foo")
    sleep(1)
    logger.info("Finishing sync foo")


def sync_bar():
    logger.info("Starting sync bar")
    sleep(1)
    logger.info("Finishing sync bar")


def run_sync():
    sync_foo()
    sync_bar()

#


async def async_foo():
    logger.info("Starting async foo")
    await asyncio.sleep(1.0001)
    logger.info("Finishing async foo")


async def async_bar():
    logger.info("Starting async bar")
    await asyncio.sleep(1)
    logger.info("Finishing async bar")


async def run_async():
    # coro_foo = async_foo()
    # await coro_foo
    await async_foo()
    await async_bar()


async def simple_async_func(task_id: int):
    logger.info("Starting task {}", task_id)
    # await asyncio.sleep(.001)
    to_sleep = 1
    if task_id % 10 == 0:
        to_sleep = 2
    await asyncio.sleep(to_sleep)
    logger.info("Finshing task {}", task_id)


async def run_main():
    logger.info("---Starting main")
    coros = [
        async_foo(),
        async_bar(),
    ]
    logger.info("---Created coros list")
    coro = asyncio.wait([asyncio.create_task(coro) for coro in coros])
    await coro
    logger.info("---Finishing main")


async def run_main_many_tasks():
    tasks = [asyncio.create_task(simple_async_func(num)) for num in range(1, 101)]
    logger.info("Starting {} tasks", len(tasks))
    coro = asyncio.wait(tasks)
    await coro
    logger.info("---Finishing multiple")


def main():
    # run_sync()
    # asyncio.run(run_async())
    # asyncio.run(run_main())
    asyncio.run(run_main_many_tasks())


if __name__ == "__main__":
    main()
