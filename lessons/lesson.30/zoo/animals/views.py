import time

from django.shortcuts import render

from animals.models import Animal
# from zoo import celery_app
from zoo.celery import celery_app

from .tasks import send_mail_task


# def index(request):
#     return render(request, 'animals/index.html')


def index(request):
    task_id = None
    if request.method == 'POST':
        print(time.time())
        task = send_mail_task.delay('subject', 'abcde')
        print(time.time())
        task_id = task.id
    context = {'task_id': task_id}

    return render(request, 'animals/index.html', context=context)


def animals_list(request):
    # animals = Animal.objects.all()
    animals = Animal.objects.select_related('kind'). \
        prefetch_related('animalfood_set').all()
    context = {
        'animals': animals
    }
    return render(request, 'animals/animals_list.html', context=context)


def status_view(request, task_id):  # status_view(request)
    # task_id = request.GET['task_id']  # /?task_id=3
    print(task_id)
    task = celery_app.AsyncResult(task_id)
    context = {'task_id': task_id,
               'status': task.status}

    return render(request, 'animals/status.html', context=context)
