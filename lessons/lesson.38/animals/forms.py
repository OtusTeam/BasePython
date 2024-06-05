from django import forms
from .models import Animal, Food


class AnimalForm(forms.ModelForm):

    name = forms.CharField(
        label='Имя животного',
        initial='New Animal',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Введите имя животного',
                'class': 'form-control'
            }
        )
    )
    food = forms.ModelMultipleChoiceField(
        queryset=Food.objects.all(),
        required=False,
        widget=forms.CheckboxSelectMultiple(
            # attrs={
            #     'class': 'form-control',
            # }
        )
    )

    class Meta:
        model = Animal
        # fields = '__all__'
        # fields = ('name',)
        exclude = ('age',)
