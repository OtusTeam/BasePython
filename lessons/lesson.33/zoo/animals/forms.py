from django.forms import ModelForm, CharField
from django.forms.widgets import Widget
from .models import Animal


class AnimalCreateForm(ModelForm):
    class Meta:
        model = Animal
        fields = "name", "kind", "age", "description"

    name = CharField(max_length=20, label="Animal name")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for name, field in self.fields.items():
            # print(name, field, field.widget)
            widget: Widget = field.widget
            widget.attrs["class"] = "form-control"
