from django.contrib.auth.forms import UserCreationForm

from zauth.models import ZooUser


class ZooUserCreateForm(UserCreationForm):
    class Meta:
        model = ZooUser
        fields = ('username', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field_obj in self.fields.items():
            field_obj.help_text = ''
            # field_obj.widget.attrs['class'] = 'form-control'
            # print(field_name, field_obj.help_text)
