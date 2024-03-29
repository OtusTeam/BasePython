import time

from celery import shared_task
from django.core.mail import send_mail


@shared_task
def send_mail_task(subject, message):
    time.sleep(20)
    send_mail(
        subject,
        message,
        'from@otus.local',
        ['to@otus.local'],
        fail_silently=False,
    )
    return 'done'

# send_mail_task.delay(subject, message)
