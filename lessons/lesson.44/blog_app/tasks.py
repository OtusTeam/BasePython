from celery import shared_task
from django.core.mail import send_mail
import time
from blog_app.models import Post


@shared_task
def add(x, y):
    time.sleep(5)
    return x + y


@shared_task
def send_notification_email(recepient_email, subject, message):
    send_mail(
        subject=subject,
        message=message,
        from_email='user@mail.ru',
        recipient_list=[recepient_email],
    )
    return f'Send email to {recepient_email}'


@shared_task
def add_post_rating():
    posts = Post.objects.all()
    for post in posts:
        post.rating += 3
        post.save()
    return f'Рейтинг {posts.count()} постов увеличин на 3'