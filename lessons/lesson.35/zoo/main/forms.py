from django import forms
from django.forms import ModelForm

from main.models import Animal


class AnimalCreateForm(ModelForm):
    class Meta:
        model = Animal
        # fields = ['name', 'kind']
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for name, field in self.fields.items():
            # print(name, field)
            # field: forms.Field
            # widget: forms.Widget = field.widget
            field.widget.attrs["class"] = "form-control"
            # if isinstance(field, forms.CharField):
            #     print(field.label, type(field.label))

    def clean_name(self):
        name = self.cleaned_data['name']
        print('name:', name)
        if name.islower():
            raise forms.ValidationError('only Capital name')
        return name
