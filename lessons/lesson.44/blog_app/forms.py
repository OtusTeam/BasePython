from typing import Any

from django import forms
from django.core.exceptions import ValidationError

from blog_app.models import Post


class PostForm(forms.Form):
    title = forms.CharField(
        max_length=200,
        label='Заголовок',
        widget=forms.TextInput(attrs={'class': "form-control", 'placeholder': 'Введите заголовок'}),
    )
    content = forms.CharField(
        label='Содержание',
        widget=forms.Textarea(attrs={'class': "form-control", 'row': 5, 'placeholder': 'Введите содержание'})
    )
    rating = forms.IntegerField(
        min_value=0,
        max_value=100,
        label='Рейтинг',
        widget=forms.NumberInput(attrs={'class': "form-control"})
    )


class PostModelForm(forms.ModelForm):
    """..."""
    class Meta:
        model = Post
        fields = ('title', 'content', 'rating', 'author', 'tags')
        labels = {
            'title': 'Заголовок',
            'content': 'Содержание',
            'rating': 'Рейтинг',
            'author': 'Автор',
            'tags': 'Тэги',
        }
        widgets = {
            'title': forms.TextInput(attrs={'class': "form-control", 'placeholder': 'Введите заголовок'}),
            'content': forms.Textarea(attrs={'class': "form-control", 'row': 5, 'placeholder': 'Введите содержание'}),
            'rating': forms.NumberInput(attrs={'class': "form-control"}),
            'author': forms.Select(attrs={'class': "form-control"}),
            'tags': forms.SelectMultiple(attrs={'class': "form-control"}),
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) < 5:
            raise ValidationError('Заголовок не может быть меньше 5 символов')
        return title

    def clean_rating(self):
        rating = self.cleaned_data['rating']
        if rating > 20:
            raise ValidationError('Рейтинг не может быть больше 20')
        return rating

    def clean(self):
        """Общая валидация формы"""
        clean_data = super().clean()
        content = clean_data.get('content')
        title = clean_data.get('title')
        FORBIDDEN_WORDS = ['крипт', 'казино']

        if content and title:
            for word in FORBIDDEN_WORDS:
                if word in content.lower():
                    raise ValidationError(f'Контент не может содержать {word}')
                if word in title.lower():
                    raise ValidationError(f'Контент не может содержать {word}')