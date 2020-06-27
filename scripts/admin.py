from django.contrib import admin

from .models import Script


class ScriptAdmin(admin.ModelAdmin):
    model = Script
    fileds = ["script","user","language"]
    list_display = ['name', 'user', 'language']

admin.site.register(Script, ScriptAdmin)