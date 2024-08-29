from celery import shared_task


import time

from django.core.mail import send_mail

from shop_app.models import Order


@shared_task
def notify_user_about_new_order(order_id: int):
    order = Order.objects.select_related("user").get(pk=order_id)
    time.sleep(8)
    recipient_email = f"{order.user.first_name} <{order.user.username}@example.com>"
    message = f"Thank you for your order!\nOrder #{order.pk} created."
    send_mail(
        subject="Thanks for your order!",
        message=message,
        from_email="care@example.com",
        recipient_list=[recipient_email],
        fail_silently=False,
    )
