import asyncio
import logging
import random
import time

import common

log = logging.getLogger(__name__)


async def get_user(user_id: int) -> dict[str, float]:
    to_sleep = random.random()
    log.info("get user %02d, sleep %0.4f", user_id, to_sleep)
    await asyncio.sleep(to_sleep)
    if random.random() > 0.7:
        log.info("create error for user %02d", user_id)
        raise ValueError(user_id)
    log.info("got user %02d", user_id)
    return {"user_id": user_id, "slept": to_sleep}


async def get_n_users(n_users: int) -> None:
    tasks = {
        # create task for each user
        asyncio.create_task(
            # the task
            get_user(user_id=i),
            # task name (coro name)
            name=f"user-{i}",
        )
        # for n users
        for i in range(1, n_users + 1)
    }
    done, pending = await asyncio.wait(tasks)

    for task in pending:
        task.cancel()
        log.info("task %s cancelled", task.get_name())

    for task in done:
        if error := task.exception():
            log.warning(
                "could not get user in task %s, error: %r",
                task.get_name(),
                error,
                # exc_info=error,
            )
            continue

        log.info(
            "result for task %s: %r",
            task.get_name(),
            task.result(),
        )


async def main():
    common.configure_logging()
    start_time = time.time()
    log.info("Starting step 6")
    await get_n_users(10**4)
    log.info("Finished step 6, total time: %0.4f", time.time() - start_time)


if __name__ == "__main__":
    asyncio.run(main())
