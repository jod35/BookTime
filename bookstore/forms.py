from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Book


class DateInput(forms.DateInput):
    input_type='date'

class UserRegisterForm(UserCreationForm):
    email=forms.CharField(max_length=80)

    class Meta:
        model=User
        fields=('username','email','password1','password2')


class BookCreationForm(forms.ModelForm):
    written=forms.DateField(widget=DateInput)
    class Meta:
        model=Book
        fields=('title','author','written','description','uploaded_by','thumbnail')








# class LoginForm()