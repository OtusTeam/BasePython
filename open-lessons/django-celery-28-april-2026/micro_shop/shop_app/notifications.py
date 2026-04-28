from time import sleep

from django.core.mail import send_mail
from django.template.loader import render_to_string

from shop_app.models import Product


def notify_product_created(product: Product) -> None:
    ctx = {"product": product}
    message = render_to_string(
        "shop_app/email/product-created.txt",
        ctx,
    )
    html_message = render_to_string(
        "shop_app/email/product-created.html",
        ctx,
    )
    # sleep(5)
    send_mail(
        subject=f"New product #{product.pk} created",
        from_email="no-reply@localhost",
        recipient_list=["admin@localhost"],
        message=message,
        html_message=html_message,
    )
