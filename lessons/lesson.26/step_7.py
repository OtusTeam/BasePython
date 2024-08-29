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
    sleep_time = random.random()
    log.info(
        "get user %02d, sleep %0.4f",
        user_id,
        sleep_time,
    )
    await asyncio.sleep(sleep_time)
    if random.random() > 0.7:
        log.info("create error for user %02d", user_id)
        raise ValueError(user_id)
    log.info("got user %02d", user_id)
    return {"user_id": user_id, "slept": sleep_time}


async def get_n_users(n_users: int) -> list[UserData]:

    tasks = {
        # create task for each user
        asyncio.create_task(
            # create coro to get this user
            get_user(user_id=user_id),
            # name after user by id
            name=f"user-{user_id:02d}",
        )
        # for n users
        for user_id in range(1, n_users + 1)
    }
    # res = await asyncio.gather(*tasks)
    # return list(res)

    done, pending = await asyncio.wait(tasks)

    for task in pending:
        task.cancel()
        log.info("task %r cancelled", task.get_name())

    users_result = []

    for task in done:
        if error := task.exception():
            log.warning(
                "task %r failed, error: %s",
                task.get_name(),
                error,
                # exc_info=error,
            )
            continue

        result = task.result()
        users_result.append(result)
        log.info(
            "result for task %r: %s",
            task.get_name(),
            result,
        )

    return users_result


async def main():
    configure_logging()
    log.info("Starting step 7 - wait")

    res = await get_n_users(10)
    log.info("got users: %s", res)

    log.info("Finished main")


if __name__ == "__main__":
    asyncio.run(main())
