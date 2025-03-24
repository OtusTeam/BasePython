from celery import shared_task
from django.core.mail import send_mail
import time
from .models import Post

@shared_task
def add(x, y):
    time.sleep(5)
    return x + y


@shared_task
def send_notification_email(recepient_email, subject, message):
    send_mail(
        subject=subject,
        message=message,
        from_email='stasik5@bk.ru',
        recipient_list=[recepient_email],
    )
    return f'Email sent to {recepient_email}'


@shared_task
def post_ratings_periods():
    posts = Post.objects.all()
    for post in posts:
        post.rating += 1
        post.save()
    return f'Rating updated for {posts.count()} posts'