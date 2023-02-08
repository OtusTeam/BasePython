import asyncio
import logging


logging.basicConfig(
    format="[%(asctime)s.%(msecs)03d] %(module)s:%(lineno)d %(levelname)s - %(message)s",
    level=logging.DEBUG,
    datefmt="%Y-%m-%d %H:%M:%S",
)

log = logging.getLogger(__name__)


async def get_users():
    log.info("Starting fetching users")
    await asyncio.sleep(1.01)
    log.info("Finished fetching users")
    return ["users"]


async def get_products():
    log.info("Starting fetching products")
    await asyncio.sleep(1)
    log.info("Finished fetching products")
    return ["products"]


async def main():
    log.info("Start (async)")
    # get_users()
    coro_users = get_users()
    log.info("users coro %s", coro_users)
    # users, products = await asyncio.gather(
    results = await asyncio.gather(
        coro_users,
        # get_users(),
        get_products(),
        # get_products(),
    )
    log.info("gather results %s", results)
    log.info("Finish (async)")


if __name__ == "__main__":
    asyncio.run(main())
