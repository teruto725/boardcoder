from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django import forms

from .models import CustomUser


class CustomUserSignUpForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('username', 'email', 'image')


class CustomUserChangeForm(UserChangeForm):# passwordはめんどくさかった
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'image')

