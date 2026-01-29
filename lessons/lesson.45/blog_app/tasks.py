from celery import shared_task
import time
from django.core.mail import send_mail
from blog_app.models import Post



@shared_task
def add(x, y):
    time.sleep(5)
    return x + y


@shared_task
def send_mail_task(email, subject, message):
    send_mail(
        subject=subject,
        message=message,
        from_email='admin@mail.ru',
        recipient_list=[email],
    )
    return f'Email отправлены на {email}'


@shared_task
def add_post_rating():
    posts = Post.objects.all()
    for post in posts:
        post.rating += 5
        post.save()
    return f'Обновлено {posts.count()} постов'