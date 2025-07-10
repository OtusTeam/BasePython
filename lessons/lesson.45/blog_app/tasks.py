from celery import shared_task
import time
# from django.core.mail import send_mail
from django.core.mail import send_mail
from .models import Post


@shared_task
def add(x, y):
    time.sleep(5)
    return x + y


@shared_task
def send_info_email(recipient_email, subject, message):
    # send_mail(
    #     subject=subject,
    #     message=message,
    #     from_email='admin@admin.ru',
    #     recipient_email=[recipient_email],
    # )
    send_mail(
        subject=subject,
        message=message,
        from_email='admin@admin.ru',
        recipient_list=[recipient_email],
    )
    return f'Почта отправлена {recipient_email}'


@shared_task
def add_post_ratings():
    posts = Post.objects.all()
    for post in posts:
        post.rating += 1
        post.save()
    return f'Рейтинг обновлен у {posts.count()} постов'