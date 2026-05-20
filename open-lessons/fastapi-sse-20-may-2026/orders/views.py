from collections.abc import AsyncGenerator
from typing import Annotated

from fastapi import APIRouter, HTTPException
from fastapi import Depends
from fastapi import Form
from fastapi import Request
from fastapi import Path
from fastapi import status
from fastapi.responses import HTMLResponse
from fastapi.responses import RedirectResponse
from fastapi.sse import ServerSentEvent, EventSourceResponse

from misc.templating import render_string
from misc.templating import templates
from orders.dependencies import create_order_uc
from orders.dependencies import get_all_orders_uc
from orders.dependencies import get_order_or_404
from orders.dependencies import order_events_subscription_uc
from orders.dtos import OrderCreate
from orders.dtos import OrderRead
from orders.entity import Order
from orders.entity import OrderStatus
from orders.storage import OrdersStorage
from orders.use_cases import CreateOrderUC
from orders.use_cases import GetAllOrdersUC
from orders.use_cases import OrderEventsSubscriptionUC

router = APIRouter(
    tags=["Orders"],
    prefix="/orders",
)

ORDER_STATUS_UPDATE_EVENT_NAME = "status"
ORDER_LIST_STATUS_UPDATE_EVENT_NAME = "list-status"


async def on_order_advance(
    storage: OrdersStorage,
    order: Order,
) -> None:
    new_status_block = render_string(
        "orders/components/status-block.html",
        order=order,
        order_statuses=[str(value) for value in OrderStatus],
    )
    await storage.publish(
        order_id=order.id,
        message=ServerSentEvent(
            event=ORDER_STATUS_UPDATE_EVENT_NAME,
            raw_data=new_status_block,
        ),
    )

    new_status_badge = render_string(
        "orders/components/status-badge.html",
        order=order,
    )
    await storage.publish(
        order_id=order.id,
        message=ServerSentEvent(
            event=ORDER_LIST_STATUS_UPDATE_EVENT_NAME,
            raw_data=new_status_badge,
        ),
    )


@router.post(
    "",
    response_model=OrderRead,
)
async def create_order(
    request: Request,
    order_create: Annotated[
        OrderCreate,
        Form(),
    ],
    create: Annotated[
        CreateOrderUC,
        Depends(create_order_uc),
    ],
) -> Order | RedirectResponse:
    order = await create(
        order_create,
        on_order_advance=on_order_advance,
    )

    if "text/html" not in request.headers.get("Accept", ""):
        return order

    return RedirectResponse(
        url=request.url_for("order_detail", order_id=order.id),
        status_code=status.HTTP_303_SEE_OTHER,
    )


@router.get(
    "/{order_id}",
    response_model=OrderRead,
    name="order_detail",
)
async def read_order(
    request: Request,
    order: Annotated[
        Order,
        Depends(get_order_or_404),
    ],
) -> Order:
    if "text/html" not in request.headers.get("Accept", ""):
        return order

    context = {
        "order": order,
        "order_statuses": [str(value) for value in OrderStatus],
        "sse_event_message": ORDER_STATUS_UPDATE_EVENT_NAME,
    }

    return templates.TemplateResponse(
        request=request,
        name="orders/details.html",
        context=context,
    )


@router.get(
    "",
    response_model=list[OrderRead],
    name="orders_list",
    # Define both media types under the 200 Status Code to build the Swagger dropdown
    responses={
        status.HTTP_200_OK: {
            "description": (
                "Returns a list of orders. Formats available: JSON array or HTML page."
            ),
            "content": {
                "application/json": {},
                "text/html": {
                    "schema": {
                        "type": "string",
                        "example": (
                            "<!DOCTYPE html><html><body>"
                            "<h1>Orders List</h1>...</body></html>"
                        ),
                    },
                },
            },
        },
    },
)
async def get_orders(
    request: Request,
    get_all: Annotated[
        GetAllOrdersUC,
        Depends(get_all_orders_uc),
    ],
) -> HTMLResponse | list[Order]:
    orders = await get_all()

    if "text/html" not in request.headers.get("Accept", ""):
        return orders

    return templates.TemplateResponse(
        request=request,
        name="orders/list.html",
        context={
            "orders": orders,
            "sse_event_message": ORDER_LIST_STATUS_UPDATE_EVENT_NAME,
        },
    )


@router.get(
    "/{order_id}/events",
    name="order_events",
    response_class=EventSourceResponse,
)
async def send_order_events(
    order: Annotated[
        Order,
        Depends(get_order_or_404),
    ],
    event_stream: Annotated[
        OrderEventsSubscriptionUC,
        Depends(order_events_subscription_uc),
    ],
) -> AsyncGenerator[ServerSentEvent]:
    async for event in event_stream(order.id):
        yield event
