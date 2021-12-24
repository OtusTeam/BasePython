import time

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView

from animals.models import Animal, AnimalKind
# from zoo import celery_app
from zoo.celery import celery_app
from .tasks import send_mail_task


def index(request):
    task_id = None
    if request.method == 'POST':
        print(time.time())
        task = send_mail_task.delay('subject', 'abcde')
        print(time.time())
        task_id = task.id
        if not task:
            return HttpResponseRedirect(reverse('animals:about'))
    context = {'task_id': task_id}

    return render(request, 'animals/index.html', context=context)


# def animals_list(request):
#     # animals = Animal.objects.all()
#     animals = Animal.objects.select_related('kind'). \
#         prefetch_related('animalfood_set').all()
#     context = {
#         'p_title': 'Zoo Animals',
#         'animal_list': animals,
#     }
#     return render(request, 'animals/animal_list.html', context=context)


class PageTitileListMixin:
    p_title = ''

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['p_title'] = self.p_title
        return context


class AnimalsListView(PageTitileListMixin, ListView):
    model = Animal
    p_title = 'Zoo Animals'

    # template_name = 'animals/animals_list.html'
    # context_object_name = 'animals'
    # paginate_by = 5

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.select_related('kind'). \
            prefetch_related('animalfood_set')
        return qs

    # def get_context_data(self, *, object_list=None, **kwargs):
    #     context = super().get_context_data(object_list=object_list, **kwargs)
    #     context['p_title'] = 'Zoo Animals'
    #     return context


# print(AnimalsListView.mro())


def status_view(request, task_id):
    print(task_id)
    task = celery_app.AsyncResult(task_id)
    context = {'task_id': task_id,
               'status': task.status}

    return render(request, 'animals/status.html', context=context)


# def about(request):
#     return render(request, 'animals/about.html')


class AnimalKindCreateView(CreateView):
    model = AnimalKind
    success_url = reverse_lazy('animals:animals_list')
    # fields = '__all__'
    fields = ('name',)


class AnimalKindUpdateView(UpdateView):
    model = AnimalKind
    success_url = reverse_lazy('animals:animals_list')
    fields = ('name',)
    pk_url_kwarg = 'item_pk'
