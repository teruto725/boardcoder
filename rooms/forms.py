from django import forms

from games.models import GAME_OPTIONS
from rooms.models import Room


class RoomCreateForm(forms.ModelForm):

    class Meta:
        model = Room
        fields = ('name', 'gamename', 'password',)
        widgets = { # can define formstypes
            'gamename': forms.Select(choices=GAME_OPTIONS),
        }