from django import forms

from .models import Category


# class CategoryForm(forms.Form):
#     name = forms.CharField(max_length=100)
#     description = forms.TextInput()


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = "name", "description"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for name, field in self.fields.items():
            print(name, field)
            field: forms.Field
            widget: forms.Widget = field.widget
            widget.attrs["class"] = "form-control"
            if isinstance(field, forms.CharField):
                print(field.label, type(field.label))
