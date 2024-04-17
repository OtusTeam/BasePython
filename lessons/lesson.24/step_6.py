import asyncio
import logging
import random
from typing import TypedDict

from common import configure_logging

log = logging.getLogger(__name__)


class UserData(TypedDict):
    user_id: int
    slept: float


async def get_user(user_id: int) -> UserData:
    to_sleep = random.random()
    log.info("get user %02d, sleep %0.4f", user_id, to_sleep)
    await asyncio.sleep(to_sleep)
    if random.random() < 0.3:
        log.warning("error fetching user %02d", user_id)
        raise ValueError(user_id)
    log.info("done getting user %02d", user_id)
    return {"user_id": user_id, "slept": to_sleep}


async def get_n_users(n_users: int) -> None:
    tasks = {
        # create task for each user
        asyncio.create_task(
            # coro to create task from
            get_user(user_id=n),
            # optional: set task name
            name=f"get-user-{n:02d}",
        )
        for n in range(1, n_users + 1)
    }
    done, pending = await asyncio.wait(tasks)

    for task in pending:
        task.cancel()
        log.info("task %r canceled", task.get_name())

    for task in done:
        if error := task.exception():
            log.warning(
                "could not get user in task %r, error: %s",
                task.get_name(),
                error,
                # exc_info=error,
            )
            continue

        log.info(
            "task %r completed w/ res %s",
            task.get_name(),
            task.result(),
        )


async def main():
    configure_logging(level=logging.DEBUG)
    log.info("Start step 6")

    # await get_user(7)
    await get_n_users(10)
    log.info("End step 6")



if __name__ == "__main__":
    asyncio.run(main())
