from celery import shared_task
from django.core.mail import send_mail
from celery.result import AsyncResult
from .models import Post

import time


@shared_task
def add(x, y):
    time.sleep(5)
    return x + y


@shared_task
def send_notification_email(recipient_email, subject, message):
    """ Фоновая задача отправки писем """
    time.sleep(3)
    send_mail(
        subject=subject,
        message=message,
        from_email='stasik5@bk.ru',
        recipient_list=[recipient_email],
    )
    return f'Email sent to {recipient_email}'


@shared_task
def check_task_status(task_id):
    result = AsyncResult(task_id)
    return {
        'task_id': task_id,
        'status': result.status,
        'result': result.result
    }


@shared_task
def update_post_ratings():
    posts = Post.objects.all()
    for post in posts:
        post.rating = post.commets.count() * 10
        post.save()
    return f'Рейтинг обновлен для {posts.count()}'
