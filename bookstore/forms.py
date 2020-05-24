from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class UserRegisterForm(UserCreationForm):
    email=forms.CharField(max_length=80)

    class Meta:
        model=User
        fields=('username','email','password','password1','password2')

