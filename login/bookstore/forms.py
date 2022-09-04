from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm



class Userform(UserCreationForm):
    email = forms.EmailField()
    username = forms.CharField(max_length = 20)
    class Meta:
        model = User
        fields = ['username', 'email', 'password']