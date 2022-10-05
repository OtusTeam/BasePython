from time import sleep

from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail


@shared_task
def log_animals_details_access(path: str, pk: int) -> None:
    sleep(pk)
    # 1/0
    print("Access to", path, "animal PK:", pk)


@shared_task
def notify_animal_created(
    animal_name: str,
    path: str,
    created_at: str,
):
    print("send email with params", locals())
    sleep(13)

    message = (
        f"A new animal {animal_name!r} was created at {created_at}"
        "\n\n"
        f"Check animal at: {settings.BASE_URL}{path}"
        "\n\n"
        "Sincerely,\nYour admin."
    )
    send_mail(
        subject=f"New animal created: {animal_name}",
        message=message,
        from_email="admin@example.com",
        recipient_list=["managers@example.com"],
    )
    return True
