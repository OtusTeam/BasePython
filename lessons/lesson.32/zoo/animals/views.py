from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin, PermissionRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView

from animals.models import Animal, Food
# from celery import current_app
from zoo.celery import celery_app as current_app
from .forms import AnimalCreateForm


# @login_required
@user_passes_test(lambda x: x.is_superuser)
def food_view(request):
    foods = Food.objects.prefetch_related('kinds').all()

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


class AnimalDetail(LoginRequiredMixin, DetailView):
    model = Animal


# class AnimalCreate(UserPassesTestMixin, CreateView):
class AnimalCreate(PermissionRequiredMixin, CreateView):
    permission_required = 'animals.create_animal'
    model = Animal
    success_url = '/'
    fields = '__all__'

    def test_func(self):
        return self.request.user.is_superuser


class AnimalUpdate(UpdateView):
    model = Animal
    success_url = reverse_lazy('main_page')
    # fields = '__all__'
    form_class = AnimalCreateForm


class AnimalDelete(PermissionRequiredMixin, DeleteView):
    permission_required = 'animals.delete_animal'

    model = Animal
    success_url = reverse_lazy('main_page')
