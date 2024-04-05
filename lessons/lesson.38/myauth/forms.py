from django.contrib.auth.forms import UserCreationForm
from django.forms import HiddenInput

from myauth.models import OtusUser


class MyUserCreateForm(UserCreationForm):
    class Meta:
        model = OtusUser
        fields = ('username', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.help_text = ''
            # if field_name == 'password2':
            # #     # field.widget = HiddenInput()
            #     field.widget.attrs['class'] = 'form-control'
            #     field.required = False

    # def save(self, commit=True):
    #     ...
    #     super().save(commit=commit)
    #     ...

    # def clean_email(self):
    #     pass

# form_data = MyUserCreateForm(data=request.data)
# form_data.is_valid()
# form_data.save()