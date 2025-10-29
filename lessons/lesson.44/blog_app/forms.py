from django import forms
from django.core.exceptions import ValidationError

from blog_app.models import Post


class PostForm(forms.Form):
    title = forms.CharField(
        max_length=100,
        label="Заголовок",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите заголовок'}),
    )
    content = forms.CharField(
        label='Содержание',
        widget = forms.Textarea(attrs={'class': 'form-control', 'row': 5, 'placeholder': 'Введите содержание поста'}),

    )
    rating = forms.IntegerField(
        min_value=0,
        max_value=100,
        label='Рейтинг',
        widget = forms.NumberInput(attrs={'class': 'form-control'}),

    )


class PostModelForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['author', 'title', 'content',  'rating', 'tags']
        labels = {
            'author': 'Автор',
            'title': 'Заголовок',
            'content': 'Содержание',
            'rating': 'Рейтинг',
            'tags': 'Тэги',
        }
        widgets = {
            'author': forms.Select(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите заголовок'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'row': 5, 'placeholder': 'Введите содержание поста'}),
            'rating': forms.NumberInput(attrs={'class': 'form-control'}),
            'tags': forms.SelectMultiple(attrs={'class': 'form-control'}),
        }

    def clean_title(self):
        """Кастомная валидация title."""
        title = self.cleaned_data.get('title')
        if len(title) < 5:
            raise ValidationError('Заголовок должен содержать минимум 5 символов')
        return title

    def clean_rating(self):
        """Кастомная валидация rating."""
        rating = self.cleaned_data.get('rating')
        if rating < 0 or rating > 100:
            raise ValidationError('rating должен быть в диапазоне от 0 до 100')
        return rating

    def clean(self):
        """Общая валидация."""
        forbidden_words = ['крипта', 'казино']
        data = super().clean()
        content = data.get('content')
        title = data.get('title')

        if content or title:
            for word in forbidden_words:
                if word in content.lower():
                    raise ValidationError(f'Контент не должен содержать слово "{word}"')
                if word in title.lower():
                    raise ValidationError(f'Заголовок не должен содержать слово "{word}"')


class PostDeleteForm(forms.Form):
    """Форма для подтверждения удаления поста."""
    confirm = forms.BooleanField(
        required=True,
        label='Подтвердите удаление',
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}),
    )