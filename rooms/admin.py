from django.contrib import admin

# Register your models here.
from .models import Room


class RoomAdmin(admin.ModelAdmin):
    model = Room
    fileds = ["name", "gamename", "password"]
    list_display = ['name', 'gamename' ]


admin.site.register(Room, RoomAdmin)
