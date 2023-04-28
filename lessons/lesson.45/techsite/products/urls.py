from django.urls import path

from .views import (
    CardListView,
    CardCreateView,
)

app_name = "products"

urlpatterns = [
    path("cards/", CardListView.as_view(), name="cards-list"),
    path(
        "cards/create/",
        CardCreateView.as_view(),
        name="create-card",
    ),
    # path(
    #     "devices/<int:device_id>/cards/create/",
    #     CardCreateForDeviceView.as_view(),
    #     name="create-card",
    # ),
]
