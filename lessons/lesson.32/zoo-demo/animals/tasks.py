from celery import shared_task
import time
from django.core.mail import send_mail


@shared_task
def notify(animal_name, animal_category_name):
    time.sleep(120)
    subject = 'New animal'
    message = f'New animal {animal_name} {animal_category_name} has been created.'
    from_email = 'myemail@gmail.com'
    recipient_list = ['admin@zoo.com', 'staff@zoo.com']
    send_mail(subject, message, from_email, recipient_list)
    return {'result': animal_name}


@shared_task
def get_request_info(url, method):
    time.sleep(5)
    print('REQUEST', method, 'on', url)