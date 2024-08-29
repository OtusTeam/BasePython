from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import (
    TemplateView,
    CreateView,
    DetailView,
    ListView,
    UpdateView,
)

from celery.result import AsyncResult

from .models import Product, Order, Category
from .forms import CategoryCreateUpdateForm
from .mixins import PageTitleMixin


class ProductsIndexView(TemplateView):
    template_name = "shop_app/products_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(
            # products=Product.objects.all(),
            products=(
                Product.objects.filter(archived=False).select_related("category").all()
            ),
        )
        return context


class OrdersIndexView(LoginRequiredMixin, TemplateView):
    template_name = "shop_app/orders_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(
            # orders=Order.objects.all(),
            # orders=Order.objects.prefetch_related("products").all(),
            # orders=Order.objects.prefetch_related("order_products").all(),
            # orders=Order.objects.prefetch_related("order_products__product").all(),
            # orders=Order.objects.select_related("user").all(),
            orders=(
                Order.objects.select_related("user")
                .prefetch_related("order_products__product")
                .all()
            ),
        )
        return context


def task_status(request: HttpRequest) -> HttpResponse:
    context = {}
    task_id = request.GET.get("task_id")
    result = AsyncResult(id=task_id)
    is_ready = result.ready()
    status = result.status
    task_result = result.result
    context.update(
        task_id=task_id,
        is_ready=is_ready,
        status=status,
        result=task_result,
    )
    return render(
        request=request,
        template_name="shop_app/task_status.html",
        context=context,
    )


def create_category(request):
    if request.method == 'POST':
        print('processing')

        form = CategoryCreateUpdateForm(request.POST, request.FILES)
        if form.is_valid():
            print('is valid')
            form.save()
            return HttpResponseRedirect('/')
        # else:
        #     print('errors')
        # print(form.errors)
    else:
        form = CategoryCreateUpdateForm()

    context = {
        'page_title': 'Category create',
        'form': form,
    }

    return render(request, 'shop_app/category_form.html', context)


class CreateCategory(PageTitleMixin, CreateView):
    model = Category
    # template_name = 'shop_app/category_form.html'
    form_class = CategoryCreateUpdateForm
    # model = Category
    # fields = '__all__'
    success_url = '/'
    page_title = 'Category create'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['page_title'] = 'Category create'
    #     # print(context)
    #     return context


class ListCategory(
    PageTitleMixin,
    PermissionRequiredMixin,
    ListView,
):
    model = Category
    paginate_by = 3
    permission_required = 'shop_app.view_category'


class UpdateCategory(PageTitleMixin, UpdateView):
    model = Category
    # template_name = 'shop_app/category_form.html'
    form_class = CategoryCreateUpdateForm
    success_url = '/'
    page_title = 'Category update'


class ReadCategory(PageTitleMixin, DetailView):
    model = Category
    page_title = 'Category update'
