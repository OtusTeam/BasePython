import time
from celery import shared_task
from django.core.mail import send_mail

from blog_app.models import Post


@shared_task
def add(x, y):
    time.sleep(2)
    return x + y


@shared_task
def send_info_email(recipient_email, subject, message):
    send_mail(
        subject=subject,
        message=message,
        from_email='admin@localhost.ru',
        recipient_list=[recipient_email]
    )
    return f"Email отправлен {recipient_email}"


@shared_task
def add_post_rating():
    posts = Post.objects.all()
    for post in posts:
        post.rating += 5
        post.save()
    return f'Обновлено {posts.count()} постов'