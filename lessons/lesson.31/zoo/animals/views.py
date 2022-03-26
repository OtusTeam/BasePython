import time

from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView

from zoo import celery_app
from .forms import AnimalCreateForm
from .models import Animal
from .tasks import send_mail_task


def index(request):
    all_animals = Animal.objects.prefetch_related('animalfood_set').all()
    task_id = None
    if request.method == 'POST':
        print('task started', time.time())
        task = send_mail_task.delay('subject', 'abcde')  # celery case
        # task = send_mail_task('subject', 'abcde')  # sync case
        print('django works', time.time())
        task_id = task.id
        # return HttpResponseRedirect('/')
    context = {
        'all_animals': all_animals,
        'task_id': task_id
    }
    return render(request, 'animals/index.html', context)


# @login_required
def task_status(request, task_id):
    task = celery_app.AsyncResult(task_id)
    status = task.status
    context = {
        'task_id': task_id,
        'status': status
    }
    return render(request, 'animals/status.html', context)


# def animal_detail(request, pk):
#     animal = get_object_or_404(Animal, pk=pk)
#     context = {
#         'my_animal': animal,
#         'page_title': 'Animal detail'
#     }
#     return render(request, 'animals/animal.html', context)


# class AnimalDetailView(DetailView):
#     template_name = 'animals/animal.html'
#     model = Animal
#     pk_url_kwarg = 'pk'
#     context_object_name = 'animal'


class PageTitleMixin:
    page_title = ''

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = self.page_title
        return context


class AnimalDetailView(PageTitleMixin, DetailView):
    model = Animal
    page_title = 'Animal detail'
    # pk_url_kwarg = 'animal_pk'
    # context_object_name = 'my_animal'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['page_title'] = 'Animal detail'
    #     return context


# def animal_food_detail(request, pk):
#     obj = get_object_or_404(AnimalFood, pk=pk)
#     context = {
#         'object': obj
#     }
#     return render(request, 'animals/animal_food.html', context)

class AnimalCreateView(CreateView):
    model = Animal
    success_url = reverse_lazy('main')
    form_class = AnimalCreateForm
    # fields = '__all__'


class AnimalUpdateView(UpdateView):
    model = Animal
    success_url = reverse_lazy('main')
    fields = '__all__'
