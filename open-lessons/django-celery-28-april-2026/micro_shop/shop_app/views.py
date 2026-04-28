from django.db import transaction
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from shop_app.forms import ProductForm
from shop_app.models import Product
from shop_app.notifications import notify_product_created
from shop_app.tasks import send_product_created_notification


class ProductsListView(ListView):
    model = Product
    template_name = "shop_app/products.html"


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = "shop_app/product_form.html"

    success_url = reverse_lazy("shop_app:products_list")

    @transaction.atomic
    def form_valid(self, form):
        result = super().form_valid(form)
        product = self.object
        # notify_product_created(product)
        # send_product_created_notification.delay(product.pk)
        transaction.on_commit(
            lambda: send_product_created_notification.delay(product.pk)
        )
        return result
