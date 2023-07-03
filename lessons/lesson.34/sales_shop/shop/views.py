from celery.result import AsyncResult
from django.db.models import Q
from django.http import HttpResponse, HttpRequest, JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import (
    TemplateView,
    ListView,
    CreateView,
    DetailView,
    UpdateView,
    DeleteView,
)

from .models import Category
from .models import Product
from .models import Order
from .forms import CategoryForm

from .tasks import notify_order_saved


"""
CRUD

Create
Read
Update
Delete
"""


class CategoriesListView(ListView):
    # model = Category
    queryset = (
        Category
        .objects
        # .exclude(archived=)
        .filter(~Q(archived=True))
        .all()
    )


class CategoryDetailView(DetailView):
    model = Category


class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryForm
    # fields = "name", "description"
    # success_url = reverse
    success_url = reverse_lazy("shop:categories")


class CategoryUpdateView(UpdateView):
    # template_name = "..."
    template_name_suffix = "_update_form"
    model = Category
    form_class = CategoryForm

    # success_url = reverse_lazy("shop:category", {})
    # fields = "description",

    def get_success_url(self):
        return reverse("shop:category", kwargs={"pk": self.object.pk})


class CategoryDeleteView(DeleteView):
    # model = Category
    success_url = reverse_lazy("shop:categories")
    queryset = (
        Category
        .objects
        # .exclude(archived=)
        .filter(~Q(archived=True))
        .all()
    )

    def form_valid(self, form):
        success_url = self.get_success_url()
        self.object.archived = True
        self.object.save()
        # return HttpResponseRedirect(success_url)
        return redirect(success_url)


class ShopIndexView(TemplateView):
    template_name = "shop/index.html"


class ProductsView(View):
    template_name = "shop/products.html"

    def get(self, request: HttpRequest) -> HttpResponse:
        products = (
            Product
            .objects
            .filter(~Q(status=Product.Status.ARCHIVED))
            .order_by("id")
            .select_related("category")
            .defer(
                "description",
                "created_at",
                "updated_at",
                "category__description",
            )
            .all()
        )

        return render(
            request=request,
            template_name=self.template_name,
            context={
                "products": products,
            },
        )


class OrdersListView(ListView):
    template_name = "shop/orders.html"
    context_object_name = "orders"
    queryset = (
        Order
        .objects
        .order_by("id")
        .select_related("user", "payment_details")
        .prefetch_related("products")
        .all()
    )


class CategoriesWithProductsTree(TemplateView):
    template_name = "shop/categories-with-products-tree.html"

    extra_context = {
        "categories": Category.objects.order_by("id").prefetch_related("products").all(),
    }

    # def post(self, request: HttpRequest):
    #     Category.objects.create(**request.POST)
    #     return ...

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     categories = Category.objects.order_by("id").prefetch_related("products").all()
    #     context.update(categories=categories)
    #     return context


def get_task_info(request: HttpRequest, task_id: str) -> HttpResponse:
    # if request.method == "GET":
    #     pass
    # if request.method == "POST":
    #     pass
    task_result: AsyncResult = notify_order_saved.AsyncResult(task_id)

    return JsonResponse({
        "task_id": task_result.task_id,
        "status": task_result.status,
        "name": task_result.name,
        # "backend": str(task_result.backend),
    })
