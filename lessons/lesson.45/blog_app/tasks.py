from celery import shared_task
from django.core.mail import send_mail
import time

from blog_app.models import Post


@shared_task
def add(x, y):
    time.sleep(7)
    return x + y


@shared_task
def send_mail_task(rec_email, subject, message):
    """Фоновая задача для отправки уведомлений на email."""
    send_mail(
        subject=subject,
        message=message,
        recipient_list=[rec_email],
        from_email='admin@mail.ru',
    )
    return f"Email sent to {rec_email}"


@shared_task
def inc_post_rating():
    posts = Post.objects.all()
    for post in posts:
        post.rating = post.rating + 1
        post.save()
    return f'Обновлено {posts.count()} постов'