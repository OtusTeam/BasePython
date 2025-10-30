from faststream.rabbit import RabbitBroker

from core.config import settings

# в вашем приложении должен быть указан полный адрес для подключения
broker = RabbitBroker(
    url=settings.rabbitmq.url,
)

user_registered = broker.publisher(
    queue=settings.rabbitmq.queues.queue_name,
    exchange=settings.rabbitmq.queues.exchange_name,
)

user_statistics = broker.publisher(
    queue=settings.rabbitmq.queues.statistics_queue_name,
    exchange=settings.rabbitmq.queues.statistics_exchange_name,
)
