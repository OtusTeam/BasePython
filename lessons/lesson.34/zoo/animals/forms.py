from django.core.exceptions import ValidationError
from django.forms import ModelForm

from animals.models import Animal


class AnimalCreateForm(ModelForm):
    class Meta:
        model = Animal
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            # print(name, field)
            # print(dir(field.widget))

    def clean_age(self):
        age = self.cleaned_data['age']
        if age > 100:
            raise ValidationError('age not valid')
        return age
