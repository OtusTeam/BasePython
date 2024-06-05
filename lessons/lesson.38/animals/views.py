from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Animal
from .forms import AnimalForm


def animals_list_view(request):
    animals = Animal.objects.select_related('category').prefetch_related('food').all()
    return render(request, 'animals/index.html', {'animals': animals})


class AnimalListView(ListView):
    model = Animal
    # paginate_by = 4


class AnimalDetailView(DetailView):
    model = Animal


class AnimalCreateView(CreateView):
    model = Animal
    form_class = AnimalForm
    success_url = reverse_lazy('animals:list')


class AnimalUpdateView(UpdateView):
    model = Animal
    fields = '__all__'
    success_url = reverse_lazy('animals:list')


class AnimalDeleteView(DeleteView):
    model = Animal
    success_url = reverse_lazy('animals:list')
