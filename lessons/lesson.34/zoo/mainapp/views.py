from django.shortcuts import render
from .models import Animal, Category
from .tasks import get_metrics, send_email_task
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import CategoryForm


def index_view(request):
    # result = get_metrics.delay(url=request.path, method=request.method)
    # result = get_metrics.delay(url=request.path, method=request.method)
    # animals = Animal.objects.all().select_related('category')
    animals = Animal.objects.all().select_related('category').prefetch_related('category__foods')
    # animals = Animal.objects.all().prefetch_related('category__foods')

    return render(request, 'mainapp/index.html', {'animals': animals})


def contact_view(request):
    if request.method == 'POST':
        text = request.POST.get('text')
        send_email_task.delay(
            from_email='admin@admin',
            to_email='help@admin.com',
            title='to us',
            text=text
        )
        return render(request, 'mainapp/contact.html')
    return render(request, 'mainapp/contact.html')


def get_task_result_view(request, task_id):
    result = get_metrics.AsyncResult(task_id)

    context = {
        'task_id': result.id,
        'status': result.status,
        'result': result.result
    }
    return render(request, 'mainapp/task_result.html', context=context)


# CRUD - Create Read Update Delete
# 5 страниц

class CategoryListView(ListView):
    model = Category
    # template_name =
    # context_object_name =

    def get(self, request, *args, **kwargs):
        print('REQUEST', request)
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        return Category.objects.filter(is_active=True)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['promo'] = 'Реклманое сообщение'
        return context


class CategoryDetailView(DetailView):
    model = Category

    # def get(self):
    #     pass
    #
    # def get_queryset(self):
    #     pass
    #
    # def get_object(self, queryset=None):
    #     pass
    #
    # def get_context_data(self, **kwargs):
    #     pass

# get
# создать форму
# вывести на страницу
# post
# получить данные
# записать их в форму
# валидация данных
# сохранить если валидны
# если не валидны вывести форму обратно
# редирект


class CategoryCreateView(CreateView):
    model = Category
    # fields = '__all__'
    form_class = CategoryForm
    success_url = '/category-list/'

    # def get_form_kwargs(self):
    #     pass
    #
    # def get(self):
    #     pass
    #
    # def get_context_data(self, **kwargs):
    #     pass
    #
    # def post(self):
    #     pass
    #
    # def form_valid(self, form):
    #     pass
    #
    # def form_invalid(self, form):
    #     pass

    # def get_success_url(self):
    #     pass


class CategoryUpdateView(UpdateView):
    model = Category
    fields = '__all__'
    success_url = '/category-list/'


class CategoryDeleteView(DeleteView):
    model = Category
    success_url = '/category-list/'

    # def get_success_url(self):
    #     pass