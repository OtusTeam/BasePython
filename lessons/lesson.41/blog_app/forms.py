from django import forms
from django.core.exceptions import ValidationError

from blog_app.models import Post


class PostForm(forms.Form):
    title = forms.CharField(
        max_length=100,
        label="Заголовок",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите заголовок поста'})
    )
    content = forms.CharField(
        label="Содержание",
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Введите содержимое поста'})
    )
    rating = forms.IntegerField(
        min_value=0,
        max_value=10,
        label="Рейтинг",
        widget=forms.NumberInput(attrs={'class': 'form-control'})

    )


class PostModelForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'rating', 'author', 'tags']
        labels = {
            'title': 'Заголовок',
            'content': 'Содержание',
            'rating': 'Рейтинг',
            'author': 'Автор',
            'tags': 'Тэги'
        }
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите заголовок поста'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Введите содержимое поста'}),
            'rating': forms.NumberInput(attrs={'class': 'form-control'}),
            'tags': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) < 5:
            raise ValidationError('Заголовок должен быть более 5 символов')
        return title

    def clean_rating(self):
        rating = self.cleaned_data['rating']
        if rating < 0 or rating > 10:
            raise ValidationError('Рейтинг должен быть от 0 до 10')
        return rating

    def clean(self):
        cleaned_data = super().clean()
        content = cleaned_data.get('content')
        forbidden_words = ['казино', 'война']

        if content:
            for word in forbidden_words:
                if word in content.lower():
                    raise ValidationError(f'В контенте не должно быть слова {word}')
