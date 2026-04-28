from celery import shared_task

from shop_app.models import Product
from shop_app.notifications import notify_product_created


@shared_task
def send_product_created_notification(product_id) -> None:
    product = Product.objects.get(pk=product_id)
    return notify_product_created(product)
