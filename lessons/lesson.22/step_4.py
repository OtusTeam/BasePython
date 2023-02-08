import asyncio
import logging

logging.basicConfig(
    format="[%(asctime)s.%(msecs)03d] %(module)s:%(lineno)d %(levelname)s - %(message)s",
    level=logging.DEBUG,
    datefmt="%Y-%m-%d %H:%M:%S",
)

log = logging.getLogger(__name__)


async def get_user(user_id):
    await asyncio.sleep(0.1)
    log.info("start get user %s", user_id)
    await asyncio.sleep(1)
    log.info("stop get user %s", user_id)
    return {"user": {"id": user_id}}


async def get_users(n_users):
    log.info("fetch %s users", n_users)
    tasks = {
        asyncio.create_task(get_user(user_id)) for user_id in range(1, n_users + 1)
    }

    await asyncio.wait(tasks)

    log.info("done fetching users")


async def main():
    await get_users(10)


if __name__ == "__main__":
    asyncio.run(main())
