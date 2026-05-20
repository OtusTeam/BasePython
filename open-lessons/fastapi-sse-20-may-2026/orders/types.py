from typing import TYPE_CHECKING
from typing import Protocol

if TYPE_CHECKING:
    from orders.entity import Order
    from orders.storage import OrdersStorage


class OnOrderAdance(Protocol):
    async def __call__(
        self,
        storage: OrdersStorage,
        order: Order,
    ) -> None: ...
