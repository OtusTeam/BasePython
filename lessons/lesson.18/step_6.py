import asyncio
import logging
import random

logging.basicConfig(format='%(asctime)s.%(msecs)03d %(message)s',
                    level=logging.DEBUG,
                    datefmt='%Y-%m-%d %H:%M:%S')
logging.getLogger('asyncio').setLevel(logging.WARNING)
logger = logging.getLogger(__name__)


async def get_user(user_id):
    to_sleep = 0.5 + random.random()
    logger.info('started get_user: %s (%f)', user_id, to_sleep)
    await asyncio.sleep(to_sleep)
    if random.random() > 0.5:
        logger.info('failed get_user: %s', user_id)
        10 / 0
    logger.info('finished get_user: %s', user_id)


async def get_users():
    logger.info('started get_users')
    tasks = set()
    for user_id in range(1, 101):
        tasks.add(asyncio.create_task(get_user(user_id)))
    done, pending = await asyncio.wait(tasks)
    logger.info('done %d, pending %d', len(done), len(pending))
    for el in done:
        t_error = el.exception()
        if t_error:
            logger.warning(t_error)

    logger.info('finished get_users')


async def main():
    logger.info('started main')
    await get_users()
    logger.info('finished main')


if __name__ == '__main__':
    asyncio.run(main())
