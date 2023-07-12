from celery.result import AsyncResult
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    PermissionRequiredMixin,
    UserPassesTestMixin,
)
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


class HelloView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return HttpResponse("<h1>Hello View</h1>")


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


class CategoryDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = "shop.delete_category"

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

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     # context.update(form2=form2)
    #     return context


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


class OrdersListView(UserPassesTestMixin, ListView):

    def test_func(self):

        # Order.objects.filter(...)
        return self.request.user.is_staff

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


class CategoriesWithProductsTree(LoginRequiredMixin, TemplateView):
    template_name = "shop/categories-with-products-tree.html"

    extra_context = {
        "categories": Category.objects.order_by("id").prefetch_related("products").all(),
    }


@login_required
def get_task_info(request: HttpRequest, task_id: str) -> HttpResponse:
    # if request.method == "GET":
    #     pass
    # if request.method == "POST":
    #     pass
    task_result: AsyncResult = notify_order_saved.AsyncResult(task_id)

    # return JsonResponse(data=None, safe=False)
    # return JsonResponse(data=["foo", "bar"], safe=False)
    return JsonResponse({
        "task_id": task_result.task_id,
        "status": task_result.status,
        "name": task_result.name,
        # "backend": str(task_result.backend),
    })
