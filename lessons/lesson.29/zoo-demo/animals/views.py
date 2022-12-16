from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from animals.models import Food, Animal
from .forms import AnimalModelForm


def main_page(request):
    foods = Food.objects.all()
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
        return Animal.objects.filter(is_active=True)

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

class AnimalCreateView(CreateView):
    model = Animal
    # fields = ('name', 'category', 'age', 'desc')
    # fields = '__all__'
    form_class = AnimalModelForm
    success_url = reverse_lazy('animals')

    # def post(self, request, *args, **kwargs):

    def form_valid(self, form):
        print('Делаем что то с формой перед сохранением', form)
        return super().form_valid(form)

    #def form_invalid(self, form):


class AnimalUpdateView(UpdateView):
    model = Animal
    # fields = ('name', 'category', 'age', 'desc')
    # fields = '__all__'
    form_class = AnimalModelForm
    success_url = reverse_lazy('animals')


class AnimalDeleteView(DeleteView):
    model = Animal
    success_url = reverse_lazy('animals')