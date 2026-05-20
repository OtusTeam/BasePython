from dataclasses import dataclass
from dataclasses import field
from datetime import UTC
from datetime import datetime
from enum import StrEnum

type OrderID = str


class OrderStatus(StrEnum):
    PENDING = "pending"
    PROCESSING = "processing"
    SHIPPED = "shipped"
    DELIVERED = "delivered"


STATUSES = list(OrderStatus)


@dataclass
class Order:
    id: OrderID
    name: str
    status: OrderStatus
    created_at: datetime = field(
        default_factory=lambda: datetime.now(UTC),
    )
