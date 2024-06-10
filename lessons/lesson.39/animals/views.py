from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin, PermissionRequiredMixin
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


class AnimalDetailView(LoginRequiredMixin, DetailView):
    model = Animal


class AnimalCreateView(UserPassesTestMixin, CreateView):
    model = Animal
    form_class = AnimalForm
    success_url = reverse_lazy('animals:list')

    def test_func(self):
        user = self.request.user
        return (self.request.user.is_staff and user.username.endswith('2')) or user.is_superuser


class AnimalUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = ["animals.change_animal"]  # view, add, change, delete
    model = Animal
    fields = '__all__'
    success_url = reverse_lazy('animals:list')


class AnimalDeleteView(DeleteView):
    model = Animal
    success_url = reverse_lazy('animals:list')
