import asyncio
import logging
import random

from common import configure_logging

log = logging.getLogger(__name__)


async def get_user(user_id: int) -> dict[str, int]:
    to_sleep = random.random()
    log.info("get user %02d sleep %0.3f", user_id, to_sleep)
    await asyncio.sleep(to_sleep)
    if random.random() > 0.7:
        log.info("error getting user %02d", user_id)
        raise ValueError(user_id)
    log.info("got user %02d", user_id)
    return {"user_id": user_id, "slept": to_sleep}


async def get_n_users(n_users: int):
    tasks = {
        asyncio.create_task(get_user(user_id=i), name=f"get_user_{i:03d}")
        for i in range(1, n_users + 1)
    }
    # await asyncio.gather(*tasks)
    done, pending = await asyncio.wait(tasks)

    for task in pending:
        task.cancel()

    for task in done:  # type: asyncio.Task
        # error = task.exception()
        # if (error := task.exception()) is not None:
        if error := task.exception():
            log.warning(
                "task %s got error %s",
                task.get_name(),
                error,
                # exc_info=error,
            )
            continue

        log.info(
            "Result for task %s: %s",
            task.get_name(),
            task.result(),
        )



async def main():
    configure_logging()

    log.info("Start main")
    await get_n_users(10**4)
    log.info("Finish main")


if __name__ == "__main__":
    asyncio.run(main())
