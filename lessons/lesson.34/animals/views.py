from django.http import HttpRequest, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from celery.result import AsyncResult
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
    TemplateView,
    FormView,
)
from .forms import AnimalForm, ContactForm

from .models import Animal, Category
from .tasks import send_contact_email


def index_view(request):
    animals = Animal.objects.select_related("category").prefetch_related("meals").all()
    context = {
        "animals": animals,
    }
    return render(
        request,
        "animals/animals-list.html",
        context,
    )


def categories_with_animals(request: HttpRequest):
    context = {"categories": (Category.objects.prefetch_related("animals").all())}
    return render(
        request,
        "animals/categories-with-animals.html",
        context,
    )


class ContactFormView(FormView):
    form_class = ContactForm
    template_name = 'animals/contact.html'
    success_url = reverse_lazy('animals:list')

    def form_valid(self, form):
        data = form.cleaned_data
        message = data['message']
        print(message)
        return super().form_valid(form)


def contact_view(request: HttpRequest):
    if request.method == "POST":
        message = request.POST["message"]
        # send_contact_email(message)
        result = send_contact_email.delay(message)
        print("RESULT", result)
        print(type(result))
        print(result.state)
        print(result.ready())

        task_id = result.id
        url = f'{reverse("animals:status")}?id={task_id}'
        return HttpResponseRedirect(url)

    return render(request, "animals/contact.html")


def status_view(request):
    id = request.GET.get("id")
    # get current status
    res = AsyncResult(id)
    is_ready = res.ready()
    status = res.state
    result = res.result
    context = {"id": id, "is_ready": is_ready, "status": status, "result": result}
    return render(request, "animals/status.html", context)


# CRUD for Animals
class AnimalListView(ListView):
    model = Animal
    # template_name = 'animals/animals-list.html'
    # context_object_name = 'animals'
    # def get(self, request, *args, **kwargs):
    #     return super().get(request, *args, **kwargs)

    def get_queryset(self):
        # получить данные
        return Animal.objects.select_related("category").all()

    def get_context_data(self, *args, **kwargs):
        # переменные контекста
        context = super().get_context_data(*args, **kwargs)
        context['some_var'] = 'New context var'
        return context


class AnimalDetailView(DetailView):
    model = Animal
    # pk_url_kwarg = 'my_pk'

    # get, get_context_data, get_queryset, get_object


class AnimalCreateView(CreateView):
    model = Animal
    # fields = ('name', 'category')
    form_class = AnimalForm
    success_url = reverse_lazy('animals:list')

    # get, get_context_data, post, form_valid, get_success_url

    def form_valid(self, form):
        data = form.cleaned_data
        print('log', data)
        return super().form_valid(form)


class AnimalUpdateView(UpdateView):
    model = Animal
    fields = ('name', 'category')
    success_url = reverse_lazy('animals:list')

    # get, get_context_data, post, form_valid, get_success_url, get_queryset, get_object


class AnimalDeleteView(DeleteView):
    model = Animal
    success_url = reverse_lazy('animals:list')

    # get, post, get_success_url, get_context_data


class AboutTemplateView(TemplateView):
    template_name = 'animals/about.html'

    # get, get_context_data