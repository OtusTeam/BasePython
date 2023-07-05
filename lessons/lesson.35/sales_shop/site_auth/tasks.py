from celery import shared_task
from django.contrib.auth import get_user_model
from mail_templated import send_mail


User = get_user_model()

@shared_task
def welcome_user(user_pk: int):
    user = User.objects.get(pk=user_pk)
    send_mail(
        "email/new-reg.html",
        {
            "user": user,
        },
        "admin@saleshop.com",
        [user.email],
        fail_silently=False,
    )
