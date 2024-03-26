import time

from django.shortcuts import render
# from django.db import connection

from animals.models import Animal
from . import tasks

from zoo import celery_app


def index(request):
    # animals_qty = len(
    #     Animal.objects.all(),  # db level -> python 1000 -> inst Animal
    # )
    animals_qty = Animal.objects.count()  # db level -> COUNT()
    animals = Animal.objects.all()
    # animals = Animal.objects.filter(
    #     name__startswith='po',
    #     # age__gte=3,
    # )
    # print(dir(animals))
    # print(animals.query)
    # animals = [
    #     {'name': 'King', 'kind': 'lion'}
    # ]

    context = {
        'animals': animals,
        'animals_qty': animals_qty,
    }

    return render(request, 'animals/index.html', context=context)


def send_mail(request):
    task_id = None

    print('task started', time.time())

    task = tasks.send_mail_task.delay('hello from Django', 'abcde')  # celery case
    # task = tasks.send_mail_task('hello from Django', 'abcde')  # sync case

    print('django works', time.time())

    try:
        task_id = task.id
        print('task_id', task_id)
    except Exception as e:
        pass

    context = {
        'task_id': task_id
    }
    return render(request, 'animals/send_mail.html', context=context)


def task_status(request, task_id):
    # task_id = request.GET['task_id']
    print(task_id)

    task = celery_app.AsyncResult(task_id)
    status = task.status
    context = {
        'task_id': task_id,
        'status': status
    }
    return render(request, 'animals/status.html', context=context)
