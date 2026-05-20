from typing import Annotated

from fastapi import HTTPException, status, Depends, Path, Request

from orders.entity import OrderID
from orders.use_cases import CreateOrderUC
from orders.use_cases import GetAllOrdersUC
from orders.use_cases import GetOrderUC
from orders.use_cases import OrderEventsSubscriptionUC


def create_order_uc() -> CreateOrderUC:
    return CreateOrderUC()


def get_order_uc() -> GetOrderUC:
    return GetOrderUC()


def get_all_orders_uc() -> GetAllOrdersUC:
    return GetAllOrdersUC()


def order_events_subscription_uc(
    request: Request,
) -> OrderEventsSubscriptionUC:
    return OrderEventsSubscriptionUC(request=request)


async def get_order_or_404(
    order_id: Annotated[
        OrderID,
        Path(),
    ],
    get: Annotated[
        GetOrderUC,
        Depends(get_order_uc),
    ],
):
    order = await get(order_id)
    if order is not None:
        return order

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Order {order_id} not found!",
    )
