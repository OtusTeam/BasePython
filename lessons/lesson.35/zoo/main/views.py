import time

from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from zoo import celery_app
from .forms import AnimalCreateForm
from .models import Animal
from .tasks import send_mail_task


# def index(request):
#     animals = Animal.objects.all()
#
#     context = {
#         'animals': animals,
#         'page_title': 'Main page',
#     }
#     return render(request, 'main/index.html', context=context)

# class AnimalCreateView(PermissionRequiredMixin, CreateView):
#     permission_required = 'animals.add_animal'

class AnimalsList(PermissionRequiredMixin, ListView):
    permission_required = 'animals.add_animal'
    model = Animal

    # template_name = 'main/index.html'
    # context_object_name = 'animals'
    # paginate_by = 2

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.filter(name__startswith='B')
        # print(qs)
        return qs

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['page_title'] = 'Main page'
        # print(context)
        return context


class AnimalsCreate(CreateView):
    model = Animal
    # fields = '__all__'
    form_class = AnimalCreateForm
    # success_url = '/'
    # success_url = reverse('animals:index')
    success_url = reverse_lazy('animals:index')


def send_mail(request):
    task_id = None
    # if request.method == 'POST':
    #     pass

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
