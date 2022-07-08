from django.forms import ModelForm, CharField

from .models import Animal


class AnimalCreateForm(ModelForm):

    class Meta:
        model = Animal
        fields = "name", "age", "kind", "description"

    name = CharField(max_length=64, label="Animal name")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for name, field in self.fields.items():
            # print("name:", name, "field:", field, field.widget)
            # field.label_suffix = " ="
            field.widget.attrs["class"] = "model-form"
            # field.label = ...

    # def save(self, commit=True):
    #     pass
    # name = CharField(max_length=64)
