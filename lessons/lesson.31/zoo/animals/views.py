from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.timezone import now
from django.views.generic import ListView, CreateView, UpdateView, DetailView

from animals.models import Animal, Food
# from celery import current_app
from zoo.celery import celery_app as current_app
from .forms import AnimalCreateForm
from .tasks import send_emails


def index_view(request):
    animals = Animal.objects.all()
    # animals = Animal.objects.select_related('kind').all()
    task_id = None

    if request.method == 'POST':
        print('before', now())
        task = send_emails.delay('hello from admin', 'lesson')
        task_id = task.id
        print('after', now())

    return render(request,
                  'animals/index.html',
                  {'animals': animals,
                   'task_id': task_id})


def food_view(request):
    # foods = Food.objects.all()
    # 0.54 ms (4 queries including 3 similar )
    foods = Food.objects.prefetch_related('kinds').all()
    # 0.46 ms (2 queries )

    return render(request,
                  'animals/foods.html',
                  {'foods': foods})


def check_task_status(request):
    task_id = request.GET['task_id']
    task = current_app.AsyncResult(task_id)
    task_status = task.status
    return render(request,
                  'animals/task_status.html',
                  {'task_id': task_id,
                   'task_status': task_status})


class AnimalList(ListView):
    model = Animal


class AnimalDetail(DetailView):
    model = Animal


class AnimalCreate(CreateView):
    model = Animal
    success_url = '/'
    fields = '__all__'


class AnimalUpdate(UpdateView):
    model = Animal
    success_url = reverse_lazy('main_page')
    # fields = '__all__'
    form_class = AnimalCreateForm

# def about(request):
#     return render(request, 'animals/contacts.html')
