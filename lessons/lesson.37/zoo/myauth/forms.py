from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User


from myauth.models import MyUser


class MyUserCreateForm(UserCreationForm):
    class Meta:
        model = MyUser
        # model = User
        fields = ('username', 'email', 'password1', 'password2', 'b_year')
