from django.core.mail import send_mail
from celery import shared_task
import time
from blog_app.models import Post


@shared_task
def add(x, y):
    time.sleep(5)
    return x + y


@shared_task
def send_info_email(rec_email, subject, message):
    """Фоновая задача для отправки уведомления по email."""
    send_mail(
        subject=subject,
        message=message,
        from_email='admin@mail.ru',
        recipient_list=[rec_email],
    )
    return f'Email sent to {rec_email}'


@shared_task
def inc_post_rating():
    posts = Post.objects.all()
    for post in posts:
        post.rating += 1
        post.save()
    return f'Обновлено {posts.count()} постов'