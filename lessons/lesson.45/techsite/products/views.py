from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, ListView
from django.db.models import F

from .models import Device, Card


# Create your views here.

class CardListView(ListView):
    model = Card
    # queryset = Card.objects.annotate(
    #     device_type2=F("device__type"),
    #     device_name2=F("device__name"),
    # ).all()


class CardCreateView(CreateView):
    success_url = reverse_lazy("products:cards-list")
    model = Card

    fields = [
        "extra_info",
        "device",
    ]

    def form_valid(self, form: forms.ModelForm):
        """If the form is valid, save the associated model."""
        self.object: Card = form.save(commit=False)
        device: Device = self.object.device
        self.object.device_type = device.type
        self.object.device_name = device.name
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

#
# class CardCreateView(CreateView):
#     model = Card
#
#     fields = [
#         "extra_info",
#         "device",
#     ]
#
#     def get_form_kwargs(self):
#         """Return the keyword arguments for instantiating the form."""
#         kwargs = super().get_form_kwargs()
#         if hasattr(self, "object"):
#             kwargs.update({"instance": self.object})
#
#         print("kwargs", self.kwargs)
#         self.request: HttpRequest
#         print(self.request.path)
#         print(self.request.path_info)
#         device = Device.objects.filter(pk=self.request.path_info)
#         kwargs.update(
#
#         )
#         return kwargs
