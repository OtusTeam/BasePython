from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin, PermissionRequiredMixin
from django.http import Http404
from django.shortcuts import render
from .models import Animal
import time
from .tasks import save_animals_task, send_mail_task
from celery import current_app
from django.views.generic import ListView, DetailView, CreateView, \
    DeleteView, UpdateView, FormView
from .forms import AnimalForm, ContactForm


@login_required
@user_passes_test(lambda user: user.is_superuser and user.username == 'admin')
def index_view(request):
    print('username', request.user.username)
    animals = Animal.objects.all()
    # task_id = None
    # if request.method == 'POST':
    #     # print(time.time())
    #     # save_animals_task.delay()
    #     # print(time.time())
    #     task = send_mail_task.delay('skubject', 'tesxfdfdf')
    #     task_id = task.id

    return render(request, 'animals/index.html', {'animals': animals})
    # Flask
    # return render(request, 'animals/index.html', animals=animals)
    # return render(request, 'animals/index.html', **{'animals': animals})


class AnimalsListView(ListView):
    model = Animal
    template_name = 'animals/index.html'

    # paginate_by = 1

    def get(self, *args, **kwargs):
        print('user', self.request.user)
        print('username', self.request.user.username)
        print(type(self.request.user.username))
        return super().get(*args, **kwargs)


class AnimalDetailView(LoginRequiredMixin, DetailView):
    model = Animal
    template_name = 'animals/detail.html'


class AnimalCreateView(PermissionRequiredMixin, CreateView):
    permission_required = 'animals.add_animal'
    model = Animal
    template_name = 'animals/edit.html'
    success_url = '/'
    fields = '__all__'


class AnimalDeleteView(UserPassesTestMixin, DeleteView):
    def test_func(self):
        user = self.request.user
        return user.is_superuser and user.username == 'toma'

    model = Animal
    template_name = 'animals/delete_confirm.html'
    success_url = '/'


class AnimalUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = 'animals.change_animal'
    model = Animal
    template_name = 'animals/edit.html'
    success_url = '/'
    # fields = ('kind', 'name')
    form_class = AnimalForm


def status_view(request):
    task_id = request.GET['task_id']
    # По id Задачи получить её данные
    task = current_app.AsyncResult(task_id)
    status = task.status
    return render(request, 'animals/status.html', {'task_id': task_id, 'status': status})


def contact_view(request):
    return render(request, 'animals/contact.html')


class ContactFormView(FormView):
    form_class = ContactForm
    template_name = 'animals/contact.html'
    success_url = '/'

    def form_valid(self, form):
        cleaned_data = form.cleaned_data
        print(cleaned_data['subject'])
        print(cleaned_data['text'])
        print(cleaned_data['email'])
        # Вызываем задачу
        return super().form_valid(form)
