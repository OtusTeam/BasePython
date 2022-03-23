import time

from django.shortcuts import render

from .tasks import send_mail_task
# from zoo.celery import celery_app
from zoo import celery_app
from .models import Animal


# def index(request):
#     all_animals = Animal.objects.prefetch_related('animalfood_set').all()
#     context = {
#         'all_animals': all_animals
#     }
#     return render(request, 'index.html', context=context)


def index(request):
    all_animals = Animal.objects.prefetch_related('animalfood_set').all()
    task_id = None
    if request.method == 'POST':
        print('task started', time.time())
        task = send_mail_task.delay('subject', 'abcde')  # celery case
        # task = send_mail_task('subject', 'abcde')  # sync case
        print('django works', time.time())
        task_id = task.id
    context = {
        'all_animals': all_animals,
        'task_id': task_id
    }
    return render(request, 'index.html', context)


def task_status(request, task_id):
    # task_id = request.GET['task_id']
    print(task_id)
    task = celery_app.AsyncResult(task_id)
    status = task.status
    context = {
        'task_id': task_id,
        'status': status
    }
    return render(request, 'status.html', context)
