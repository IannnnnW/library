from multiprocessing import AuthenticationError
from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class LoginForm(AuthenticationForm):
    pass
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['username'].widget.attrs.update(
    #     {'class': 'my-username-class'}
    #     )
    #     self.fields['password'].widget.attrs.update(
    #     {'class': 'my-password-class'}
    #     )


class registerform(UserCreationForm):
    email = forms.EmailField()
    first_name=forms.CharField()
    last_name=forms.CharField()
    registration_number=forms.CharField(required=True)

    class Meta:
        model = User
        fields = ["first_name","last_name","username" , "email" , "password1", "password2"]

