from datetime import datetime

from pydantic import BaseModel

from orders.entity import OrderStatus


class OrderBase(BaseModel):
    name: str


class OrderCreate(OrderBase):
    name: str


class OrderRead(OrderBase):
    id: str
    status: OrderStatus
    created_at: datetime
