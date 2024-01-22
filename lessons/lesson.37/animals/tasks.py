import time
from celery import shared_task
from django.core.mail import send_mail


@shared_task
def write_to_file(message):
    time.sleep(20)
    with open("messages.txt", "a", encoding="utf-8") as f:
        f.write(f"{message}\n")


@shared_task
def send_contact_email(message):
    time.sleep(20)
    send_mail(
        "contact message",
        message,
        "admin@admin.com",
        [
            "admin@admin.com",
            "virtual@owner.com",
        ],
        fail_silently=False,
    )
    return "sent"
