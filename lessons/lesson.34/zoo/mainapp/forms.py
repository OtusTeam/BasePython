from django import forms
from .models import Category
from .models import Food


class CategoryForm(forms.ModelForm):

    name = forms.CharField(label='Имя', widget=forms.TextInput(attrs={'class': 'form-control'}))

    max_age = forms.IntegerField(initial=50, widget=forms.NumberInput(
        attrs={
            'placeholder': 'максимальный возраст',
            'class': 'form-control'
        }
    ))

    foods = forms.ModelMultipleChoiceField(queryset=Food.objects.all(), widget=forms.CheckboxSelectMultiple(
        # attrs={'class': "form-check-input"}
    ))

    class Meta:
        model = Category
        # fields = '__all__'
        # fields = ('name', 'foods')
        exclude = ('is_active',)