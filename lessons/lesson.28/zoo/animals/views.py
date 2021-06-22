from django.http import Http404
from django.shortcuts import render
from .models import Animal
import time
from .tasks import save_animals_task, send_mail_task
from celery import current_app


# Create your views here.
def index_view(request):
    animals = Animal.objects.all()
    task_id = None
    if request.method == 'POST':
        # print(time.time())
        # save_animals_task.delay()
        # print(time.time())
        task = send_mail_task.delay('skubject', 'tesxfdfdf')
        task_id = task.id

    return render(request, 'animals/index.html', {'animals': animals, 'task_id': task_id})
    # Flask
    # return render(request, 'animals/index.html', animals=animals)
    # return render(request, 'animals/index.html', **{'animals': animals})


def status_view(request):
    task_id = request.GET['task_id']
    # По id Задачи получить её данные
    task = current_app.AsyncResult(task_id)
    status = task.status
    return render(request, 'animals/status.html', {'task_id': task_id, 'status': status})
