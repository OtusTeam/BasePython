from celery import shared_task
import time
from django.core.mail import send_mail

from .models import Post


@shared_task
def add(x, y):
    time.sleep(5)
    return x + y


@shared_task
def send_notifcation_email(recipient_email, subject, message):
    """Фоновая задача отправки уведомления на email."""
    send_mail(
        subject=subject,
        message=message,
        from_email='admin@example.com',
        recipient_list=[recipient_email],
    )
    return f"Почта была отправлена {recipient_email}"


@shared_task
def increase_post_rating():
    """Фоновая задача увеличения рейтинга поста."""
    posts = Post.objects.all()
    for post in posts:
        post.rating += 1
        post.save()
    return f"Рейтинг постов был увеличен на 1"