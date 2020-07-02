from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponsePermanentRedirect
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.utils.safestring import mark_safe
import json

from django.views.generic import CreateView, ListView, DetailView, DeleteView, TemplateView, RedirectView
from rooms.forms import RoomCreateForm
from rooms.models import Room


class RoomCreateView(CreateView):
    model = Room
    form_class = RoomCreateForm
    template_name = "rooms/create.html"
    success_url = reverse_lazy('rooms:index')


class RoomListView(ListView):
    model = Room
    template_name = "rooms/list.html"


class RoomView(DetailView):
    model = Room
    template_name = "rooms/room.html"
    context_object_name = "room"

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        user = self.request.user
        room = Room.objects.get(pk=self.object.pk)
        result = room.add_user(user=user)
        self.object = self.get_object()
        if result == "full":
            messages.error(self.request, "Room is already full")
            return HttpResponseRedirect(reverse('rooms:index'))
        elif result == "already":
            messages.error(self.request, "You already in this room")
            context = super().get_context_data(object=self.object)
            return self.render_to_response(context)
        elif result == "success":
            context = super().get_context_data(object=self.object)
            return self.render_to_response(context)


class ExitRoom(RedirectView):
    def get(self, request, *args, **kwargs):
        pk = self.kwargs.get("pk")
        room = Room.objects.get(pk=pk)
        user = self.request.user
        result = room.disconnect(user)
        if result == "success":
            messages.success(self.request, "Exitting Room Succeeded")
            return HttpResponseRedirect(reverse('rooms:index'))
        elif result == "no_exist":
            messages.error(self.request, "You don't exist in this room")
            return HttpResponseRedirect(reverse('home:home'))



