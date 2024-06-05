from django import forms


class ContactForm(forms.Form):
    message = forms.CharField(
        required=True,
        widget=forms.Textarea(
            attrs={
                'class': 'form-control'
            }
        )
      )