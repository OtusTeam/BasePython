from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin, PermissionRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Animal
from .forms import AnimalForm


def animals_list_view(request):
    animals = Animal.objects.select_related('category').prefetch_related('food').all()
    return render(request, 'animals/index.html', {'animals': animals})


class AnimalListView(ListView):
    model = Animal
    # paginate_by = 4

    # get
    def get(self, request, *args, **kwargs):
        print('REQUEST DATA', request.GET)
        return super().get(request, *args, **kwargs)

    # get context data

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['new_text'] = 'Our new text'
        return context

    def get_queryset(self):
        return Animal.objects.select_related('category').all()


class AnimalDetailView(LoginRequiredMixin, DetailView):
    model = Animal

    # get
    # get_context_data
    # get_queryset
    # get_object


class AnimalCreateView(UserPassesTestMixin, CreateView):
    model = Animal
    form_class = AnimalForm
    success_url = reverse_lazy('animals:list')

    # get
    # get_context_data
    # post
    # form_valid - форма валидна и мы хотим что то сделать перед её созранение
    # form_invalid
    # get_success_url

    def test_func(self):
        user = self.request.user
        return (self.request.user.is_staff and user.username.endswith('2')) or user.is_superuser


class AnimalUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = ["animals.change_animal"]  # view, add, change, delete
    model = Animal
    fields = '__all__'
    # success_url = reverse_lazy('animals:list')

    def post(self, request, *args, **kwargs):
        self.pk = kwargs['pk']
        return super().post(request, *args, **kwargs)

    def get_success_url(self):
        url = reverse('animals:detail', kwargs={'pk': self.pk})
        return url

    # get_queryset
    # get_object


class AnimalDeleteView(DeleteView):
    model = Animal
    success_url = reverse_lazy('animals:list')

    # get_queryset
    # get_object
