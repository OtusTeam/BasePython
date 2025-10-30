import asyncio
import random
import string

from faststream.rabbit import RabbitRouter

from core.config import settings
from events.schemas.user_events import UserStatisticsRequest, UserStatisticsResponse

router = RabbitRouter()


@router.subscriber(
    queue=settings.rabbitmq.queues.statistics_queue_name,
    exchange=settings.rabbitmq.queues.statistics_exchange_name,
)
async def user_statistics(
    request: UserStatisticsRequest,
) -> UserStatisticsResponse:

    # якобы CPU нагрузка
    await asyncio.sleep(random.random())

    return UserStatisticsResponse(
        user_id=request.user_id,
        kind=request.kind,
        foo=random.randint(1, 100),
        bar=random.choice(string.ascii_uppercase),
        baz=random.random(),
    )
