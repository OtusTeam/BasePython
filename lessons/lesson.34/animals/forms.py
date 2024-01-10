from django import forms
from .models import Animal, Food, Category

# ModelForm, Form


class ContactForm(forms.Form):
    message = forms.CharField(max_length=100)


class AnimalForm(forms.ModelForm):
    name = forms.CharField(
        label='Имя животного',
        help_text='Как его зовут?',
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Как его зовут?',
                'class': 'form-control',
            }
        )
    )

    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        widget=forms.Select(
            attrs={
                'class': 'form-control'
            }
        )
    )

    meals = forms.ModelMultipleChoiceField(
        queryset=Food.objects.all(),
        required=False,
        widget=forms.CheckboxSelectMultiple(
            # attrs={
            #     'class': 'form-control'
            # }
        )
    )

    class Meta:
        model = Animal
        fields = '__all__'