from django import forms
from .models import Post, Author
from django.core.exceptions import ValidationError


class PostForm(forms.Form):
    title = forms.CharField(
        max_length=200,
        label="Заголовок",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите заголовок поста'})
    )
    content = forms.CharField(
        label="Текст",
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Введите текст поста'})
    )
    rating = forms.IntegerField(
        min_value=0,
        max_value=20,
        label="Рейтинг",
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Введите рейтинг поста'})
    )


class PostModelForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'rating', 'tags']
        labels = {
            'title': 'Заголовок',
            'content': 'Текст',
            'rating': 'Рейтинг',
            'tags': 'Теги',
        }
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите заголовок поста'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Введите текст поста'}),
            'rating': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Введите рейтинг поста'}),
            'tags': forms.CheckboxSelectMultiple(attrs={'class': 'form-control'}),
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) < 10:
            raise forms.ValidationError('Заголовок должен содержать не менее 10 символов')
        return title

    def clean(self):
        cleaned_data = super().clean()
        content = cleaned_data.get('content')
        forbidden_words = ['казино', 'криптовалюта', 'крипта']
        if content:
            for word in forbidden_words:
                if word in content.lower():
                    raise ValidationError(f'Содержит запрещенное слово: {word}')