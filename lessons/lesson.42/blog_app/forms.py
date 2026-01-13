from django import forms
from django.core.exceptions import ValidationError
from .models import Post


class PostForm(forms.Form):
    title = forms.CharField(
        max_length=200,
        label='Заголовок',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите заголовок'})
    )
    content = forms.CharField(
        label='Содержание',
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Введите содержание'})

    )
    rating = forms.IntegerField(
        min_value=0,
        max_value=100,
        label='Рейтинг',
        widget=forms.NumberInput(attrs={'class': 'form-control'})

    )


class PostModelForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'author', 'content', 'rating', 'tags')
        labels = {
            'title': 'Заголовок',
            'author': 'Автор',
            'content': 'Содержание',
            'rating': 'Рейтинг',
            'tags': 'Тэги',
        }
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите заголовок'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Введите содержание'}),
            'rating': forms.NumberInput(attrs={'class': 'form-control'}),
            'tags': forms.SelectMultiple(attrs={'class': 'form-control'}),
        }

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if len(title) < 5:
            raise ValidationError('Заголовок должен быть более 5 символов')
        return title


    def clean_rating(self):
        rating = self.cleaned_data.get('rating')
        if rating < 0 or rating > 100:
            raise ValidationError('Рейтинг должен быть от 0 до 100')
        return rating


    def clean(self):
        FORBIDDEN_WORDS = ['крипта', 'казино']
        data = super().clean()
        content = data.get('content')
        title = data.get('title')
        # print(type(title))
        # print(title)

        if content and title: # Тут заменил or на end - поэтому наше условие не отработало
            for  word in FORBIDDEN_WORDS:
                if word in content.lower():
                    raise ValidationError(f'Контент не должен содержать слово {word}')
                if word in title:
                    raise ValidationError(f'Заголовок не должен содержать слово {word}')

        # Можно такой вариант, чтобы независимо проверять
        # for  word in FORBIDDEN_WORDS:
        #     if content is not None and word in content.lower():
        #         raise ValidationError(f'Контент не должен содержать слово {word}')
        #     if title is not None and word in title:
        #         raise ValidationError(f'Заголовок не должен содержать слово {word}')