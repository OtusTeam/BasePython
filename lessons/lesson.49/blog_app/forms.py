from django import forms
from django.core.exceptions import ValidationError


from blog_app.models import Post


class PostForm(forms.Form):
    title = forms.CharField(
        max_length=100,
        label="Заголовок",
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Введите заголовок"}
        ),
    )
    content = forms.CharField(
        label="Содержание",
        widget=forms.Textarea(
            attrs={
                "class": "form-control",
                "rows": 5,
                "placeholder": "Введите содержание поста",
            }
        ),
    )
    rating = forms.IntegerField(
        min_value=0,
        max_value=100,
        label="Рейтинг",
        widget=forms.NumberInput(attrs={"class": "form-control"}),
    )


class PostModelForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("title", "author", "content", "rating", "tags")
        labels = {
            "title": "Заголовок",
            "author": "Автор",
            "content": "Содержание",
            "rating": "Рейтинг",
            "tags": "Тэги",
        }
        widgets = {
            "title": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Введите заголовок"}
            ),
            "author": forms.Select(attrs={"class": "form-control"}),
            "content": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 5,
                    "placeholder": "Введите содержание поста",
                }
            ),
            "rating": forms.NumberInput(attrs={"class": "form-control"}),
            "tags": forms.SelectMultiple(attrs={"class": "form-control"}),
        }

    def clean_title(self):
        title = self.cleaned_data["title"]
        if len(title) < 10:
            raise ValidationError("Заголовок не должен быть менее 10 символов")
        return title

    def clean_rating(self):
        rating = self.cleaned_data["rating"]
        if rating > 10:
            raise ValidationError("Рейтинг не должен быть более 10 символов")
        return rating

    def clean(self):
        clean_data = super().clean()
        title = clean_data["title"]
        content = clean_data.get("content")
        forbidden_words = ["казино", "крипта"]

        if content or title:
            for word in forbidden_words:
                if word in content.lower():
                    raise ValidationError(
                        f"Контент не должен содержать запрещенное слово {word}"
                    )
                if word in title.lower():
                    raise ValidationError(
                        f"Заголовок не должен содержать запрещенное слово {word}"
                    )
