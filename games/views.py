from django.shortcuts import render
from django.utils.safestring import mark_safe
import json

from django.views.generic import CreateView, ListView, DetailView, DeleteView



def index(request):
    return render(request, 'games/index.html', {})

def room(request, room_name):
    return render(request, 'games/room.html', {
        'room_name_json': mark_safe(json.dumps(room_name))
    })

