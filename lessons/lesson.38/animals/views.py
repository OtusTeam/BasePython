import time

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView, ListView, CreateView

from animals.models import Animal
from zoo import celery_app
from . import tasks


# from django.db import connection


class PageTitleMixin:
    page_title = 'Zoo'

    # def dispatch(self):
    #     pass

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        # print(f'{context=}')
        context['page_title'] = self.page_title

        return context


# @login_required
# def index(request):
#     # animals_qty = len(
#     #     Animal.objects.all(),  # db level -> python 1000 -> inst Animal
#     # )
#     animals_qty = Animal.objects.count()  # db level -> COUNT()
#     # animals = Animal.objects.all()
#     # animals = Animal.objects.select_related(
#     #     'kind',
#     #     'animalprofile',
#     # ).all()  # db level
#     animals = Animal.objects.prefetch_related(
#         'food_set',
#     ).all()  # python level
#     # Prefetch.
#     # for el in animals.iterator():
#     #     pass
#     # animals = Animal.objects.filter(
#     #     name__startswith='po',
#     #     # age__gte=3,
#     # )
#     # print(dir(animals))
#     # print(animals.query)
#     # animals = [
#     #     {'name': 'King', 'kind': 'lion'}
#     # ]
#
#     context = {
#         'object_list': animals,
#         'animals_qty': animals_qty,
#     }
#
#     return render(request, 'animals/animal_list.html', context=context)


class AnimalsList(
    PageTitleMixin,
    LoginRequiredMixin,
    ListView,
):
    page_title = 'Animals'
    model = Animal
    paginate_by = 2


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


# def animal(request, pk):
#     animal = get_object_or_404(Animal, pk=pk)
#     context = {
#         'page_title': 'Animal page',
#         'animal': animal,
#     }
#     return render(request, 'animals/animal.html', context)

class AnimalCreate(PermissionRequiredMixin, CreateView):
    model = Animal
    fields = '__all__'
    # form_class = ...
    # success_url = ...
    success_url = '/'
    permission_required = 'animals.add_animal'


class AnimalDetail(PageTitleMixin, DetailView):
    page_title = 'Animal page'
    model = Animal
    # template_name = 'animals/animal.html'
    # template_name_suffix = '_info'

    # def get_queryset(self):
    #     qs = super().get_queryset()
    #     qs.order_by('-id')
    #     return qs

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #
    #     # print(f'{context=}')
    #     context['page_title'] = 'Animal page'
    #
    #     return context
