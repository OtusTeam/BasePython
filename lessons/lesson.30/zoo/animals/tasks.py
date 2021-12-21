from celery import shared_task
import time
from .models import Animal
from django.core.mail import send_mail


# @shared_task
# def save_animals_task():
#     print('save_animals_task pre')
#     time.sleep(10)
#     print('save_animals_task after')
#     animals = Animal.objects.all()
#     with open('animals.txt', 'w', encoding='utf-8') as f:
#         for animal in animals:
#             f.write(animal.name + '\n')


@shared_task
def send_mail_task(subject, message):
    time.sleep(5)
    send_mail(subject, message, 'from@example.com',
              ['to@example.com'], fail_silently=False)
