import asyncio
import random
from operator import attrgetter
from uuid import uuid4

from fastapi.sse import ServerSentEvent

from misc.pubsub import EventQueue
from misc.pubsub import PubSub
from orders.dtos import OrderCreate
from orders.entity import STATUSES
from orders.entity import Order
from orders.entity import OrderID
from orders.entity import OrderStatus
from orders.types import OnOrderAdance


class OrdersStorage:
    def __init__(self) -> None:
        self._orders = dict[OrderID, Order]()
        self._progression_tasks = dict[OrderID, asyncio.Task[None]]()
        self._pubsub = PubSub()

    @classmethod
    def _new_id(cls) -> OrderID:
        # return secrets.token_urlsafe(6)  # noqa: ERA001
        return uuid4().hex[:6]

    def create(self, order_create: OrderCreate) -> Order:
        order = Order(
            id=self._new_id(),
            status=OrderStatus.PENDING,
            **order_create.model_dump(),
        )
        self._orders[order.id] = order
        return order

    def get(self, order_id: OrderID) -> Order | None:
        return self._orders.get(order_id)

    def get_all(self) -> list[Order]:
        return sorted(
            self._orders.values(),
            key=attrgetter("created_at"),
            reverse=True,
        )

    async def start_progression_task(
        self,
        order_id: OrderID,
        on_order_advance: OnOrderAdance,
    ) -> None:
        existing_task = self._progression_tasks.get(order_id)
        if existing_task is not None and existing_task.done():
            return

        self._progression_tasks[order_id] = asyncio.create_task(
            self._advance(
                order_id=order_id,
                on_order_advance=on_order_advance,
            ),
        )

    async def _advance(
        self,
        order_id: OrderID,
        on_order_advance: OnOrderAdance,
    ) -> None:
        order = self._orders.get(order_id)
        if order is None:
            return

        start_index = STATUSES.index(order.status) + 1
        new_statues = STATUSES[start_index:]
        for status in new_statues:
            await self._advance_order_status(
                order_id=order_id,
                status=status,
                on_order_advance=on_order_advance,
            )

    async def _advance_order_status(
        self,
        order_id: OrderID,
        status: OrderStatus,
        on_order_advance: OnOrderAdance,
    ) -> None:
        sleep_time = random.randint(3, 7)
        await asyncio.sleep(sleep_time)
        order = self._orders.get(order_id)
        if order is None:
            return

        order.status = status

        await on_order_advance(self, order)

    async def subscribe(self, order_id: OrderID) -> EventQueue:
        return await self._pubsub.subscribe(order_id)

    def unsubscribe(self, order_id: OrderID, queue: EventQueue) -> None:
        return self._pubsub.unsubscribe(order_id, queue)

    async def publish(self, order_id: OrderID, message: ServerSentEvent) -> None:
        await self._pubsub.publish(order_id, message)


storage = OrdersStorage()
