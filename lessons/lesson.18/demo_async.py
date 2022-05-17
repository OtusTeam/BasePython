import asyncio
from time import sleep

from loguru import logger


def func_foo():
    logger.info("Starting sync foo")
    sleep(1)
    logger.info("Finishing sync foo")


def func_bar():
    logger.info("Starting sync bar")
    sleep(1)
    logger.info("Finishing sync bar")


def run_sync():
    func_foo()
    func_bar()


# async

async def foo():
    logger.info("Starting async foo")
    await asyncio.sleep(1.0001)
    logger.info("Finishing async foo")


async def bar():
    logger.info("Starting async bar")
    await asyncio.sleep(1)
    logger.info("Finishing async bar")


async def run_by_one():
    logger.info("run by one")
    foo_coro = foo()
    logger.info("foo coro: {}", foo_coro)
    await bar()
    await foo_coro


def generate_sleep_time(task_id: int):
    # pseudo-random sleep time!!!
    to_sleep = 1

    if task_id % 5 == 0:
        is_add = (task_id // 10) % 2 == 0
        to_sleep += (task_id / 1000) * (1 if is_add else -1)

    return to_sleep


async def some_async_func(task_id: int):
    to_sleep = generate_sleep_time(task_id)
    logger.info("Start task #{:4d} and sleep {:.2f}", task_id, to_sleep)
    await asyncio.sleep(to_sleep)
    # sleep(to_sleep)
    logger.info("Finish task #{}", task_id)


async def run_many_tasks():
    tasks = {
        asyncio.create_task(
            some_async_func(task_id)
        )
        for task_id in range(1, 125)
    }
    coro = asyncio.wait(tasks)
    await coro


async def run_async_main():
    logger.info("Starting async main")
    # await run_by_one()
    await asyncio.gather(foo(), bar())
    await run_many_tasks()


def main():
    logger.info("Starting main")
    # run_sync()
    asyncio.run(run_async_main())
    logger.info("Finishing main")


if __name__ == '__main__':
    main()
