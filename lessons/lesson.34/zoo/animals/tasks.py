from time import sleep

from celery import shared_task
from django.core.mail import send_mail


@shared_task
def send_emails(subject, message):
    sleep(10)
    send_mail(subject,
              message,
              from_email='admin@otus.local',
              recipient_list=['user_1@mail.local'])
