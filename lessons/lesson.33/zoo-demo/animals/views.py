import celery.result
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin, PermissionRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView

from animals.models import Food, Animal
from .forms import AnimalModelForm
from .tasks import get_request_info, notify


# @login_required
def main_page(request):
    # foods = Food.objects.all().prefetch_related('animals', 'animals__category')
    foods = Food.objects.all().prefetch_related('animals__category')
    context = {
        # 'animals': [
        #     {'kind': 'monkey'},
        #     {'kind': 'bear'},
        #     {'kind': 'rabbit'},
        # ],
        'foods': foods
    }
    return render(request, 'animals/index.html', context=context)


# CRUD - Animal
class AnimalListView(ListView):
    model = Animal
    template_name = 'animals/animal_list.html'
    context_object_name = 'animals'

    # def get(self, request, *args, **kwargs):

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['help_text'] = 'Тебе в помощь'
        return context

    def get_queryset(self):
        return Animal.objects.filter(is_active=True).select_related('category')

    # def get(self, request, *args, **kwargs):
    #     pass
class AnimalDetailView(DetailView):
    model = Animal

    # def get_queryset(self):

    # def get_object(self, queryset=None):

# Создание
# GET
# нарисовать форму по модели
# вывести ее на страницу
# POST
# получить данные со страницы
# сделать валидацию
# сохранить в базу
# redirect
# FORM


class AnimalCreateView(UserPassesTestMixin, CreateView):
    model = Animal
    # fields = ('name', 'category', 'age', 'desc')
    # fields = '__all__'
    form_class = AnimalModelForm
    success_url = reverse_lazy('animals')

    def test_func(self):
        return self.request.user.is_staff or self.request.user.is_superuser

    def post(self, request, *args, **kwargs):
        get_request_info.delay(url=request.path, method=request.method)
        return super().post(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        get_request_info.delay(url=request.path, method=request.method)
        return super().get(request, *args, **kwargs)

    def form_valid(self, form):
        # print('Делаем что то с формой перед сохранением', form)
        #new_animal = form.save()
        #notify(new_animal)
        return super().form_valid(form)

    def get_success_url(self):
        task = notify.delay(self.object.name, self.object.category.name)
        print('ID', task.id)
        get_request_info.delay(url='TEST', method='TEST')
        return super().get_success_url()

    #def form_invalid(self, form):


class AnimalUpdateView(PermissionRequiredMixin, UpdateView):
    model = Animal
    permission_required = 'animals.change_animal'
    # fields = ('name', 'category', 'age', 'desc')
    # fields = '__all__'
    form_class = AnimalModelForm
    success_url = reverse_lazy('animals')


class AnimalDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = 'animals.delete_animal'
    model = Animal
    success_url = reverse_lazy('animals')


class TaskResultTemplateView(TemplateView):
    template_name = 'animals/task_result.html'

    def get(self, request, *args, **kwargs):
        self.task_id = kwargs['task_id']
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        task = celery.result.AsyncResult(id=self.task_id)
        context['task'] = task
        return context