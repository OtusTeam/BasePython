from django import forms
from .models import Animal


class AnimalForm(forms.ModelForm):
    name = forms.CharField(help_text='Имя животного',
                           widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Animal
        fields = ('name', 'kind')


class ContactForm(forms.Form):
    subject = forms.CharField(label='Тема письма')
    text = forms.CharField(label='Текст', widget=forms.Textarea())
    email = forms.EmailField(label='Почта')
