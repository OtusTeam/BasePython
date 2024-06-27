from create_fastapi_app import create_app

from views.index import router as router_index
from views.products import router as router_products

app = create_app(create_custom_static_urls=True)

app.include_router(router_index)
app.include_router(router_products)
