from django import forms
from django.core.exceptions import ValidationError
from .models import Post


class PostForm(forms.Form):
    title = forms.CharField(
        max_length=100,
        label='Заголовок',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите заголовок'}),
    )
    content = forms.CharField(
        label='Содержание',
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Введите содержание поста'}),
    )
    rating = forms.IntegerField(
        label='Рейтинг',
        min_value=0,
        max_value=100,
        widget=forms.NumberInput(attrs={'class': 'form-control'}),
    )


class PostModelForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content', 'author', 'rating', 'tags')
        labels = {
            'title': 'Заголовок',
            'content': 'Содержание',
            'author': 'Автор',
            'rating': 'Рейтинг',
            'tags': 'Тэги',
        }
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите заголовок'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Введите содержание поста'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
            'rating': forms.NumberInput(attrs={'class': 'form-control'}),
            'tags': forms.SelectMultiple(attrs={'class': 'form-control'}),
        }

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if len(title) < 5:
            raise ValidationError('Заголовок не должен быть менее 5 символов')
        return title

    def clean_rating(self):
        rating = self.cleaned_data.get('rating')
        if rating < 0 or rating > 50:
            raise ValidationError('Рейтинг должен быть от 0 до 50')
        return rating

    def clean(self):
        FORBIDDEN_WORDS = ['крипта', 'казино']
        data = super().clean()
        content = data.get('content')
        title = data.get('title')

        if content and title:
            for word in FORBIDDEN_WORDS:
                if word in content.lower():
                    raise ValidationError(f'Контент не должен содержать {word}')
                if word in title.lower():
                    raise ValidationError(f'Заголовок не должен содержать {word}')

    # def clean_rating(self):


class PostDeleteForm(forms.Form):
    """Форма для подтверждения удаления поста."""
    confirm = forms.BooleanField(
        required=True,
        label="Подтверждение удаления",
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )