from django import forms
from django.core.exceptions import ValidationError
from .models import Author, Post



class PostForm(forms.Form):
    title = forms.CharField(
        max_length=100,
        label='Заголовок',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите заголовок'})

    )
    content = forms.CharField(
        label='Содержание',
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Введите пост'})

    )
    rating = forms.IntegerField(
        min_value=0,
        max_value=100,
        label='Рейтинг',
        widget=forms.NumberInput(attrs={'class': 'form-control'})

    )

    author = forms.ModelChoiceField(
        queryset=Author.objects.all(),
        label='Автор',
        empty_label='Выберите автора',
        widget = forms.Select(attrs={'class': 'form-control'})
    )


class PostModelForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'rating', 'author', 'tags']
        labels = {
            'title': 'Заголовок',
            'content': 'Содержание',
            'rating': 'Рейтинг',
            'author': 'Авторы',
            'tags': 'Тэги',
        }
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите заголовок'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Введите пост'}),
            'rating': forms.NumberInput(attrs={'class': 'form-control'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
            'tags': forms.SelectMultiple(attrs={'class': 'form-control'}),
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) < 5:
            raise ValidationError('Заголовок должен быть более 5 символов')
        return title

    def clean(self):
        cleaned_data = super().clean()
        content = cleaned_data.get('content')
        X_WORDS = ['казино', '1xbet']
        if content:
            for word in X_WORDS:
                if word in content.lower():
                    raise ValidationError(f'Пост не должен содержать {word}')
