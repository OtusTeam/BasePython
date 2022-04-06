import time

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView

from zoo import celery_app
from .forms import AnimalCreateForm
from .models import Animal
from .tasks import send_mail_task

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin, PermissionRequiredMixin


@login_required
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


def task_status(request, task_id):
    task = celery_app.AsyncResult(task_id)
    status = task.status
    context = {
        'task_id': task_id,
        'status': status
    }
    return render(request, 'animals/status.html', context)


class PageTitleMixin:
    page_title = ''

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = self.page_title
        return context


class AnimalDetailView(PageTitleMixin, DetailView):
    model = Animal
    page_title = 'Animal detail'


# class AnimalCreateView(LoginRequiredMixin, CreateView):
# class AnimalCreateView(UserPassesTestMixin, CreateView):
class AnimalCreateView(PermissionRequiredMixin, CreateView):
    permission_required = 'animals.add_animal'
    model = Animal
    success_url = reverse_lazy('main')
    form_class = AnimalCreateForm
    # fields = '__all__'

    def test_func(self):
        print(self.request.user)
        return self.request.user.is_superuser


class AnimalUpdateView(UpdateView):
    model = Animal
    success_url = reverse_lazy('main')
    fields = '__all__'
