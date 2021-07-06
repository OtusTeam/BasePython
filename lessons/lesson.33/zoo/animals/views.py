from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.mixins import LoginRequiredMixin, \
    UserPassesTestMixin, PermissionRequiredMixin
from django.http import Http404
from django.shortcuts import render
from django.urls import reverse_lazy, reverse

from .models import Animal, Food
import time
from .tasks import save_animals_task, send_mail_task
from celery import current_app
from django.views.generic import ListView, DetailView, CreateView, \
    DeleteView, UpdateView, FormView
from django.views.generic.base import ContextMixin
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
    # reverse('index')
    return render(request, 'animals/index.html', {'animals': animals, 'news': '...'})
    # Flask
    # return render(request, 'animals/index.html', animals=animals)
    # return render(request, 'animals/index.html', **{'animals': animals})


class NewsContextMixin(ContextMixin):

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['news'] = 'Какие то новости'
        return context


class AnimalsListView(NewsContextMixin, ListView):
    model = Animal
    template_name = 'animals/index.html'

    # paginate_by = 1
    def get_queryset(self):
        # object_list = super().get_queryset()
        # object_list = Animal.objects.select_related('kind', 'kind__family')
        object_list = Animal.objects.select_related('kind__family')
        return object_list.order_by('-name')

    def get(self, *args, **kwargs):
        print('user', self.request.user)
        return super().get(*args, **kwargs)


class AnimalDetailView(LoginRequiredMixin, DetailView):
    model = Animal
    template_name = 'animals/detail.html'

    # def get_queryset(self):
    #     pass

    # def get_object(self, queryset=None):
    #     pass


class AnimalCreateView(PermissionRequiredMixin, CreateView):
    permission_required = 'animals.add_animal'
    model = Animal
    template_name = 'animals/edit.html'
    success_url = reverse_lazy('index')
    fields = '__all__'

    # def post(self, request, *args, **kwargs):
    #     pass

    # def form_valid(self, form):
    #     pass

    # def get_success_url(self):
    #     pass


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


class ContactFormView(NewsContextMixin, FormView):
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


class FoodListView(NewsContextMixin, ListView):
    model = Food
    template_name = 'animals/food.html'

    def get_queryset(self):
        result = Food.objects.prefetch_related('kinds')
        return result
