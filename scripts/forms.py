from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django import forms

from games.models import GAME_OPTIONS
from .models import Script


class ScriptCreateForm(forms.ModelForm):

    class Meta:
        model = Script
        fields = ('name', 'language', 'file',"gamename")
        LANG_CHOICES = (
            ('python', 'python'),
            ('java', 'java'),
            ('c++', 'c++'),
        )
        widgets = {# can define formstypes
            'language': forms.Select(choices=LANG_CHOICES),
            'gamename': forms.Select(choices=GAME_OPTIONS),
        }