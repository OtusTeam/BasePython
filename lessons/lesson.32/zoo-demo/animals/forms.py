from django import forms
from .models import Animal
from .models import Category


# ModelForm, Form
class AnimalModelForm(forms.ModelForm):
    name = forms.CharField(label='Имя', widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))
    age = forms.IntegerField(label='Возраст', initial=0, widget=forms.NumberInput(attrs={
        'class': 'form-control'
    }))

    category = forms.ModelChoiceField(queryset=Category.objects.all(), widget=forms.Select(attrs={
        'class': 'form-control'
    }))

    # def __init__(self):


    class Meta:
        model = Animal
        fields = ('name', 'category', 'age', 'desc')