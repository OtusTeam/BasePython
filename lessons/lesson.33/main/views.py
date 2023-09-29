import time

from django.shortcuts import render

from zoo import celery_app
from .tasks import send_mail_task


def index(request):
    print('do smth')
    return render(request, 'main/index.html')


def send_mail(request):
    task_id = None

    print('task started', time.time())

    task = send_mail_task.delay('subject', 'abcde')  # celery case
    # task = send_mail_task('subject', 'abcde')  # sync case

    print('django works', time.time())

    try:
        task_id = task.id
    except Exception as e:
        pass

    context = {
        'task_id': task_id
    }
    return render(request, 'main/send_mail.html', context=context)


def task_status(request, task_id):
    # task_id = request.GET['task_id']
    print(task_id)

    task = celery_app.AsyncResult(task_id)
    status = task.status
    context = {
        'task_id': task_id,
        'status': status
    }
    return render(request, 'main/status.html', context=context)
