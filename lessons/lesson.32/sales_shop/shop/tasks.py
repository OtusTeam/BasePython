from celery import shared_task
from django.core.mail import send_mail


@shared_task
def notify_order_saved(order_pk, promocode):
    # from time import sleep
    # sleep(3)

    send_mail(
        f"Order #{order_pk} saved",
        f"Here is the message. Order #{order_pk}, promocode: {promocode}",
        "from@example.com",
        ["to@example.com"],
        fail_silently=True,
    )
