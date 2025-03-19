from django import forms
from .models import Post


class PostForm(forms.Form):
    title = forms.CharField(
        max_length=200,
        label="Заголовок",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите заголовок'})
    )
    content = forms.CharField(
        label="Содержание",
        widget=forms.Textarea(attrs={'class': 'form-control', 'row': 5,'placeholder': 'Введите текст поста'})
    )
    rating = forms.IntegerField(
        min_value=0,
        max_value=100,
        label="Рейтинг",
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Введите рейтинг'})
    )


class PostModelForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'rating', 'tags', 'author']
        labels = {
            'title': 'Заголовок',
            'content': 'Содержание',
            'rating': 'Рейтинг',
            'tags': 'Теги',
            'author': 'Автор',
        }
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите заголовок'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Введите текст поста'}),
            'rating': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Введите рейтинг'}),
            'tags': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) < 5:
            raise forms.ValidationError("Заголовок не должен содержать не менее 5 символов")
        return title

    def clean_rating(self):
        rating = self.cleaned_data['rating']
        if rating < 0 or rating > 5:
            raise forms.ValidationError("Рейтинг должен быть в диапазоне от 0 до 50")
        return rating

    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get('title')
        content = cleaned_data.get('content')
        forbidden_words = ['казино', 'криптовалюта', 'крипта']
        if content:
            for word in forbidden_words:
                if word in content.lower():
                    raise forms.ValidationError(f"Содержание поста не должно содержать слово '{word}'")

        return cleaned_data


class PostDeleteForm(forms.Form):
    confirm = forms.BooleanField(
        required=True,
        label="Подтвердите удаление",
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )