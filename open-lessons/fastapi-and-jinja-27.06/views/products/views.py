from typing import Annotated

from fastapi import APIRouter, Request, HTTPException, status, Form
from fastapi.responses import HTMLResponse
from annotated_types import Gt
from starlette.responses import RedirectResponse

from utils.templating import TemplateResponse

from .crud import storage
from .schemas import ProductCreateSchema

router = APIRouter(
    prefix="/products",
    tags=["Products"],
)


@router.get(
    "/",
    name="products:list",
    response_class=HTMLResponse,
)
def get_products_list(request: Request):
    products_list = storage.products_list()
    return TemplateResponse(
        request=request,
        name="products/list.html",
        context={"products": products_list},
    )


@router.get(path="/create/", response_class=HTMLResponse)
def show_form_to_create_new_product():
    # TODO
    pass


@router.post(
    path="/create/",
    response_class=RedirectResponse,
    status_code=status.HTTP_303_SEE_OTHER,
)
def create_new_product(
    name: str = Form(...),
    price: int = Form(...),
):
    product_in = ProductCreateSchema(name=name, price=price)
    product = storage.create_product(product_in=product_in)

    return router.url_path_for("products:details", product_id=product.id)


@router.get(
    "/{product_id}/",
    name="products:details",
    response_class=HTMLResponse,
)
def get_product_details(
    request: Request,
    product_id: Annotated[int, Gt(0)],
):
    product = storage.product_details(product_id=product_id)
    if product is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Product #{product_id} not found",
        )
    return TemplateResponse(
        request=request,
        name="products/details.html",
        context={"product": product},
    )
